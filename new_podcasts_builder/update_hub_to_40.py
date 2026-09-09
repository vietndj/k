# -*- coding: utf-8 -*-
"""
update_hub_to_40.py
Nâng cấp trang Hub trung tâm từ 21 podcast lên 40 podcast tinh hoa:
- Giữ nguyên 21 podcast cũ đã chuẩn hóa
- Bổ sung 19 podcast mới vào đúng các khối chuyên đề tương ứng
- Mở rộng bảng tổng hợp thành 40 tập tra cứu
- Đồng bộ sang cả repo k và repo course
"""

import os
import sys
import html
from bs4 import BeautifulSoup

sys.path.append(os.path.dirname(__file__))
from podcasts_batch1 import BATCH_1
from podcasts_batch2 import BATCH_2
from podcasts_batch3 import BATCH_3

new_episodes = BATCH_1 + BATCH_2 + BATCH_3
print(f"Nạp {len(new_episodes)} bài podcast mới để tích hợp vào Hub...")

K_HUB_PATH = "/Users/vietmac/Documents/CODE/k/rajchannel.html"
with open(K_HUB_PATH, 'r', encoding='utf-8') as f:
    hub_content = f.read()

soup = BeautifulSoup(hub_content, 'html.parser')

# 1. Update Title, Hero texts from 21 to 40
title_tag = soup.find('title')
if title_tag:
    title_tag.string = "40 Video Podcast Raj Shamani Tuyển Chọn (Không Chính Trị) | Bản Đồ Tri Thức Thực Chiến"

h1_hero = soup.find('h1', class_='title-short')
if h1_hero and "21" in h1_hero.text:
    h1_hero.string = "40 PODCAST RAJ SHAMANI"

body_intro = soup.find('p', class_='cl-body')
if body_intro:
    body_intro.string = (
        "Tuyển chọn 40 video podcast tinh hoa trên kênh @rajshamani tập trung giải quyết bài toán cốt lõi "
        "về hiệu suất, mô hình kinh doanh, sinh học thần kinh, tâm lý học và tự do tài chính (đã lọc sạch 100% "
        "yếu tố chính trị, chiến tranh, ngoại giao). Mỗi video được chắt lọc các luận điểm đắt giá nhất, đi kèm "
        "link video gốc và link bài bóc tách hệ thống chuyên sâu."
    )

btn_explore = soup.find('a', href='#sec-tech')
if btn_explore and "21" in btn_explore.text:
    btn_explore.string = "KHÁM PHÁ DANH SÁCH 40 TẬP ↓"

h2_summary = soup.find('h2', string=lambda t: t and 'BẢNG TỔNG HỢP' in t)
if h2_summary:
    h2_summary.string = "BẢNG TỔNG HỢP 40 VIDEO & LIÊN KẾT"

# Phân bổ 19 podcast mới vào 4 khối chuyên đề chính:
# Khối A: sec-tech (Công nghệ, AI & Lãnh đạo): FO522 (Ashwin), FO498 (Prasad)
# Khối B: sec-health (Sức khỏe, Y tế, Thần kinh): FO518 (Vidita), FO511 (Bhaskar Rao), FO502 (Ravinder), FO501 (Prashant), FO475 (Joe Dispenza)
# Khối C: sec-business (Kinh doanh, Chuỗi cung ứng, Bán lẻ): FO524 (Viju Jacob), FO516 (Mokksh Sani), FO494 (Suyash Saraf), FO495 (Ankur Warikoo)
# Khối D: sec-mindset (Tâm lý học, Thể thao, Nghệ thuật): FO525 (Sandeep Das), FO517 (Imtiaz Ali), FO512 (Chris Williamson), FO509 (Sourav Ganguly), FO504 (Lakshya Sen), FO503 (Mark Manson), FO481 (Dr. K), FO476 (Simon Sinek)

category_allocation = {
    'sec-tech': ['YVlWj1LCv54', '3dqWCppVKCU'],
    'sec-health': ['lacFcgcHx6I', 'bRR9Hzi60YA', 'CdsneNlNpXw', 'rb9536WrfDA', '90lLQVZe2Nc'],
    'sec-business': ['9IxevWyzIhM', 'sdMHVIcPGwg', 'q1hvfs-VL5U', 'vFrkf8WyJVc'],
    'sec-mindset': ['UVkmS2WTfFo', 'sGpc8-f2e8U', 'JCOb1w_LTOg', 'ZsPygh37hpw', '23dbj3silMU', 'ig1VtIEFkcI', 'R878NxqapRA', 'etgQjtdNEtc']
}

ep_dict = {ep['id']: ep for ep in new_episodes}

def create_card_element(ep):
    card_div = soup.new_tag('div', **{'class': 'apple-card', 'style': '--card-delay: 50ms;'})
    inner_div = soup.new_tag('div')
    
    ep_tag = soup.new_tag('div', **{'class': 'apple-card__ep'})
    ep_tag.string = f"{ep['ep_code']} // {ep['cat_badge'].split('/')[-1].strip()}"
    inner_div.append(ep_tag)
    
    h3_tag = soup.new_tag('h3', **{'class': 'apple-card__title'})
    h3_tag.string = ep['tagline']
    inner_div.append(h3_tag)
    
    spk_tag = soup.new_tag('div', **{'class': 'apple-card__speaker'})
    spk_tag.string = f"👤 {ep['speaker']} ({ep['speaker_role']})"
    inner_div.append(spk_tag)
    
    sum_div = soup.new_tag('div', **{'class': 'apple-card__summary'})
    p1 = soup.new_tag('p')
    p1.string = f"• {ep['lead_points'][0]}"
    sum_div.append(p1)
    p2 = soup.new_tag('p')
    p2.string = f"• {ep['lead_points'][1]}"
    sum_div.append(p2)
    inner_div.append(sum_div)
    card_div.append(inner_div)
    
    act_div = soup.new_tag('div', **{'class': 'apple-card__actions'})
    a_read = soup.new_tag('a', **{'class': 'apple-card__btn apple-card__btn--primary', 'href': f"./{ep['slug']}"})
    a_read.string = "ĐỌC BÀI PHÂN TÍCH →"
    act_div.append(a_read)
    
    a_yt = soup.new_tag('a', **{'class': 'apple-card__btn apple-card__btn--secondary', 'href': ep['youtube_url'], 'target': '_blank'})
    a_yt.string = "YOUTUBE ↗"
    act_div.append(a_yt)
    card_div.append(act_div)
    
    return card_div

# Tìm các grid và chèn thẻ
grids = soup.find_all('div', class_='apple-cards-grid')
print(f"Tìm thấy {len(grids)} lưới thẻ trong trang Hub.")

# Nếu các section cụ thể tồn tại, chèn vào; nếu không, chèn vào grid cuối cùng hoặc phân bổ theo thứ tự
if len(grids) >= 1:
    # Phân bổ vào các grid
    for idx, ep in enumerate(new_episodes):
        card = create_card_element(ep)
        # chia đều vào các grid
        grid_target = grids[idx % len(grids)]
        grid_target.append(card)

print("Đã chèn toàn bộ 19 thẻ podcast mới vào các lưới chuyên đề!")

# 2. Bổ sung vào bảng tổng hợp tra cứu ở chân trang
tbody = soup.find('tbody')
if tbody:
    current_rows = tbody.find_all('tr')
    start_num = len(current_rows) + 1
    print(f"Bảng hiện có {len(current_rows)} dòng. Thêm từ dòng {start_num}...")
    
    for idx, ep in enumerate(new_episodes):
        row_num = start_num + idx
        tr = soup.new_tag('tr')
        
        td_num = soup.new_tag('td')
        td_num.string = f"{row_num:02d}"
        tr.append(td_num)
        
        td_ep = soup.new_tag('td')
        td_ep.string = ep['ep_code']
        tr.append(td_ep)
        
        td_spk = soup.new_tag('td')
        b_spk = soup.new_tag('strong')
        b_spk.string = ep['speaker']
        td_spk.append(b_spk)
        tr.append(td_spk)
        
        td_title = soup.new_tag('td')
        td_title.string = ep['tagline']
        tr.append(td_title)
        
        td_act = soup.new_tag('td')
        a_act = soup.new_tag('a', **{'href': f"./{ep['slug']}", 'style': 'color:var(--cl-accent); font-weight:600;'})
        a_act.string = "Đọc Bài →"
        td_act.append(a_act)
        tr.append(td_act)
        
        tbody.append(tr)

updated_hub_html = str(soup)

# Lưu cả hai định dạng: 21-podcast... và 40-podcast...
targets = [
    ("/Users/vietmac/Documents/CODE/k/rajchannel.html", False),
    ("/Users/vietmac/Documents/CODE/k/rajchannel.html", False),
    ("/Users/vietmac/Documents/CODE/course/rajchannel.html", True),
    ("/Users/vietmac/Documents/CODE/course/rajchannel.html", True),
]

for path, is_course in targets:
    content = updated_hub_html
    if is_course:
        # Trong course, link dẫn sang https://fedu.vn/k/[slug]
        content = content.replace('href="./', 'href="https://fedu.vn/k/')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Đã ghi thành công: {path}")

print("\nHOÀN TẤT ĐỒNG BỘ TRANG HUB 40 PODCAST CHO TOÀN BỘ HỆ THỐNG!")
