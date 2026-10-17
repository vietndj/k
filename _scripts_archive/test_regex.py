import re
with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'r') as file:
    content = file.read()
f = "Cry_from_the_Frozen_Pass+.mp3"
pattern = r'<div class="relative w-full overflow-hidden rounded-lg"[^>]*>.*?<em>\*Thay DUMMY_VIDEO_ID bằng ID video YouTube của bài ' + re.escape(f) + r'\*</em>\s*</div>'
m = re.search(pattern, content, flags=re.DOTALL)
if m:
    print("Match found!")
else:
    print("No match.")
