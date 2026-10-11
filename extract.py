import os
import glob
from bs4 import BeautifulSoup

files = [
    "logickenh-danghuong-yquan.html",
    "logickenh-gymcoach.html",
    "logickenh-he-thong-hoa-storytelling-lat-cat-vi-mo.html",
    "logickenh-he-thong-hoa-tu-duy-view-chat-luong.html",
    "logickenh-huuviet-pa1.html",
    "logickenh-huuviet-pa2.html",
    "logickenh-huuviet-pa3.html",
    "logickenh-huuviet.html",
    "logickenh-katlynn.html",
    "logickenh-leminhduc.html"
]

out = []
for f in files:
    path = os.path.join("/Users/vietmac/Documents/CODE/k", f)
    if not os.path.exists(path):
        continue
    html = open(path, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    out.append(f"--- FILE: {f} ---\n{text}\n")

with open("/Users/vietmac/Documents/CODE/k/scratch_extracted.txt", "w", encoding="utf-8") as outf:
    outf.write("\n".join(out))
print("Done")
