#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
update_hub_page.py
Chuyển toàn bộ tiêu đề tiếng Anh trong 21-podcast-raj-shamani-khong-chinh-tri.html
thành tiếng Việt dễ hiểu, bộc lộ rõ nội dung bên trong, và loại bỏ hoàn toàn chữ 'Dòng 1', 'Dòng 2'.
"""

import re
from bs4 import BeautifulSoup

TITLE_MAP = {
    "FO558": "Tư duy CTO: Lý do thực sự khiến bạn không thể thăng tiến & bứt phá thu nhập",
    "FO557": "Hệ thống Second Brain & Tự động hóa AI: Cỗ máy nhân bản năng suất & doanh thu trăm tỷ",
    "FO556": "Khoa học thần kinh: Thói quen làm chủ dopamine, giấc ngủ sâu & kích hoạt não bộ đỉnh cao",
    "FO552": "Cảnh báo y tế dự phòng: Gan nhiễm mỡ giấu mặt, suy thoái đường ruột & bẫy sức khỏe giới trẻ",
    "FO534": "Bí ẩn tiểu đường châu Á: Kiểu hình béo gầy, cắt giảm tinh bột & cửa sổ vàng đảo ngược bệnh",
    "FO537": "Khởi nghiệp công nghệ sinh học từ 120 USD: Hành trình đế chế Biocon tỷ đô cứu sống hàng triệu người",
    "FO555": "Kinh doanh hàng xa xỉ: Nghệ thuật chế tác vi cơ khí & định giá theo giá trị cảm xúc",
    "FO551": "Đỉnh cao xe siêu sang Bentley: Cạnh tranh bằng cảm xúc & tạo hình thủ công độc bản",
    "FO553": "Nghệ thuật tái cấu trúc tập đoàn tỷ USD: Quyết đoán lãnh đạo & thâu tóm doanh nghiệp ngập nợ",
    "FO546": "Chiến lược chiếm lĩnh kệ hàng Walmart: Xây dựng thương hiệu bán lẻ triệu đô toàn cầu & TikTok Shop",
    "FO549": "Mã hóa ngôn ngữ cơ thể: 4 chiếc hộp tâm lý định đoạt lòng tin trong 3 giây đầu tiên",
    "FO541": "Bác sĩ tâm thần Harvard giải mã: Bản chất ngoại tình & lặp lại chấn thương trong tình yêu",
    "FO543": "Tâm lý học lừa đảo qua điện thoại: Bẫy thao túng nỗi sợ & cách phòng thủ an ninh mạng trước Deepfake",
    "FO529": "CEO Binance giải mã: Vì sao hệ thống ngân hàng suy yếu, sụp đổ tiền tệ & tương lai Bitcoin",
    "FO540": "Bẫy tiền bạc SoftBank Vision Fund: Vì sao càng nhiều tiền càng chưa chắc tự do & bài học WeWork",
    "FO535": "Lời cảnh báo giới trung lưu: Bẫy nợ tiêu dùng trả góp EMI & chiến lược đầu tư cổ phiếu độc quyền",
    "FO533": "Bí mật quỹ đầu tư tư nhân Kotak Alts: Công thức làm giàu từ phần bù thanh khoản & bảo vệ gia sản",
    "FO536": "Trải nghiệm trạm vũ trụ ISS: Tư duy không trọng lực, biến đổi sinh học & Hiệu ứng Tổng quan Trái Đất",
    "FO548": "Tâm thái nhà vô địch thế giới tuổi 18: Kỷ luật thép đổi lấy 9 cúp vàng một năm & bản lĩnh match point",
    "FO538": "Triết lý âm nhạc Sufi: Cội nguồn văn hóa truyền thống & bản lĩnh giữ mình trước cám dỗ hư danh",
    "FO530": "Nghệ thuật hài độc thoại: Nỗi bất an bản sắc thế hệ con cái nhập cư & sức mạnh của sự chân thật"
}

CATEGORY_MAP = {
    "FO558": "FO558 // LÃNH ĐẠO CÔNG NGHỆ",
    "FO557": "FO557 // HỆ THỐNG AI & TỰ ĐỘNG HÓA",
    "FO556": "FO556 // KHOA HỌC THẦN KINH",
    "FO552": "FO552 // Y TẾ DỰ PHÒNG & TẾ BÀO",
    "FO534": "FO534 // ĐIỀU TRỊ ĐÁI THÁO ĐƯỜNG",
    "FO537": "FO537 // CÔNG NGHỆ SINH HỌC",
    "FO555": "FO555 // CHẾ TÁC ĐỒNG HỒ XA XỈ",
    "FO551": "FO551 // CÔNG NGHỆ SIÊU XE BENTLEY",
    "FO553": "FO553 // QUẢN TRỊ TẬP ĐOÀN TỶ ĐÔ",
    "FO546": "FO546 // CHIẾN LƯỢC BÁN LẺ TOÀN CẦU",
    "FO549": "FO549 // NGÔN NGỮ CƠ THỂ",
    "FO541": "FO541 // TÂM THẦN HỌC HARVARD",
    "FO543": "FO543 // AN NINH MẠNG & BẢO MẬT",
    "FO529": "FO529 // TÀI CHÍNH PHI TẬP TRUNG",
    "FO540": "FO540 // TRIẾT LÝ TIỀN TỆ & ĐẦU TƯ",
    "FO535": "FO535 // ĐẦU TƯ GIÁ TRỊ TRUNG LƯU",
    "FO533": "FO533 // QUỸ ĐẦU TƯ TƯ NHÂN",
    "FO536": "FO536 // HÀNG KHÔNG VŨ TRỤ",
    "FO548": "FO548 // THỂ THAO ĐỈNH CAO",
    "FO538": "FO538 // NGHỆ THUẬT & ÂM NHẠC SUFI",
    "FO530": "FO530 // NGHỆ THUẬT HÀI ĐỘC THOẠI"
}

def transform_hub_html(content, is_course_repo=False):
    # 1. Update Title tag & Hero intro
    content = content.replace(
        "21 Video Podcast Raj Shamani Không Chính Trị &amp; Chiến Tranh | Tóm Tắt 2 Dòng",
        "21 Video Podcast Raj Shamani Tuyển Chọn (Không Chính Trị) | Bản Đồ Tri Thức Thực Chiến"
    )
    content = content.replace(
        "Mỗi video được cô đọng đúng 2 dòng đắt giá, đi kèm link video gốc và link bóc tách hệ thống.",
        "Mỗi video được chắt lọc các luận điểm đắt giá nhất, đi kèm link video gốc và link bài bóc tách hệ thống chuyên sâu."
    )

    soup = BeautifulSoup(content, 'html.parser')

    cards = soup.find_all('div', class_='apple-card')
    print(f"Tìm thấy {len(cards)} thẻ podcast...")

    for card in cards:
        ep_el = card.find('div', class_='apple-card__ep')
        title_el = card.find('h3', class_='apple-card__title')
        summary_el = card.find('div', class_='apple-card__summary')

        if not ep_el or not title_el or not summary_el:
            continue

        ep_text = ep_el.text.strip()
        ep_code = None
        for code in TITLE_MAP.keys():
            if code in ep_text:
                ep_code = code
                break

        if ep_code:
            # Update title
            new_title = TITLE_MAP[ep_code]
            title_el.string = new_title

            # Update category tag to Vietnamese
            if ep_code in CATEGORY_MAP:
                ep_el.string = CATEGORY_MAP[ep_code]

        # Clean summary: remove 'Dòng 1:', 'Dòng 2:'
        for p in summary_el.find_all('p'):
            p_text = p.decode_contents()
            # Remove 🔹 <strong>Dòng 1:</strong> or 🔹 <strong>Dòng 2:</strong>
            p_text_clean = re.sub(r'🔹\s*<strong>Dòng\s*\d+:?</strong>\s*', '• ', p_text)
            p_text_clean = re.sub(r'<strong>Dòng\s*\d+:?</strong>\s*', '• ', p_text_clean)
            p_text_clean = re.sub(r'Dòng\s*\d+:?\s*', '• ', p_text_clean)
            if not p_text_clean.strip().startswith('•'):
                p_text_clean = '• ' + p_text_clean.strip()
            p.clear()
            p.append(BeautifulSoup(p_text_clean, 'html.parser'))

        # Check links
        if is_course_repo:
            read_btn = card.find('a', class_='apple-card__btn--primary')
            if read_btn and 'href' in read_btn.attrs:
                href = read_btn['href']
                slug = href.split('/')[-1]
                read_btn['href'] = f"https://fedu.vn/k/{slug}"

    # Also update the summary table at the bottom
    table = soup.find('table', class_='cl-table')
    if table:
        for row in table.find_all('tr'):
            tds = row.find_all('td')
            if len(tds) >= 4:
                ep_code = tds[1].text.strip()
                if ep_code in TITLE_MAP:
                    tds[3].string = TITLE_MAP[ep_code]
                if is_course_repo:
                    link_a = tds[4].find('a')
                    if link_a and 'href' in link_a.attrs:
                        slug = link_a['href'].split('/')[-1]
                        link_a['href'] = f"https://fedu.vn/k/{slug}"

    return str(soup)

def main():
    k_file = '/Users/vietmac/Documents/CODE/k/21-podcast-raj-shamani-khong-chinh-tri.html'
    course_file = '/Users/vietmac/Documents/CODE/course/21-podcast-raj-shamani-khong-chinh-tri.html'

    with open(k_file, 'r', encoding='utf-8') as f:
        k_content = f.read()

    print("Cập nhật cho repo k...")
    updated_k = transform_hub_html(k_content, is_course_repo=False)
    with open(k_file, 'w', encoding='utf-8') as f:
        f.write(updated_k)
    print("✅ Đã ghi file repo k thành công!")

    print("Cập nhật cho repo course...")
    updated_course = transform_hub_html(k_content, is_course_repo=True)
    with open(course_file, 'w', encoding='utf-8') as f:
        f.write(updated_course)
    print("✅ Đã ghi file repo course thành công!")

if __name__ == '__main__':
    main()
