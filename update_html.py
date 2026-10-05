import re
import sys

ids = {
    "Cry_from_the_Frozen_Pass+.mp3": "17nRCnc6t48YbapJEIYF0CqbhvXOqKvP6",
    "The_Final_Surge+.mp3": "1IVX8lpxYcaTHpzRat9s1In25eo_DseWc",
    "Song_of_the_Red_Earth+.mp3": "15UArirfgNmY2fGzfcx4qHidi2xeBJvSB",
    "The_Gathering_at_the_Ridge+.mp3": "1a8N0hfT9XW-iCjmHuykTME9_MbbCsuA6"
}

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'r', encoding='utf-8') as file:
    content = file.read()

for f, file_id in ids.items():
    pattern = r'<div class="relative w-full overflow-hidden rounded-lg"[^>]*>.*?<em>\*Thay DUMMY_VIDEO_ID bằng ID video YouTube của bài ' + re.escape(f) + r'\*</em>\s*</div>'
    replacement = f'''<audio controls class="w-full">
                            <source src="https://drive.google.com/uc?export=download&id={file_id}" type="audio/mpeg">
                            Trình duyệt của bạn không hỗ trợ thẻ audio.
                        </audio>'''
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'w', encoding='utf-8') as file:
    file.write(content)
