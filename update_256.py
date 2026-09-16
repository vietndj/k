with open("generate_manifest.py", "r", encoding="utf-8") as f:
    content = f.read()

import re
# find the end of cover_mapping
pattern = r'("shubhanshu-shukla-astronaut-space-zero-gravity-podcast\.html": "https://pub[^"]+"\n\s*)}'

replacement = r'\1,\n        "bill-ackman-kich-ban-dau-tu.html": "./assets/covers/poster_256_mad_men.jpg"\n    }'

new_content = re.sub(pattern, replacement, content)

with open("generate_manifest.py", "w", encoding="utf-8") as f:
    f.write(new_content)
