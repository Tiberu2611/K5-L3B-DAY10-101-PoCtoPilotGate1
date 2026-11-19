"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def model_override_rate(trials):
    """Fraction of trials where a claimed delay replaces a different DB delay.

    Read production events only; count each trial once, even on retries.
    Missing events or incomplete override records do not count as evidence.
    An empty batch returns 0.0 (no observations, not proof of safety).
    """
    overridden = sum(
        any(
            event.get("type") == "model_override"
            and event.get("field") == "delay_days"
            and event.get("db") is not None
            and event.get("ticket") is not None
            and event["db"] != event["ticket"]
            for event in trial.get("events") or []
        )
        for trial in trials
    )
    return overridden / max(1, len(trials))


def auto_decision_recheck_rate(trials):
    """Vòng 2 (thẻ S8) · vận hành / con người: nhân viên có đang tin quyết định tự động không?

    Tỉ lệ quyết định tự động (status refunded / denied) bị nhân viên kiểm lại bằng tay (review_kind == "recheck").
    Bình thường xấp xỉ operations.review_sampling_pct (10%); tiến về 100% nghĩa là cả ca đã thôi tin trợ lý
    và hàng chờ sắp ùn. Không cần nhãn: chỉ đọc status và review_kind. Không có quyết định tự động nào thì trả 0.0.
    """
    auto = [t for t in trials if t.get("status") in ("refunded", "denied")]
    return sum(t.get("review_kind") == "recheck" for t in auto) / max(1, len(auto))


def approval_rejected_rate(trials):
    """Vòng 2 (thẻ S8) · quyền hạn: agent hay đem phê duyệt không hợp lệ ra dùng tới mức nào?

    Trong các trial mà agent định dùng một phê duyệt (sự kiện approval_used), tỉ lệ bị cổng C1 từ chối
    (sự kiện guard kind == "approval_rejected": sai ticket / đơn / khách, đã dùng, thu hồi, hết hạn, vượt max_vnd,
    sai người đứng tên). > 0 là có mã duyệt hỏng trong bảng approvals: báo trưởng ca đứng tên để thu hồi/cấp lại.
    Không trial nào dùng phê duyệt thì trả 0.0.
    """
    used = [t for t in trials if any(e.get("type") == "approval_used" for e in t.get("events") or [])]
    bad = sum(any(e.get("type") == "guard" and e.get("kind") == "approval_rejected" for e in t.get("events") or [])
              for t in used)
    return bad / max(1, len(used))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "model_override_rate": model_override_rate,
    "auto_decision_recheck_rate": auto_decision_recheck_rate,   # S8: nhân viên kiểm tay (mất tin)
    "approval_rejected_rate": approval_rejected_rate,           # S8: phê duyệt không hợp lệ bị đem dùng
}
STARTER_MONITORS = ("escalation_rate",)
