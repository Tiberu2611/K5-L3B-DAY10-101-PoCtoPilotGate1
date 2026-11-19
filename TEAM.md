# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `101`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-101-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Đức Hải | 2A202603899 | Kỹ sư cổng (TV1) |             |
|   2 | Vũ Văn Chủ  | 2A202603873 | Kỹ sư cổng (TV2) |             |
|   3 | Nguyễn Văn Hiếu | 2A202603746 | Sản phẩm và kinh doanh (TV3) |             |
|   4 | Nguyễn Lê Trọng Mạnh | 2A202603857 | Vận hành và pháp lý (TV4) | * |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công

Bốn thành viên ngang nhau, mỗi người **10 đầu việc**; việc nặng (★) được rải đều, mỗi người 1–2 việc. Phút là phút trên đồng hồ lab (0–240). Chi tiết từng việc (lệnh, chỗ viết, điều kiện xong) nằm trong mục cá nhân của từng người bên dưới.

### Tổng quan

| # | TV1 · Hải · Kỹ sư cổng | TV2 · Chủ · Kỹ sư cổng | TV3 · Hiếu · Sản phẩm và kinh doanh | TV4 · Mạnh · Vận hành và pháp lý |
|--:|---|---|---|---|
| 1 | 1.3 Metric offline (A2) | 1.6(d) Ranh giới đầu ra (A4) | 1.1 Mục tiêu hệ thống (A1) | 1.2 Mục tiêu chị Oanh, chị Hạnh (A1) |
| 2 | 1.5 Khoảng tin cậy (A3) | 2.2 Trace `T-002@55` (B2) | 1.4 Telemetry production (A2) | 2.4 HAZOP vòng 1 (B4) |
| 3 | 2.1 Chạy mốc base (B0, B1) | 2.5 Ghi chép pre-mortem (B6) | ★ 1.6 Bản tiêu chí (A4) | 2.4 Checklist 9 nhóm (B5) |
| 4 | ★ 2.6 Code cổng `guards.py` (B7.1) | 2.7 Tránh rò rỉ dữ liệu (B7.2) | Ký tiêu chí, lệnh 1 (A5) | ★ 2.10 `operations`, `legal`, runbook 1–3 (B7.5) |
| 5 | Chốt vòng 1, lệnh 5 (B8 bằng chứng) | 2.8 Test hành vi (B7.3) | 2.3 Bản đồ dữ liệu (B3) | 2.10 Giờ cao điểm (B7.6) |
| 6 | 3.0 Ghi chép (C1) | 3.0 Nhận thẻ, lệnh 6 (C0) | 2.9 Mục `business` (B7.4) | 3.1 Phần riêng theo thẻ (C3) |
| 7 | 3.4 Fault tree trước (C6) | 3.1 Bảng soát lỗi thẻ (C2) | Quyết định v1 (B8) | 3.1 HAZOP của thẻ (C4) |
| 8 | ★ 3.5 Sửa code (C7) | ★ 3.6 Chỉ số theo dõi (C8) | 3.2 Specification (C5) | 3.3 Giả định môi trường (C5) |
| 9 | 3.7 Risk register (C10) | 3.7 Fault tree sau (C9) | 3.5 Sửa `business` (C7) | 3.5 Sửa `operations`, `legal` (C7) |
| 10 | Lệnh 7, push bài cuối | Điền `submission.json` | ★ Quyết định v2 (C12) | ★ 3.7 Checklist, runbook 4–5 (C11) |

### Lịch theo thời gian

| Phút | Khối | TV1 · Hải | TV2 · Chủ | TV3 · Hiếu | TV4 · Mạnh |
|---|---|---|---|---|---|
| 0–15 | Cài đặt | Clone, chạy test | Clone, chạy test | Clone, đọc `ops_facts`, `ops_limits` | Clone, đọc PRD §2, §6, `staff` |
| 15–60 | Khối 1 | 1.3 · 1.5 | 1.6(d) | 1.1 · 1.4 · 1.6 | 1.2 |
| 60–65 | Ký | Soát cùng | Soát cùng | Lệnh 1, push, A5 | Soát cùng |
| 65–85 | Khối 2A | 2.1 | 2.2 · ghi B6 | 2.3 | 2.4 (B4, B5) |
| 85–105 | Khối 2B | 2.6 | 2.7 · 2.8 | 2.9 | 2.10 (B7.5, B7.6) |
| 105–115 | Chốt v1 | Lệnh 5, eval prepared | Soát report | Viết v1 (B8) | Soát runbook khớp config |
| 115–125 | Nghỉ | | | | |
| 125–135 | Nhận thẻ | Ghi C1 | Nhận thẻ, lệnh 6, C0 | Đọc khối kinh doanh | Đọc thẻ, phần riêng |
| 135–155 | Phân tích | C6 | C2 | C5 (3.2) | C3 · C4 · C5 (3.3) |
| 155–185 | Sửa | Sửa code · C10 | `monitors.py` · C8 · C9 | Sửa `business` · tổng hợp C7 | Sửa `operations`, `legal` · C11 |
| 185–200 | v2, gom bài | Lệnh 7, push | `submission.json` | C12 | Hoàn thiện runbook 4–5 |
| 200–240 | Demo, nộp | Chạy lệnh phản biện | Trình bày cổng, sự cố | Trình bày v1 → v2 | Trả số đổi thử về bản v2 |

Ở Khối 1, TV1, TV2, TV4 việc nhẹ hơn: dùng thời gian đó soát ngưỡng Bản tiêu chí cùng TV3, vì **không sửa được sau khi ký**.

### Cả 4 người cùng làm

- Viết mục cá nhân của mình bên dưới (đóng góp, bằng chứng, exit ticket).
- Câu 1.5, câu 2.5 pre-mortem, câu 3.0, câu 3.4 fault tree: cả bàn thảo luận, người được giao chỉ là người viết.
- Chốt quyết định v1 và v2.
- Demo ba mốc và phản biện bàn cùng thẻ (phút 200–230).
- **Mỗi người tự nộp link repo trên LMS** trước deadline.

### Năm điều dễ bị loại bài

1. **Ký trước, đo sau.** Ký tiêu chí và push trước lần chạy `eval` đầu tiên.
2. **Không sửa tiêu chí** sau khi ký, kể cả một dấu cách trong `config/acceptance_criteria.json`.
3. **Chốt vòng 1 trước phút 115.** Không sửa `lab10/guards_round1.py`, `config/operating_gates.round1.json`, `config/round1.lock`.
4. **Chỉ sửa chỗ được phép** (README mục 1); file khác bị khoá hash. Không xử lý riêng theo mã ticket, không chặn hết, không thu hẹp về 0.
5. **Không chọn "Tiếp tục"** khi report còn vượt trần hoặc còn ngưỡng đã ký chưa đạt.

## Cá nhân

Mỗi thành viên tự viết phần Đóng góp cụ thể, Bằng chứng và Exit ticket trong mục của mình.

## NguyenDucHai-2A202603899

### Phần việc phụ trách

Vai: **Kỹ sư cổng** (TV1). File: `lab10/guards.py`; chạy lệnh 2, 4, 5, 7.

| # | Phút | Câu | Việc cần làm | Viết hoặc sửa ở đâu | Lệnh | Xong khi |
|--:|---|---|---|---|---|---|
| 1 | 15–60 | 1.3 | Chọn **một** bước của agent (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Thiết kế metric offline cho bước đó: Thước đo · Dữ liệu (lấy gì, ở đâu, ai gán nhãn) · Cách tính. | Phiếu A, A2, cột Offline | | Đủ ba ô; hai người tính độc lập ra cùng kết quả |
| 2 | 15–60 | 1.5 | Đọc số minh hoạ X (0,98, CI 95% [0,94; 1,0]) và Y (1,0). Chọn một kết luận (a)–(d), giải thích một câu. Cả bàn thống nhất trước khi ghi. | Phiếu A, A3 | | Có đáp án và một câu lý do |
| 3 | 65–85 | 2.1 | Chạy mốc base, so với tiêu chí đã ký. Đọc `[ĐẠT ]`/`[CHƯA]`, khối "kinh doanh và vận hành", khối "theo kho và hãng". Viết lý lẽ ủng hộ và phản đối để cổng **tự chặn** bản phát hành; khoanh: tự chặn / người duyệt / kết hợp. | Phiếu B, B0 (dòng 1), B1 | `python3 -m lab10.eval --suite base --stage base --note "baseline"`<br>`python3 -m lab10.gate --run runs/<mã>/report.json` | Có mã lần chạy base ở B0 |
| 4 | 85–105 | 2.6 ★ | Code 2–3 cổng trong `pre_guard(ctx)` / `write_gate(ctx, action)`. Mỗi cổng ứng với một lý do pre-mortem (B6) hoặc một dòng HAZOP (B4). Đặt kiểm tra trước `return Verdict.allow()`. Dùng hàm tra cứu trong `lab10/helpers.py`. Không xử lý theo mã ticket. | `lab10/guards.py`; Phiếu B, B7.1 | `python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."`<br>`python3 -m unittest discover -s tests` | Report `base · after` không có ca mới hỏng; test `OK` |
| 5 | 105–115 | Chốt | Chốt cổng vòng 1, chạy mốc prepared, so tiêu chí. Đưa ba dòng bằng chứng (kèm mã lần chạy) cho TV3 viết B8. Commit và push theo lệnh cuối B8. | Phiếu B, B8 (bằng chứng) | `python3 -m lab10.checkpoint`<br>`python3 -m lab10.eval --suite base --stage prepared`<br>`python3 -m lab10.gate --run runs/<mã>/report.json` | Máy in `ĐÃ CHỐT cổng vòng 1`; push xong trước phút 115 |
| 6 | 125–135 | 3.0 | Ghi chép thảo luận của cả bàn: cổng vòng 1 đỡ được ô nào; khối kinh doanh và vận hành có dòng nào vượt trần; sự cố có nằm trong pre-mortem không (đối chiếu B6). | Phiếu C, C1 | | Đủ ba ý |
| 7 | 135–155 | 3.4 | Vẽ fault tree **trước khi sửa**: sự kiện đỉnh là tác hại; ≥ 2 nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (`ticket@seed`, trường dữ liệu, hoặc dòng report). | Phiếu C, C6 | | Lá nào cũng có bằng chứng |
| 8 | 155–180 | 3.5 ★ | Sửa nhánh kỹ thuật trong `guards.py` cho nguyên nhân tìm được ở C2, C6. Ghi từng biện pháp **giảm khả năng** hay **ngăn hẳn**. Không chặn hết. | `lab10/guards.py`; Phiếu C, C7 (phần code) | `python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."`<br>`python3 -m lab10.eval --suite base --stage after --note "kiểm lại bộ nền"`<br>`python3 -m lab10.grade --incident Sx` | Report có `regression ✅` |
| 9 | 180–185 | 3.7 | Thêm ≥ 1 dòng risk register (rủi ro còn lại sau khi sửa, khả năng, tác động, người theo dõi). | Phiếu C, C10 | | ≥ 1 dòng đủ cột |
| 10 | 185–240 | Nộp | Chạy lệnh 7, sửa từng dòng `[THIẾU]` theo hướng dẫn `->`. Sau demo chạy lại lệnh 6 và lệnh 7. Đẩy bài lần cuối. | `submission/` | `python3 -m lab10.check_submission --collect`<br>`git add -u`<br>`git add submission templates TEAM.md`<br>`git commit -m "LAB 10: bài nộp"`<br>`git push` | Dòng cuối `ĐỦ THÀNH PHẦN`; trên GitHub có `submission/runs/` (journal, grade-report, report ba mốc) |

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## VuVanChu-2A202603873

### Phần việc phụ trách

Vai: **Kỹ sư cổng** (TV2). File: `lab10/monitors.py`, `submission/submission.json`; chạy lệnh 3, 6.

| # | Phút | Câu | Việc cần làm | Viết hoặc sửa ở đâu | Lệnh | Xong khi |
|--:|---|---|---|---|---|---|
| 1 | 15–60 | 1.6(d) | Viết hai câu ranh giới đầu ra (**không thêm trường JSON**): một đầu ra hoặc hành động bị cấm; một ngưỡng chuyển cho người duyệt. | Phiếu A, A4, mục "Ranh giới đầu ra" | | Đủ hai câu, có con số |
| 2 | 65–85 | 2.2 | Dò trace `T-002@55`. Điền bảng soát lỗi: lỗi và loại lỗi, nguồn, hướng xử lý. | Phiếu B, B2 | `python3 -m lab10.trace --suite base --ticket T-002 --seed 55` | Lỗi được xếp loại |
| 3 | 65–85 | 2.5 | Ghi chép pre-mortem bốn lăng kính (kỹ thuật, kinh doanh, con người và vận hành, pháp lý). Lăng kính nào trống thì nhắc bàn viết thêm. Đánh dấu 2–3 lý do sẽ thành cổng, chuyển cho TV1. | Phiếu B, B6 | | Đủ bốn lăng kính; có 2–3 lý do được đánh dấu |
| 4 | 85–105 | 2.7 | Nêu 2 bước cụ thể tránh rò rỉ dữ liệu khi chỉnh cổng trên chính bộ dùng để chấm. Gắn với bộ nền, gói sự cố, bài kiểm tra ẩn. | Phiếu B, B7.2 | | Hai bước, mỗi bước gắn với thứ có thật trong lab |
| 5 | 85–105 | 2.8 | Phát biểu một tính chất (một câu). Viết 2 ticket mới kiểm tính chất đó, chạy bằng `--adhoc`, dán kết quả. Giữ 2 ticket này làm "ticket hiểm" cho demo. | Phiếu B, B7.3 | `python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx` | Có tính chất, 2 ticket, kết quả dán vào |
| 6 | 125–135 | 3.0 | Nhận đúng thẻ của bàn, gõ từng dòng. Chạy lệnh 6 **trước khi sửa gì**. Ghi số thẻ vào dòng `Thẻ đã bốc:` đầu Phiếu C, ghi mã prepared vào C0. Push để cả bàn kéo về. | Phiếu C, C0; dòng `Thẻ đã bốc:` | `git fetch https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_cards.git main`<br>`git checkout FETCH_HEAD -- incidents/Sx`<br>`git commit -m "Nhận thẻ Sx"`<br>`python3 -m lab10.grade --incident Sx`<br>`git push` | `incidents/Sx` có đủ 4 file; report in `1 integrity \| ✅` và `Thẻ đã bốc … khớp` |
| 7 | 135–155 | 3.1 | Dò ≥ 2 ticket hỏng theo hai kiểu khác nhau. Bảng soát lỗi: ≥ 2 lỗi có nguồn khác nhau, ≥ 1 lỗi chìm. Nêu tác hại: cho ai, đo bằng gì, bao nhiêu ở mốc base. | Phiếu C, C2 | `python3 -m lab10.trace --suite Sx --ticket Sx-01 --seed 11` | Đủ số lỗi; có lỗi chìm |
| 8 | 155–180 | 3.6 ★ | Viết một hàm mới phía trên dict `MONITORS` (nhận `trials` chưa có nhãn, trả về một số), đăng ký `"tên_chỉ_số": tên_hàm`. Điền ba ô thước đo → dữ liệu → cách tính. `escalation_rate` có sẵn không tính. | `lab10/monitors.py`; Phiếu C, C8 | `python3 -m lab10.grade --incident Sx` | Report có `monitor ✅` |
| 9 | 180–185 | 3.7 | Cập nhật fault tree **sau khi sửa**: cổng nằm ở nhánh nào, tầng nào; nhánh nào còn hở. | Phiếu C, C9 | | Mỗi cổng gắn vào đúng nhánh |
| 10 | 185–200 | Nộp | Điền `team` (giống tiêu chí đã ký), `members` dạng `"HoVaTen-MSSV"`, `incident`, `decision_v1`, `decision_v2`, ba câu `three_lines` chép từ C12. | `submission/submission.json` | | Lệnh 7 không báo thiếu trường |

### Đóng góp cụ thể

Người thực hiện: **Vũ Văn Chủ — 2A202603873**, thành viên 2, vai Kỹ sư cổng. Đã đọc đề, hướng dẫn, phân công, dữ liệu mock, luồng agent, cổng, monitor, bộ đo và quy trình nộp để thực hiện đúng các mục được giao. Chỉ sửa các mục TV2 trong ba phiếu, `lab10/monitors.py`, `submission/submission.json` và mục cá nhân này.

| # | Đầu việc TV2 | Phần đã thực hiện và trạng thái |
|--:|---|---|
| 1 | 1.6(d), A4 | Đã viết hai ranh giới: không lấy số ngày khách khai làm căn cứ ghi tiền/lỗi hãng; chuyển người khi vượt hạn mức mà thiếu phê duyệt hợp lệ. Giải thích ngưỡng trên 200.000đ theo REFUND-v3/ngày mock, cần tra lại khi chính sách đổi. |
| 2 | 2.2, B2 | Đã điền đủ ba phần soát lỗi `T-002@55`: hoàn sai 20.000đ và lỗi oan VNX cùng bắt nguồn từ `model_override` 2→5 ngày. Nguồn là code, DB và trace mẫu phát sẵn; chưa chạy trace thực tế vì chưa ký tiêu chí. |
| 3 | 2.5, B6 | Đã ghi bản pre-mortem đủ bốn lăng kính, năm lý do và chọn ba cổng đề xuất; có nguồn dữ liệu và người phụ trách triển khai theo phân công. Bản ghi chờ cả bàn rà soát, không khẳng định đã họp hoặc cài cổng. |
| 4 | 2.7, B7.2 | Đã viết hai bước chống chỉnh theo bộ chấm: dùng bộ nền cho phát triển/regression, giữ mốc prepared trước khi xem thẻ và giữ test ẩn độc lập. |
| 5 | 2.8, B7.3 | Đã phát biểu tính chất, soạn hai ticket mới trên O-1002/C-02 và O-1004/C-04, có lệnh adhoc/seed và kết quả mong đợi theo tracking. Chờ ký tiêu chí để chạy thực tế; chưa kết luận đạt. |
| 6 | 3.0, nhận thẻ/C0 | Chờ số thẻ S1–S8 được giao, tiêu chí đã ký/commit/push và bản chốt vòng 1. Chưa lấy thẻ hoặc chạy grade; không tự chọn số thẻ. |
| 7 | 3.1, C2 | Đã ghi cách chọn hai lỗi có nguồn khác nhau từ report và dò đúng seed; chưa có thẻ/report để điền bằng chứng. Không dùng hai hậu quả cùng nguồn ở B2 thay cho yêu cầu của C2. |
| 8 | 3.6, monitors/C8 | Đã cài và đăng ký `model_override_rate`, điền đủ thước đo → dữ liệu → cách tính, cảnh báo và điểm mù. Đã kiểm thử sự kiện tổng hợp; cần thẻ thật của nhóm để xác nhận metric phân biệt thẻ với bộ nền hoặc bổ sung tín hiệu đúng thẻ. |
| 9 | 3.7, C9 | Đã ghi rõ điều kiện hoàn tất và giới hạn của monitor; chờ cây trước C6, các sửa đổi C7 và report after. Chưa khẳng định cổng đã ngăn nhánh nào khi `guards.py` còn mặc định. |
| 10 | submission.json | Đã điền tên repo và đủ bốn thành viên theo bảng TEAM. `incident` chờ số thẻ; v1/v2 và ba dòng bắt buộc chờ TV3 chốt ở B8/C12 để sao chép nguyên văn, không quyết định thay nhóm. |

**Phụ thuộc còn thiếu:** TV3 hoàn tất tiêu chí, ký/commit/push trước khi đo; TV1 hoàn tất/chốt cổng vòng 1 và C6; nhóm cung cấp số thẻ chính xác; TV1/TV3/TV4 ghi sửa đổi C7 và quyết định B8/C12. Khi có đủ, TV2 chạy trace/adhoc, nhận đúng thẻ, grade lần đầu trước khi sửa theo thẻ, phân tích C2, kiểm monitor, hoàn tất C9 và sao chép các trường còn lại vào submission.json.

**Sử dụng AI:** Có dùng Codex hỗ trợ đọc project, đối chiếu dữ kiện, soạn phần phiếu TV2, cài monitor và kiểm tra. Không dùng dữ liệu/tài liệu bên ngoài; phần B2 dẫn code, dữ liệu và trace mẫu trong chính repo. Các ngưỡng kinh doanh/vận hành, chữ ký tiêu chí và quyết định của nhóm vẫn cần người được phân công chốt.

### Bằng chứng

- `templates/form-a-criteria.md`: A4, hai câu ranh giới đầu ra.
- `templates/form-b-evaluation-gates.md`: B2, B6, B7.2 và B7.3; phân biệt rõ phân tích tĩnh, kết quả mong đợi và dữ liệu chưa đo.
- `lab10/monitors.py`: hàm `model_override_rate` và đăng ký trong `MONITORS`; `templates/form-c-incident.md`: C8 giải thích công thức, C0/C2/C9 ghi phụ thuộc chưa có.
- `submission/submission.json`: `team` và bốn `members` khớp bảng thành viên; các trường chưa có nguồn được giữ trống đúng kiểu JSON.
- Chưa tạo commit hoặc mã lần chạy eval/grade; chưa có `runs/journal.jsonl`. Không dùng output mẫu làm mã lần chạy của nhóm.
- Kiểm tra ngày **19/11/2026 (GMT+7)**: `python -B -X utf8 -m unittest discover -s tests -v` → **13/13 tests OK**. Đây là bộ kiểm tra cài đặt/regression công khai được hướng dẫn chạy ở CP1, không phải report eval/grade của nhóm.
- Kiểm thử monitor trực tiếp bằng sự kiện tổng hợp trong bộ nhớ: **9 ca đạt** (batch rỗng; thiếu events; batch hỗn hợp trả 0.5; retry chỉ tính một trial; độ trễ bằng nhau; độ trễ DB bằng 0; sự kiện thiếu giá trị; sự kiện khác loại/trường; trial đã chuyển người). Kiểm thêm không đổi dữ liệu đầu vào và không phụ thuộc nhãn, `pass`, mã ticket hay seed; tất cả đạt.
- Kiểm JSON: tên repo, đủ bốn `members`/MSSV và mục cá nhân tương ứng đều khớp; các trường thẻ/quyết định/ba dòng chưa có nguồn vẫn để trống. Các lệnh Python dùng `-B` và kiểm tra trong bộ nhớ, không tạo file test phụ hoặc bytecode.
- Kiểm phạm vi: chỉ sáu file có thay đổi nội dung; các mục cá nhân khác và các mục phiếu giao cho TV1/TV3/TV4 giữ nguyên. `git diff --check` không báo lỗi; không có file mới.
- Khắc phục môi trường Windows: checkout ban đầu dùng `core.autocrlf=true`, làm 19 file khóa có xuống dòng CRLF khác hash. Đã xác minh từng file chỉ khác xuống dòng, khôi phục đúng byte LF từ HEAD có hash trùng MANIFEST và đặt riêng repo `core.autocrlf=input`. Cả **19/19 file khóa hiện có khớp hash**, không thay nội dung, không có thay đổi nào được stage/commit. Đây là kiểm hash file, chưa phải kết quả grade cho thẻ.

### Exit ticket

- **Điều học được:** Một lần thay dữ kiện DB bằng lời khách có thể tạo cả chi tiền sai lẫn lỗi oan cho bên thứ ba; pass_rate cao và việc tool báo thành công chưa đủ chứng minh an toàn. Monitor phát hiện sự kiện không tự bảo đảm chặn tác hại.
- **Điều còn chưa chắc:** Chưa biết thẻ nhóm được giao và chưa có dữ liệu ba mốc nên chưa thể kết luận monitor hiện tại bắt được sự cố của nhóm hay các cổng sửa xong đã loại được nhánh nào; cần đo và kiểm lại sau khi đủ đầu vào, kể cả trong pilot thật.

## NguyenVanHieu-2A202603746

### Phần việc phụ trách

Vai: **Sản phẩm và kinh doanh** (TV3). File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`; chạy lệnh 1.

| # | Phút | Câu | Việc cần làm | Viết hoặc sửa ở đâu | Lệnh | Xong khi |
|--:|---|---|---|---|---|---|
| 1 | 15–60 | 1.1 | Một mục tiêu cấp hệ thống của trợ lý, khác "model trả lời đúng". Dựa PRD v1.1 §3. | Phiếu A, A1 | | Một câu, bám tình huống LogiX |
| 2 | 15–60 | 1.4 | Telemetry production để biết trợ lý có gây thiệt hại bên ngoài LogiX không: Thước đo · Dữ liệu · Cách tính, thêm **khung thời gian** và **ngưỡng báo động**. Production không có nhãn. | Phiếu A, A2, cột Telemetry production | | Đủ năm ô |
| 3 | 15–60 | 1.6 ★ | (a) Mỗi chỉ số bắt buộc thành câu "Nếu … thì chúng tôi sẽ …". (b) Soát bốn câu hỏi: có ý nghĩa với mọi bên? ai thiệt? ngày 1? ngày 1.000? (c) Điền JSON: `team`, `signed_by`; `required` (`pass_rate_min`, `pass_k_min`, `wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`); `nice_to_have.escalation_rate_max`; `business_ops` (`cost_per_ticket_vnd_max`, `roi_min`, `queue_stuck_max`); `stop_condition`; bốn dòng `decision_rule`. Số lấy từ `data/world.json` → `ops_facts`; **không chép ngưỡng từ file example**. | Phiếu A, A4; `config/acceptance_criteria.json` | | Đủ mọi khoá; cả bàn đã soát |
| 4 | 60–65 | Ký | Soát lần cuối, ký, chạy **đúng** dòng Git máy in ra. Ghi giờ ký và mã commit. Từ đây không mở file tiêu chí bằng trình soạn thảo tự định dạng. | Phiếu A, A5 | `python3 -m lab10.criteria sign`<br>`git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push` | Máy in `ĐÃ KÝ.`; push xong **trước** lần chạy eval đầu tiên |
| 5 | 65–85 | 2.3 | Bản đồ dữ liệu: trường then chốt, nguồn sự thật hay bản sao, thế giới thật làm lệch ở đâu. Một ví dụ drift trong 3 tháng: cái gì đổi, ngày nào, trường nào cho thấy, con số nào của tiêu chí bị ảnh hưởng; đầu vào đổi hay quan hệ vào–ra đổi; chỉ số nào phát hiện. Gợi ý: `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`. | Phiếu B, B3 | | Có ví dụ drift cụ thể có ngày và trường |
| 6 | 85–105 | 2.9 | Điền `business`: `daily_refund_cap_vnd`, `cost_budget_per_ticket_vnd`, `pilot_scope` (tất cả / kho nào / bao nhiêu %), `roi_min`. Mỗi số kèm một câu lý do từ `ops_limits`, `ops_facts`. | `config/operating_gates.json` mục `business`; Phiếu B, B7.4 | | Không còn `null`; mỗi số có lý do |
| 7 | 105–115 | v1 | Cột v1: một quyết định (Tiếp tục / Thu hẹp / Cải tiến thêm / Dừng), ba bằng chứng có mã lần chạy (lấy từ TV1), dòng `decision_rule` tương ứng, kho hoặc hãng có số xấu nhất, ngày quyết định lại. Cả bàn chốt. | Phiếu B, B8 | | Đủ các ô; push cùng TV1 |
| 8 | 135–155 | 3.2 | Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ. Kiểm được bằng code hoặc bằng một con số trong report. | Phiếu C, C5 (câu 3.2) | | Kiểm được bằng máy |
| 9 | 155–180 | 3.5 | Nếu nguyên nhân là tiền hoặc phạm vi: sửa `business` (`pilot_scope`, trần, ngân sách). Không thu hẹp về 0. Tổng hợp bảng C7 (gộp phần của TV1, TV4), ghi giảm khả năng hay ngăn hẳn. | `config/operating_gates.json` mục `business`; Phiếu C, C7 | `python3 -m lab10.grade --incident Sx` | Bảng C7 đủ mọi biện pháp |
| 10 | 185–200 | v2 ★ | Cột v2: quyết định, đổi hay giữ so với v1 và vì con số nào, mã lần chạy ba mốc, mục "Chỉ ở v2", **ba dòng bắt buộc** (giả định môi trường; cổng giảm hay ngăn, vì sao; cần đo lại gì trong pilot thật). **Không chọn Tiếp tục** khi report còn vượt trần hoặc còn ngưỡng chưa đạt. | Phiếu C, C12 | | Ba dòng có con số; quyết định khớp report |

### Đóng góp cụ thể

- Câu 1.1: viết mục tiêu cấp hệ thống cho trợ lý hoàn tiền giao trễ, dựa trên PRD v1.1 của Lab 9 (§3) và luồng ghi tiền, ghi lỗi hãng của Lab 10. Đã dùng AI để đọc yêu cầu và soát câu chữ.
- Câu 1.4: thiết kế telemetry theo ca cho lỗi hãng thiếu căn cứ, dùng log ghi lỗi, tracking và chính sách; nêu công thức, ngưỡng báo động và điểm mù. Đã dùng AI để soát thước đo và cách tính.
- Câu 1.6: dự thảo ngưỡng chấp nhận, bốn quy tắc quyết định và điều kiện dừng từ dữ liệu vận hành của lab. Lúc dự thảo, các mục Phiếu A của đồng đội còn trống nên chưa ký; sau khi bàn bổ sung, TV1 ký tiêu chí lúc 15:46:54 ngày 19/11/2026 rồi tạo commit `1850257`. Tôi đã kiểm tra hash JSON khớp `acceptance_criteria.lock`; không sửa tiêu chí sau khi ký. Đã dùng AI để soát câu chữ và cấu trúc JSON.
- Câu 2.3: tôi lập bản đồ nguồn dữ liệu và kịch bản đổi từ REFUND-v3 sang REFUND-v4 ngày 01/12/2026 trong commit `a76a77e`. Bản Phiếu B cuối do nhánh `tv1-hai` điền cùng chủ đề, được giữ nguyên khi gộp để bảo toàn bản chốt vòng 1; không nhận bản cuối là phần tôi tự viết. Đã dùng AI để đối chiếu dữ liệu mock và luồng chọn chính sách.
- Câu 2.9 và quyết định v1: B7.4, `business` và B8 đã có trong commit nhóm `96bed0e`. Tôi đã đối chiếu các khóa với ngưỡng đã ký và `ops_limits`, `ops_facts`, rồi chạy lại bộ nền mốc prepared để xác nhận các số v1 chính. Không nhận các mục này là phần tôi tự điền.

### Bằng chứng

- Commit `fcd424a`: `templates/form-a-criteria.md` mục A1 câu 1.1, A2 cột Telemetry production, A4; `config/acceptance_criteria.json` trước ký. Commit ký `1850257` và `config/acceptance_criteria.lock` nằm trong lịch sử chung.
- Commit `a76a77e`: bản nháp B3; bản nhóm hiện ở `templates/form-b-evaluation-gates.md` mục B3. Đối chiếu với `data/world.json` phần `policies`, `orders[].parcels` và `lab10/agent.py` phần chọn chính sách; đây là kịch bản drift, không phải kết quả eval.
- Phiếu B mục B7.4, B8 và `config/operating_gates.json` phần `business` là nội dung vòng 1 của nhóm. Lần kiểm độc lập `R-base-prepared-20261119-162844-fd4774` (report local trong `runs/`, chưa gom bài) cho 110 trial: pass_rate = 1,0; pass_k = 1,0; hoàn sai, lỗi hãng oan, lộ PII đều 0; chi phí 4.456đ/ticket; ROI 1,24; 0 ca ùn. `lab10.gate` báo mọi ngưỡng đã ký đều đạt. Report gốc của mốc base trong B8 vẫn cần nhóm cung cấp khi gom bài.

### Exit ticket

- **Điều học được:** Ngày hiệu lực của chính sách mới là căn cứ chọn phiên bản; cờ `index_active` có thể chậm cập nhật và làm cùng tracking sinh ra quyết định tiền hoặc lỗi hãng sai.
- **Điều còn chưa chắc:** Chưa có thẻ sự cố được Lab Coach xác nhận và chưa có report ba mốc của thẻ, nên chưa thể kết luận v1 chịu được sự cố hay ra quyết định v2. Cần đo trên đúng thẻ và đối soát chi phí, hàng chờ trên dữ liệu pilot thật.

## NguyenLeTrongManh-2A202603857

### Phần việc phụ trách

Vai: **Vận hành và pháp lý** (TV4), trưởng nhóm. File: `config/operating_gates.json` mục `operations`, `legal`.

| # | Phút | Câu | Việc cần làm | Viết hoặc sửa ở đâu | Lệnh | Xong khi |
|--:|---|---|---|---|---|---|
| 1 | 15–60 | 1.2 | Một mục tiêu nhìn từ chị Oanh (kế toán đối soát, khớp sổ với hãng và shop mỗi tuần) và một từ chị Hạnh (trưởng ca CSKH, duyệt ca trợ lý chuyển sang). Dựa PRD §2, §6 và `data/world.json` → `staff`. | Phiếu A, A1 | | Hai mục tiêu, mỗi người một |
| 2 | 65–85 | 2.4 | HAZOP vòng 1 trên một tool ghi: ≥ 3 dòng, cộng **≥ 2 dòng ngoài kỹ thuật** (người duyệt, ngân sách, phạm vi pilot, dữ liệu gửi bên thứ ba). | Phiếu B, B4 | | ≥ 5 dòng, có dòng ngoài kỹ thuật |
| 3 | 65–85 | 2.4 | Checklist 9 nhóm việc go-live lần 1: trạng thái, bằng chứng, **PIC có tên** cho từng dòng. | Phiếu B, B5 | | 9 dòng đều có PIC |
| 4 | 85–105 | 2.10 ★ | Điền `operations`: `pic`, `approver_id`, `reviewers_on_shift`, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`. Điền `legal`: `pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`. Viết runbook phần 1–3 **khớp các con số đó**, có dòng thời hạn dừng (từ tín hiệu đỏ tới lúc dừng xong tối đa bao nhiêu phút, ai bấm). | `config/operating_gates.json` mục `operations`, `legal`; Phiếu B, B7.5 | | `pic` không trống; runbook khớp config |
| 5 | 85–105 | 2.10 | Mục Giờ cao điểm: ai trực, mấy người, ngưỡng gọi thêm người, ngưỡng thu hẹp hoặc tắt. | Phiếu B, B7.6 | | Đủ bốn ý, có số |
| 6 | 135–155 | 3.1 | Làm phần riêng theo thẻ (chỉ phần của số đã bốc; thẻ S4 không cần). | Phiếu C, C3 | | Đúng phần của thẻ |
| 7 | 135–155 | 3.1 | HAZOP của thẻ ≥ 3 dòng, mục riêng, **không ghi đè** HAZOP vòng 1. | Phiếu C, C4 | | ≥ 3 dòng |
| 8 | 135–155 | 3.3 | Một giả định về môi trường mà người thiết kế đã ngầm tin nhưng nhiều khả năng sai ngoài thực tế. | Phiếu C, C5 (câu 3.3) | | Một giả định cụ thể |
| 9 | 155–180 | 3.5 | Nếu nguyên nhân là người, quy trình, pháp lý: sửa `operations` (`reviewers_on_shift`, `review_sampling_pct`, `decision_note`) và `legal`. Không xếp quá nhiều người trực. Gửi phần của mình cho TV3 gộp vào C7. | `config/operating_gates.json`; Phiếu C, C7 (phần vận hành) | `python3 -m lab10.grade --incident Sx` | Số trong config khớp runbook |
| 10 | 180–200 | 3.7 ★ | Cập nhật checklist 9 nhóm (cột PIC). Viết runbook phần 4–5. | Phiếu C, C11 | | Runbook 4–5 khớp config sau khi sửa |

### Đóng góp cụ thể

Người thực hiện: **Nguyễn Lê Trọng Mạnh — 2A202603857**, thành viên 4, vai Vận hành và pháp lý, trưởng nhóm.

| # | Đầu việc TV4 | Phần đã thực hiện và trạng thái |
|--:|---|---|
| 1 | 1.2, A1 | Đã viết hai mục tiêu. **Chị Oanh:** cuối tuần khớp sổ với hãng và shop mà không phải tra ngược hay đảo bút toán nào do trợ lý ghi: đúng số tiền, đúng `payer`, có căn cứ, mỗi lỗi hãng đúng hãng, đúng kiện, có nguyên nhân. **Chị Hạnh:** ca chuyển sang vừa sức một ca trực (1 người, 6 ca/giờ), được nhận trong 60 phút, không ùn, có ghi chú giải thích; không dùng phê duyệt mang tên chị khi đã hết hạn, đã dùng hoặc vượt `max_vnd`. Số liệu lấy từ `staff`, `ops_limits`, `ops_facts`, `carriers`, `staff_behavior` trong `data/world.json`. |
| 2 | Soát tiêu chí (phút 60–65) | Đã soát `config/acceptance_criteria.json` theo góc vận hành và pháp lý: ba chỉ số an toàn bằng 0, `queue_stuck_max` = 0 khớp mục tiêu chị Hạnh, `escalation_rate_max` 0,35 trong sức một người duyệt, `cost_per_ticket_vnd_max` 8.500đ dưới mức làm tay 10.000đ, đủ `stop_condition` và bốn dòng `decision_rule`, không chép ngưỡng từ file example. |
| 3 | 2.4, 2.10 (B4, B5, B7.5, B7.6) | Phiếu B mục B4, B5, B7.5, B7.6 và mục `operations`, `legal` trong `config/operating_gates.json` đã điền trước khi chốt vòng 1 (commit `96bed0e`, 15:49). |
| 4 | Gộp bài vào `main` (trưởng nhóm) | Gộp nhánh `tv1-hai` vào `main` để đưa tiêu chí đã ký và bản chốt vòng 1 lên nhánh nộp. Xử lý xung đột: Phiếu A giữ ô 1.6(d) của TV2, Phiếu B giữ bản có trace thật của `tv1-hai`. Không sửa `acceptance_criteria.json`, `.lock` và các file `.round1`. |
| 5 | Môi trường Windows | Phát hiện `core.autocrlf=true` làm file khoá và file tiêu chí trên đĩa đổi sang CRLF, lệch hash với MANIFEST và `.lock`. Đã tắt autocrlf cho repo, đưa file về LF; không đổi nội dung commit nào. Đổi email Git sang `2A202603857@example.com` theo RULES. |
| 6–10 | 3.1 (C3, C4), 3.3 (C5), 3.5 (C7 phần vận hành), 3.7 (C11) | Chờ thẻ sự cố (phút 125). |

**Sử dụng AI:** Có dùng Claude Code để đọc đề, dữ liệu mock và code; soạn nháp câu 1.2; soát ngưỡng tiêu chí; kiểm hash file khoá; hỗ trợ gộp nhánh và xử lý xung đột. Các con số dẫn trong phiếu đều lấy từ dữ liệu của repo; lựa chọn giữ bản nào khi xung đột do tôi quyết định.

### Bằng chứng

- `templates/form-a-criteria.md`, mục A1, câu 1.2 — commit `8d4ecc5`.
- Commit gộp `2f0628e` "Merge tv1-hai vào main: tiêu chí đã ký, chốt vòng 1, Phiếu A/B".
- Kiểm sau khi gộp: `python -m lab10.criteria verify` không báo lỗi (hash `75be12e3…` khớp bản ký lúc 15:46:54); lịch sử còn commit `Sign acceptance criteria` (`1850257`, 15:47:02) và file tiêu chí không đổi từ đó; bản chốt vòng 1 khớp `config/round1.lock` (15:49:43); 19/19 file khoá khớp `lab10/MANIFEST.json`; `python -m unittest discover -s tests` → 13 tests OK.
- Chưa có mã lần chạy `eval`/`grade` của riêng TV4 (vòng 2 chưa bắt đầu).

### Exit ticket

- **Điều học được:** Tiêu chí phải ký trước khi xem số, và "đã ký" chỉ có giá trị khi đúng từng byte: một lần đổi xuống dòng CRLF hay một lần push đè nhánh cũng đủ làm bằng chứng ký mất hiệu lực, dù nội dung không ai sửa.
- **Điều còn chưa chắc:** Sức một người duyệt (6 ca/giờ) có đủ khi lượng ticket tăng ở giờ cao điểm hay khi mở rộng ra nhiều depot không; cần đo lại hàng chờ thật trong pilot.
