import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
import ssl

# Ignore SSL errors just in case
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('/Users/vietmac/Documents/CODE/k/database.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

urls = [(p['id'], p['image']) for p in db['posters']]
total = len(urls)
print(f"Checking {total} images...")

broken = []

def check_url(item):
    pid, url = item
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=5) as response:
            if response.status >= 400:
                return (pid, url, response.status)
    except urllib.error.HTTPError as e:
        return (pid, url, e.code)
    except Exception as e:
        return (pid, url, str(e))
    return None

with ThreadPoolExecutor(max_workers=50) as executor:
    futures = {executor.submit(check_url, item): item for item in urls}
    count = 0
    for future in as_completed(futures):
        count += 1
        if count % 500 == 0:
            print(f"Checked {count}/{total}...")
        res = future.result()
        if res:
            broken.append(res)

print(f"\nFound {len(broken)} broken images.")
with open('broken_images.json', 'w') as f:
    json.dump(broken, f, indent=2)

if broken:
    print("Sample of broken images:")
    for b in broken[:10]:
        print(b)
