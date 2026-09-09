# -*- coding: utf-8 -*-
"""
generate_all.py
Render 19 podcast HTML files to repo k and repo course.
"""

import os
import sys

sys.path.append(os.path.dirname(__file__))
from podcasts_batch1 import BATCH_1
from podcasts_batch2 import BATCH_2
from podcasts_batch3 import BATCH_3
from template import render_podcast_html

all_episodes = BATCH_1 + BATCH_2 + BATCH_3
print(f"Bắt đầu xuất bản {len(all_episodes)} bài podcast chuyên sâu...")

K_DIR = "/Users/vietmac/Documents/CODE/k"
COURSE_DIR = "/Users/vietmac/Documents/CODE/course"

for idx, ep in enumerate(all_episodes):
    slug = ep['slug']
    html_content = render_podcast_html(ep)
    
    # Kiểm tra an toàn
    assert "30NGAYVIRAL // BỐ CỤC ĐỌC CHUẨN" not in html_content, f"Phát hiện nhãn 30ngayviral trong {slug}!"
    assert "Tiempos Text" in html_content, f"Thiếu Tiempos Text trong {slug}!"
    assert "FD Aeonik Extended" in html_content, f"Thiếu FD Aeonik Extended trong {slug}!"
    assert "#0f172a" in html_content, f"Thiếu Slate 900 WCAG AAA trong {slug}!"
    
    # Ghi vào repo k
    k_path = os.path.join(K_DIR, slug)
    with open(k_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    # Ghi vào repo course
    course_path = os.path.join(COURSE_DIR, slug)
    with open(course_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"[{idx+1:02d}/19] Đã xuất bản thành công: {slug} (Kích thước: {len(html_content):,} bytes)")

print("\nHOÀN TẤT XUẤT BẢN TOÀN BỘ 19 BÀI PODCAST MỚI!")
