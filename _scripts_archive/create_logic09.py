import re

with open('logic08.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer
# We can find where the sidebar toc starts, clear it.
# We can find where the article content starts, clear it.

# To simplify, we use regex to replace everything inside `<ul class="ink-toc-list">` and `<article class="ink-content ink-mode-dialogue">`.

# Rebuild the file based on the template
html_template = content

# Replace the TOC
new_toc = """
<li style="margin-top: 12px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 12px; text-transform: uppercase;">SINH HỌC SÁNG TẠO</li>
<li><a class="ink-toc-link" href="#q1">Q1. Ảo tưởng đối tác AI</a></li>
<li><a class="ink-toc-link" href="#q2">Q2. Sổ tay vật lý</a></li>
<li><a class="ink-toc-link" href="#q3">Q3. Ảo tưởng dữ liệu</a></li>
<li><a class="ink-toc-link" href="#q4">Q4. Thao túng não bộ</a></li>
"""

# Find TOC list content
toc_pattern = r'(<ul class="ink-toc-list">).*?(</ul>)'
html_template = re.sub(toc_pattern, r'\1\n' + new_toc + r'\n\2', html_template, flags=re.DOTALL)

# Replace the Main Content
new_content = """
<h1 class="is-short">BẢN CHẤT SINH HỌC CỦA SỰ SÁNG TẠO: ĐẬP TAN ẢO TƯỞNG AI</h1>
<div class="ink-meta">
  <span>System Identity: [INKDOC-09]</span>
  <span class="mx-2">•</span>
  <span>Render Mode: [Dialogue]</span>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q1" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q1: HIỆN TƯỢNG "CHIÊN GIÒN" & ẢO TƯỞNG ĐỐI TÁC AI<br>Bạn nghĩ vừa làm việc vừa hỏi đáp liên tục với AI sẽ giúp não "nảy số" nhanh và giải quyết vấn đề sắc bén hơn? Tại sao dưới góc độ Ti thể (sinh học năng lượng), việc ỷ lại vào máy móc lại đang vắt kiệt nơ-ron, "chiên giòn" bộ não và biến bạn thành một cái máy photocopy vô hồn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>
Đó là chấn thương sinh lý mang tên <strong>Cạn kiệt chuyển hóa</strong>.<br>
Vòng lặp <em>Nảy ý ➡️ Hỏi AI ➡️ Bị cuốn theo hướng khác</em> tạo ra các cú giật nơ-ron tàn bạo (Chuyển đổi bối cảnh). Ti thể (nhà máy năng lượng tế bào não) bị ép đốt sạch nhẵn ATP dự trữ chỉ để liên tục đập bỏ và xây lại luồng tư duy. Bạn không hề sáng tạo, bạn chỉ đang phản xạ bị động để đổi lấy chút Dopamine rác từ sự tò mò. Sự phân tâm này làm vỏ não trước trán quá nhiệt, ngập ngụa gốc tự do. Sự đột phá nguyên bản không sinh ra từ việc nhồi nhét ồn ào, nó nảy mầm từ sự cách ly tuyệt đối!</p>
<blockquote>
<p><em>Chạy theo máy móc ồn ào,<br/>Chiên giòn não bộ lọt vào u mê.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q2" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q2: SỔ TAY VẬT LÝ VS. BÀN PHÍM VÔ HỒN<br>Kể cả khi đã dùng ý chí để ngắt toàn bộ Internet, thì tại sao việc gõ phím nhoay nhoáy trên laptop vẫn là "nhát dao" tàn sát sự đột phá? Một cuốn sổ tay rẻ tiền ẩn chứa ma thuật gì mà có thể bẻ gãy bản năng sinh tồn hàng triệu năm của bạn?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>
Vì tốc độ và ánh sáng màn hình chính là kẻ thù của chiều sâu!<br>
Theo <strong>Tiến hóa</strong>, nhịp gõ chớp nhoáng và ánh sáng màn hình kích hoạt Hạch hạnh nhân, ép não bật radar "Cảnh giác" sinh tồn (Sóng Beta căng thẳng). Còn theo <strong>Vật lý Lượng tử (Hiệu ứng Zeno)</strong>, ý tưởng bị phơi bày ra chữ quá nhanh chính là sự "đo lường thô bạo", ép mầm sáng tạo đang vô định phải đóng băng thành một khuôn mẫu rập khuôn.<br>
Ngược lại, tháo "Kính VR máy tính" xuống để dùng sổ tay sẽ tạo ra <strong>Lực ma sát vật lý</strong>. Nó ép tốc độ tư duy phanh lại, phát tín hiệu "an toàn tuyệt đối" để tắt radar sinh tồn. Khi đó, sóng Theta kiến tạo mở khóa, 100% dòng điện ATP cuộn lại thành một mũi khoan đâm xuyên qua mọi bế tắc.</p>
<blockquote>
<p><em>Màn hình gõ vội mỏi tay,<br/>Sổ ghi nét chậm mọc ngay rễ bền.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q3" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q3: TÁI KHUNG: ĐẬP VỠ ẢO TƯỞNG THU THẬP DỮ LIỆU<br>Tại sao khát khao "lướt mạng tìm thêm dữ liệu cho toàn diện" lại là nấm mồ chôn vùi sự khác biệt? Đâu là giới hạn sinh lý cốt lõi giữa việc làm một "Kiến trúc sư" kiến tạo kiệt tác và một gã "Thợ hồ" khuân vác thông tin?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>
Vì Đầu vào (Tiêu thụ) và Đầu ra (Kiến tạo) là 2 trạng thái sinh học triệt để bài xích nhau!<br>
Sự nguyên bản không đến từ phép CỘNG thông tin, mà nảy sinh từ <strong>Sự đói khát thông tin (Information Starvation)</strong>. Bạn là Kiến trúc sư, AI là Thợ hồ. Khi đang phác thảo cốt lõi móng nhà trong phòng kín, gọi AI ném thêm dữ kiện chỉ làm vỡ vụn sự tập trung và chắp vá ý tưởng. Đừng dùng dữ liệu rác để che đậy sự lười biếng đào sâu. Dám nhốt tâm trí vào sự thiếu thốn tột cùng là con đường duy nhất ép nó vắt kiệt kho báu độc bản từ bên trong.</p>
<blockquote>
<p><em>Nhặt gom dữ liệu tràn lan,<br/>Giết mầm sáng tạo lụi tàn héo hon.</em></p>
</blockquote>
</div>
</div>

<div class="dialogue-turn">
<h2 class="dialogue-prompt" id="q4" style="margin-top: 0; font-size: 1.25rem; font-weight: 600;">❓ Q4: MICRO-STEPS TÀN NHẪN THAO TÚNG NÃO BỘ<br>Mọi logic sẽ sụp đổ nếu cơ thể đã lỡ nghiện Dopamine ăn liền. Bằng thuật toán vi bước (Micro-step) thực chiến nào, bạn có thể thao túng tiềm thức, ép cơ thể tự nguyện khát khao sự "tĩnh lặng" mà không cần gồng ép bằng ý chí?</h2>
<div class="dialogue-response">
<p><strong>💡 ĐÁP:</strong><br>
Đừng chống lại cơn nghiện bằng ý chí, hãy thao túng não bộ bằng <strong>Hormone quyền lực</strong> qua 2 bước:</p>
<ol>
<li><strong>Tù đày 20 phút & Kỹ thuật Hộp rác (Brain Dump):</strong> Khóa mình với sổ bút. Khi cơn "vã AI" ập tới, đừng chống cự, hãy lấy bút viết thẳng câu hỏi ra mép giấy. Thao tác này đánh lừa não: <em>"Đã lưu, không mất đâu mà sợ"</em>, dập tắt ngay Cortisol lo âu. Qua 10 phút, Serotonin tràn ra, bạn chìm vào Dòng chảy (Flow).</li>
<li><strong>Kỹ thuật Bánh kẹp:</strong> Chỉ khi phác thảo xong bộ khung móng cốt lõi trên giấy, mới bật máy quăng cho AI "đắp thịt". Cảm giác đảo ngược vị thế, sai phái cỗ máy siêu việt làm nô lệ hầu hạ bản thiết kế của mình sẽ kích hoạt <strong>Endorphin</strong>. Nó lập trình lại nơ-ron, khiến não bạn tự "nghiện" vị thế làm chủ quyền lực này và thèm khát sự tĩnh lặng vào ngày mai.</li>
</ol>
<blockquote>
<p><em>Nhốt mình hai chục phút đầu,<br/>Vượt cơn bứt rứt trí sâu tỏ tường.</em></p>
</blockquote>
</div>
</div>

<p style="margin-top: 3rem; color: var(--ink-text-light);"><em>(Hệ thống đã mã hóa 4 rãnh Data cốt lõi...)</em></p>
"""

content_pattern = r'(<article class="ink-content ink-mode-dialogue">).*?(</article>)'
html_template = re.sub(content_pattern, r'\1\n' + new_content + r'\n\2', html_template, flags=re.DOTALL)

# update document title
title_pattern = r'<title>.*?</title>'
html_template = re.sub(title_pattern, '<title>[INKDOC-09] BẢN CHẤT SINH HỌC CỦA SỰ SÁNG TẠO</title>', html_template)

with open('logic09.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

