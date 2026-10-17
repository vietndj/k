import os
import re
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

base_dir = "/Users/vietmac/Documents/CODE/k"
output_file = os.path.join(base_dir, "extracted_knowledge", "tong_hop_chunk_4.md")
os.makedirs(os.path.dirname(output_file), exist_ok=True)

md_content = ["# TỔNG HỢP KIẾN THỨC Q&A (CHUNK 4)\n\n"]

qa_patterns = re.compile(r'(câu \d+|hỏi|tại sao|làm thế nào|\?|q&a)', re.IGNORECASE)

for f in files:
    path = os.path.join(base_dir, f)
    if not os.path.exists(path):
        continue
    
    html = open(path, encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # We will traverse all tags and if a tag is a header, we check if it is a question
    # If it is, we collect the content until the next header of the same or higher level
    
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    extracted_qas = []
    
    for i, header in enumerate(headers):
        text = header.get_text(strip=True)
        # Identify if it's a Q&A candidate
        if qa_patterns.search(text):
            # It's a question
            question = text
            answer_parts = []
            
            # Find all siblings until next header
            sibling = header.find_next_sibling()
            while sibling:
                if sibling.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    # Stop if it's another header, unless it's a sub-header (optional logic, but let's just break on major headers h1/h2)
                    # Actually, just stop if it's ANY header that looks like a question or is h1/h2/h3. 
                    # To keep it simple, we stop on any heading that is same level or higher
                    level_current = int(header.name[1])
                    level_sibling = int(sibling.name[1])
                    if level_sibling <= level_current:
                        break
                    
                # If it's a paragraph, list, or blockquote, table
                if sibling.name in ['p', 'ul', 'ol', 'blockquote', 'table']:
                    answer_parts.append(sibling.get_text(separator=' ', strip=True))
                elif sibling.name in ['h3', 'h4', 'h5', 'h6']:
                    answer_parts.append(f"**{sibling.get_text(strip=True)}**")
                
                sibling = sibling.find_next_sibling()
                
            if answer_parts:
                extracted_qas.append((question, "\n\n".join(answer_parts)))
                
    if extracted_qas:
        md_content.append(f"## Từ file: `{f}`\n")
        for q, a in extracted_qas:
            md_content.append(f"### Q: {q}\n\n**A:** {a}\n\n---\n")

with open(output_file, 'w', encoding='utf-8') as out_f:
    out_f.write("\n".join(md_content))

print(f"Extraction successful, saved to {output_file}")
