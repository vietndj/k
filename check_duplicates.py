import re
from collections import Counter

with open("generate_manifest.py", "r") as f: content = f.read()
mapping_text = re.search(r'cover_mapping\s*=\s*\{([\s\S]*?)\}', content).group(1)
current_covers = dict(re.findall(r'"([^"]+\.html)"\s*:\s*"([^"]+)"', mapping_text))

urls = list(current_covers.values())
counter = Counter(urls)
duplicates = {url: count for url, count in counter.items() if count > 1}

print(f"Total unique HTMLs mapped: {len(current_covers)}")
print(f"Total unique images used: {len(set(urls))}")
print(f"Images mapped multiple times: {len(duplicates)}")
if duplicates:
    for url, count in list(duplicates.items())[:10]:
        print(f"  {url}: mapped {count} times")
