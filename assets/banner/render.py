import os
import glob
import re
import subprocess
import tempfile
import sys

template_path = "/Users/vietmac/.gemini/antigravity/brain/02681e0b-b6e1-407d-860d-e19a05dff8c9/poster_final.html"
banner_dir = "/Users/vietmac/Documents/CODE/k/assets/banner"
chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

with open(template_path, "r", encoding="utf-8") as f:
    template_html = f.read()

for i in range(1, 19):
    pattern = os.path.join(banner_dir, f"banner_style_{i}_*.jpg")
    matches = glob.glob(pattern)
    if not matches:
        print(f"Warning: No match for banner_style_{i}_*.jpg")
        continue
    
    img_path = matches[0]
    print(f"Processing style {i}: {os.path.basename(img_path)}")
    
    new_html = re.sub(r"background-image:\s*url\('[^']+'\);", f"background-image: url('file://{img_path}');", template_html)
    
    fd, temp_path = tempfile.mkstemp(suffix=".html")
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    out_png = os.path.join(banner_dir, f"composite_style_{i}.png")
    
    cmd = [
        chrome_bin,
        "--headless",
        f"--screenshot={out_png}",
        "--window-size=800,1066",
        f"file://{temp_path}"
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Saved: {out_png}")
    except subprocess.CalledProcessError as e:
        print(f"Error rendering {out_png}:\n{e.stderr.decode()}")
    finally:
        os.remove(temp_path)

print("All done!")
