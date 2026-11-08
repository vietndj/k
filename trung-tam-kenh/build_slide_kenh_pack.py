#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_slide_kenh_pack.py
========================
Đóng gói nguyên văn 100% (0% cắt xén, 0% diễn giải) toàn bộ hệ sinh thái 16 trang thực chiến
của kenh.fedu.vn (sau khi đã dọn sạch tên kênh riêng ở luồng 8bb739ec) + 35 slide gốc của luồng
'slide logic kênh' (e5c3bb6e / bee3c217) + kho thơ lục bát gốc của anh Việt thành 5 tập <= 43.000 bytes/tập,
khớp trần đọc 1-turn song song của Thư ký CLAUDE2 (Claude Opus 5.5 Pro).
"""

import glob
import os
import re
from bs4 import BeautifulSoup

ROOT_KENH = "/Users/vietmac/Documents/CODE/kenh.fedu.vn"
ROOT_K = "/Users/vietmac/Documents/CODE/k/trung-tam-kenh"
OUT_DIR = "/Users/vietmac/Documents/CODE/kenh.fedu.vn/slide_pack"
SLIDE_35_PATH = "/Users/vietmac/.gemini/antigravity/brain/bee3c217-3545-45b0-83e2-5516153b8ce1/kich_ban_35_slide_logic_xay_kenh.md"

os.makedirs(OUT_DIR, exist_ok=True)


def clean_html_structured(fp: str) -> str:
    """Trích xuất văn bản có giữ phân cấp Markdown H1/H2/H3/Table/List nguyên văn, bỏ nav/header/footer/script/style."""
    raw = open(fp, "r", encoding="utf-8").read()
    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "svg", "nav", "header", "footer"]):
        tag.decompose()

    # Đánh dấu heading & list nhẹ nhàng để giữ cấu trúc gốc mà không làm phình byte
    for h1 in soup.find_all("h1"):
        h1.insert_before("\n### [H1] ")
    for h2 in soup.find_all("h2"):
        h2.insert_before("\n#### [H2] ")
    for h3 in soup.find_all("h3"):
        h3.insert_before("\n##### [H3] ")
    for tr in soup.find_all("tr"):
        cells = [re.sub(r"\s+", " ", c.get_text(" ", strip=True)) for c in tr.find_all(["th", "td"])]
        if cells:
            tr.replace_with("\n| " + " | ".join(cells) + " |\n")

    lines = []
    for line in soup.get_text("\n").splitlines():
        s = re.sub(r"\s+", " ", line).strip()
        if s:
            lines.append(s)
    return "\n".join(lines)


def harvest_clean_poems() -> str:
    """Thu thập các khổ thơ lục bát gốc (ưu tiên khổ 4 câu và tối đa 2 khổ/bài) từ kho bài viết repo k."""
    blocks_4 = []
    blocks_2 = []
    seen = set()
    candidates = sorted(glob.glob("/Users/vietmac/Documents/CODE/k/logic*.html"), reverse=True)
    for fp in candidates:
        bn = os.path.basename(fp)
        soup = BeautifulSoup(open(fp, "r", encoding="utf-8").read(), "html.parser")
        h1 = soup.find("h1")
        title = h1.get_text(" ", strip=True) if h1 else bn
        per_file = 0
        for el in soup.find_all(["blockquote", "div", "p"]):
            if per_file >= 2:
                break
            cls = " ".join(el.get("class") or [])
            if not any(k in cls.lower() for k in ("poem", "verse", "luc-bat", "tho")) and el.name != "blockquote":
                continue
            raw_lines = [re.sub(r"\s+", " ", x).strip(" \"'“”‘’") for x in el.get_text("\n").splitlines()]
            raw_lines = [x for x in raw_lines if x and not x.startswith(("📜", "Ý nghĩa", "4 câu", "("))]
            valid_pairs = []
            for i in range(0, len(raw_lines) - 1, 2):
                w1 = len(raw_lines[i].rstrip(",.;!?").split())
                w2 = len(raw_lines[i + 1].rstrip(",.;!?").split())
                if w1 == 6 and w2 == 8:
                    valid_pairs.append((raw_lines[i], raw_lines[i + 1]))
            if valid_pairs:
                txt = "\n".join(f"{a}\n{b}" for a, b in valid_pairs[:2])
                if txt not in seen:
                    seen.add(txt)
                    per_file += 1
                    entry = f"- **[{bn} — {title[:55]}]**\n" + "\n".join(f"  > {l}" for l in txt.splitlines())
                    if len(valid_pairs) >= 2:
                        blocks_4.append(entry)
                    else:
                        blocks_2.append(entry)
    return "\n\n".join((blocks_4 + blocks_2)[:24])


def write_pack(filename: str, title: str, sections: list[tuple[str, str]]):
    out_fp = os.path.join(OUT_DIR, filename)
    parts = [f"# {title}\n"]
    for sec_title, sec_body in sections:
        parts.append(f"---\n\n## {sec_title}\n\n{sec_body}\n")
    content = "\n".join(parts)
    with open(out_fp, "w", encoding="utf-8") as f:
        f.write(content)
    return out_fp, len(content.encode("utf-8"))


def main():
    # Tập 1: Trục Logic 5 Mắt Xích & Điều phối định dạng
    t1_pages = [
        ("00 · index.html — Bản đồ xây kênh từ 0 đến khách tự chốt", os.path.join(ROOT_KENH, "index.html")),
        ("01 · 01-tu-duy.html — Bản chất cuộc chơi & Bài toán 7 giờ (420 phút, 3 bức tường, 90-9-1, 84% chia sẻ ngầm)", os.path.join(ROOT_KENH, "01-tu-duy.html")),
        ("02 · 02-bat-dau.html — Tín hiệu đắt giá, 3 đầu ra đóng gói chuyên môn & Vòng gửi xe 3 giây", os.path.join(ROOT_KENH, "02-bat-dau.html")),
        ("03 · 03-logic-kenh.html — Dây chuyền 5 mắt xích, 3 dòng nội dung & Chuỗi 11 điểm chạm cho người thứ hai", os.path.join(ROOT_KENH, "03-logic-kenh.html")),
        ("04 · 04-niem-tin.html — Tâm lý 4 tầng (đào ngược, nói xuôi), Cốc giấy mủn 3s & Tráng men thể diện Tầng 2.5", os.path.join(ROOT_KENH, "04-niem-tin.html")),
        ("05 · 05-dinh-dang-2.0.html — Chọn định dạng theo độ dạn ống kính & Phân nhánh tuần này", os.path.join(ROOT_KENH, "05-dinh-dang-2.0.html")),
    ]
    t1 = [(label, clean_html_structured(fp)) for label, fp in t1_pages]

    # Tập 2: Định dạng 5.1, 5.2, 5.3
    t2_pages = [
        ("5.1 · dinh-dang/voiceover3.0.html — Voice-Over & thao tác tay (0% lộ mặt, dựng hình trước thu âm sau, kịch bản 2 cột, cảnh trám 3 lớp)", os.path.join(ROOT_KENH, "dinh-dang/voiceover3.0.html")),
        ("5.2 · dinh-dang/walkntalk2.0.html — Walk & Talk (Vừa đi vừa nói thả lỏng cơ thể, đổi góc >= 45 độ, dẫn tour cơ sở)", os.path.join(ROOT_KENH, "dinh-dang/walkntalk2.0.html")),
        ("5.3 · dinh-dang/talkinghead2.0.html — Talking Head (Ngồi bàn làm việc, tỷ lệ 20% mặt / 80% cảnh, 2 góc máy điện thoại, kịch bản 7 câu)", os.path.join(ROOT_KENH, "dinh-dang/talkinghead2.0.html")),
    ]
    t2 = [(label, clean_html_structured(fp)) for label, fp in t2_pages]

    # Tập 3: Định dạng 5.4, Kỹ thuật 5.5 Chuyển cảnh, 5.7 Kho 31 Vỏ bọc
    t3_pages = [
        ("5.4 · dinh-dang/storytelling2.0.html — Storytelling (Lát cắt 5 giây chiếc khăn lau yên xe, tráng men thể diện & nối quy luật nghề)", os.path.join(ROOT_KENH, "dinh-dang/storytelling2.0.html")),
        ("5.5 · dinh-dang/chuyencanh2.0.html — Chuyển cảnh trong chuyển động (Quy tắc cắt ở 70% đà 70/30, cầm tay selfie vs chân máy lệch >30°, khóa tâm mắt)", os.path.join(ROOT_KENH, "dinh-dang/chuyencanh2.0.html")),
        ("5.7 · dinh-dang/vo-boc-31.html — 31 vỏ bọc video tạo khách chia theo 5 nhóm tình huống đời thường", os.path.join(ROOT_KENH, "dinh-dang/vo-boc-31.html")),
    ]
    t3 = [(label, clean_html_structured(fp)) for label, fp in t3_pages]

    # Tập 4: Kỹ thuật 5.6 Bố cục sạch, 5.8 MegaPrompt AI (cả bản 4 định dạng & Lõi V3.1 Khay đá 5 ngăn), 06 Lộ trình thực hành 4 tuần
    t4 = [
        ("5.6 · dinh-dang/bocucquay.html — Bố cục khung hình sạch (6 Quy tắc: Đường 2x-3x 3 lớp, Động, Sáng 90°-135° -0.7EV, Giờ, Tĩnh, Vào cắt 1.5s đầu)", clean_html_structured(os.path.join(ROOT_KENH, "dinh-dang/bocucquay.html"))),
        ("5.8A · dinh-dang/megaprompt2.0.html (Bản 4 Định Dạng Kịch Bản Khớp Góc Quay trên repo k)", clean_html_structured(os.path.join(ROOT_K, "dinh-dang/megaprompt2.0.html"))),
        ("5.8B · dinh-dang/megaprompt2.0.html (Bản Trạm Kịch Bản 30 Giây Lõi V3.1 — Khay Đá 5 Ngăn kichban.fedu.vn)", clean_html_structured(os.path.join(ROOT_KENH, "dinh-dang/megaprompt2.0.html"))),
        ("06 · 07-thuc-hanh.html — Lộ trình 4 tuần & 4 kỹ năng ngưỡng đủ qua vòng gửi xe (Nhịp 2,5 giờ/tuần)", clean_html_structured(os.path.join(ROOT_KENH, "07-thuc-hanh.html"))),
    ]

    # Tập 5: 35 Slide hiện có + 09-case.html + Kho thơ lục bát gốc
    slide35_raw = open(SLIDE_35_PATH, "r", encoding="utf-8").read()
    poems_md = harvest_clean_poems()
    t5 = [
        ("PHẦN A · NGUYÊN VĂN 35 SLIDE HIỆN CÓ CỦA LUỒNG 'SLIDE LOGIC KÊNH' (01..35 — Chưng cất từ logic-tong-hop.html)", slide35_raw),
        ("PHẦN B · 07 · 09-case.html — Giải phẫu 7 kênh mẫu ngoài đời (Nhóm A 4 kênh liền mạch vs Nhóm B 3 kênh đứt 1 mắt xích)", clean_html_structured(os.path.join(ROOT_KENH, "09-case.html"))),
        ("PHẦN C · TUYỂN TẬP KHỔ THƠ LỤC BÁT GỐC TRONG KHO LOGIC ANH VIỆT (Dùng làm mỏ neo cho trạm nghỉ poem_sanctuary)", poems_md),
    ]

    packs = [
        ("01_TRUC_LOGIC_5_MAT_XICH.md", "TẬP 1/5: TRỤC LOGIC 5 MẮT XÍCH & BẢNG ĐIỀU PHỐI ĐỊNH DẠNG (kenh.fedu.vn)", t1),
        ("02_DINH_DANG_1_2_3.md", "TẬP 2/5: BA ĐỊNH DẠNG ĐẦU TIÊN — VOICE-OVER · WALK & TALK · TALKING HEAD (kenh.fedu.vn)", t2),
        ("03_DINH_DANG_4_CHUYEN_CANH_VO_BOC.md", "TẬP 3/5: STORYTELLING 5S · CHUYỂN CẢNH 70% ĐÀ · 31 VỎ BỌC VIDEO (kenh.fedu.vn)", t3),
        ("04_BO_CUC_MEGAPROMPT_THUC_HANH.md", "TẬP 4/5: 6 QUY TẮC BỐ CỤC SẠCH · CÂU LỆNH AI KHAY ĐÁ 5 NGĂN · LỘ TRÌNH 4 TUẦN (kenh.fedu.vn)", t4),
        ("05_35_SLIDE_CU_CASE_VA_KHO_THO.md", "TẬP 5/5: BỘ 35 SLIDE LOGIC KÊNH HIỆN CÓ (01..35) · 7 KÊNH MẪU · KHO THƠ LỤC BÁT GỐC", t5),
    ]

    print("=== SLIDE KENH PACK SUMMARY ===")
    for fn, title, secs in packs:
        fp, sz = write_pack(fn, title, secs)
        status = "OK <= 45KB (1-turn Read)" if sz <= 45500 else "WARNING > 45KB"
        print(f"  {fn:40s} : {sz:8,d} bytes  [{status}]")


if __name__ == "__main__":
    main()
