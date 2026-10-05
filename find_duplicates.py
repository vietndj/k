import json
import re
import os
import hashlib
from collections import Counter

# Known anchor hashes
ANCHOR_HASHES = {
    "1094380a9c2a9f2b7fbc9c13c196a733": "viet_real_master_crop_006",
    "ea8f89a7486a4da71d8769ecb1b94874": "viet_avatar_002"
}

def get_md5(filepath):
    if not os.path.exists(filepath): return None
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

with open("generate_manifest.py", "r") as f: content = f.read()
mapping_text = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content).group(1)
current_covers = dict(re.findall(r'"([^"]+\.html)"\s*:\s*"([^"]+)"', mapping_text))

with open("master_poster_tasks.json", "r") as f: master = json.load(f)
master_dict = {t["target_html"]: t for t in master}

urls = list(current_covers.values())
url_counts = Counter(urls)

faulty_htmls = []
report_data = []

for html, url in current_covers.items():
    local_path = url.replace("./", "")
    md5_hash = get_md5(local_path)
    
    is_duplicate_mapped = url_counts[url] > 1
    is_anchor_copy = md5_hash in ANCHOR_HASHES
    
    if is_duplicate_mapped or is_anchor_copy:
        faulty_htmls.append(html)
        task = master_dict.get(html, {})
        report_data.append({
            "html": html,
            "title": task.get("target_title", ""),
            "movie": task.get("movie", ""),
            "reason": "Anchor Copy" if is_anchor_copy else f"Mapped {url_counts[url]} times",
            "url": url
        })

with open("duplicate_report.json", "w") as f:
    json.dump(report_data, f, indent=4, ensure_ascii=False)

print(f"Total faulty/duplicate items found: {len(report_data)}")
