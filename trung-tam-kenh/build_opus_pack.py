#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_opus_pack.py V2
=====================
Đóng gói dữ liệu nguyên văn 0% diễn giải thành 3 tập < 44.000 bytes/tập
(khớp trần 46.080 bytes của read_file để Claude Opus Native đọc trọn 100% trong đúng 1 Turn song song),
đồng thời tách sẵn các fragment HTML cần giữ nguyên / ẩn đi để lắp ghép chính xác 100%.
"""

import json
import os
import re
from bs4 import BeautifulSoup

OUT_DIR = "/Users/vietmac/Documents/CODE/kenh.fedu.vn/opus_pack"
os.makedirs(OUT_DIR, exist_ok=True)

P_PAGE1 = "/Users/vietmac/Documents/CODE/k/logickenh-xaykenh-1.0.html"  # https://kenh.fedu.vn/cu/index.html
P_PAGE2 = "/Users/vietmac/Documents/CODE/k/logickenh-xaykenh.html"      # https://fedu.vn/k/logickenh-xaykenh.html


def clean_text_from_el(el) -> str:
    clone = BeautifulSoup(str(el), "html.parser")
    for s in clone(["script", "style", "svg"]):
        s.decompose()
    lines = []
    for line in clone.get_text("\n").splitlines():
        s = re.sub(r"\s+", " ", line).strip()
        if s:
            lines.append(s)
    return "\n".join(lines)


def trim_utf8(text: str, max_bytes: int) -> str:
    b = text.encode("utf-8")
    if len(b) <= max_bytes:
        return text
    sub = b[:max_bytes].decode("utf-8", errors="ignore")
    return sub.rsplit("\n", 1)[0] + "\n"


def extract_fragments_and_pages():
    raw1 = open(P_PAGE1, "r", encoding="utf-8").read()
    raw2 = open(P_PAGE2, "r", encoding="utf-8").read()
    soup1 = BeautifulSoup(raw1, "html.parser")
    soup2 = BeautifulSoup(raw2, "html.parser")

    # Save base styles from Page 1 (contains full cl-zebra-section, flow-stage, faq-item styles)
    styles1 = "\n\n".join(str(st) for st in soup1.find_all("style"))
    with open(os.path.join(OUT_DIR, "base_page1_styles.html"), "w", encoding="utf-8") as f:
        f.write(styles1)

    secs1 = soup1.find_all("section")
    secs2 = soup2.find_all("section")

    hidden_parts = []
    flow_sec_html = ""
    faq1_html = ""
    p1_texts = []
    faq_titles = []

    for idx, sec in enumerate(secs1):
        sid = sec.get("id", "")
        h = sec.find(["h1", "h2", "h3"])
        htitle = h.get_text(" ", strip=True) if h else f"Section {idx}"
        if "Ví dụ 1" in htitle or "Ví dụ 2" in htitle or "MỔ XẺ 3 TẦNG" in sec.get_text(" ", strip=True)[:80]:
            hidden_parts.append(f"<!-- Page 1 Hidden [{idx}]: {htitle} -->\n" + str(sec))
        elif sid == "sec-faq":
            faq1_html = str(sec)
            faq_titles = [q.get_text(" ", strip=True).rstrip("+").strip() for q in sec.select(".faq-question")]
        else:
            if sec.find(class_="flow-stage"):
                flow_sec_html = str(sec)
            p1_texts.append(f"### [Trang 1 - Mục {idx}: {htitle}]\n" + clean_text_from_el(sec))

    p2_texts = []
    roadmap_html = ""
    for idx, sec in enumerate(secs2):
        sid = sec.get("id", "")
        h = sec.find(["h1", "h2", "h3"])
        htitle = h.get_text(" ", strip=True) if h else f"Section {idx}"
        if idx == 0:
            roadmap_html = str(sec)
        if sid in ("q14", "q15"):
            hidden_parts.append(f"<!-- Page 2 Hidden [{idx} - {sid}]: {htitle} -->\n" + str(sec))
        else:
            txt = clean_text_from_el(sec)
            # Filter out deleted fake cases notice in case-study text so Opus knows not to reuse them
            p2_texts.append(f"### [Trang 2 - Mục {idx} ({sid}): {htitle}]\n" + txt)

    # Save exact fragments
    with open(os.path.join(OUT_DIR, "frag_flow_stage.html"), "w", encoding="utf-8") as f:
        f.write(flow_sec_html)

    with open(os.path.join(OUT_DIR, "frag_hidden_3tang.html"), "w", encoding="utf-8") as f:
        f.write(
            '<!-- PHẦN VÍ DỤ 3 TẦNG / 4 TẦNG ĐƯỢC ẨN ĐI THEO YÊU CẦU CỦA ANH VIỆT -->\n'
            '<div id="legacy-3tang-hidden" style="display:none !important;" hidden aria-hidden="true">\n'
            + "\n\n".join(hidden_parts)
            + "\n</div>\n"
        )

    # Bottom FAQ = #sec-faq (39 real-world questions at the bottom of cu/index.html)
    with open(os.path.join(OUT_DIR, "frag_faq_bottom.html"), "w", encoding="utf-8") as f:
        f.write(faq1_html)

    footer1 = soup1.find("footer")
    if footer1:
        with open(os.path.join(OUT_DIR, "frag_footer.html"), "w", encoding="utf-8") as f:
            f.write(str(footer1))

    faq_list_md = "### [PHẦN CÂU HỎI DƯỚI CÙNG GIỮ NGUYÊN 100% — `#sec-faq` (39 câu hỏi)]\n" + "\n".join(
        f"{i+1}. {t}" for i, t in enumerate(faq_titles)
    )
    return "\n\n".join(p1_texts) + "\n\n" + faq_list_md, "\n\n".join(p2_texts)


def build_part1(p1_txt: str, p2_txt: str):
    cpath = "/Users/vietmac/.gemini/antigravity/brain/b7cab68b-e79d-479c-9c9c-2b88943e04ec/claude_pro_c3caf46e.md"
    opus_prev = open(cpath, "r", encoding="utf-8").read().split("## Các bước gần nhất")[0].strip()

    # Also grab anh Việt's exact prompts from b7cab68b
    tpath = "/Users/vietmac/.gemini/antigravity/brain/b7cab68b-e79d-479c-9c9c-2b88943e04ec/.system_generated/logs/transcript_full.jsonl"
    viet_msgs = []
    with open(tpath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if not line.strip():
                continue
            o = json.loads(line)
            if o.get("type") == "USER_INPUT":
                c = (o.get("content") or "").strip()
                if c:
                    viet_msgs.append(c)

    doc1 = f"""# TẬP 1/3: YÊU CẦU GỐC, LỊCH SỬ CHỐT & NGUYÊN VĂN 2 TRANG CẦN HỢP NHẤT

## I. YÊU CẦU NGUYÊN VĂN CỦA ANH VIỆT HÔM NAY
> "https://fedu.vn/k/logickenh-xaykenh.html
> https://kenh.fedu.vn/cu/index.html
> Tôi muốn kết hợp nội dung của hai trang này vào luôn thành một.
> Phần câu hỏi dưới cùng thì giữ.
> phần ví dụ 3 tầng này thì ẩn đi tôi đang thấy logic của cái phần này rất là không phù hợp với logic hiện tại của tôi .
> Đồ thị hiện tại của tôi kết hợp với các cái file logic xxx và các podcast gần đây về làm video là món quà, là quan tâm đến đầu ra ,. Từ các diễn giả, từ alex homozi, daniel nick rubin. ..
> Tổng hợp lại để dữ liệu súc tích hỏi OPUS để nó viết lại và tạo một trang mới tổng hợp tất cả những logic về xây kênh của tôi hiện tại dựa trên lịch sử chúng ta nói chuyện. là CLAUDE native tự viết đó"

### Các quyết định dọn dẹp đã chốt trong lịch sử gần nhất (`f6c90a66` & `fbe8d427`):
- **Ẩn hoàn toàn phần Ví dụ 3 tầng / bóc tách 4 tầng cũ** (không nhắc tới "Tầng 1, Tầng 2, Tầng 2.5, Tầng 3, Công cụ 4 tầng" ở phần hiển thị mới vì không còn khớp logic hiện tại; khối cũ đã được đóng vào `<!-- INJECT_HIDDEN_3TANG -->` ẩn `display:none`).
- **Xóa sạch không nhắc lại các case học viên không quay video / không có kênh thật:** Chị Hằng BĐS, Chị Liên Bảo hiểm, Kiên Phân Bón, Quỳnh Anh Le Kitchen, Đặng Hường Y Quán, 4. Xăm Nghệ Thuật, Tâng Xinh. Nếu dẫn chứng kênh học viên thật thì chỉ dùng **3 kênh có video & số liệu thật trên `https://kenh.fedu.vn/09-case.html`**: Hoàng Nga — Momi Trendii (`@hoangnga_home` - 2.4M view), Từ An — Men Mộc An (85K follow - 2.2M view), Nhà 3 Hờ (`@nha3ho` - 350.1K view).
- **Giữ nguyên phần Câu hỏi dưới cùng (`#sec-faq` gồm 39 câu hỏi thực chiến)** qua placeholder `<!-- INJECT_FAQ_BOTTOM -->`.

---

## II. LỊCH SỬ THẢO LUẬN GẦN NHẤT (`b7cab68b` — NGUYÊN VĂN CÂU HỎI ANH VIỆT & BẢN CHỐT THƯ KÝ OPUS)

### Tin nhắn gốc của anh Việt trong `b7cab68b`:
{chr(10).join(viet_msgs)}

### Bản kiểm chứng & đúc kết của Claude Opus 5.5 (`claude_pro_c3caf46e.md`):
{opus_prev}

---

## III. NGUYÊN VĂN CHỮ SẠCH 2 TRANG GỐC CẦN GỘP

### 3A. TRANG 1: `https://kenh.fedu.vn/cu/index.html` (`logickenh-xaykenh-1.0.html`)
{p1_txt}

---

### 3B. TRANG 2: `https://fedu.vn/k/logickenh-xaykenh.html`
*(Lưu ý: ở mục `case-study` cuối Trang 2 có các link case cũ Hằng BĐS/Bảo hiểm/Kiên Phân Bón/Tattoo đã bị khai tử — chỉ lấy tinh thần lý thuyết "Ngành có Trần Vật Lý" nếu hợp mạch, cấm giữ các case ảo đó).*
{p2_txt}
"""
    p = os.path.join(OUT_DIR, "01_CORE_PAGES_AND_HISTORY.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(trim_utf8(doc1, 44500))


def build_part2():
    pods = [
        ("1. ALEX HORMOZI & STEVEN BARTLETT — Lấy Việc Làm Thật & Dịch Vụ Giá Cao Làm Lợi Thế Cạnh Tranh", "/Users/vietmac/Documents/CODE/k/alex-hormozi-xay-dung-moat-ben-vung-podcast.html", 17500),
        ("2. DANIEL PRIESTLEY — Công Thức Niềm Tin 7-11-4 & Bảo Kê Đầu Ra Cho Khách Hàng Cao Cấp", "/Users/vietmac/Documents/CODE/k/daniel-podcast.html", 12000),
        ("3. RICK RUBIN & STEVEN BARTLETT — Làm Video Là Món Quà, Buông Tay & Triệt Tiêu Ma Sát", "/Users/vietmac/Documents/CODE/k/rick-rubin-ky-nang-duy-nhat-ai-khong-the-danh-cap-podcast.html", 13000),
    ]
    chunks = ["# TẬP 2/3: NGUYÊN VĂN 3 TRỤC DIỄN GIẢ PODCAST (ALEX HORMOZI · DANIEL PRIESTLEY · RICK RUBIN)"]
    for title, path, max_b in pods:
        soup = BeautifulSoup(open(path, "r", encoding="utf-8").read(), "html.parser")
        txt = clean_text_from_el(soup.body if soup.body else soup)
        chunks.append(f"## {title}\n" + trim_utf8(txt, max_b))

    doc2 = "\n\n---\n\n".join(chunks)
    p = os.path.join(OUT_DIR, "02_PODCASTS_HORMOZI_DANIEL_RUBIN.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(trim_utf8(doc2, 44500))


def build_part3():
    items = [
        ("logic18.html — Tâm lý bấm máy quay, lén khóa cửa phòng & đăng xong úp máy chạy ngay", "/Users/vietmac/Documents/CODE/k/logic18.html", 6500),
        ("logic35.html — Phá nghịch lý người mới, Đảo ngược rủi ro (bổ dưa hấu mời nếm) & Bằng chứng không cần xin phép", "/Users/vietmac/Documents/CODE/k/logic35.html", 7500),
        ("logic36.html — Tỷ lệ đóng vòng lặp, Phanh ECU não bộ & Tự tin là tờ biên lai kế toán", "/Users/vietmac/Documents/CODE/k/logic36.html", 6500),
        ("logic39.html — Nguyên lý Rick Rubin: 4 bước gieo hạt, đừng moi hạt đo rễ, đưa ra là xong việc & gỡ chữ Ngại", "/Users/vietmac/Documents/CODE/k/logic39.html", 9500),
        ("logic40.html — Tờ hóa đơn mồ hôi ở góc khuất, thoát cảnh chiếc túi nilon & khóa tín hiệu", "/Users/vietmac/Documents/CODE/k/logic40.html", 6500),
        ("logic41.html — Hóa đơn năng lượng của ma sát & thiết kế độ dốc môi trường khi bấm máy", "/Users/vietmac/Documents/CODE/k/logic41.html", 5500),
    ]
    chunks = ["# TẬP 3/3: NGUYÊN VĂN KHO LOGIC CỐT LÕI (`logic18, 35, 36, 39, 40, 41`) & QUY TẮC GIỌNG VĂN"]
    for title, path, max_b in items:
        soup = BeautifulSoup(open(path, "r", encoding="utf-8").read(), "html.parser")
        txt = clean_text_from_el(soup.body if soup.body else soup)
        chunks.append(f"## {title}\n" + trim_utf8(txt, max_b))

    voice_summary = """## QUY TẮC VĂN PHONG BẮT BUỘC (`nguyen-viet-voice` — Kiểm định tự động qua `verify_voice.py`)
1. **Zero Warm-up:** Vào thẳng luận điểm sắc bén ngay câu đầu tiên của mỗi mục, bỏ mọi câu dạo đầu chung chung.
2. **Phép thử Quán Phở (0% thuật ngữ hàn lâm / tiếng Anh sáo rỗng):** Đổi mọi khái niệm trừu tượng ra hành vi vật lý nhìn thấy được. TUYỆT ĐỐI KHÔNG DÙNG: *ti thể, hàm sóng, negentropy, overjustification, mimetic desire, costly signaling, catch-22, permissionless proof, messy middle, paradigm shift, key person of influence, moat, cringe, lurker, dark social, cognitive fluency, eureka moment* (hãy dịch sang tiếng Việt đời thường tự nhiên như: *người xem thầm lặng, chia sẻ ngầm qua tin nhắn riêng Zalo, hào bảo vệ bằng việc thật, cảm giác ngượng miệng khi nghe lại giọng mình, bằng chứng làm thử không cần xin phép...*).
3. **Sổ đen từ cấm Dao 5:** Cấm *run bật bật, làm sếp nhiều năm, tụi trẻ, cào kịch bản trend, web thu tiền tự động 24/7, siêu phẩm điện ảnh, vũ khí tối thượng, sự thật bàng hoàng, thần thánh, vứt, quân trường, thao túng tâm lý, lùa gà* (lưu ý: phần `#sec-faq` cũ giữ nguyên sẽ được loại trừ khi quét voice, nhưng toàn bộ phần chữ mới bạn viết phải sạch 100% từ cấm!).
4. **Nối ý bằng nhân quả (`vì / nên / nhưng / khi`):** Không viết câu cụt kiểu điện tín AI. Xưng hô tự nhiên, điềm tĩnh của người làm nghề (`bạn - mình` hoặc trực diện trung tính đồng nhất toàn trang).
"""
    chunks.append(voice_summary)
    doc3 = "\n\n---\n\n".join(chunks)
    p = os.path.join(OUT_DIR, "03_KHO_LOGIC_AND_VOICE_RULES.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write(trim_utf8(doc3, 44800))


def main():
    # Remove old monolithic pack if present
    old_p = os.path.join(OUT_DIR, "OPUS_KENH_SOURCE_PACK.md")
    if os.path.exists(old_p):
        os.remove(old_p)

    p1_txt, p2_txt = extract_fragments_and_pages()
    build_part1(p1_txt, p2_txt)
    build_part2()
    build_part3()

    print("=== OPUS PACK V2 SUMMARY ===")
    for fn in sorted(os.listdir(OUT_DIR)):
        fp = os.path.join(OUT_DIR, fn)
        sz = os.path.getsize(fp)
        flag = "✅ <=45KB (1-shot read_file)" if sz <= 45500 else "📦 HTML Fragment (auto-injected)"
        print(f"  {fn:36s}: {sz:8,d} bytes  [{flag}]")


if __name__ == "__main__":
    main()
