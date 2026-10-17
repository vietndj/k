import glob
import os
import hashlib

covers_dir = "/Users/vietmac/Documents/CODE/k/assets/covers"
ERROR_MD5 = "cb7dcd0abfd677456c788374f1e829b0"

def get_md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

error_webps = []
for filepath in glob.glob(os.path.join(covers_dir, "poster_batch_*.webp")):
    if get_md5(filepath) == ERROR_MD5:
        error_webps.add(os.path.basename(filepath))

print(f"Found {len(error_webps)} error files in folder.")
