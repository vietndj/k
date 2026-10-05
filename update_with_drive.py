import subprocess
import re

files = [
    "Cry_from_the_Frozen_Pass+.mp3",
    "The_Final_Surge+.mp3",
    "Song_of_the_Red_Earth+.mp3",
    "The_Gathering_at_the_Ridge+.mp3"
]

ids = {}

for f in files:
    print(f"Getting link for {f}...")
    res = subprocess.run(["rclone", "link", f"gdrive:Music_Epic_Masterclass/{f}"], capture_output=True, text=True)
    link = res.stdout.strip()
    m = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    if m:
        ids[f] = m.group(1)
        print(f"ID: {ids[f]}")
    else:
        print(f"Failed to get link for {f}: {link}")

if not ids:
    print("Failed to get any IDs.")
    exit(1)

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
    f.write(content)

print("HTML updated successfully.")

