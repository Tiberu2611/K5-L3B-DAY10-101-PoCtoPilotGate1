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
|   1 |           |      | Kỹ sư cổng (TV1) |             |
|   2 |           |      | Kỹ sư cổng (TV2) |             |
|   3 |           |      | Sản phẩm và kinh doanh (TV3) |             |
|   4 |           |      | Vận hành và pháp lý (TV4) |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công

Bốn thành viên ngang nhau, mỗi người 10 đầu việc; việc nặng (★) mỗi người 1–2 việc. Chi tiết từng việc (lệnh, chỗ viết, điều kiện xong): [`PHAN_CONG.md`](PHAN_CONG.md).

| # | TV1 · Kỹ sư cổng | TV2 · Kỹ sư cổng | TV3 · Sản phẩm và kinh doanh | TV4 · Vận hành và pháp lý |
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

Cả bàn cùng làm: câu 1.5, 2.5, 3.0, 3.4; chốt quyết định v1 và v2; demo. Mỗi người tự viết mục cá nhân bên dưới và tự nộp link repo trên LMS.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV (TV1)

### Phần việc phụ trách

Vai: **Kỹ sư cổng**. File: `lab10/guards.py`; chạy lệnh 2, 4, 5, 7.

1. Câu 1.3: metric offline cho một bước của agent (Phiếu A, A2, cột Offline).
2. Câu 1.5: đọc khoảng tin cậy, chọn kết luận (Phiếu A, A3).
3. Câu 2.1: chạy mốc base, so tiêu chí, khuyến nghị tự chặn / người duyệt / kết hợp (Phiếu B, B0, B1).
4. ★ Câu 2.6: code 2–3 cổng trong `pre_guard`, `write_gate` (`lab10/guards.py`; Phiếu B, B7.1).
5. Chốt vòng 1: `python3 -m lab10.checkpoint`, eval mốc prepared, lệnh 4; ghi bằng chứng cho B8.
6. Câu 3.0: ghi chép cổng vòng 1 đỡ được gì (Phiếu C, C1).
7. Câu 3.4: fault tree trước khi sửa (Phiếu C, C6).
8. ★ Câu 3.5: sửa nhánh kỹ thuật trong `lab10/guards.py` (Phiếu C, C7 phần code).
9. Câu 3.7: risk register (Phiếu C, C10).
10. Lệnh 7 `python3 -m lab10.check_submission --collect` tới khi `ĐỦ THÀNH PHẦN`; push bài cuối.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## HoVaTen-MSSV (TV2)

### Phần việc phụ trách

Vai: **Kỹ sư cổng**. File: `lab10/monitors.py`, `submission/submission.json`; chạy lệnh 3, 6.

1. Câu 1.6(d): hai câu ranh giới đầu ra (Phiếu A, A4).
2. Câu 2.2: trace `T-002@55`, bảng soát lỗi (Phiếu B, B2).
3. Câu 2.5: ghi chép pre-mortem bốn lăng kính (Phiếu B, B6).
4. Câu 2.7: hai bước tránh rò rỉ dữ liệu (Phiếu B, B7.2).
5. Câu 2.8: test hành vi và 2 ticket hiểm chạy `--adhoc` (Phiếu B, B7.3).
6. Câu 3.0: nhận thẻ, chạy `python3 -m lab10.grade --incident Sx`, ghi `Thẻ đã bốc:` và C0.
7. Câu 3.1: dò ≥ 2 ticket hỏng, bảng soát lỗi của thẻ (Phiếu C, C2).
8. ★ Câu 3.6: chỉ số theo dõi mới trong `lab10/monitors.py` (Phiếu C, C8).
9. Câu 3.7: fault tree sau khi sửa (Phiếu C, C9).
10. Điền `submission/submission.json`.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## HoVaTen-MSSV (TV3)

### Phần việc phụ trách

Vai: **Sản phẩm và kinh doanh**. File: `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`; chạy lệnh 1.

1. Câu 1.1: mục tiêu cấp hệ thống (Phiếu A, A1).
2. Câu 1.4: telemetry production (Phiếu A, A2, cột Telemetry production).
3. ★ Câu 1.6: Bản tiêu chí và `config/acceptance_criteria.json` (Phiếu A, A4).
4. Ký tiêu chí: `python3 -m lab10.criteria sign`, commit, push; ghi giờ ký, mã commit (Phiếu A, A5).
5. Câu 2.3: bản đồ dữ liệu, ví dụ drift (Phiếu B, B3).
6. Câu 2.9: mục `business` trong `config/operating_gates.json` (Phiếu B, B7.4).
7. Quyết định v1 (Phiếu B, B8).
8. Câu 3.2: specification (Phiếu C, C5).
9. Câu 3.5: sửa `business`, tổng hợp bảng sửa (Phiếu C, C7).
10. ★ Quyết định v2 và ba dòng bắt buộc (Phiếu C, C12).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## HoVaTen-MSSV (TV4)

### Phần việc phụ trách

Vai: **Vận hành và pháp lý**. File: `config/operating_gates.json` mục `operations`, `legal`.

1. Câu 1.2: mục tiêu nhìn từ chị Oanh và chị Hạnh (Phiếu A, A1).
2. Câu 2.4: HAZOP vòng 1, ≥ 3 dòng và ≥ 2 dòng ngoài kỹ thuật (Phiếu B, B4).
3. Câu 2.4: checklist 9 nhóm việc, PIC có tên (Phiếu B, B5).
4. ★ Câu 2.10: mục `operations`, `legal` và runbook phần 1–3 (Phiếu B, B7.5).
5. Câu 2.10: mục Giờ cao điểm (Phiếu B, B7.6).
6. Câu 3.1: phần riêng theo thẻ (Phiếu C, C3).
7. Câu 3.1: HAZOP của thẻ (Phiếu C, C4).
8. Câu 3.3: giả định về môi trường (Phiếu C, C5).
9. Câu 3.5: sửa `operations`, `legal` (Phiếu C, C7 phần vận hành).
10. ★ Câu 3.7: cập nhật checklist, runbook phần 4–5 (Phiếu C, C11).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
