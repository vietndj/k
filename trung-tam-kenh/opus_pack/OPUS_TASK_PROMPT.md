# NHIỆM VỤ CHẤP BÚT & DỰNG TRANG HỢP NHẤT LOGIC XÂY KÊNH (100% CLAUDE OPUS 5.5 NATIVE TỰ VIẾT)

Anh Việt giao trực tiếp cho bạn (**Claude Opus 5.5 Native**) tự tay tổ chức cấu trúc và viết mới toàn bộ câu chữ cho **Trang Tổng Hợp Logic Xây Kênh Hiện Tại** (hợp nhất `https://kenh.fedu.vn/cu/index.html` và `https://fedu.vn/k/logickenh-xaykenh.html` cùng Kho Logic & 3 trục Podcast mới nhất). Toàn bộ dữ liệu gốc đã được Python lọc sạch vỏ rác HTML (0% diễn giải qua trung gian) để bạn đọc trọn vẹn trong đúng 1 lượt đầu tiên.

---

## BƯỚC 1 — ĐỌC TRỌN BỘ DỮ LIỆU GỐC TRONG ĐÚNG 1 LƯỢT SONG SONG (CẤM ĐI MÒ FILE NGOÀI)
Hãy gọi `read_file` song song cho đúng **4 file dưới đây** (mỗi file đều `< 45KB`, đọc 1 phát hết 100% không cần truyền `StartLine`/`EndLine`):
1. `/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/01_CORE_PAGES_AND_HISTORY.md`
2. `/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/02_PODCASTS_HORMOZI_DANIEL_RUBIN.md`
3. `/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/03_KHO_LOGIC_AND_VOICE_RULES.md`
4. `/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/frag_flow_stage.html`

---

## BƯỚC 2 — TỰ TAY VIẾT & DỰNG BẢN THẢO TRANG MỚI (`opus_draft_body.html`)
Hãy tạo file `/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/opus_draft_body.html` (HTML5 hoàn chỉnh `<!DOCTYPE html><html lang="vi">...</html>`) tuân thủ chặt chẽ các yêu cầu của anh Việt:

### A. Cấu trúc Kỹ thuật & Lắp ghép Tái sử dụng (Tiết kiệm tối đa Output Token, 0% sai sót):
1. Trong `<head>`:
   - Khai báo `<meta charset="UTF-8">`, `<meta name="viewport" content="width=device-width, initial-scale=1.0">`, Google Fonts (`Be Vietnam Pro`, `Plus Jakarta Sans`, `JetBrains Mono` giống trang gốc) và tiêu đề trang thật sắc.
   - Đặt dòng comment `<!-- INJECT_BASE_STYLES -->` để kế thừa toàn bộ hệ thống CSS gốc (`cl-zebra-section`, `cl-zebra--light`, `cl-zebra--tint`, `.flow-stage`, `.flow-item`, `.faq-item`...).
   - Mở thêm 1 thẻ `<style>` riêng của bạn để tinh chỉnh bố cục, thanh điều hướng mục lục neo nhanh (`sticky` gọn đẹp), sơ đồ/đồ thị mở rộng, thẻ so sánh, hộp kết luận nhân quả, bảng cuộn ngang mượt trên di động (`390px`) và thoáng sắc trên máy tính (`1280px`).
2. Đầu `<body>`:
   - Thanh điều hướng trên cùng gọn sạch dẫn về `https://kenh.fedu.vn/` (`← Trung tâm Logic Xây Kênh`) + thanh nhảy nhanh tới các chương chính trong trang.
3. Cuối `<body>` (ngay sau phần bài viết tổng hợp mới của bạn và trước `</body>`), **BẮT BUỘC đặt đúng 3 dòng placeholder sau (mỗi dòng 1 hàng riêng)**:
   ```html
   <!-- INJECT_HIDDEN_3TANG -->
   <!-- INJECT_FAQ_BOTTOM -->
   <!-- INJECT_FOOTER -->
   ```
   - `<!-- INJECT_HIDDEN_3TANG -->` sẽ tự nạp khối Ví dụ 3 tầng / 4 tầng cũ ở chế độ `display:none !important; hidden` đúng ý anh Việt (*"phần ví dụ 3 tầng này thì ẩn đi"*).
   - `<!-- INJECT_FAQ_BOTTOM -->` sẽ tự nạp nguyên vẹn 100% khối `#sec-faq` (39 câu hỏi thực chiến dưới cùng của `cu/index.html` — *"Phần câu hỏi dưới cùng thì giữ"*).
   - `<!-- INJECT_FOOTER -->` sẽ tự nạp chân trang đồng bộ.

### B. Kiến trúc Nội dung & Đồ thị Tổng hợp (Do bạn trực tiếp cầm bút 100%, độ dài phần viết mới ~2.200 – 3.500 từ tinh chất, đanh gọn, giàu hình ảnh đời thực):
Hãy đan cài nhuần nhuyễn tất cả mảnh ghép thành **một dòng chảy nhân quả duy nhất không vết nối**, gồm đầy đủ các trụ cột:
1. **Luật Chơi Mới Thời Máy Móc Viết Hộ — Hàng Giá Rẻ Bán Bằng Lượt Xem, Hàng Giá Cao Bán Bằng Bằng Chứng Bảo Kê Đầu Ra:**
   - Gộp tinh thần mở màn của `cu/index.html` với Alex Hormozi & Daniel Priestley: Khi công cụ tự động viết mẹo nhanh hơn người trong vài giây, lời khuyên suông rớt giá về 0. Thứ duy nhất máy không làm thay được là **đứng ra chịu trách nhiệm khi việc hỏng**.
   - Kẻ rõ **trục thiệt hại của người nghe**: việc rủi ro thấp (như kẻ mắt sai rửa mặt là hết) thì xem ai cũng được; việc rủi ro cao (kinh doanh, sửa nhà, sức khỏe, đào tạo — sai một bước là mất tiền mặt hoặc hỏng việc) thì khách không mua kỹ năng lẻ mà mua **sự bảo kê đầu ra**, và thứ duy nhất chứng minh bạn đủ sức bảo kê là **công việc thật ngoài đời**.
2. **Đường Đi Thật Của Tiền — Quy Tắc 90–9–1, Người Xem Thầm Lặng & 84% Chia Sẻ Ngầm Qua Zalo:**
   - Kết hợp phần 90–9–1 và đường đi chuyển đổi của cả 2 trang: Đừng làm nội dung chiều lòng 1% người thích tranh luận công khai; khách có tiền nằm trong nhóm 90% quan sát im lặng (vì bình luận công khai về nỗi lo công việc chẳng khác nào đứng phát biểu giữa hội trường đông người).
   - Chỉ số sinh ra tiền thật là lượt **Lưu lại** và **Gửi riêng qua tin nhắn Zalo/Messenger** cho người nhà, cộng sự.
3. **Phá Nghịch Lý Người Mới & Gỡ Chữ Ngại — Bằng Chứng Nén Thời Gian Thật & Câu Khóa "Video Là Món Quà, Dịch Vụ Là Cam Kết":**
   - Giải phẫu thẳng cảm giác ngượng miệng khi khóa cửa phòng tự quay giây thứ 3, tật giả vờ sắm đồ nghề để trì hoãn, hay bấm đăng xong úp điện thoại bỏ chạy (`logic18`, thiết kế hạ ma sát tĩnh `logic41`).
   - **Chưa có thành tích lớn thì quay cái gì?** Bỏ hẳn lối "kể khổ, dạy đạo lý chung chung". Hãy lấy **khối lượng va chạm thật** làm bằng chứng: bật máy quay 1 ngày 12 tiếng làm việc thật (gọi khách, đo đạc, sửa ca hỏng) rồi cắt lấy 3 phút đắt nhất — người xem được lời vì khỏi tự mò 12 tiếng (Alex Hormozi), hoặc làm thử trước một phần như bổ miếng dưa hấu đỏ mời nếm trước khi thu tiền (`logic35`), tích lũy "tờ biên lai kế toán" của sự tự tin (`logic36`) và "tờ hóa đơn mồ hôi ở góc khuất" (`logic40`). Chưa quen lộ mặt thì quay đôi tay đang làm việc kèm giọng dẫn tự nhiên.
   - **Gỡ sạch độ vênh tưởng như trái ngược giữa Rick Rubin và Hormozi/Daniel Priestley:**
     + Với **người xem trên mạng** (Rick Rubin, `logic39`): Họ chưa trả đồng nào — họ là **người nhận quà**, chưa phải khách hàng. Mỗi video là món quà tặng người đi sau mình một bước; bấm nút đăng là xong trọn việc hôm đó, không moi hạt mầm lên đo rễ từng giờ.
     + Với **người rút ví trả tiền** (Daniel Priestley & Hormozi): Họ mới là **khách hàng** đang gánh rủi ro tài chính, nên dịch vụ của bạn là **cam kết bảo kê đầu ra** (dám nói trước rủi ro, dám từ chối ca không hợp, dám chịu trách nhiệm). Và chính kho video quay việc thật mỗi ngày là bằng chứng sống khiến khách tin lời cam kết đó.
4. **Đồ Thị Hệ Thống Trung Tâm (Nâng Cấp Từ Đồ Thị `flow-stage` Hiện Tại):**
   - Nhúng và nâng cấp trực tiếp khối **Đồ thị tương tác `.flow-stage`** (giữ đủ các thẻ `.flow-item` bấm kiểm tra `onclick="toggleFlowCheck(this)"` và thanh trạng thái `#flowStatusText` / `#flowResetBtn` từ `frag_flow_stage.html`, bạn có thể tinh chỉnh câu chữ bên trong cho thật sắc và sạch 100% từ cấm, đồng thời thiết kế thêm tầng Đầu Vào ở trên và tầng Đầu Ra ở dưới nối liền vào `.flow-stage`):
     + **Tầng Đầu Vào Tự Chủ:** Việc làm thật ngoài đời + Tâm thế trao quà (đếm số giờ làm thật & số video xuất xưởng).
     + **Vòng Gửi Xe & Lõi Chấm Điểm Kép (`.flow-stage` tương tác):**
       - *Nhánh Thị Giác (Chiếc hộp sạch bọc nhẫn vàng — qua 3 giây đầu):* Khung hình gọn sáng, âm thanh sạch không đè giọng, nhịp cắt dứt khoát 120–140 từ/phút để mắt và tai người xem không mỏi.
       - *Nhánh Trí Tuệ (Mô tả đúng bệnh ở cấp độ hành vi vi mô trong nghề):* Thay thế hoàn toàn mô hình 3-4 tầng cũ bằng nguyên lý chạm trúng chi tiết vướng mắc cụ thể ngoài hiện trường (lấy từ nhật ký làm việc với những khách hàng kỹ tính nhất; máy móc chỉ sắp xếp câu chữ chứ không được bịa chất liệu). Khi bạn gọi đúng chỗ kẹt chính xác hơn chính người trong cuộc, họ tự hiểu bạn nắm lời giải.
     + **Tầng Tích Lũy & Chuyển Hóa Đầu Ra:** Đủ **7 giờ tiếp xúc × 11 điểm chạm × 4 nơi xuất hiện** (Daniel Priestley) → Lưu & gửi riêng qua Zalo → Khách tự nhắn tin đặt hàng trong im lặng (*"Em theo dõi anh lâu rồi"*).
5. **Thước Đo Hai Pha Thực Tế & Áp Dụng Cho Ngành Dịch Vụ Giá Cao (Không Hứa Lố, Không Bỏ Cuộc Ở 300 Tờ Rơi):**
   - Sửa thẳng điểm mù "4 tuần tự động chốt đơn": 4 tuần đầu chỉ mới tạo ra khoảng 20 phút nội dung (~5% của 7 giờ), nên tháng đầu lượt lưu và tin nhắn gần bằng 0 là hoàn toàn bình thường.
   - Chia rõ **Pha 1 (4 tuần đầu — Vượt ma sát tĩnh & Chuẩn hóa Vòng gửi xe)**: Chỉ đo thứ tay mình làm chủ được (số buổi bấm máy, số video sạch đã tặng đi). Đừng phát 300 tờ rơi đã kết luận không ai cần trong khi ngưỡng đủ độ phủ là 5.000 tờ (Hormozi).
   - **Pha 2 (Vài tháng tiếp theo — Đánh giá theo cả lô & Nâng giá trị ca làm việc)**: Đo lượt Lưu và tin nhắn Zalo theo từng lô 20–30 video; dẫn chứng ngắn gọn 3 kênh học viên có video thật triệu view (`Hoàng Nga — Momi Trendii`, `Từ An — Men Mộc An`, `Nhà 3 Hờ` liên kết tới `https://kenh.fedu.vn/09-case.html`) và bài toán ngành dịch vụ cá nhân bị giới hạn giờ làm trực tiếp (*Trần vật lý*: dùng kênh làm bộ lọc để chọn đúng khách phù hợp và nâng đơn giá thay vì ôm khách đại trà).

### C. Ràng buộc Cứng (Kiểm định tự động bằng Script):
- **TUYỆT ĐỐI CẤM** xuất hiện các cụm `"3 tầng"`, `"4 tầng"`, `"ba tầng"`, `"bốn tầng"`, `"tầng 1"`, `"tầng 2"`, `"tầng 2.5"`, `"tầng 3"`, `"công cụ 4 tầng"` trong phần văn bản hiển thị mới.
- **TUYỆT ĐỐI CẤM** nhắc tới các case cũ đã xóa (*Hằng BĐS, Liên Bảo hiểm, Kiên Phân Bón, Quỳnh Anh Le Kitchen, Đặng Hường, Xăm Nghệ Thuật, Tâng Xinh*). Nếu nêu con số ví dụ minh họa phễu chuyển đổi thì ghi rõ là *ví dụ minh họa*.
- Tuân thủ 100% quy tắc văn phong và Sổ đen từ cấm trong Tập 3/3.

---

## BƯỚC 3 — LẮP GHÉP & CHẠY KIỂM ĐỊNH 6 CỔNG TẤT ĐỊNH
Sau khi ghi xong `/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/opus_draft_body.html`, chạy lệnh:
```bash
python3 /Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack/assemble_and_verify.py
```
- Nếu script báo bất kỳ lỗi nào ở Gate 1..6 (bao gồm `verify_voice.py`), hãy dùng `edit_file` sửa triệt để trong `opus_draft_body.html` và chạy lại `assemble_and_verify.py` cho đến khi màn hình in ra **`✅ ALL 6 GATES PASSED!`**.
- Khi đã PASS 6/6 cổng:
  1. Ghi tóm tắt cấu trúc trang mới và các điểm kết tinh nổi bật vào file `/Users/vietmac/.gemini/antigravity/brain/bee3c217-3545-45b0-83e2-5516153b8ce1/silent_80_result.md`.
  2. Trả lời kết thúc ngắn gọn (`≤ 15 dòng`) báo đã hoàn tất 6/6 cổng kèm đường dẫn file để hệ thống đánh thức luồng chính.
