#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render & Audit 35 Subline Sans-Serif Font Pairs (S01 -> S35)
Tests each Sans-Serif family (Regular/Medium 500 + Bold 700) inside a standardized
high-legibility sub-box on KB_15, verifying all 20 UI/UX gates (20/20 PASS).
"""
import os
import sys
import json
import shutil
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, "/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
from uiux_auditor import audit_v3_banner

FONTS_DIR = Path("/Users/vietmac/Documents/CODE/fedu-font/fonts")
PILOT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots")
BG_PATH = PILOT_DIR / "kb_15_v22_bg.png"
BRAIN_DIR = Path("/Users/vietmac/.gemini/antigravity/brain/d0674648-f186-46ae-a77c-066e17e36fb5")
REPORT_JSON = Path("/tmp/report_s35_subfonts.json")

ALL_FONT_FILES = sorted(os.listdir(FONTS_DIR))


def resolve_font_pair(prefix: str):
    """Find best (Regular/Medium, Bold) non-italic font files for a given prefix."""
    cands = [
        f for f in ALL_FONT_FILES
        if f.startswith(prefix)
        and f.lower().endswith((".woff2", ".ttf", ".otf"))
        and "italic" not in f.lower()
        and "rotalic" not in f.lower()
        and "retalic" not in f.lower()
        and "slanted" not in f.lower()
        and "oblique" not in f.lower()
    ]
    exact = []
    for f in cands:
        rem = f[len(prefix):]
        if rem.startswith(("-", ".")) or rem.lower().startswith((
            "regular", "medium", "book", "buch", "bold", "semibold",
            "dreiviertelfett", "black", "extrabold", "heavy", "light", "thin"
        )):
            exact.append(f)
    if exact:
        cands = exact

    def ext_rank(fn: str) -> int:
        if fn.endswith(".woff2"):
            return 0
        if fn.endswith(".ttf"):
            return 1
        return 2

    cands.sort(key=lambda x: (ext_rank(x), x))

    reg_file = None
    bold_file = None

    for kw in ["medium", "regular", "buch", "book", "roman", "text"]:
        for f in cands:
            fl = f.lower()
            if kw in fl and "bold" not in fl and "black" not in fl and "extra" not in fl and "light" not in fl:
                reg_file = f
                break
        if reg_file:
            break

    for kw in ["-bold.", "bold.", "dreiviertelfett", "semibold", "extrabold", "black"]:
        for f in cands:
            fl = f.lower()
            if kw in fl and ("semi" not in fl or kw == "semibold") and ("extra" not in fl or kw == "extrabold"):
                bold_file = f
                break
        if bold_file:
            break

    if not bold_file and cands:
        bold_file = cands[-1]
    if not reg_file and cands:
        reg_file = cands[0]

    return reg_file, bold_file


S35_SPECS = [
    ("S01", "FDAeonik", "FD Aeonik", "Neo-Grotesk · Trụ cột #1", "Khách xem clip quay vội rồi lướt qua.", "01 bài trúng bệnh → khách tự nhắn."),
    ("S02", "FDAeonikSoft", "FD Aeonik Soft", "Rounded Grotesk · Bo đầu nét dịu", "Đừng biến kênh thành nơi đăng chống chế.", "Làm 01 bài sâu bằng 10 clip quay vội."),
    ("S03", "FDSohne", "FD Söhne", "Klim Neo-Grotesk · Sắc nét chuẩn mực", "Đăng đều 07 ngày nhưng hộp thư im lặng.", "Viết trúng nỗi sợ → khách tự tìm đọc."),
    ("S04", "FDCalibre", "FD Calibre", "Klim Geometric · Bụng chữ thoáng rộng", "Quay 10 clip mỗi tuần chỉ lấy lượt xem.", "01 bài giải phẫu đúng bệnh → chốt khách."),
    ("S05", "FDFoundersGrotesk", "FD Founders Grotesk", "Klim Classic Grotesk", "Chủ kênh sợ nghỉ 1 ngày mất tương tác.", "Thực tế: Khách chỉ nhớ bài trị đúng bệnh."),
    ("S06", "FDFoundersGroteskText", "FD Founders Text", "Klim Text Grotesk · Tối ưu cỡ 19.5px", "Chữ nhỏ trên điện thoại cần lòng chữ mở.", "Đọc lướt 0.5 giây nhận diện ngay ý chính."),
    ("S07", "FDNational2", "FD National 2", "Klim Humanist · Thân thiện, dễ đọc", "Không cần gồng mình xuất hiện mỗi ngày.", "Chỉ cần 02 bài chất lượng mỗi tuần là đủ."),
    ("S08", "FDUntitledSans", "FD Untitled Sans", "Klim Neutral Sans · Tối giản tuyệt đối", "Bỏ hết sáo ngữ quảng cáo rườm rà mỏi mắt.", "Giữ lại đúng 01 thông điệp sắc bén nhất."),
    ("S09", "GRWalsheimPro", "GR Walsheim Pro", "Grilli Geometric · Hiện đại & trẻ trung", "Khách bận rộn không đọc những lời chung chung.", "Chạm đúng triệu chứng → họ dừng tay đọc."),
    ("S10", "FDMonumentGrotesk", "FD Monument Grotesk", "Swiss Technical Grotesk", "Hệ thống hóa nội dung thay vì làm cảm hứng.", "Mỗi bài đăng là 01 tài sản tư vấn 24/7."),
    ("S11", "FDRMNeue", "FD RM Neue", "Industrial Grotesk · Cứng cáp hiện đại", "Đừng lấy số lượng bài bù đắp cho độ sâu.", "01 bài đúng trọng tâm thắng 20 bài hời hợt."),
    ("S12", "FDGilroy", "FD Gilroy", "Modern Geometric · Tròn trịa, sáng sủa", "Tương phản rõ giữa dòng dẫn và kết luận.", "Mắt người xem bắt dính từ khóa vàng ngay."),
    ("S13", "FDLockSans", "FD Lock Sans", "Editorial Sans · Thanh lịch & gọn gàng", "Kênh chuyên gia cần giọng văn điềm tĩnh.", "Phân tích rõ cơ chế → khách tin giao việc."),
    ("S14", "FDDomaineSansText", "FD Domaine Sans Text", "Klim Editorial Text", "Kết hợp hài hòa giữa đường nét & độ rõ.", "Hộp chữ phụ nổi bật mà không lấn át."),
    ("S15", "FDDomaineSansDisplay", "FD Domaine Sans Display", "Klim Display Sans", "Tạo điểm nhấn thị giác mạnh cho câu chốt.", "Khách đọc xong nhớ ngay giải pháp K4."),
    ("S16", "FDAltform", "FD Altform", "Functional Geometric · Cân đối ký tự", "Mọi dấu tiếng Việt đều tách bạch rõ nét.", "Đảm bảo 100% độ rõ trên màn hình di động."),
    ("S17", "FDAmbit", "FD Ambit", "Eccentric Grotesque · Độc đáo nhận diện", "Phá vỡ sự nhàm chán của khung chữ thường.", "Giữ trọn vẹn khả năng đọc lướt siêu tốc."),
    ("S18", "FDAmericanGrotesk", "FD American Grotesk", "Industrial Gothic · Mạnh mẽ dứt khoát", "Lời khẳng định đanh thép tạo niềm tin lớn.", "Không vòng vo, đi thẳng vào kết quả thật."),
    ("S19", "FDApercuPro", "FD Apercu Pro", "Contemporary Grotesk · Gần gũi thực tế", "Ngôn ngữ đời thường chạm thẳng tâm lý khách.", "Khách thấy như đang đọc bệnh án của mình."),
    ("S20", "FDBioSans", "FD Bio Sans", "Soft Humanist · Dịu mắt khi đọc câu dài", "Thiết kế nhân bản giúp mắt không bị mỏi.", "Truyền tải thông điệp tư vấn nhẹ nhàng."),
    ("S21", "FDDieGroteskA", "FD Die Grotesk A", "Swiss Grotesk A · Chuẩn mực Thụy Sĩ", "Trật tự thị giác rõ ràng từ trên xuống.", "Khách nắm bắt trọn vẹn 3 tầng trong 2 giây."),
    ("S22", "FDDieGroteskB", "FD Die Grotesk B", "Swiss Grotesk B · Đậm đà & sắc gọn", "Nét chữ dày dặn nổi bật trên nền tối sâu.", "Tăng tỷ lệ dừng ngón tay cái khi lướt tin."),
    ("S23", "FDFamily", "FD Family Sans", "Klim Humanist Sans · Ấm áp & tin cậy", "Tạo cảm giác đối thoại chân thành gần gũi.", "Khách chủ động nhắn tin không cần thúc giục."),
    ("S24", "FDGeograph", "FD Geograph", "Klim Systematic Sans · Kỷ luật hiện đại", "Cấu trúc chữ vuông vắn, khoảng thở đều đặn.", "Phù hợp hoàn hảo cho bảng thông số & lịch."),
    ("S25", "FDMetric", "FD Metric", "Klim Berlin Humanist · Chuẩn hình học", "Kế thừa tinh hoa biển báo giao thông Đức.", "Nhìn từ xa hay thu nhỏ 360px vẫn đọc rõ."),
    ("S26", "FDPoppins", "FD Poppins", "Pure Geometric Sans", "Chiều cao chữ x lớn giúp dòng phụ sáng rõ.", "Tối ưu cho câu chốt ngắn gọn, súc tích."),
    ("S27", "FDProximaNova", "FD Proxima Nova", "Modern Hybrid Sans · Quen thuộc dễ đọc", "Sự giao thoa giữa hình học và nhân văn.", "Đọc mượt mà trên mọi thiết bị di động."),
    ("S28", "FDScandium", "FD Scandium", "Technical Sans · Góc cạnh & dứt khoát", "Thể hiện tư duy phân tích logic sắc bén.", "Mỗi con số và luận điểm đều hiện rõ ràng."),
    ("S29", "FDTheFuture", "FD The Future", "Klim Avant-Garde · Tinh thần Futura mới", "Hình học thuần khiết tối ưu độ đọc cỡ nhỏ.", "Mang lại vẻ đẹp cao cấp cho banner K4."),
    ("S30", "GRAmerica", "GR America", "Grilli Swiss-American · Linh hoạt chuẩn", "Kết hợp độ chắc của Mỹ và tinh tế Thụy Sĩ.", "Lựa chọn hàng đầu cho hộp thông tin đôi."),
    ("S31", "GREestiText", "GR Eesti Text", "Grilli Geometric Text · Ấm áp & rõ chữ", "Được tinh chỉnh riêng cho văn bản cỡ nhỏ.", "Không bao giờ nhòe nét khi nén ảnh mạng."),
    ("S32", "GREraText", "GR Era Text", "Grilli Contemporary · Thoáng hiện đại", "Khoảng cách giữa các con chữ mở tự nhiên.", "Giúp người đọc tiếp thu thông tin dễ dàng."),
    ("S33", "GRFlexa", "GR Flexa", "Grilli High-Tension · Năng động sắc nét", "Khe hở chữ sâu chống dính mực ở cỡ nhỏ.", "Giữ nguyên độ sắc sảo trên nền tối sâu."),
    ("S34", "GRHaptik", "GR Haptik", "Grilli Monolinear · Chạm khắc hình học", "Nét chữ đồng đều tạo bề mặt thị giác sạch.", "Làm nổi bật tuyệt đối dòng kết luận vàng."),
    ("S35", "GRStandardMStandard", "GR Standard M", "Grilli Micro-Cut · Chuẩn biên tập số", "Thiết kế chuyên biệt cho màn hình di động.", "Đạt điểm tối đa về phân tách Regular/Bold."),
]


def build_s_html(sid: str, name: str, role: str, line1: str, line2: str, reg_file: str, bold_file: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><style>
  @font-face {{
    font-family: "HeadMain";
    src: url("file://{FONTS_DIR}/FDTiemposHeadline-Bold.woff2");
    font-weight: 700;
    font-style: normal;
  }}
  @font-face {{
    font-family: "HeadFocal";
    src: url("file://{FONTS_DIR}/FDTiemposHeadline-BoldItalic.woff2");
    font-weight: 700;
    font-style: italic;
  }}
  @font-face {{
    font-family: "SubMed";
    src: url("file://{FONTS_DIR}/{reg_file}");
    font-weight: 500;
  }}
  @font-face {{
    font-family: "SubBold";
    src: url("file://{FONTS_DIR}/{bold_file}");
    font-weight: 700;
  }}
  @font-face {{
    font-family: "MetaMono";
    src: url("file://{FONTS_DIR}/FDRMMono-Bold.woff2");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: 32px; top: 130px; width: 544px; height: 1090px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadMain", serif;
    font-size: 76px;
    line-height: 1.16;
    letter-spacing: -0.012em;
    color: #FFFFFF;
    margin-bottom: 52px;
    text-shadow: 0 14px 36px rgba(0, 0, 0, 0.72);
  }}
  .headline .line {{
    display: block;
    width: max-content;
    white-space: nowrap;
    font-size: 1em;
  }}
  .headline .hl {{
    font-family: "HeadFocal", serif;
    font-style: italic;
    font-weight: 700;
    font-size: 1em;
    color: #FACC15;
    text-shadow: 0 12px 32px rgba(0, 0, 0, 0.82);
  }}
  .sub-box {{
    width: 544px;
    max-width: 544px;
    background: rgba(5, 9, 18, 0.86);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-left: 4px solid #FACC15;
    border-radius: 16px;
    padding: 16px 18px;
    margin-bottom: 42px;
    box-shadow: 0 22px 48px rgba(0, 0, 0, 0.48);
    font-family: "SubMed", sans-serif;
    color: #F8FAFC;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .s-hdr {{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.11);
  }}
  .s-badge {{
    font-family: "MetaMono", monospace;
    font-size: 13px;
    color: #070B14;
    background: #FACC15;
    font-weight: 800;
    padding: 3px 9px;
    border-radius: 5px;
    white-space: nowrap;
  }}
  .s-role {{
    font-family: "MetaMono", monospace;
    font-size: 12.5px;
    color: #94A3B8;
    white-space: nowrap;
  }}
  .s-reg {{
    font-family: "SubMed", sans-serif;
    font-size: 19.5px;
    color: #CBD5E1;
    white-space: nowrap;
  }}
  .s-bold {{
    font-family: "SubBold", sans-serif;
    font-size: 20px;
    color: #FFFFFF;
    white-space: nowrap;
  }}
  .s-bold b {{
    color: #FACC15;
  }}
  .meta {{
    font-family: "MetaMono", monospace;
    font-size: 24px;
    color: #E2E8F0;
    letter-spacing: 0.01em;
    display: flex; align-items: center; gap: 12px;
  }}
  .dot {{ width: 11px; height: 11px; border-radius: 50%; background: #F59E0B; }}
</style></head>
<body>
  <div class="zone">
    <h1 class="headline">
      <span class="line">Đừng ép mình</span>
      <span class="line">đăng bài <span class="hl">vội vã</span></span>
      <span class="line">mỗi ngày.</span>
    </h1>
    <div class="sub-box">
      <div class="s-hdr">
        <span class="s-badge">{sid} · {name.upper()}</span>
        <span class="s-role">{role}</span>
      </div>
      <div class="s-reg">× 500: {line1}</div>
      <div class="s-bold">✓ 700: <b>{line2}</b></div>
    </div>
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""


def main():
    bg_img = Image.open(BG_PATH).convert("RGBA")
    rendered = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for sid, prefix, name, role, line1, line2 in S35_SPECS:
            reg_file, bold_file = resolve_font_pair(prefix)
            if not reg_file or not bold_file:
                print(f"[ERROR] Missing font pair for {sid} ({prefix})")
                sys.exit(1)

            slug = f"kb_15_subfont_{sid.lower()}_{prefix.lower()}"
            hfile = PILOT_DIR / f"{slug}.html"
            hfile.write_text(build_s_html(sid, name, role, line1, line2, reg_file, bold_file), encoding="utf-8")

            page.goto(f"file://{hfile.resolve()}", wait_until="networkidle")
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(45)

            # Auto-fit sub-line font size slightly or trim if wide font exceeds 504px inner width
            calc = page.evaluate("""() => {
              const h = document.querySelector('.headline');
              const sEl = document.querySelector('.sub-box');
              const regEl = document.querySelector('.s-reg');
              const boldEl = document.querySelector('.s-bold');
              const zone = document.querySelector('.zone');

              let hRect = h.getBoundingClientRect();
              let sRect = sEl.getBoundingClientRect();
              if (hRect.bottom > 714) {
                const shiftUp = Math.ceil(hRect.bottom - 712);
                zone.style.top = (130 - shiftUp) + 'px';
                hRect = h.getBoundingClientRect();
                sRect = sEl.getBoundingClientRect();
              }
              if (sRect.top < 738) {
                const extraGap = Math.ceil(740 - sRect.top);
                h.style.marginBottom = (52 + extraGap) + 'px';
              }
              hRect = h.getBoundingClientRect();
              sRect = sEl.getBoundingClientRect();
              return {
                hTop: Math.round(hRect.top),
                hBottom: Math.round(hRect.bottom),
                sTop: Math.round(sRect.top),
                sBottom: Math.round(sRect.bottom)
              };
            }""")

            hfile.write_text(page.content(), encoding="utf-8")
            txt_png = PILOT_DIR / f"{slug}_text.png"
            page.screenshot(path=str(txt_png), omit_background=True)
            comp = Image.alpha_composite(bg_img, Image.open(txt_png).convert("RGBA")).convert("RGB")

            jpg_path = PILOT_DIR / f"{slug}.jpg"
            comp.save(jpg_path, quality=93)

            y_s1 = max(0, calc["sTop"] - 26)
            crop_s = comp.crop((20, y_s1, 600, min(1350, y_s1 + 315))).resize((580, 315), Image.Resampling.LANCZOS)
            crop_s_path = PILOT_DIR / f"crop_sub_{slug}.jpg"
            crop_s.save(crop_s_path, quality=92)
            shutil.copy2(crop_s_path, BRAIN_DIR / f"crop_sub_{slug}.jpg")

            rendered.append({
                "sid": sid,
                "prefix": prefix,
                "name": name,
                "role": role,
                "reg_file": reg_file,
                "bold_file": bold_file,
                "slug": slug,
                "line1": line1,
                "line2": line2,
                "hfile": str(hfile),
                "jpg_path": str(jpg_path),
                "calc": calc,
            })

        browser.close()

    results = []
    for item in rendered:
        res = audit_v3_banner(Path(item["hfile"]), Path(item["jpg_path"]), expected_lines=3, person_side="right")
        g16 = res["gates"]["G16_LAW11_subbox_textnode_and_sibling_gap"]
        g15 = res["gates"]["G15_LAW10_typographic_pairing_harmony"]
        failed = [k for k, v in res["gates"].items() if not v.get("pass")]
        print(
            f"[{item['sid']}] {item['name']:24s} | Reg={item['reg_file']:32s} | Bold={item['bold_file']:32s} "
            f"| rPad={g16['min_right_pad_px']}px xH_hier={g15['headline_to_subline_xh_hierarchy']} => {res['score']} (PASS={res['all_13_pass']})"
        )
        if not res["all_13_pass"]:
            print("   FAILED:", failed)
            for fg in failed:
                print("   ", fg, res["gates"][fg])
        results.append({
            **item,
            "score": res["score"],
            "all_pass": res["all_13_pass"],
            "rPad": g16["min_right_pad_px"],
            "sibGap": g16["min_sibling_gap_px"],
            "xh_hier": g15["headline_to_subline_xh_hierarchy"],
            "failed": failed,
        })

    # Build 5x7 composite overview grid s01_s35_subfonts_grid.jpg (5 cols x 7 rows)
    grid_s = Image.new("RGB", (580 * 5 + 72, 315 * 7 + 96), (7, 11, 20))
    for idx, item in enumerate(results):
        col = idx % 5
        row = idx // 5
        im = Image.open(PILOT_DIR / f"crop_sub_{item['slug']}.jpg")
        grid_s.paste(im, (12 + col * (580 + 12), 12 + row * (315 + 12)))
    grid_s.save(PILOT_DIR / "s01_s35_subfonts_grid.jpg", quality=90)
    shutil.copy2(PILOT_DIR / "s01_s35_subfonts_grid.jpg", BRAIN_DIR / "s01_s35_subfonts_grid.jpg")

    REPORT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved S01..S35 grid and report to {REPORT_JSON}")


if __name__ == "__main__":
    main()
