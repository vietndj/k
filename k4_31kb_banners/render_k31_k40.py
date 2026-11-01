#!/usr/bin/env python3
"""
Render & Audit 10 NEW Subline Box Styles (K31 -> K40, 0% overlap with K01..K30)
and update /Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html (total 39 Subboxes K01..K40, excluding #11).
Every render is verified via uiux_auditor.py (16/16 gates PASS).
"""
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, "/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
from uiux_auditor import audit_v3_banner

FONT_DIR = Path("/Users/vietmac/Documents/CODE/fedu-font/fonts")
PILOT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots")
BG_PATH = PILOT_DIR / "kb_15_v22_bg.png"
BRAIN_DIR = Path("/Users/vietmac/.gemini/antigravity/brain/d0674648-f186-46ae-a77c-066e17e36fb5")
HUB_HTML = Path("/Users/vietmac/Documents/CODE/k/bo-chon-chu-banner.html")

NEW_K31_K40_SPECS: List[Dict[str, Any]] = [
    {
        "kid": "K31",
        "kgroup": "KA",
        "kgroup_label": "Họ 1 • Đối Lập & So Sánh 2 Vế",
        "sid": "kb_15_new_k31_can_can_2dia",
        "name": "Cán Cân Đối Trọng 2 Đĩa ([10 Clip] < [01 Bài])",
        "author": "GEMINI",
        "sample_quote": "[10 CLIP QUAY VỘI] < [01 BÀI GIẢI MÃ SÂU] — Khách chọn độ sâu chuyên môn, không đếm bài.",
        "desc": "Đặt hai vế lên bàn cân đối trọng qua tâm điểm dấu bất đẳng thức vàng (<), chốt câu kết luận ở thanh đế phía dưới.",
        "h_main_file": "GRCanonLNarrowBold.woff2",
        "h_focal_file": "GRCanonLNarrowBold.woff2",
        "h_focal_style": "normal",
        "sub_med_file": "GRWalsheimPro-Medium.woff2",
        "sub_bold_file": "GRWalsheimPro-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k31">
          <div class="scale-top">
            <span class="sc-pan old"><b class="mono">10</b> CLIP QUAY VỘI</span>
            <span class="sc-fulcrum mono">&lt;</span>
            <span class="sc-pan new"><b class="mono">01</b> BÀI GIẢI MÃ SÂU</span>
          </div>
          <div class="scale-base">Khách chọn <b class="gold">độ sâu chuyên môn</b>, không đếm bài.</div>
        </div>
        """,
    },
    {
        "kid": "K32",
        "kgroup": "KB",
        "kgroup_label": "Họ 2 • Con Số & Thời Gian / Lịch",
        "sid": "kb_15_new_k32_dong_ho_3giay",
        "name": "Đồng Hồ Điểm Rơi 3 Giây Đầu (00:03s Hook Gate)",
        "author": "CLAUDE2",
        "sample_quote": "[00:03s] 01–03s: Giữ chân bằng triệu chứng | 04–60s: Giải mã cơ chế khiến khách nhắn.",
        "desc": "Bên trái là đồng hồ Timecode Studio 00:03s, bên phải chia 2 mốc thời gian giữ chân và chuyển đổi khách hàng.",
        "h_main_file": "GRFlaireBasicBold.woff2",
        "h_focal_file": "GRFlaireBasicBoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDGraphik-Medium.woff2",
        "sub_bold_file": "FDGraphik-Bold.woff2",
        "mono_file": "JetBrainsMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k32">
          <div class="tc-clock mono">
            <span class="tc-lbl">MỐC GIỮ CHÂN</span>
            <span class="tc-num">00:03s</span>
          </div>
          <div class="tc-right">
            <div class="tc-line old"><span class="tc-pill mono">01–03s</span><span>Giữ chân bằng đúng triệu chứng.</span></div>
            <div class="tc-line new"><span class="tc-pill active mono">04–60s</span><span>Giải mã cơ chế khiến khách nhắn.</span></div>
          </div>
        </div>
        """,
    },
    {
        "kid": "K33",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k33_kieng_3chan",
        "name": "Kiềng 3 Chân Nội Dung (3-Column Mini Cards)",
        "author": "GEMINI",
        "sample_quote": "[01 · BẮT BỆNH: Đúng triệu chứng] | [02 · MỔ XẺ: Đúng cơ chế] | [03 · KẾT QUẢ: Khách tự nhắn]",
        "desc": "Chia khung thành 3 thẻ cột đứng song song (3-Column Mini Cards), thẻ thứ 3 phát sáng vàng chốt hành động.",
        "h_main_file": "GRZirkonBold.woff2",
        "h_focal_file": "GRZirkonBoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDAeonikSoft-Medium.woff2",
        "sub_bold_file": "FDAeonikSoft-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k33">
          <div class="tri-grid">
            <div class="tri-card">
              <div class="tri-hd mono">01 · BẮT BỆNH</div>
              <div class="tri-bd">Đúng triệu chứng</div>
            </div>
            <div class="tri-card">
              <div class="tri-hd mono">02 · MỔ XẺ</div>
              <div class="tri-bd">Đúng cơ chế gốc</div>
            </div>
            <div class="tri-card active">
              <div class="tri-hd mono gold">03 · KẾT QUẢ</div>
              <div class="tri-bd gold">Khách tự nhắn</div>
            </div>
          </div>
          <div class="tri-foot">Đủ <b class="mono gold">03</b> <b class="gold">chân kiềng</b>: đăng <b class="mono">01</b> bài vẫn ra đơn đều.</div>
        </div>
        """,
    },
    {
        "kid": "K34",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k34_binh_luan_ghim",
        "name": "Thẻ Bình Luận Khách Thật Được Ghim (Pinned Comment)",
        "author": "CLAUDE2",
        "sample_quote": "📌 BÌNH LUẬN ĐƯỢC GHIM: “Xem đúng 01 bài bóc tách của anh là em nhắn đăng ký luôn.”",
        "desc": "Mô phỏng bình luận khách thật được ghim trên đầu bài viết kèm nhãn xác thực học viên thực tế.",
        "h_main_file": "FDTiemposFine-Bold.woff2",
        "h_focal_file": "FDTiemposFine-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDUntitledSans-Medium.woff2",
        "sub_bold_file": "FDUntitledSans-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k34">
          <div class="pin-head">
            <span class="pin-tag mono">📌 BÌNH LUẬN ĐƯỢC GHIM</span>
            <span class="pin-user mono">HỌC VIÊN K3</span>
          </div>
          <div class="pin-quote">“Xem đúng <b class="gold">01 bài bóc tách</b> của anh là em nhắn đăng ký luôn.”</div>
        </div>
        """,
    },
    {
        "kid": "K35",
        "kgroup": "KA",
        "kgroup_label": "Họ 1 • Đối Lập & So Sánh 2 Vế",
        "sid": "kb_15_new_k35_lat_cat_2tang",
        "name": "Lát Cắt Giải Phẫu 2 Tầng ([BỀ NỔI] / [GỐC RỄ])",
        "author": "GEMINI",
        "sample_quote": "[BỀ NỔI] Đăng vội mỗi ngày chờ thuật toán  |  [GỐC RỄ] Gọi trúng nỗi sợ khiến khách tự nhắn",
        "desc": "Hai dải hộp xếp chồng khít lên nhau như lát cắt địa chất: tầng bề nổi tối mờ, tầng gốc rễ nền vàng rực.",
        "h_main_file": "FDLockSerifStencil-Bold.woff2",
        "h_focal_file": "FDLockSerifStencil-Bold.woff2",
        "h_focal_style": "normal",
        "sub_med_file": "FDLockSans-Medium.woff2",
        "sub_bold_file": "FDLockSans-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k35">
          <div class="layer-band top-band">
            <span class="ly-tag mono">BỀ NỔI</span>
            <span class="ly-txt">Đăng vội mỗi ngày chờ thuật toán thương</span>
          </div>
          <div class="layer-band bot-band">
            <span class="ly-tag gold-tag mono">GỐC RỄ</span>
            <span class="ly-txt bright">Gọi trúng nỗi sợ khiến khách tự nhắn</span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K36",
        "kgroup": "KB",
        "kgroup_label": "Họ 2 • Con Số & Thời Gian / Lịch",
        "sid": "kb_15_new_k36_the_diem_hang_a",
        "name": "Thẻ Điểm Chuyển Đổi Thực Chiến (Scorecard A+ Bên Phải)",
        "author": "CLAUDE2",
        "sample_quote": "Lịch đăng: Giảm còn 02 bài/tuần · Khách nhắn: Tăng gấp 4.5 lần  |  [HIỆU SUẤT A+]",
        "desc": "Đảo chiều thị giác: đặt cột thông số giảm tải bên trái và đóng dấu Huy Hiệu Xếp Hạng A+ rực sáng ở bên phải.",
        "h_main_file": "FDDomaineDisplayNarrow-Bold.woff2",
        "h_focal_file": "FDDomaineDisplayNarrow-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDNational2-Medium.woff2",
        "sub_bold_file": "FDNational2-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k36">
          <div class="sc-left">
            <div class="sc-row1">Lịch đăng: Giảm còn <b class="mono">02</b> <b>bài/tuần</b></div>
            <div class="sc-row2">Lượng khách nhắn: <b class="gold">Tăng gấp 4.5 lần</b></div>
          </div>
          <div class="sc-badge mono">
            <span class="b-top">HIỆU SUẤT</span>
            <span class="b-bot">A+</span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K37",
        "kgroup": "KE",
        "kgroup_label": "Họ 5 • Tuyên Ngôn & Đúc Kết",
        "sid": "kb_15_new_k37_dieu_khoan_luat",
        "name": "Điều Khoản Luật Bất Biến (ĐIỀU 01 · QUY LUẬT K4)",
        "author": "GEMINI",
        "sample_quote": "── ĐIỀU 01 · QUY LUẬT CHUYỂN ĐỔI ── Bài đăng vội lấp đầy tường. Bài sâu lấp đầy lịch hẹn.",
        "desc": "Trình bày trang trọng như một điều khoản hiến chương chuyên gia với vạch kẻ đối xứng hai bên tiêu đề.",
        "h_main_file": "FDCharter-Bold.woff2",
        "h_focal_file": "FDCharter-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDPitch-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k37">
          <div class="law-hdr">
            <span class="law-line"></span>
            <span class="law-title mono">ĐIỀU 01 · QUY LUẬT CHUYỂN ĐỔI</span>
            <span class="law-line"></span>
          </div>
          <div class="law-p1">Bài đăng vội chỉ lấp đầy trang cá nhân.</div>
          <div class="law-p2">Bài giải mã sâu mới lấp đầy lịch hẹn khách hàng.</div>
        </div>
        """,
    },
    {
        "kid": "K38",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k38_bo_loc_tin_hieu",
        "name": "Bộ Thu Tín Hiệu Khách Hàng (Nhiễu Sóng vs Trúng Đích)",
        "author": "CLAUDE2",
        "sample_quote": "[≈ NHIỄU SÓNG] 07 clip bắt trend → 00 khách hỏi  |  [⌖ TRÚNG ĐÍCH] 01 bài mổ xẻ → Khách tự tìm",
        "desc": "Phân tách tín hiệu thị trường thành 2 dải sóng: Nhiễu sóng (bắt trend vô bổ) đối lập với Trúng đích (mổ xẻ bệnh nghề).",
        "h_main_file": "FDOrbikular-Bold.woff2",
        "h_focal_file": "FDOrbikular-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDRMNeue-Regular.woff2",
        "sub_bold_file": "FDRMNeue-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k38">
          <div class="sig-row old">
            <span class="sig-pill muted mono">≈ NHIỄU SÓNG</span>
            <span class="sig-txt"><b class="mono">07</b> clip bắt trend → <b class="mono">00</b> khách hỏi</span>
          </div>
          <div class="div-line"></div>
          <div class="sig-row new">
            <span class="sig-pill active mono">⌖ TRÚNG ĐÍCH</span>
            <span class="sig-txt"><b class="mono gold">01</b> bài mổ xẻ bệnh → <b class="gold">Khách tự tìm</b></span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K39",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k39_cap_thoai_lech",
        "name": "Cặp Thoại Tư Duy Ngược Lệch Trái – Phải (Đám Đông vs K4)",
        "author": "GEMINI",
        "sample_quote": "[SỐ ĐÔNG] “Phải đăng mỗi ngày khách mới nhớ”  ↔  [THỰC TẾ K4] “Khách chỉ nhớ người trị đúng bệnh”",
        "desc": "Hai hộp thoại đặt lệch trái – phải (Staggered Dual Bubbles) tạo nhịp đối đáp trực diện giữa Số Đông và Thực Tế K4.",
        "h_main_file": "GRUltraStandard-Bold.woff2",
        "h_focal_file": "GRUltraStandard-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "GRWalsheimPro-Medium.woff2",
        "sub_bold_file": "GRWalsheimPro-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k39">
          <div class="bub-left">
            <span class="bub-lbl mono">SỐ ĐÔNG</span>
            <span class="bub-txt">“Phải đăng mỗi ngày khách mới nhớ”</span>
          </div>
          <div class="bub-right">
            <span class="bub-lbl gold mono">THỰC TẾ K4</span>
            <span class="bub-txt gold">“Khách chỉ nhớ người trị đúng bệnh”</span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K40",
        "kgroup": "KE",
        "kgroup_label": "Họ 5 • Tuyên Ngôn & Đúc Kết",
        "sid": "kb_15_new_k40_dai_bang_kiem_chung",
        "name": "Dải Băng Kiểm Chứng Thực Nghiệm (Header Ribbon 31/31 Ngành)",
        "author": "CLAUDE2",
        "sample_quote": "[✓ ĐÃ KIỂM CHỨNG TRÊN 31 NGÀNH NGHỀ · K4] ▪ Không gồng quay mỗi ngày ▪ Chỉ cần 01 bài Giải Mã.",
        "desc": "Thiết kế thẻ hồ sơ có thanh Header Ribbon vàng tràn đỉnh hộp, bên dưới chốt 2 nguyên tắc giải phóng sức lao động.",
        "h_main_file": "FDKarbonSlabStencil-Bold.woff2",
        "h_focal_file": "FDKarbonSlabStencil-Bold.woff2",
        "h_focal_style": "normal",
        "sub_med_file": "FDAeonik-Medium.woff2",
        "sub_bold_file": "FDAeonik-Bold.woff2",
        "mono_file": "JetBrainsMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k40">
          <div class="rib-head mono">✓ ĐÃ KIỂM CHỨNG TRÊN 31 NGÀNH NGHỀ · K4</div>
          <div class="rib-body">
            <div class="rib-item old">▪ Không cần gồng mình quay clip mỗi ngày.</div>
            <div class="rib-item new">▪ Chỉ cần <b class="gold">01 bài đúng cấu trúc Giải Mã 3 Tầng.</b></div>
          </div>
        </div>
        """,
    },
]


def build_html(spec: Dict[str, Any]) -> str:
    focal_style = spec.get("h_focal_style", "italic")
    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8"><style>
  @font-face {{
    font-family: "HeadMain";
    src: url("file://{FONT_DIR}/{spec['h_main_file']}");
    font-weight: 700;
    font-style: normal;
  }}
  @font-face {{
    font-family: "HeadFocal";
    src: url("file://{FONT_DIR}/{spec['h_focal_file']}");
    font-weight: 700;
    font-style: {focal_style};
  }}
  @font-face {{
    font-family: "SubMed";
    src: url("file://{FONT_DIR}/{spec['sub_med_file']}");
    font-weight: 500;
  }}
  @font-face {{
    font-family: "SubBold";
    src: url("file://{FONT_DIR}/{spec['sub_bold_file']}");
    font-weight: 700;
  }}
  @font-face {{
    font-family: "MetaMono";
    src: url("file://{FONT_DIR}/{spec['mono_file']}");
    font-weight: 700;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
  body {{ width: 1080px; height: 1350px; background: transparent; overflow: hidden; position: relative; }}
  .zone {{
    position: absolute; left: 40px; top: 135px; width: 570px; height: 1090px;
    display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
  }}
  .headline {{
    font-family: "HeadMain", serif;
    font-size: 86px;
    line-height: 1.08;
    letter-spacing: -0.010em;
    color: #FFFFFF;
    margin-bottom: 50px;
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
    font-style: {focal_style};
    font-weight: 700;
    font-size: 1em;
    color: #FACC15;
    text-shadow: 0 12px 32px rgba(0, 0, 0, 0.82);
  }}

  .sub-box {{
    width: 546px;
    max-width: 546px;
    background: rgba(5, 9, 18, 0.82);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 44px;
    box-shadow: 0 22px 48px rgba(0, 0, 0, 0.48);
    font-family: "SubMed", sans-serif;
    color: #F8FAFC;
  }}
  .mono {{
    font-family: "MetaMono", monospace !important;
    letter-spacing: -0.01em;
  }}
  .gold {{ color: #FACC15 !important; }}
  .div-line {{ height: 1px; background: rgba(255, 255, 255, 0.11); width: 100%; margin: 12px 0; }}

  /* K31 Balance Scale */
  .scale-top {{ display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-bottom: 12px; }}
  .sc-pan {{ flex: 1; text-align: center; padding: 7px 10px; border-radius: 9px; font-size: 18px; white-space: nowrap; }}
  .sc-pan.old {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(148,163,184,0.25); color: #94A3B8; }}
  .sc-pan.new {{ background: rgba(250,204,21,0.14); border: 1.5px solid #FACC15; color: #FACC15; font-family: "SubBold", sans-serif; }}
  .sc-fulcrum {{ width: 32px; height: 32px; border-radius: 50%; background: #FACC15; color: #070B14; display: flex; align-items: center; justify-content: center; font-size: 19px; font-weight: 900; flex-shrink: 0; }}
  .scale-base {{ text-align: center; background: rgba(255,255,255,0.04); border-top: 2px solid rgba(250,204,21,0.45); padding-top: 9px; font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; white-space: nowrap; }}

  /* K32 Studio Clock 00:03s */
  .box-k32 {{ display: flex; align-items: center; gap: 14px; }}
  .tc-clock {{ background: rgba(250,204,21,0.11); border: 1.5px solid #FACC15; border-radius: 12px; padding: 9px 11px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; }}
  .tc-lbl {{ font-size: 11.5px; color: #CBD5E1; letter-spacing: 0.04em; margin-bottom: 3px; white-space: nowrap; }}
  .tc-num {{ font-size: 24px; color: #FACC15; font-weight: 800; white-space: nowrap; }}
  .tc-right {{ display: flex; flex-direction: column; gap: 9px; flex: 1; min-width: 0; }}
  .tc-line {{ display: flex; align-items: center; gap: 10px; font-size: 19.5px; line-height: 1.28; white-space: nowrap; }}
  .tc-line.old {{ color: #94A3B8; }}
  .tc-line.new {{ color: #FFFFFF; font-family: "SubBold", sans-serif; }}
  .tc-pill {{ font-size: 13.5px; padding: 3px 7px; border-radius: 5px; background: rgba(148,163,184,0.16); color: #CBD5E1; flex-shrink: 0; }}
  .tc-pill.active {{ background: #FACC15; color: #070B14; font-weight: 800; }}

  /* K33 3-Column Mini Cards */
  .tri-grid {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-bottom: 10px; }}
  .tri-card {{ background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.14); border-radius: 10px; padding: 9px 10px; display: flex; flex-direction: column; gap: 5px; }}
  .tri-card.active {{ background: rgba(250,204,21,0.12); border: 1.5px solid #FACC15; }}
  .tri-hd {{ font-size: 13px; color: #94A3B8; white-space: nowrap; }}
  .tri-bd {{ font-family: "SubBold", sans-serif; font-size: 16.5px; color: #FFFFFF; line-height: 1.25; white-space: nowrap; }}
  .tri-foot {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; text-align: center; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.11); white-space: nowrap; }}

  /* K34 Pinned Comment */
  .pin-head {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 9px; padding-bottom: 8px; border-bottom: 1px solid rgba(255,255,255,0.11); }}
  .pin-tag {{ font-size: 14.5px; color: #FACC15; white-space: nowrap; }}
  .pin-user {{ font-size: 13.5px; color: #94A3B8; background: rgba(255,255,255,0.07); padding: 3px 8px; border-radius: 6px; white-space: nowrap; }}
  .pin-quote {{ font-family: "SubBold", sans-serif; font-size: 20.5px; color: #FFFFFF; line-height: 1.35; white-space: normal; }}

  /* K35 Stacked Layer Slice */
  .box-k35 {{ display: flex; flex-direction: column; gap: 9px; }}
  .layer-band {{ display: flex; align-items: center; gap: 11px; padding: 10px 12px; border-radius: 10px; }}
  .layer-band.top-band {{ background: rgba(255,255,255,0.04); border: 1px solid rgba(148,163,184,0.22); color: #94A3B8; }}
  .layer-band.bot-band {{ background: rgba(250,204,21,0.13); border: 1.5px solid #FACC15; color: #FFFFFF; }}
  .ly-tag {{ font-size: 14px; padding: 3px 8px; border-radius: 5px; background: rgba(148,163,184,0.18); color: #CBD5E1; white-space: nowrap; flex-shrink: 0; }}
  .ly-tag.gold-tag {{ background: #FACC15; color: #070B14; font-weight: 800; }}
  .ly-txt {{ font-size: 19.5px; white-space: nowrap; }}
  .ly-txt.bright {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; }}

  /* K36 Right Scorecard A+ */
  .box-k36 {{ display: flex; align-items: center; justify-content: space-between; gap: 16px; }}
  .sc-left {{ display: flex; flex-direction: column; gap: 8px; flex: 1; min-width: 0; }}
  .sc-row1 {{ font-size: 19.5px; color: #CBD5E1; white-space: nowrap; }}
  .sc-row2 {{ font-family: "SubBold", sans-serif; font-size: 20.5px; color: #FFFFFF; white-space: nowrap; }}
  .sc-badge {{ border: 2px solid #FACC15; background: rgba(250,204,21,0.14); border-radius: 12px; padding: 8px 14px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; }}
  .sc-badge .b-top {{ font-size: 12px; color: #FACC15; letter-spacing: 0.05em; white-space: nowrap; }}
  .sc-badge .b-bot {{ font-size: 29px; color: #FACC15; font-weight: 900; line-height: 1.1; white-space: nowrap; }}

  /* K37 Legal Statute Clause */
  .law-hdr {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }}
  .law-line {{ flex: 1; height: 1px; background: rgba(250,204,21,0.45); }}
  .law-title {{ font-size: 14px; color: #FACC15; letter-spacing: 0.05em; white-space: nowrap; }}
  .law-p1 {{ text-align: center; font-size: 19.5px; color: #CBD5E1; margin-bottom: 6px; white-space: nowrap; }}
  .law-p2 {{ text-align: center; font-family: "SubBold", sans-serif; font-size: 20.5px; color: #FACC15; white-space: nowrap; }}

  /* K38 Signal vs Noise */
  .sig-row {{ display: flex; align-items: center; gap: 11px; font-size: 19.5px; }}
  .sig-pill {{ font-size: 14px; padding: 4px 8px; border-radius: 6px; white-space: nowrap; flex-shrink: 0; }}
  .sig-pill.muted {{ background: rgba(148,163,184,0.16); border: 1px solid rgba(148,163,184,0.3); color: #94A3B8; }}
  .sig-pill.active {{ background: #FACC15; color: #070B14; font-weight: 800; }}
  .sig-row.old .sig-txt {{ color: #94A3B8; font-size: 19.5px; white-space: nowrap; }}
  .sig-row.new .sig-txt {{ font-family: "SubBold", sans-serif; font-size: 20px; color: #FFFFFF; white-space: nowrap; }}

  /* K39 Staggered Dual Bubbles */
  .box-k39 {{ display: flex; flex-direction: column; gap: 10px; }}
  .bub-left {{ align-self: flex-start; background: rgba(255,255,255,0.05); border: 1px solid rgba(148,163,184,0.28); border-radius: 12px 12px 12px 3px; padding: 8px 12px; color: #94A3B8; display: flex; align-items: center; gap: 10px; white-space: nowrap; }}
  .bub-right {{ align-self: flex-end; background: rgba(250,204,21,0.13); border: 1.5px solid #FACC15; border-radius: 12px 12px 3px 12px; padding: 8px 12px; font-family: "SubBold", sans-serif; color: #FFFFFF; display: flex; align-items: center; gap: 10px; white-space: nowrap; }}
  .bub-lbl {{ font-size: 13px; color: #CBD5E1; background: rgba(255,255,255,0.08); padding: 2px 6px; border-radius: 4px; flex-shrink: 0; }}
  .bub-txt {{ font-size: 19.5px; white-space: nowrap; }}

  /* K40 Header Ribbon Card */
  .box-k40 {{ padding-top: 14px; }}
  .rib-head {{ background: rgba(250,204,21,0.16); border: 1px solid rgba(250,204,21,0.5); color: #FACC15; font-size: 14px; padding: 5px 12px; border-radius: 8px; margin-bottom: 10px; text-align: center; letter-spacing: 0.03em; white-space: nowrap; }}
  .rib-body {{ display: flex; flex-direction: column; gap: 6px; }}
  .rib-item {{ font-size: 19.5px; white-space: nowrap; }}
  .rib-item.old {{ color: #94A3B8; }}
  .rib-item.new {{ font-family: "SubBold", sans-serif; color: #FFFFFF; font-size: 20px; }}

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
    {spec["subbox_html"]}
    <div class="meta"><span class="dot"></span><span>Offline Hà Nội · 07–08/11</span></div>
  </div>
</body></html>"""


def render_and_audit():
    bg_img = Image.open(BG_PATH).convert("RGBA")
    rendered_by_sid: Dict[str, Any] = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350})

        for spec in NEW_K31_K40_SPECS:
            sid = spec["sid"]
            hfile = PILOT_DIR / f"{sid}.html"
            hfile.write_text(build_html(spec), encoding="utf-8")

            page.goto(f"file://{hfile}", wait_until="networkidle")
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(50)

            calc = page.evaluate("""() => {
              const h = document.querySelector('.headline');
              const lines = Array.from(document.querySelectorAll('.headline .line'));
              const c = document.createElement('canvas');
              c.width = 700; c.height = 260;
              const ctx = c.getContext('2d');
              const base = 170;

              function measureGlyphRatio(fontSpec, ch, fs) {
                ctx.clearRect(0, 0, 700, 260);
                ctx.font = fontSpec;
                ctx.fillStyle = '#fff';
                ctx.textBaseline = 'alphabetic';
                ctx.fillText(ch, 20, base);
                const d = ctx.getImageData(0, 0, 700, 260).data;
                let minY = 260, maxY = 0;
                for (let y = 0; y < 260; y++) {
                  for (let x = 0; x < 700; x++) {
                    if (d[(y * 700 + x) * 4 + 3] > 25) {
                      if (y < minY) minY = y;
                      if (y > maxY) maxY = y;
                    }
                  }
                }
                return (maxY - minY) / fs;
              }

              const fam = getComputedStyle(h).fontFamily;
              const wt = getComputedStyle(h).fontWeight;
              const xH = +measureGlyphRatio(wt + ' 90px ' + fam, 'x', 90).toFixed(3);
              const capH = +measureGlyphRatio(wt + ' 90px ' + fam, 'H', 90).toFixed(3);

              let lsEm = +Math.max(-0.020, Math.min(-0.006, -0.012 - 0.08 * (xH - 0.47))).toFixed(4);
              h.style.letterSpacing = lsEm + 'em';

              let fs = 95;
              h.style.fontSize = fs + 'px';
              while (fs > 76) {
                const maxW = Math.max(...lines.map(el => el.getBoundingClientRect().width));
                if (maxW <= 546) break;
                fs -= 1;
                h.style.fontSize = fs + 'px';
              }

              const fontSpec = wt + ' ' + fs + 'px ' + fam;
              function getInkProfile(str) {
                ctx.clearRect(0, 0, 700, 260);
                ctx.font = fontSpec;
                if ('letterSpacing' in ctx) ctx.letterSpacing = lsEm + 'em';
                ctx.fillStyle = '#fff';
                ctx.textBaseline = 'alphabetic';
                ctx.fillText(str, 10, base);
                const d = ctx.getImageData(0, 0, 700, 260).data;
                const topCol = new Array(700).fill(999);
                const botCol = new Array(700).fill(-999);
                for (let x = 0; x < 700; x++) {
                  for (let y = 0; y < 260; y++) {
                    if (d[(y * 700 + x) * 4 + 3] > 25) {
                      const relY = y - base;
                      if (relY < topCol[x]) topCol[x] = relY;
                      if (relY > botCol[x]) botCol[x] = relY;
                    }
                  }
                }
                return {topCol, botCol};
              }

              const p1 = getInkProfile('Đừng ép mình');
              const p2 = getInkProfile('đăng bài vội vã');
              const p3 = getInkProfile('mỗi ngày.');

              const gMin = Math.max(8, Math.round(0.095 * fs));
              function minDist2D(pUpper, pLower) {
                let reqD = 0;
                const r = 5;
                for (let x = 0; x < 700; x++) {
                  if (pUpper.botCol[x] === -999) continue;
                  for (let dx = -r; dx <= r; dx++) {
                    const x2 = x + dx;
                    if (x2 >= 0 && x2 < 700 && pLower.topCol[x2] !== 999) {
                      const needed = pUpper.botCol[x] - pLower.topCol[x2] + gMin;
                      if (needed > reqD) reqD = needed;
                    }
                  }
                }
                return reqD;
              }

              const d12_2d = minDist2D(p1, p2);
              const d23_2d = minDist2D(p2, p3);
              const L_2D = +((Math.max(d12_2d, d23_2d)) / fs).toFixed(2);
              const L_rhythm = +Math.max(1.01, Math.min(1.15, 2.22 * xH)).toFixed(2);
              const L_max_tight = +(2.34 * xH).toFixed(2);
              const L_target = +Math.min(L_max_tight, Math.max(L_rhythm, L_2D)).toFixed(2);
              const W_ratio = +((L_target - xH) / xH).toFixed(2);

              h.style.lineHeight = String(L_target);
              lines.forEach(l => { l.style.lineHeight = String(L_target); });

              let hRect = h.getBoundingClientRect();
              let sEl = document.querySelector('.sub-box');
              let sRect = sEl.getBoundingClientRect();
              const zone = document.querySelector('.zone');
              if (hRect.bottom > 718) {
                const shiftUp = Math.ceil(hRect.bottom - 714);
                zone.style.top = (135 - shiftUp) + 'px';
                hRect = h.getBoundingClientRect();
                sRect = sEl.getBoundingClientRect();
              }
              if (sRect.top < 738) {
                const extraGap = Math.ceil(740 - sRect.top);
                h.style.marginBottom = (50 + extraGap) + 'px';
              }

              hRect = h.getBoundingClientRect();
              sRect = sEl.getBoundingClientRect();
              return {
                fs, xH, capH, lsEm, L_2D, L_rhythm, L_target, W_ratio,
                hTop: Math.round(hRect.top), hBottom: Math.round(hRect.bottom),
                sTop: Math.round(sRect.top), sBottom: Math.round(sRect.bottom)
              };
            }""")

            hfile.write_text(page.content(), encoding="utf-8")
            txt_png = PILOT_DIR / f"{sid}_text.png"
            page.screenshot(path=str(txt_png), omit_background=True)
            comp = Image.alpha_composite(bg_img, Image.open(txt_png).convert("RGBA")).convert("RGB")

            jpg_path = PILOT_DIR / f"{sid}.jpg"
            comp.save(jpg_path, quality=93)
            shutil.copy2(jpg_path, BRAIN_DIR / f"{sid}.jpg")

            y_h2 = min(calc["sTop"] - 12, calc["hBottom"] + 46)
            y_h1 = max(0, y_h2 - 440)
            crop_h = comp.crop((16, y_h1, 636, y_h2)).resize((620, 440), Image.Resampling.LANCZOS)
            crop_h_path = PILOT_DIR / f"crop_head_{sid}.jpg"
            crop_h.save(crop_h_path, quality=92)
            shutil.copy2(crop_h_path, BRAIN_DIR / f"crop_head_{sid}.jpg")

            y_s1 = max(0, calc["sTop"] - 26)
            crop_s = comp.crop((20, y_s1, 600, min(1350, y_s1 + 315))).resize((580, 315), Image.Resampling.LANCZOS)
            crop_s_path = PILOT_DIR / f"crop_sub_{sid}.jpg"
            crop_s.save(crop_s_path, quality=92)
            shutil.copy2(crop_s_path, BRAIN_DIR / f"crop_sub_{sid}.jpg")

            rendered_by_sid[sid] = {
                "calc": calc,
                "hfile": str(hfile),
                "jpg_path": str(jpg_path),
            }

        browser.close()

    for sid, info in rendered_by_sid.items():
        calc = info["calc"]
        hfile = Path(info["hfile"])
        jpg_path = Path(info["jpg_path"])
        audit_res = audit_v3_banner(hfile, jpg_path, expected_lines=3, person_side="right")
        g2 = audit_res["gates"]["G2_LAW09_per_font_optical_leading"]
        g16 = audit_res["gates"]["G16_LAW11_subbox_textnode_and_sibling_gap"]

        rendered_by_sid[sid] = {
            "calc": calc,
            "score": audit_res["score"],
            "all_pass": audit_res["all_13_pass"],
            "gap2D": g2["min_2d_ink_gap_px"],
            "rPad": g16["min_right_pad_px"],
            "sibGap": g16["min_sibling_gap_px"],
            "failed": [k for k, v in audit_res["gates"].items() if not v.get("pass")],
        }
        print(
            f"[{sid:35s}] fs={calc['fs']}px LH={calc['L_target']} gap2D={g2['min_2d_ink_gap_px']}px "
            f"rPad={g16['min_right_pad_px']}px sibGap={g16['min_sibling_gap_px']}px "
            f"hBot={calc['hBottom']} sTop={calc['sTop']} => {audit_res['score']} (PASS={audit_res['all_13_pass']})"
        )
        if not audit_res["all_13_pass"]:
            print("   FAILED:", rendered_by_sid[sid]["failed"])
            for fg in rendered_by_sid[sid]["failed"]:
                print("   ", fg, audit_res["gates"][fg])

    # Build 5x2 composite overview grid k31_k40_10subboxes_grid.jpg
    grid_k = Image.new("RGB", (580 * 2 + 36, 315 * 5 + 72), (7, 11, 20))
    for idx, kspec in enumerate(NEW_K31_K40_SPECS):
        col = idx % 2
        row = idx // 2
        im = Image.open(PILOT_DIR / f"crop_sub_{kspec['sid']}.jpg")
        grid_k.paste(im, (12 + col * (580 + 12), 12 + row * (315 + 12)))
    grid_k.save(PILOT_DIR / "k31_k40_10subboxes_grid.jpg", quality=92)
    shutil.copy2(PILOT_DIR / "k31_k40_10subboxes_grid.jpg", BRAIN_DIR / "k31_k40_10subboxes_grid.jpg")

    # Update bo-chon-chu-banner.html cleanly using the exact item-card k-card template
    badge_map = {
        "KA": "background:rgba(245,158,11,0.18);color:#FACC15;border:1px solid rgba(245,158,11,0.45);",
        "KB": "background:rgba(56,189,248,0.18);color:#38BDF8;border:1px solid rgba(56,189,248,0.45);",
        "KC": "background:rgba(34,197,94,0.18);color:#4ADE80;border:1px solid rgba(34,197,94,0.45);",
        "KD": "background:rgba(168,85,247,0.18);color:#C084FC;border:1px solid rgba(168,85,247,0.45);",
        "KE": "background:rgba(244,63,94,0.18);color:#FB7185;border:1px solid rgba(244,63,94,0.45);",
    }
    k_cards_html = []
    for kspec in NEW_K31_K40_SPECS:
        kid = kspec["kid"]
        sid = kspec["sid"]
        rinfo = rendered_by_sid[sid]
        grp = kspec["kgroup"]
        k_cards_html.append(f"""
        <article class="item-card k-card" data-kid="{kid}" data-kgroup="{grp}" data-kname="{kspec['name']}" data-crop="k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg?v=h30_k40" data-full="k4_31kb_banners/v2_pilots/{sid}.jpg?v=h30_k40" onclick="selectSubbox('{kid}')">
          <div class="card-head">
            <div class="card-top-row">
              <span class="code-pill k-pill">{kid} • {kspec['name'].upper()}</span>
              <span class="grp-badge" style="{badge_map[grp]}">{kspec['kgroup_label']}</span>
            </div>
            <div class="sample-quote">{kspec['sample_quote']}</div>
            <p class="card-desc">{kspec['desc']}</p>
          </div>
          <div class="img-box sub-img-box" onclick="event.stopPropagation(); selectSubbox('{kid}'); openBigPreviewModal();" title="Click vào ảnh để mở BẢNG XEM TO (Ảnh Ví Dụ 1080×1350)">
            <img class="preview-img" src="k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg?v=h30_k40" alt="{kid} {kspec['name']}" loading="lazy" />
            <span class="img-mode-tag sub-tag">🔍 CLICK ẢNH XEM BẢNG TO (LỚP 2)</span>
          </div>
          <div class="card-foot">
            <span>Tác giả khuôn: <code>{kspec['author']}</code> • rPad={rinfo['rPad']}px • Đạt 16/16 Cổng</span>
            <div style="display:flex;gap:6px;">
              <button type="button" class="btn-pick" style="background:rgba(56,189,248,0.16);color:#38BDF8;border-color:rgba(56,189,248,0.4);" onclick="event.stopPropagation(); selectSubbox('{kid}'); openBigPreviewModal();">🖼️ Xem Bảng To</button>
              <button type="button" class="btn-pick k-btn" onclick="event.stopPropagation(); selectSubbox('{kid}')">✓ Chọn {kid}</button>
            </div>
          </div>
        </article>""")

    html = HUB_HTML.read_text(encoding="utf-8")
    # Remove any previous K31..K40 articles
    html = re.sub(r'\s*<!-- K3[1-9]|K40:[\s\S]*?</article>', '', html)
    html = re.sub(r'\s*<article class="card subbox-card" id="card-K(?:3[1-9]|40)"[\s\S]*?</article>', '', html)
    html = re.sub(r'\s*<article class="item-card k-card" data-kid="K(?:3[1-9]|40)"[\s\S]*?</article>', '', html)

    k30_pos = html.find('data-kid="K30"')
    k30_end = html.find('</article>', k30_pos) + len('</article>')
    html = html[:k30_end] + "\n" + "\n".join(k_cards_html) + html[k30_end:]

    html = html.replace("29 Khuôn Chữ Bé (K01–K30)", "39 Khuôn Chữ Bé (K01–K40)")
    html = html.replace("29 Khuôn Khung Chữ Bé (K01–K30)", "39 Khuôn Khung Chữ Bé (K01–K40)")
    html = html.replace("KHUNG CHỮ BÉ (K01–K30)", "KHUNG CHỮ BÉ (K01–K40)")
    html = html.replace("KHUNG K01–K30", "KHUNG K01–K40")
    html = html.replace("29 KHUÔN CHIA THEO 5 HỌ LOGIC: K01–K10 &amp; K12–K30, BỎ #11", "39 KHUÔN CHIA THEO 5 HỌ LOGIC: K01–K10 &amp; K12–K40, BỎ #11")
    html = html.replace("Tất cả 29 Khuôn Khung Chữ Bé (K01–K30, Đã bỏ #11)", "Tất cả 39 Khuôn Khung Chữ Bé (K01–K40, Đã bỏ #11)")
    html = html.replace("3. ĐỔI NHANH 29 KHUÔN KHUNG CHỮ BÉ (K01 → K30, ĐÃ BỎ #11):", "3. ĐỔI NHANH 39 KHUÔN KHUNG CHỮ BÉ (K01 → K40, ĐÃ BỎ #11):")

    HUB_HTML.write_text(html, encoding="utf-8")
    print("Updated bo-chon-chu-banner.html cleanly with K31..K40!")


if __name__ == "__main__":
    render_and_audit()
