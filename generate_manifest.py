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
            "kichbanoffline-kich-ban-bds-30-phut-dap-tan-su-tri-hoan.html": "https://khoai.fedu.vn/k_covers/cover_kich_ban_bds_1789517341819.jpg",
            "kichbanoffline.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_offline_script_1789495439415.jpg",
            "kichbanoffline-kich-ban-08-chuyen-mon-vung-nhung-vang-khach.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_no_customers_1789495449887.jpg",
            "kichbanoffline-phan-tich-video-fb-ads-6.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_fb_ads_6_1789495461241.jpg",
            "kichbanoffline-phan-tich-video-fb-ads-5.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_fb_ads_5_1789495475061.jpg",
            "kichbanoffline-phan-tich-video-fb-ads-4.html": "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev/k_covers/cover_fb_ads_4_1789495486846.jpg",
            "dom.html": "https://khoai.fedu.vn/k_covers/dom_cover_1789497856188.jpg",
            "cong-thuc-1-kenh-de-phat-trien-podcast.html": "https://khoai.fedu.vn/k_covers/cong_thuc_1_kenh_1789497880178.jpg",
            "so-tay-thuc-chien-khoi-nghiep-ky-nguyen-ai-podcast.html": "https://khoai.fedu.vn/k_covers/so_tay_thuc_chien_1789497894359.jpg",
            "how-to-teach-and-grow-rich-business-model-podcast.html": "https://khoai.fedu.vn/k_covers/how_to_teach_and_grow_1789497904910.jpg",
            "10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.html": "https://khoai.fedu.vn/k_covers/10_protocols_andrew_1789497917055.jpg",
            "toi-uu-hieu-suat-nao-bo-suc-manh-nootropic-tu-creatine-va-che-do-an-thit-carnivore-dinh-cao-toi-gian-nang-luong-tu-joe-rogan-elon-musk.html": "https://khoai.fedu.vn/k_covers/toi_uu_hieu_suat_nao_bo_1789497940470.jpg",
            "su-giau-co-va-thanh-cong-tot-dinh-khong-bat-dau-tu-chien-thuat-kinh-doanh-hao-nhoang-ma-khoi-nguon-tu-nang-luc-quan-tri-tam-tri-ban-phai-thiet-ke-mot-moi-truong-khien-ky-luat-tro-nen-de-dang.html": "https://khoai.fedu.vn/k_covers/su_giau_co_va_thanh_cong_1789497961114.jpg",
            "no-den-tu-long-dung-cam-dam-lam-ra-nhung-video-toi-te-ban-dau-kien-tri-cai-thien-1-moi-ngay-va-tap-trung-phuc-vu-sau-sac-cho-nhom-khan-gia-ngach-dang-chiu-chung-noi-dau-ma-ban-tung-vuot-qua-podcast.html": "https://khoai.fedu.vn/k_covers/no_den_tu_long_dung_cam_1789497983814.jpg",
            "be-khoa-thuat-toan-xay-kenh-niche-podcast.html": "https://khoai.fedu.vn/k_covers/be_khoa_thuat_toan_1789498007808.jpg",
            "nghe-thuat-chuyen-minh-10-nam-dam-phan-hop-dong-molly-mcadam-podcast.html": "https://khoai.fedu.vn/k_covers/nghe_thuat_chuyen_minh_1789498030877.jpg",
            "co-the-ban-khong-he-ghet-ban-no-chi-dang-lam-xuat-sac-nhiem-vu-sinh-ton-bang-cach-bat-che-do-khang-cu-lai-su-sut-giam-calo-trong-mot-the.html": "https://khoai.fedu.vn/k_covers/co_the_ban_khong_he_ghet_1789498064292.jpg",
            "giac-ngu-hieu-suat-dinh-cao-science-long-form.html": "https://khoai.fedu.vn/k_covers/giac_ngu_hieu_suat_dinh_cao_1789498074896.jpg",
            "dr-v-mohan-diabetes-sugar-genetics-health-podcast.html": "https://khoai.fedu.vn/k_covers/dr_v_mohan_diabetes_1789498087376.jpg",
            "su-thay-doi-khong-den-tu-viec-tim-kiem-mot-cuoc-song-de-dang-hon-ma-den-tu-viec-chu-dong-lua-chon-nhung-kho-khan-co-chu-dich-ap-luc-khong.html": "https://khoai.fedu.vn/k_covers/su_thay_doi_khong_den_tu_1789498100264.jpg",
            "mat-ma-cua-su-loi-cuon-podcast-science.html": "https://khoai.fedu.vn/k_covers/mat_ma_cua_su_loi_cuon_1789498111501.jpg",
            "co-hoc-luong-tu-va-truc-giac-tam-linh.html": "https://khoai.fedu.vn/k_covers/co_hoc_luong_tu_1789498159596.jpg",
            "dr-joe-dispenza-rewire-brain-neuroplasticity-fear-podcast.html": "https://khoai.fedu.vn/k_covers/dr_joe_dispenza_1789498172191.jpg",
            "hanh-trinh-khai-mo-sang-tao-chua-lanh-noi-dau-podcast.html": "https://khoai.fedu.vn/k_covers/hanh_trinh_khai_mo_1789498182380.jpg",
            "hanh-trinh-hack-nao-bo-science.html": "https://khoai.fedu.vn/k_covers/hanh_trinh_hack_nao_bo_1789498197546.jpg",
            "chung-ta-khong-phai-la-nhung-co-may-thuan-ly-tri-co-the-thoat-khoi-quy-luat-sinh-hoc-con-nguoi-hien-dai-dang-van-hanh-bang-he-dieu-hanh-cua-to-tien-tren-thao-nguyen-podcast-science.html": "https://khoai.fedu.vn/k_covers/chung_ta_khong_phai_1789498209355.jpg",
            "tamlyhoc-tam-ly-phong-thu-cua-nguoi-mua.html": "https://khoai.fedu.vn/k_covers/tamlyhoc_tam_ly_phong_thu_1789498264428.jpg",
            "he-thong-phuc-hop-prompt-4-giai-ma-ban-chat-he-dieu-hanh-vu-tru-va-kien-truc-nhan-thuc-bac-cao.html": "https://khoai.fedu.vn/k_covers/he_thong_phuc_hop_1789498278127.jpg",
            "tu-duy-van-hanh-cua-ceo-uber-science.html": "https://khoai.fedu.vn/k_covers/tu_duy_van_hanh_1789498289898.jpg",
            "giai-phong-tam-tri-tu-co-the-podcast.html": "https://khoai.fedu.vn/k_covers/giai_phong_tam_tri_1789498301154.jpg",
            "dai-chien-tu-duy-tranh-luan-nay-lua-giua-kevin-oleary-cenk-uygur-ve-tac-dong-cua-ai-den-that-nghiep-cuoc-dua-dia-chinh-tri-my-trung-va.html": "https://khoai.fedu.vn/k_covers/dai_chien_tu_duy_1789498312827.jpg"
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
