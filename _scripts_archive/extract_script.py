import os
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

out_lines = []
base_dir = "/Users/vietmac/Documents/CODE/k"
for filename in files:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Try to find main content, or fallback to body
    content = soup.find('body')
    if not content:
        continue
        
    out_lines.append(f"\n\n# Source: {filename}")
    
    # We want to extract text blocks that might contain Q&A.
    # Look for headings, paragraphs, bold text
    for elem in content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'li', 'td', 'th']):
        text = elem.get_text(strip=True)
        if not text: continue
        
        # Avoid short nav links
        if len(text) < 10 and elem.name != 'th':
            continue
            
        out_lines.append(text)

with open('/Users/vietmac/Documents/CODE/k/scratch_extracted.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out_lines))
print("Extraction complete.")
