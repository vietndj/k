import json
import urllib.request
import urllib.error
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

posts_file = "/Users/vietmac/Documents/CODE/k/posts-manifest.json"

with open(posts_file, "r", encoding="utf-8") as f:
    posts = json.load(f)["posts"]

def check_url(post):
    cover = post.get("cover_image", "")
    if not cover:
        return {"filename": post.get("filename"), "status": "Empty URL"}
    
    # URL encode if there are spaces (not strictly necessary but safe)
    url_parts = list(urllib.parse.urlparse(cover))
    url_parts[2] = urllib.parse.quote(url_parts[2])
    safe_url = urllib.parse.urlunparse(url_parts)
    
    try:
        req = urllib.request.Request(safe_url, method='HEAD')
        with urllib.request.urlopen(req, timeout=3) as response:
            size = int(response.headers.get('Content-Length', 0))
            if size < 500: # Very small file might be corrupted
                return {"filename": post.get("filename"), "url": cover, "status": f"Too small ({size} bytes)"}
            return None
    except urllib.error.HTTPError as e:
        return {"filename": post.get("filename"), "url": cover, "status": f"HTTP Error {e.code}"}
    except Exception as e:
        return {"filename": post.get("filename"), "url": cover, "status": f"Connection Error"}

print(f"Auditing {len(posts)} posts...")
errors = []

# Use multi-threading to speed up HTTP requests
with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(check_url, posts)
    for res in results:
        if res:
            errors.append(res)

print(f"\nFound {len(errors)} errors out of {len(posts)} posts.")
for e in errors[:20]:
    print(f"- {e['filename']}: {e['status']} ({e.get('url','')})")
if len(errors) > 20:
    print(f"... and {len(errors)-20} more.")

# Write full report
with open("/Users/vietmac/Documents/CODE/Quản gia/bang.md", "w", encoding="utf-8") as f:
    f.write("# Audit Toàn Diện Banners (Lỗi Hiển Thị)\n\n")
    f.write("| STT | Tên file HTML | Trạng thái lỗi | URL bị lỗi |\n")
    f.write("|---|---|---|---|\n")
    for i, e in enumerate(errors, 1):
        f.write(f"| {i} | {e['filename']} | {e['status']} | {e.get('url','-')} |\n")
