import sys
import os
from bs4 import BeautifulSoup
import markdownify
import re

files = [
    "logic24.html", "logic25.html", "logic26.html", "logic27.html", 
    "logic28.html", "logic29.html", "logic30.html", 
    "logickenh-baohiem.html", "logickenh-bep-duc.html", 
    "logickenh-cac-trend-ap-dung-trong-lam-noi-dung-the-nao.html"
]

output_file = "/Users/vietmac/Documents/CODE/k/extracted_knowledge/tong_hop_chunk_3.md"
base_dir = "/Users/vietmac/Documents/CODE/k"

with open(output_file, 'w', encoding='utf-8') as out_f:
    out_f.write("# TỔNG HỢP KIẾN THỨC (CHUNK 3)\n\n")
    
    for filename in files:
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            print(f"File không tồn tại: {filepath}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        main_content = soup.find('article') or soup.find('main') or soup.body
        
        if main_content:
            # Loại bỏ các thẻ không cần thiết
            for tag in main_content(['script', 'style', 'nav', 'header', 'footer']):
                tag.decompose()
            
            # Có thể extract riêng Q&A nếu cần, nhưng chuyển toàn bộ sang Markdown cũng rất tốt
            md = markdownify.markdownify(str(main_content), heading_style="ATX", wrap=False)
            
            # Xóa các dòng trống thừa
            md = re.sub(r'\n{3,}', '\n\n', md)
            
            # Ghi vào file
            out_f.write(f"## NGUỒN: {filename}\n\n")
            out_f.write(md.strip())
            out_f.write("\n\n---\n\n")
            print(f"Đã xử lý: {filename}")

print(f"Đã lưu kết quả vào {output_file}")
