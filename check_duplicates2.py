import re
import os
import glob
import json
import urllib.request
import ssl
from collections import defaultdict

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

hash_map = defaultdict(list)
missing_on_r2 = []

for html_file, url in mapped_covers.items():
    if url.startswith("http"):
        try:
            req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5, context=ctx) as response:
                pass
        except urllib.error.HTTPError as e:
            if e.code in [403, 404]:
                missing_on_r2.append({"html": html_file, "url": url})
        except Exception as e:
            pass

print(f"Total missing/fallback on R2 (403/404): {len(missing_on_r2)}")

with open("duplicates_report.json", "w", encoding="utf-8") as f:
    json.dump(missing_on_r2, f, indent=2, ensure_ascii=False)
