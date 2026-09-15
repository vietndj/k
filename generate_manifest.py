import os
import glob
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup

def generate():
    files = glob.glob("*.html")
    exclude = ["index.html", "404.html", "rajchannel.html", "fix-url.html", "skills.html", "dom.html"]
    posts = []

    for f in files:
        if f in exclude:
            continue
            
        filepath = os.path.join(os.getcwd(), f)
        stat = os.stat(filepath)
        mod_time = datetime.fromtimestamp(stat.st_mtime).isoformat()
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else f.replace('.html', '').replace('-', ' ').title()
            
            # Simple excerpt (first paragraph with text > 50 chars)
            excerpt = "Bài viết chuyên sâu từ kho dữ liệu Antigravity."
            for p in soup.find_all('p'):
                text = p.text.strip()
                if len(text) > 50:
                    excerpt = text[:150] + "..."
                    break
                    
            # Determine category based on filename keywords
            fname_lower = f.lower()
            if 'broll' in fname_lower or 'quay' in fname_lower:
                cat = "broll"
                cat_label = "🎬 B-Roll & Cảnh Trám"
            elif 'podcast' in fname_lower:
                cat = "science"
                cat_label = "🧠 Tâm Lý & Não Bộ"
            elif 'science' in fname_lower:
                cat = "science"
                cat_label = "🧠 Khoa Học"
            else:
                cat = "other"
                cat_label = "📌 Bài Viết"
                
        
        cover_mapping = {
            # Top 4 bài mới nhất trên trang chủ
            "cong-thuc-1-kenh-de-phat-trien-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_growth_playbook.jpg",
            "so-tay-thuc-chien-khoi-nghiep-ky-nguyen-ai-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_khoi_nghiep_ai.jpg",
            "how-to-teach-and-grow-rich-business-model-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_day_hoc_lam_giau.jpg",
            "10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_protocols_nao_bo.jpg",
            
            # 5 bài bối cảnh phòng làm việc cá nhân (Webcam room)
            "an-toan-ai-02-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_sieu_tri_tue.jpg",
            "hau-qua-cua-nhin-linh-tinh-science.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_khoa_hoc_than_kinh.jpg",
            "complex-5-anxiety-is-not-what-you-think.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_phuong_trinh_lo_au.jpg",
            "suyash-saraf-d2c-branding-gen-z-marketing-podcast.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_branding_trieu_do.jpg",
            "law-5-stress-is-not-what-happens-to-you.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_quy_tac_90_giay.jpg",

            # 5 bài Kịch bản Offline
            "kichbanoffline.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_offline_script_1789495439415.jpg",
            "kichbanoffline-kich-ban-08-chuyen-mon-vung-nhung-vang-khach.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_no_customers_1789495449887.jpg",
            "kichbanoffline-phan-tich-video-fb-ads-6.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_fb_ads_6_1789495461241.jpg",
            "kichbanoffline-phan-tich-video-fb-ads-5.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_fb_ads_5_1789495475061.jpg",
            "kichbanoffline-phan-tich-video-fb-ads-4.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_fb_ads_4_1789495486846.jpg"
        }
        cover_img = cover_mapping.get(f, "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80")

        posts.append({
            "filename": f,
            "title": title,
            "excerpt": excerpt,
            "category_key": cat,
            "category_label": cat_label,
            "cover_image": cover_img,
            "updated_at": mod_time,
            "read_time": "5 phút đọc",
            "file_size_kb": round(stat.st_size / 1024)
        })

    # Sort by updated_at descending
    posts.sort(key=lambda x: x['updated_at'], reverse=True)

    with open('posts-manifest.json', 'w', encoding='utf-8') as out:
        json.dump({"posts": posts}, out, ensure_ascii=False, indent=2)
        
    print(f"Generated manifest with {len(posts)} posts.")

if __name__ == "__main__":
    generate()
