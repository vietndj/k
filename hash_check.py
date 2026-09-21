import os
import hashlib
from collections import defaultdict

fixes_dir = "/Users/vietmac/Documents/CODE/k/assets/images_gen_fixes/"
hashes = defaultdict(list)

for f in os.listdir(fixes_dir):
    if f.endswith(".jpg"):
        path = os.path.join(fixes_dir, f)
        with open(path, "rb") as file:
            h = hashlib.md5(file.read()).hexdigest()
            hashes[h].append(f)

duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
print(f"Total unique images: {len(hashes)}")
print(f"Total duplicates: {len(duplicates)}")
for k, v in duplicates.items():
    print(f"{len(v)} duplicates: {v[:5]}")
