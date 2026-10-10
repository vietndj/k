import re
import requests
from concurrent.futures import ThreadPoolExecutor

url = "https://raw.githubusercontent.com/vietndj/k/main/banner.html"
html = requests.get(url).text
images = list(set(re.findall(r'src="(https://media.fedu.vn/banner/[^"]+)"', html)))

def check_size(img_url):
    try:
        r = requests.head(img_url, timeout=5)
        if r.status_code == 200:
            size = int(r.headers.get('content-length', 0))
            if size == 0:
                return f"{img_url} (0 bytes)"
        else:
            return f"{img_url} ({r.status_code})"
    except:
        return f"{img_url} (Error)"
    return None

print("Checking sizes...")
issues = []
with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(check_size, images)
    for r in results:
        if r:
            issues.append(r)

if issues:
    print("\nIssues found:")
    for i in issues:
        print(i)
else:
    print("All images are > 0 bytes and 200 OK.")
