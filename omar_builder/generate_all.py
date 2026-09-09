# -*- coding: utf-8 -*-
"""
generate_all.py
Render 40 trang HTML phân tích chi tiết podcast Omar Eltakrori
và lưu vào cả /Users/vietmac/Documents/CODE/k/ và /Users/vietmac/Documents/CODE/course/
"""
import os
import sys

from template import render_omar_podcast_html
from episodes_batch1 import BATCH_1
from episodes_batch2 import BATCH_2
from episodes_batch3 import BATCH_3
from episodes_batch4 import BATCH_4

ALL_EPISODES = BATCH_1 + BATCH_2 + BATCH_3 + BATCH_4
print(f"Tổng số tập chuẩn bị xuất bản: {len(ALL_EPISODES)}")

DIR_K = "/Users/vietmac/Documents/CODE/k"
DIR_COURSE = "/Users/vietmac/Documents/CODE/course"

os.makedirs(DIR_K, exist_ok=True)
os.makedirs(DIR_COURSE, exist_ok=True)

success_count = 0
for idx, ep in enumerate(ALL_EPISODES, 1):
    html_content = render_omar_podcast_html(ep)
    slug = ep['slug']
    
    path_k = os.path.join(DIR_K, slug)
    with open(path_k, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    path_course = os.path.join(DIR_COURSE, slug)
    with open(path_course, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"[{idx:02d}/40] {ep['ep_code']}: Đã lưu {slug} ({len(html_content):,} bytes)")
    success_count += 1

print(f"\n🎉 THÀNH CÔNG RỰC RỠ: Đã xuất bản hoàn tất {success_count}/40 trang HTML vào cả repo k và course!")
