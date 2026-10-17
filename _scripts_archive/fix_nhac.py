import os
import shutil
import re
from urllib.parse import quote

# 1. Copy files
src_dir = os.path.expanduser("~/Downloads/giong hat")
dest_dir = "/Users/vietmac/Documents/CODE/k/assets/audio"
os.makedirs(dest_dir, exist_ok=True)

print("Copying audio files...")
for f in os.listdir(src_dir):
    if f.endswith(".mp3"):
        shutil.copy2(os.path.join(src_dir, f), os.path.join(dest_dir, f))

# 2. Update HTML
html_path = "/Users/vietmac/Documents/CODE/k/nhac.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update Titles in TOC and Body
replacements = {
    "1. Nordic Ritual (Nghi lễ Bắc Âu)": "1. Nghi Lễ Bắc Âu",
    "2. Rhythmic Chant (Hô vang nhóm)": "2. Khúc Tráng Ca Tập Thể",
    "3. South African Vocals (Xướng Họa Nam Phi)": "3. Xướng Họa Nam Phi",
    "4. Percussive Vocal Ensemble": "4. Nhịp Gõ Thanh Âm",
    "5. Call-and-Response Vocal": "5. Xướng Họa Hùng Ca",
    "6. Voice as Rhythm Instrument": "6. Hơi Thở Dẫn Nhịp"
}
for old, new in replacements.items():
    content = content.replace(old, new)

# Define description blocks
desc_4 = """
                <div class="prose-narrative mb-6">
                    <p><strong>Nội dung & Tác dụng của Prompt:</strong></p>
                    <ul class="list-disc pl-6 space-y-2 mt-4">
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Giọng Hát</span>
                                <span>Giọng người đóng vai trò hoàn toàn như một bộ gõ trong dàn nhạc. Các âm tiết cực ngắn như "ha", "ho", "hey", khô và dứt khoát, khóa chặt vào từng nhịp trống.</span>
                            </div>
                        </li>
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Cấu Trúc 10s</span>
                                <span>Mở đầu tối giản bằng các giọng nhấn thả đúng nhịp, tiếng vỗ tay khô khốc và nhịp tim dồn dập, tạo sự tập trung tuyệt đối.</span>
                            </div>
                        </li>
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Dẫn Nhịp</span>
                                <span>Nhịp điệu hòa quyện hoàn hảo với tiếng trống Taiko, đẩy năng lượng lên một cách chắc nịch, không lấn lướt dàn nhạc hay làm mờ đi lời nói của MC.</span>
                            </div>
                        </li>
                    </ul>
                </div>
"""

desc_5 = """
                <div class="prose-narrative mb-6">
                    <p><strong>Nội dung & Tác dụng của Prompt:</strong></p>
                    <ul class="list-disc pl-6 space-y-2 mt-4">
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Xướng & Họa</span>
                                <span>Sự giao thoa đa văn hóa: một giọng chính cất tiếng gọi (call), và một nhóm tập thể đáp lời (response) bằng một cụm âm thanh đứt đoạn, sắc bén và hùng hồn.</span>
                            </div>
                        </li>
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Tịnh Tiến</span>
                                <span>Cấu trúc tăng dần đều qua từng nhịp trống và tiếng dậm chân. Bắt đầu từ 6 người rồi lan tỏa thành 14 người, liên tục bồi đắp khí thế.</span>
                            </div>
                        </li>
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Ứng Dụng</span>
                                <span>Cao trào cuối bùng nổ cùng dàn nhạc, rất thích hợp cho video giới thiệu (intro) hoặc trailer phim kịch tính, thể hiện tinh thần không khuất phục.</span>
                            </div>
                        </li>
                    </ul>
                </div>
"""

desc_6 = """
                <div class="prose-narrative mb-6">
                    <p><strong>Nội dung & Tác dụng của Prompt:</strong></p>
                    <ul class="list-disc pl-6 space-y-2 mt-4">
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Âm Cấu Cơ Thể</span>
                                <span>Giọng người đóng vai trò như một nhạc cụ giữ nhịp (snare, woodblock) với các tiếng thì thầm "sh-ha", tiếng lấy hơi sắc bén, chính xác tuyệt đối.</span>
                            </div>
                        </li>
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Ngắt Nhịp</span>
                                <span>Mở đầu hoàn toàn bằng thanh âm tự nhiên của cơ thể người. Năng lượng mãnh liệt, hùng tráng như một đội quân xuất trận, không cần lời ca.</span>
                            </div>
                        </li>
                        <li>
                            <div class="flex items-start gap-4">
                                <span class="hig-badge shrink-0 mt-1">Cắt Gãy</span>
                                <span>Âm thanh cắt gãy gọn ở giây thứ 50 (cut abruptly), không ngân vang, tạo một nhịp ngắt sắc lẹm cho các pha chuyển cảnh kỹ xảo.</span>
                            </div>
                        </li>
                    </ul>
                </div>
"""

# Chèn description vào sau <button class="... Copy Prompt ...</button>\n                </div>
# Tìm đúng vị trí mục 4
content = re.sub(
    r'(<h2 class="font-display font-semibold text-2xl">4\. Nhịp Gõ Thanh Âm</h2>.*?</button>\s*</div>)',
    r'\1\n' + desc_4,
    content,
    flags=re.DOTALL
)
# Mục 5
content = re.sub(
    r'(<h2 class="font-display font-semibold text-2xl">5\. Xướng Họa Hùng Ca</h2>.*?</button>\s*</div>)',
    r'\1\n' + desc_5,
    content,
    flags=re.DOTALL
)
# Mục 6
content = re.sub(
    r'(<h2 class="font-display font-semibold text-2xl">6\. Hơi Thở Dẫn Nhịp</h2>.*?</button>\s*</div>)',
    r'\1\n' + desc_6,
    content,
    flags=re.DOTALL
)

# 3. Replace GDrive links with local assets links
# Dùng Regex để tìm tên file trong <span ...> và gán xuống thẻ <source src="..."> ngay dưới nó.
def replace_source(match):
    span_content = match.group(1)
    file_name_match = re.search(r'</svg>\s*(.+?\.mp3)\s*</span>', span_content)
    if not file_name_match:
        return match.group(0) # fail safe
    file_name = file_name_match.group(1).strip()
    # file_name có thể chứa khoảng trắng, encode nó
    encoded_file_name = quote(file_name)
    local_src = f'assets/audio/{encoded_file_name}'
    
    # Thay thế phần source bên dưới
    full_block = match.group(0)
    new_block = re.sub(r'<source src="https://drive\.usercontent\.google\.com/download\?id=[^"]+"', f'<source src="{local_src}"', full_block)
    # Thay thế cả dạng docs.google.com nếu có
    new_block = re.sub(r'<source src="https://docs\.google\.com/[^"]+"', f'<source src="{local_src}"', new_block)
    
    return new_block

# Regex matching the block from <span class="font-medium text-sm text-slate-700 flex items-center gap-2"> to the </audio>
content = re.sub(r'(<span class="font-medium text-sm text-slate-700 flex items-center gap-2">.*?</audio>)', replace_source, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("HTML updated successfully!")

