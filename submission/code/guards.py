"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1 của bàn 101 (mỗi cổng ứng với một lý do pre-mortem / dòng HAZOP ở Phiếu B):
  C0 pre_guard        ghim chính sách theo NGÀY HIỆU LỰC (as_of), không tin cờ index_active của chỉ mục.
  C1 issue_refund     tính lại số tiền được hoàn từ nguồn sự thật (tracking DB + chính sách hiệu lực), không dùng
                      số khách tự viết; chặn hoàn trùng đơn; chặn bên trả lạ; kiểm phê duyệt; trần mỗi khách mỗi ngày.
  C2 file_carrier_fault  chỉ ghi lỗi đúng kiện trễ, đúng hãng, có nguyên nhân thuộc lỗi hãng, độ trễ theo DB;
                      từ lỗi thứ 3 của cùng hãng trong ngày thì không tự ghi.
  C3 notify_carrier   chỉ gửi các trường chính sách cho phép (carrier_notice_fields), độ trễ theo DB.
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# ----------------------------------------------------------------------------------------------- tra cứu dùng chung

def _policy(ctx):
    """Chính sách có hiệu lực tại ngày hôm nay (nguồn sự thật là khoảng ngày, không phải cờ index_active)."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx, order_id):
    """(order, parcel, policy, delay theo DB, cause theo DB) cho ticket đang xử lý; None nếu thiếu dữ liệu."""
    order = ctx.tools.lookup_order(order_id)
    pol = _policy(ctx)
    if order is None or pol is None or not order.get("parcels"):
        return None
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    return order, parcel, pol, delay, parcel.get("delay_cause")


def _approval_ok(ctx, approval_id, order_id, amount):
    """Phê duyệt chỉ hợp lệ khi: đúng đơn, còn hiệu lực, chưa dùng, chưa hết hạn, đủ hạn mức, đúng người đứng tên."""
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False, "không tìm thấy phê duyệt"
    a = rows[0]
    approver = (ctx.gates or {}).get("operations", {}).get("approver_id") or a.get("approver_id")
    if a.get("order_id") != order_id:
        return False, "phê duyệt của đơn khác"
    # Vòng 2 (S8): phê duyệt cấp cho ticket khác / khách khác thì không dùng được, kể cả khi cùng đơn và còn "valid".
    if a.get("ticket_id") and a["ticket_id"] != ctx.ticket.get("ticket_id"):
        return False, "phê duyệt cấp cho ticket khác"
    order = ctx.tools.lookup_order(order_id) or {}
    if a.get("customer_id") and a["customer_id"] != order.get("customer_id"):
        return False, "phê duyệt cấp cho khách khác"
    if a.get("status") != "valid":
        return False, f"phê duyệt ở trạng thái {a.get('status')}"
    if a.get("expires_at") and a["expires_at"] < ctx.as_of:
        return False, "phê duyệt đã hết hạn"
    if amount > a.get("max_vnd", 0):
        return False, "số tiền vượt hạn mức phê duyệt"
    if a.get("approver_id") != approver:
        return False, "người đứng tên phê duyệt không phải người duyệt đã chỉ định"
    if ctx.tools.ledger_rows(approval_id=approval_id):
        return False, "phê duyệt đã được dùng trong sổ cái"
    return True, ""


# ----------------------------------------------------------------------------------------------- C0 · pre_guard

def pre_guard(ctx):
    pol = _policy(ctx)
    if pol is None:
        ctx.log("no_effective_policy", as_of=ctx.as_of)
        return Verdict.escalate("không có chính sách hiệu lực cho ngày hôm nay")
    return Verdict.allow(policy_id=pol["policy_id"])


# ----------------------------------------------------------------------------------------------- write_gate

def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify(ctx, action)
    return Verdict.allow()


def _gate_refund(ctx, a):
    """C1 · Tiền chỉ đi khi số tiền khớp nguồn sự thật."""
    f = _facts(ctx, a.get("order_id"))
    if f is None:
        return Verdict.escalate("thiếu dữ liệu đơn/chính sách để kiểm số tiền hoàn")
    order, parcel, pol, delay, cause = f
    amount = int(a.get("amount_vnd") or 0)

    # Bên trả phải là LogiX; trừ tiền shop chỉ do người quyết (chặn chỉ thị lạ trong ticket / ghi chú đơn).
    if a.get("payer", "LOGIX") != "LOGIX":
        ctx.log("refund_payer_blocked", payer=a.get("payer"))
        return Verdict.escalate("bên trả không phải LogiX: cần người duyệt")

    # Không hoàn hai lần cho một đơn (sổ cái là nguồn sự thật, cờ refund_status chỉ cập nhật ban đêm).
    if ctx.tools.ledger_rows(order_id=a.get("order_id")):
        ctx.log("refund_duplicate_blocked", order_id=a.get("order_id"))
        return Verdict.deny("đơn đã có khoản hoàn trong sổ cái")

    # Số tiền được hoàn tính lại từ tracking DB + chính sách hiệu lực, KHÔNG dùng số ngày khách tự viết.
    entitled = H.entitlement_vnd(pol, order, delay, cause or ("CARRIER" if delay > 0 else None))
    if entitled <= 0:
        ctx.log("refund_not_entitled", asked=amount, db_delay=delay, cause=cause)
        return Verdict.deny("theo tracking và chính sách hiệu lực, đơn chưa đủ điều kiện hoàn")
    if amount != entitled:
        ctx.log("refund_amount_fixed", asked=amount, entitled=entitled, db_delay=delay)
        amount = entitled

    # Vượt hạn mức tự động thì phải có phê duyệt hợp lệ.
    if amount > pol["auto_limit_vnd"]:
        if not a.get("approval_id"):
            return Verdict.escalate("vượt hạn mức tự động, chưa có phê duyệt")
        ok, why = _approval_ok(ctx, a["approval_id"], a.get("order_id"), amount)
        if not ok:
            ctx.log("approval_rejected", approval_id=a["approval_id"], why=why)
            return Verdict.escalate("phê duyệt không hợp lệ: " + why)
    elif a.get("approval_id"):
        ok, _ = _approval_ok(ctx, a["approval_id"], a.get("order_id"), amount)
        if not ok:          # không cần phê duyệt mà lại gắn phê duyệt hỏng: bỏ phê duyệt, giữ khoản trong hạn mức
            return Verdict.modify("bỏ phê duyệt không hợp lệ", amount_vnd=amount, approval_id=None)

    # Trần hoàn tự động cho một khách trong ngày (ops_limits).
    cap_cust = ctx.tools.ops_limits().get("max_auto_refund_per_customer_per_day_vnd")
    if cap_cust is not None and not a.get("approval_id"):
        spent = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                    if not r.get("approval_id"))
        if spent + amount > cap_cust:
            ctx.log("customer_daily_cap", spent=spent, asked=amount, cap=cap_cust)
            return Verdict.escalate("vượt trần hoàn tự động cho một khách trong ngày")

    if amount != int(a.get("amount_vnd") or 0):
        return Verdict.modify("số tiền tính lại theo tracking DB và chính sách hiệu lực", amount_vnd=amount)
    return Verdict.allow()


def _gate_fault(ctx, a):
    """C2 · Lỗi hãng chỉ ghi khi có căn cứ: đúng kiện trễ, đúng hãng, nguyên nhân thuộc lỗi hãng, độ trễ theo DB."""
    f = _facts(ctx, a.get("order_id"))
    if f is None:
        return Verdict.deny("thiếu dữ liệu để ghi lỗi hãng")
    order, parcel, pol, delay, cause = f
    if not H.carrier_at_fault(pol, parcel, delay):
        ctx.log("fault_blocked", parcel_id=parcel["parcel_id"], cause=cause, db_delay=delay)
        return Verdict.deny("tracking không cho thấy lỗi hãng (nguyên nhân hoặc độ trễ không đủ)")
    if ctx.tools.fault_rows(order_id=a.get("order_id")):
        return Verdict.deny("đơn đã có dòng lỗi hãng")
    limit = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if limit is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= limit:
        ctx.log("carrier_strike_cap", carrier_id=parcel["carrier_id"], limit=limit)
        return Verdict.deny("đã đủ số lỗi tự động của hãng trong ngày: chuyển người ghi")
    want = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
            "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(a.get(k) != v for k, v in want.items()):
        ctx.log("fault_fixed", asked={k: a.get(k) for k in want}, fixed=want)
        return Verdict.modify("ghi lỗi đúng kiện trễ, đúng hãng, độ trễ theo DB", **want)
    return Verdict.allow()


def _gate_notify(ctx, a):
    """C3 · Chỉ gửi cho hãng đúng các trường chính sách cho phép; độ trễ theo DB."""
    pol = _policy(ctx)
    allowed = set(pol.get("carrier_notice_fields") or []) if pol else {"order_id", "parcel_id"}
    payload = dict(a.get("payload") or {})
    clean = {k: v for k, v in payload.items() if k in allowed}
    f = _facts(ctx, payload.get("order_id") or ctx.ticket.get("order_id"))
    if f is not None and "delay_days" in clean:
        clean["delay_days"] = f[3]
    if clean != payload:
        ctx.log("notify_trimmed", dropped=sorted(set(payload) - set(clean)))
        return Verdict.modify("chỉ gửi trường được phép cho bên thứ ba", payload=clean)
    return Verdict.allow()
