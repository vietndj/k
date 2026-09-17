import re
import os
import glob
import json
import urllib.request
import ssl
from collections import defaultdict

# Ignore SSL certificate verification
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

manifest_file = "generate_manifest.py"
with open(manifest_file, "r", encoding="utf-8") as f:
    content = f.read()

mapping_block = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content)
mapping_text = mapping_block.group(1) if mapping_block else ""
pattern = re.compile(r'"([^"]+\.html)"\s*:\s*"([^"]+)"')
mapped_covers = dict(pattern.findall(mapping_text))

all_html_files = [os.path.basename(f) for f in glob.glob("*.html")]
missing_htmls = [f for f in all_html_files if f not in mapped_covers]
with open("missing_posters_report.json", "w", encoding="utf-8") as f:
    json.dump(missing_htmls, f, indent=2, ensure_ascii=False)

hash_map = defaultdict(list)
for html_file, url in mapped_covers.items():
    try:
        if url.startswith("http"):
            req = urllib.request.Request(url, method='HEAD')
            with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
                content_length = response.headers.get('Content-Length')
                etag = response.headers.get('ETag', '').strip('"')
                key = etag if etag else content_length
                if not key:
                    key = url # fallback if no header
                hash_map[key].append({"html": html_file, "url": url})
        else:
            local_path = url
            if local_path.startswith("./"): local_path = local_path[2:]
            if os.path.exists(local_path):
                size = str(os.path.getsize(local_path))
                hash_map[size].append({"html": html_file, "url": url})
    except Exception as e:
        print(f"Failed to check {url}: {e}")

duplicates_report = []
for key, items in hash_map.items():
    if len(items) > 1:
        duplicates_report.append(items)

with open("duplicates_report.json", "w", encoding="utf-8") as f:
    json.dump(duplicates_report, f, indent=2, ensure_ascii=False)

print(f"Missing HTMLs: {len(missing_htmls)}")
print(f"Duplicate groups found: {len(duplicates_report)}")
