#!/bin/bash
FILES=("Cry_from_the_Frozen_Pass+.mp3" "The_Final_Surge+.mp3" "Song_of_the_Red_Earth+.mp3" "The_Gathering_at_the_Ridge+.mp3")
for f in "${FILES[@]}"; do
  echo "Getting link for $f"
  id=$(rclone link "gdrive:Music_Epic_Masterclass/$f" | grep -o "id=.*" | cut -d= -f2)
  echo "ID is $id"
  # Replace in html
  python3 -c "
import sys, re
f = sys.argv[1]
fid = sys.argv[2]
with open('nhac.html', 'r') as file:
    content = file.read()
pattern = r'<div class=\"relative w-full overflow-hidden rounded-lg\"[^>]*>.*?<em>\\\*Thay DUMMY_VIDEO_ID bằng ID video YouTube của bài ' + re.escape(f) + r'\\\*</em>\s*</div>'
replacement = f'''<audio controls class=\"w-full\">
                            <source src=\"https://drive.google.com/uc?export=download&id={fid}\" type=\"audio/mpeg\">
                            Trình duyệt của bạn không hỗ trợ thẻ audio.
                        </audio>'''
content = re.sub(pattern, replacement, content, flags=re.DOTALL)
with open('nhac.html', 'w') as file:
    file.write(content)
" "$f" "$id"
done
