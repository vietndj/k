#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG KẾT XUẤT & KIỂM TOÁN 16/16 CỔNG UI/UX CHO:
- 10 Kiểu Chữ To Mới (H21 -> H30): Khai thác 10 họ Font Có Chân / Slab / Stencil / Flare trong kho 424 font FEDU (0% trùng H01..H20)
- 8 Kiểu Khuôn Chữ Nhỏ Mới (K23 -> K30): 8 cấu trúc UI/UX mới hoàn toàn (0% trùng K01..K22)
Tất cả đều chạy qua uiux_auditor.py (16/16 cổng G1..G16, bao gồm G16_LAW11 TreeWalker(SHOW_TEXT) + sibling_gap >= 8px).
"""
import json
import shutil
import sys
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

sys.path.insert(0, "/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
from uiux_auditor import audit_v3_banner

PILOT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots")
BG_PATH = PILOT_DIR / "kb_15_v22_bg.png"
FONT_DIR = "/Users/vietmac/Documents/CODE/fedu-font/fonts"
BRAIN_DIR = Path("/Users/vietmac/.gemini/antigravity/brain/d0674648-f186-46ae-a77c-066e17e36fb5")

# ==================== 8 NEW SUBLINE BOX ARCHETYPES (K23 -> K30) ====================
NEW_SUBBOX_SPECS: List[Dict[str, Any]] = [
    {
        "kid": "K23",
        "kgroup": "KB",
        "kgroup_label": "Họ 2 • Con Số & Thời Gian / Lịch",
        "sid": "kb_15_new_k23_bac_thang_3buoc",
        "name": "Bậc Thang 3 Bước Chuyển Hóa (01 → 02 → 03)",
        "author": "GEMINI × CLAUDE2",
        "sample_quote": "[01 · Bắt bệnh] → [02 · Giải mã] → [03 · Khách nhắn] | Tuần 01 bài vẫn kín lịch.",
        "desc": "Trình bày chuỗi chuyển hóa 3 bước ngang bằng thẻ pill đánh số 01 → 02 → 03 (bước 03 viền vàng sáng) kèm câu chốt dưới đáy.",
        "h_main_file": "GRCanonLNarrowBold.woff2",
        "h_focal_file": "GRCanonLNarrowBold.woff2",
        "h_focal_style": "normal",
        "sub_med_file": "FDSohne-Halbfett.woff2",
        "sub_bold_file": "FDSohne-Dreiviertelfett.woff2",
        "mono_file": "FDAeonikMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k23">
          <div class="step3-row">
            <span class="st-pill"><b class="mono">01</b> Bắt bệnh</span>
            <span class="st-arr mono">→</span>
            <span class="st-pill"><b class="mono">02</b> Giải mã</span>
            <span class="st-arr mono">→</span>
            <span class="st-pill active"><b class="mono">03</b> Khách nhắn</span>
          </div>
          <div class="step3-sub">Đúng <b class="mono gold">03</b> <b class="gold">nhịp</b> này: tuần đăng <b class="mono">01</b> bài vẫn đều khách.</div>
        </div>
        """,
    },
    {
        "kid": "K24",
        "kgroup": "KA",
        "kgroup_label": "Họ 1 • Đối Chiếu Sai × / Đúng ✓",
        "sid": "kb_15_new_k24_ma_tran_cong_suc",
        "name": "Ma Trận Tỷ Trọng Công Sức – Kết Quả (2×3 Grid)",
        "author": "CLAUDE2",
        "sample_quote": "[ĐĂNG VỘI] Công sức 100% · Khách 0%  |  [BÀI TRÚNG] Công sức 20% · Khách 90%",
        "desc": "Đặt 2 dòng đối chiếu trực diện trên lưới 3 cột thẳng tắp: so sánh tỷ lệ Công sức bỏ ra và tỷ lệ Khách nhắn thực tế.",
        "h_main_file": "GRFlaireBasicBold.woff2",
        "h_focal_file": "GRFlaireBasicBoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDMonumentGrotesk-Medium.woff2",
        "sub_bold_file": "FDMonumentGrotesk-Bold.woff2",
        "mono_file": "FDMonumentGroteskMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k24">
          <div class="roi-row old">
            <span class="badge-muted">ĐĂNG VỘI</span>
            <span class="roi-cell">Công sức: <b class="mono">100%</b></span>
            <span class="roi-cell">Khách nhắn: <b class="mono">00%</b></span>
          </div>
          <div class="div-line"></div>
          <div class="roi-row new">
            <span class="badge-gold">BÀI TRÚNG</span>
            <span class="roi-cell">Công sức: <b class="mono">20%</b></span>
            <span class="roi-cell gold">Khách nhắn: <b class="mono">90%</b></span>
          </div>
        </div>
        """,
    },
    {
        "kid": "K25",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k25_pheu_loc_2tang",
        "name": "Phễu Lọc Khách Thật 2 Tầng ([LỌC] ↓ [CHỐT])",
        "author": "GEMINI",
        "sample_quote": "[TẦNG 1 · LỌC] Loại 90% xem dạo  |  [TẦNG 2 · CHỐT] Giữ 10% khách thật tự nhắn",
        "desc": "Cấu trúc phễu lọc 2 tầng: Tầng 1 lọc bỏ người xem dạo, Tầng 2 thu hút đúng khách hàng sẵn sàng chi trả.",
        "h_main_file": "GRZirkonBold.woff2",
        "h_focal_file": "GRZirkonBoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDAeonikSoft-Medium.woff2",
        "sub_bold_file": "FDAeonikSoft-Bold.woff2",
        "mono_file": "FDAeonikMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k25">
          <div class="def-row old"><span class="badge-muted">TẦNG 1 · LỌC</span><span>Loại <b class="mono" style="margin-right:3px;">90%</b> khách xem dạo ngay từ tiêu đề</span></div>
          <div class="div-line"></div>
          <div class="def-row new"><span class="badge-gold">TẦNG 2 · CHỐT</span><span>Giữ <b class="mono gold" style="margin-right:3px;">10%</b> khách thật tự nhắn hỏi lịch</span></div>
        </div>
        """,
    },
    {
        "kid": "K26",
        "kgroup": "KD",
        "kgroup_label": "Họ 4 • Tin Nhắn & Hỏi–Đáp",
        "sid": "kb_15_new_k26_thong_bao_dat_lich",
        "name": "Thông Báo Đặt Lịch Thực Tế (Live Booking Proof)",
        "author": "CLAUDE2",
        "sample_quote": "● BÁO CÁO LỊCH HẸN [+03 HỌC VIÊN MỚI] — Từ 01 bài giải mã tối thứ Tư — 0đ chi phí Ads.",
        "desc": "Mô phỏng thẻ thông báo kết quả chuyển đổi thực tế với chấm xanh hoạt động và huy hiệu số lượng khách đăng ký mới.",
        "h_main_file": "FDTiemposFine-Bold.woff2",
        "h_focal_file": "FDTiemposFine-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDUntitledSans-Medium.woff2",
        "sub_bold_file": "FDUntitledSans-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k26">
          <div class="notif-top">
            <span class="notif-left"><span class="live-dot"></span><span class="mono">BÁO CÁO LỊCH HẸN</span></span>
            <span class="notif-pill mono">+03 HỌC VIÊN MỚI</span>
          </div>
          <div class="notif-body">Từ <b class="gold"><span class="mono">01</span> bài giải mã</b> tối thứ Tư — <b class="mono">0đ</b> chi phí Ads.</div>
        </div>
        """,
    },
    {
        "kid": "K27",
        "kgroup": "KE",
        "kgroup_label": "Họ 5 • Tuyên Ngôn & Đúc Kết",
        "sid": "kb_15_new_k27_cot_tru_la_ma",
        "name": "Hai Cột Trụ Số La Mã Biên Tập (I. / II.)",
        "author": "GEMINI",
        "sample_quote": "I. Đừng biến kênh thành nhật ký đăng vội  |  II. Hãy biến mỗi bài thành 1 lần khám bệnh",
        "desc": "Phong cách tạp chí kinh doanh quốc tế: chia 2 cột đối xứng đánh số La Mã I. / II. ngăn cách bởi đường kẻ dọc màu vàng.",
        "h_main_file": "FDLockSerifStencil-Bold.woff2",
        "h_focal_file": "FDLockSerifStencil-Bold.woff2",
        "h_focal_style": "normal",
        "sub_med_file": "FDLockSans-Medium.woff2",
        "sub_bold_file": "FDLockSans-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k27">
          <div class="roman-col">
            <div class="r-head mono">I · THÓI QUEN CŨ</div>
            <div class="r-txt muted">Biến kênh thành nhật ký đăng vội mỗi ngày.</div>
          </div>
          <div class="roman-sep"></div>
          <div class="roman-col">
            <div class="r-head mono gold">II · VỊ THẾ CHUYÊN GIA</div>
            <div class="r-txt bright">Mỗi bài đăng là <b class="mono gold">01</b> lần khám đúng bệnh.</div>
          </div>
        </div>
        """,
    },
    {
        "kid": "K28",
        "kgroup": "KB",
        "kgroup_label": "Họ 2 • Con Số & Thời Gian / Lịch",
        "sid": "kb_15_new_k28_tuoi_tho_bai_dang",
        "name": "Đối Chiếu Tuổi Thọ Bài Đăng (03 Giây vs 30 Ngày)",
        "author": "CLAUDE2",
        "sample_quote": "[10 CLIP VỘI: Trôi sau 03 giây]  ↔  [01 BÀI SÂU: Nuôi kênh 30 ngày]",
        "desc": "Đo lường trực tiếp vòng đời nội dung (Content Lifespan): 10 clip vội trôi tuột sau 3 giây đối lập với 1 bài sâu nuôi kênh 30 ngày.",
        "h_main_file": "FDDomaineDisplayNarrow-Bold.woff2",
        "h_focal_file": "FDDomaineDisplayNarrow-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDNational2-Medium.woff2",
        "sub_bold_file": "FDNational2-Bold.woff2",
        "mono_file": "FDMonumentGroteskMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k28">
          <div class="span-box old">
            <div class="sp-tag mono">10 CLIP QUAY VỘI</div>
            <div class="sp-val">Trôi tuột sau <b class="mono">03</b> <b>giây</b></div>
          </div>
          <div class="span-box new">
            <div class="sp-tag mono gold">01 BÀI GIẢI MÃ SÂU</div>
            <div class="sp-val bright">Nuôi kênh suốt <b class="mono gold">30</b> <b class="gold">ngày</b></div>
          </div>
        </div>
        """,
    },
    {
        "kid": "K29",
        "kgroup": "KC",
        "kgroup_label": "Họ 3 • Công Thức & Bảng Kiểm",
        "sid": "kb_15_new_k29_khoa_3_dieu_kien",
        "name": "Khóa Chốt 3 Điều Kiện Đủ ([✓ A] + [✓ B] + [✓ C])",
        "author": "GEMINI",
        "sample_quote": "[✓ Đúng bệnh] + [✓ Đúng cơ chế] + [✓ Bằng chứng] → Đăng 01 bài khách tự nhắn.",
        "desc": "Hàng trên đóng khóa 3 điều kiện đủ bằng thẻ tag có tích vàng, hàng dưới là kết luận hành động dứt khoát.",
        "h_main_file": "FDCharter-Bold.woff2",
        "h_focal_file": "FDCharter-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "mono_file": "FDPitch-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k29">
          <div class="cond3-row">
            <span class="c3-pill"><b class="gold">✓</b> Đúng bệnh</span>
            <span class="c3-plus mono">+</span>
            <span class="c3-pill"><b class="gold">✓</b> Đúng cơ chế</span>
            <span class="c3-plus mono">+</span>
            <span class="c3-pill"><b class="gold">✓</b> Bằng chứng</span>
          </div>
          <div class="cond3-bot">→ Đủ <b class="mono gold">03</b> <b class="gold">chốt</b> này: đăng <b class="mono">01</b> bài khách tự nhắn.</div>
        </div>
        """,
    },
    {
        "kid": "K30",
        "kgroup": "KE",
        "kgroup_label": "Họ 5 • Tuyên Ngôn & Đúc Kết",
        "sid": "kb_15_new_k30_dau_niem_phong",
        "name": "Con Dấu Niêm Phong Chuyên Gia (K4 Verdict Seal)",
        "author": "CLAUDE2",
        "sample_quote": "[ĐÚC KẾT K4] Khách chỉ trả tiền cho người gọi đúng bệnh. 01 bài trúng hơn 100 lời rao.",
        "desc": "Bên trái là con dấu chữ nhật đứng đóng khung viền vàng kép (ĐÚC KẾT K4), bên phải là 2 dòng phán quyết đanh thép.",
        "h_main_file": "FDOrbikular-Bold.woff2",
        "h_focal_file": "FDOrbikular-BoldItalic.woff2",
        "h_focal_style": "italic",
        "sub_med_file": "FDRMNeue-Regular.woff2",
        "sub_bold_file": "FDRMNeue-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k30">
          <div class="seal-stamp mono">
            <span class="s-top">ĐÚC KẾT</span>
            <span class="s-bot">K4</span>
          </div>
          <div class="seal-copy">
            <div class="sc-1">Khách chỉ trả tiền cho người gọi đúng bệnh.</div>
            <div class="sc-2"><b class="mono">01</b> bài trúng huyệt hơn <b class="mono">100</b> lời chào hàng.</div>
          </div>
        </div>
        """,
    },
]

# ==================== 10 NEW HEADLINE TYPEFACES (H21 -> H30, 0% OVERLAP WITH H01..H20) ====================
# Note: H21..H28 reuse the 8 renders above + H29 & H30 have their own dedicated renders!
NEW_HEADLINE_SPECS: List[Dict[str, Any]] = [
    {
        "hid": "H21",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k23_bac_thang_3buoc",
        "name": "Canon L Narrow Bold",
        "font_file": "GRCanonLNarrowBold.woff2",
        "focal_file": "GRCanonLNarrowBold.woff2",
        "focal_style": "normal",
        "foundry": "Grilli Type",
        "desc": "Kỷ lục chiều cao chữ thường thực tế: thân chữ Narrow siêu gọn cho phép đẩy cỡ chữ lên cực đại (94px) mà vẫn giữ lòng chữ rộng xH=0.515.",
    },
    {
        "hid": "H22",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k24_ma_tran_cong_suc",
        "name": "GT Flaire Basic Bold (Incised Flare)",
        "font_file": "GRFlaireBasicBold.woff2",
        "focal_file": "GRFlaireBasicBoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Chân chữ vát loe nhọn kiểu khắc bia đá Thụy Sĩ (Incised Flare Serif), lòng chữ mở cao xH=0.518, cực kỳ sắc nét trên nền tối.",
    },
    {
        "hid": "H23",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k25_pheu_loc_2tang",
        "name": "GT Zirkon Bold (Chiseled Serif)",
        "font_file": "GRZirkonBold.woff2",
        "focal_file": "GRZirkonBoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Chân chữ vát góc cạnh như đục khắc đá kết hợp nét ngang dày khỏe gần giống Slab Serif, chống lóa nền tối tuyệt đối.",
    },
    {
        "hid": "H24",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k26_thong_bao_dat_lich",
        "name": "Tiempos Fine Bold (Razor Contrast)",
        "font_file": "FDTiemposFine-Bold.woff2",
        "focal_file": "FDTiemposFine-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Klim Type Foundry",
        "desc": "Nhánh Fine cao cấp nhất của họ Tiempos với nét phụ mảnh sắc như dao cạo và lòng chữ cực đại (xH=0.539), chuẩn tạp chí thượng lưu.",
    },
    {
        "hid": "H25",
        "hgroup": "H1A",
        "hgroup_label": "Nhóm 1A • Lòng Rộng (xH ≥ 0.50)",
        "sid": "kb_15_new_k27_cot_tru_la_ma",
        "name": "Lock Serif Stencil Bold",
        "font_file": "FDLockSerifStencil-Bold.woff2",
        "focal_file": "FDLockSerifStencil-Bold.woff2",
        "focal_style": "normal",
        "foundry": "CoType Foundry",
        "desc": "Họ Font Có Chân duy nhất trong kho có khe cắt Stencil công nghiệp mạnh mẽ, tạo điểm nhấn thị giác độc bản cho chủ đề Hệ thống/Kỹ thuật.",
    },
    {
        "hid": "H26",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_k28_tuoi_tho_bai_dang",
        "name": "Domaine Display Narrow Bold",
        "font_file": "FDDomaineDisplayNarrow-Bold.woff2",
        "focal_file": "FDDomaineDisplayNarrow-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Klim Type Foundry",
        "desc": "Vũ khí trị các câu tiêu đề dài của Klim Type: thân chữ hẹp ngang tự nhiên giúp đẩy cỡ chữ lên 88px mà vẫn giữ trọn đường cong Baroque.",
    },
    {
        "hid": "H27",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_k29_khoa_3_dieu_kien",
        "name": "Charter Bold (Matthew Carter Wedge)",
        "font_file": "FDCharter-Bold.woff2",
        "focal_file": "FDCharter-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Matthew Carter",
        "desc": "Thiết kế chân chữ hình nêm bất hủ của Matthew Carter; cấu trúc chữ đầm chắc, khoảng hở dấu tiếng Việt tách bạch hoàn hảo.",
    },
    {
        "hid": "H28",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_k30_dau_niem_phong",
        "name": "Orbikular Bold (Geometric Luxury Serif)",
        "font_file": "FDOrbikular-Bold.woff2",
        "focal_file": "FDOrbikular-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "CoType Foundry",
        "desc": "Các chữ cái có bụng tròn (o, đ, ă, ô) được vẽ theo đường tròn hình học đối xứng lạ mắt, cực hợp chủ đề Sáng tạo, Thời trang, Nghệ thuật.",
    },
    {
        "hid": "H29",
        "hgroup": "H1B",
        "hgroup_label": "Nhóm 1B • Sắc Bén (xH 0.47–0.49)",
        "sid": "kb_15_new_h29_ultra_standard",
        "name": "GT Ultra Standard Bold (Flared Hybrid)",
        "font_file": "GRUltraStandard-Bold.woff2",
        "focal_file": "GRUltraStandard-BoldItalic.woff2",
        "focal_style": "italic",
        "foundry": "Grilli Type",
        "desc": "Thiết kế lai đột phá của Grilli Type: kết hợp khung xương Sans hiện đại với đầu nét vát loe (Flared Calligraphic) đầy uy lực.",
        "sub_med_file": "GRWalsheimPro-Medium.woff2",
        "sub_bold_file": "GRWalsheimPro-Bold.woff2",
        "mono_file": "FDAeonikMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k23">
          <div class="step3-row">
            <span class="st-pill"><b class="mono">01</b> Bắt bệnh</span>
            <span class="st-arr mono">→</span>
            <span class="st-pill"><b class="mono">02</b> Giải mã</span>
            <span class="st-arr mono">→</span>
            <span class="st-pill active"><b class="mono">03</b> Khách nhắn</span>
          </div>
          <div class="step3-sub">Đúng <b class="mono gold">03</b> <b class="gold">nhịp</b> này: tuần đăng <b class="mono">01</b> bài vẫn đều khách.</div>
        </div>
        """,
    },
    {
        "hid": "H30",
        "hgroup": "H1C",
        "hgroup_label": "Nhóm 1C • Thân Gọn Chữ To (89–96px)",
        "sid": "kb_15_new_h30_karbon_slab_stencil",
        "name": "Karbon Slab Stencil Bold (89px Slab)",
        "font_file": "FDKarbonSlabStencil-Bold.woff2",
        "focal_file": "FDKarbonSlabStencil-Bold.woff2",
        "focal_style": "normal",
        "foundry": "Klim Type Foundry",
        "desc": "Chân chữ Slab vuông khỏe kết hợp khe cắt Stencil hiện đại của Klim Type; thân chữ gọn giúp đẩy cỡ chữ lên 89px.",
        "sub_med_file": "FDRMNeue-Regular.woff2",
        "sub_bold_file": "FDRMNeue-Bold.woff2",
        "mono_file": "FDRMMono-Bold.woff2",
        "subbox_html": """
        <div class="sub-box box-k30">
          <div class="seal-stamp mono">
            <span class="s-top">ĐÚC KẾT</span>
            <span class="s-bot">K4</span>
          </div>
          <div class="seal-copy">
            <div class="sc-1">Khách chỉ trả tiền cho người gọi đúng bệnh.</div>
            <div class="sc-2"><b class="mono">01</b> bài trúng huyệt hơn <b class="mono">100</b> lời chào hàng.</div>
          </div>
        </div>
        """,
    },
]


def build_banner_html(spec: Dict[str, Any]) -> str:
    focal_style = spec["h_focal_style"]
    return f"""<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">
<style>
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
  .badge-muted {{ font-family: "MetaMono", monospace; font-size: 15.5px; color: #94A3B8; background: rgba(148,163,184,0.15); border: 1px solid rgba(148,163,184,0.3); padding: 3px 8px; border-radius: 6px; white-space: nowrap; flex-shrink: 0; }}
  .badge-gold {{ font-family: "MetaMono", monospace; font-size: 15.5px; color: #070B14; background: #FACC15; padding: 3px 8px; border-radius: 6px; font-weight: 800; white-space: nowrap; flex-shrink: 0; }}
  .live-dot {{ display: inline-block; width: 9px; height: 9px; border-radius: 50%; background: #22C55E; flex-shrink: 0; }}

  /* K23 Step 3 Pills */
  .step3-row {{ display: flex; align-items: center; justify-content: space-between; gap: 8px; margin-bottom: 12px; }}
  .st-pill {{ background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.15); padding: 6px 10px; border-radius: 8px; font-size: 19px; color: #CBD5E1; white-space: nowrap; }}
  .st-pill.active {{ background: rgba(250,204,21,0.18); border: 1.5px solid #FACC15; color: #FACC15; font-family: "SubBold", sans-serif; }}
  .st-arr {{ color: #64748B; font-size: 18px; flex-shrink: 0; }}
  .step3-sub {{ font-family: "SubBold", sans-serif; font-size: 21.5px; color: #FFFFFF; line-height: 1.34; white-space: normal; overflow-wrap: break-word; }}

  /* K24 ROI Matrix 2x3 */
  .roi-row {{ display: grid; grid-template-columns: 112px 1fr 1fr; align-items: center; gap: 12px; font-size: 20.5px; line-height: 1.32; }}
  .roi-row.old {{ color: #94A3B8; }}
  .roi-row.new {{ color: #FFFFFF; font-family: "SubBold", sans-serif; }}
  .roi-cell {{ white-space: nowrap; }}

  /* K25 Funnel 2 Stages */
  .def-row {{ display: flex; align-items: baseline; gap: 12px; font-size: 21.5px; line-height: 1.34; }}
  .def-row > span:last-child {{ min-width: 0; white-space: normal; overflow-wrap: break-word; text-wrap: pretty; }}
  .def-row.old {{ color: #94A3B8; font-size: 21px; }}
  .def-row.new {{ color: #FFFFFF; font-family: "SubBold", sans-serif; font-size: 22px; }}

  /* K26 Live Booking Notification */
  .notif-top {{ display: flex; align-items: center; justify-content: space-between; gap: 12px; margin-bottom: 10px; padding-bottom: 9px; border-bottom: 1px solid rgba(255,255,255,0.10); }}
  .notif-left {{ display: flex; align-items: center; gap: 9px; font-size: 16.5px; color: #94A3B8; white-space: nowrap; }}
  .notif-pill {{ background: rgba(250,204,21,0.18); border: 1px solid rgba(250,204,21,0.5); color: #FACC15; font-size: 15.5px; padding: 3px 9px; border-radius: 99px; white-space: nowrap; }}
  .notif-body {{ font-family: "SubBold", sans-serif; font-size: 22.5px; color: #FFFFFF; line-height: 1.34; white-space: normal; overflow-wrap: break-word; }}

  /* K27 Roman Pillars I / II */
  .box-k27 {{ display: grid; grid-template-columns: 1fr 1px 1fr; gap: 16px; align-items: stretch; }}
  .roman-sep {{ background: rgba(250,204,21,0.35); width: 1px; }}
  .roman-col {{ display: flex; flex-direction: column; gap: 6px; min-width: 0; }}
  .r-head {{ font-size: 15px; color: #94A3B8; letter-spacing: 0.03em; white-space: nowrap; }}
  .r-txt {{ font-size: 20px; line-height: 1.32; white-space: normal; overflow-wrap: break-word; }}
  .r-txt.muted {{ color: #94A3B8; }}
  .r-txt.bright {{ color: #FFFFFF; font-family: "SubBold", sans-serif; }}

  /* K28 Content Lifespan Split */
  .box-k28 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
  .span-box {{ padding: 11px 13px; border-radius: 11px; display: flex; flex-direction: column; gap: 5px; min-width: 0; }}
  .span-box.old {{ background: rgba(255,255,255,0.04); border: 1px solid rgba(148,163,184,0.2); }}
  .span-box.new {{ background: rgba(250,204,21,0.10); border: 1.5px solid rgba(250,204,21,0.45); }}
  .sp-tag {{ font-size: 14.5px; color: #94A3B8; white-space: nowrap; }}
  .sp-val {{ font-size: 19.5px; color: #CBD5E1; line-height: 1.30; white-space: normal; overflow-wrap: break-word; }}
  .sp-val.bright {{ color: #FFFFFF; font-family: "SubBold", sans-serif; }}

  /* K29 Triple Condition Lock */
  .cond3-row {{ display: flex; align-items: center; justify-content: space-between; gap: 7px; margin-bottom: 11px; }}
  .c3-pill {{ background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.16); padding: 5px 9px; border-radius: 7px; font-size: 18px; color: #E2E8F0; white-space: nowrap; }}
  .c3-plus {{ color: #FACC15; font-size: 18px; flex-shrink: 0; }}
  .cond3-bot {{ background: rgba(250,204,21,0.12); border-left: 3px solid #FACC15; padding: 7px 11px; border-radius: 6px; font-family: "SubBold", sans-serif; font-size: 21px; color: #FFFFFF; line-height: 1.32; white-space: normal; overflow-wrap: break-word; }}

  /* K30 Verdict Seal Stamp */
  .box-k30 {{ display: flex; align-items: center; gap: 16px; }}
  .seal-stamp {{ border: 2px solid #FACC15; background: rgba(250,204,21,0.12); border-radius: 10px; padding: 8px 11px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; line-height: 1.15; }}
  .seal-stamp .s-top {{ font-size: 13.5px; color: #FACC15; letter-spacing: 0.06em; white-space: nowrap; }}
  .seal-stamp .s-bot {{ font-size: 28px; color: #FACC15; font-weight: 800; white-space: nowrap; }}
  .seal-copy {{ display: flex; flex-direction: column; gap: 6px; min-width: 0; flex: 1; }}
  .sc-1 {{ font-size: 20.5px; color: #CBD5E1; line-height: 1.32; white-space: normal; overflow-wrap: break-word; }}
  .sc-2 {{ font-family: "SubBold", sans-serif; font-size: 21.5px; color: #FACC15; line-height: 1.32; white-space: normal; overflow-wrap: break-word; }}

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


def render_all():
    bg_img = Image.open(BG_PATH).convert("RGBA")

    # Build combined list of 10 unique render jobs (8 for K23..K30 which also cover H21..H28, plus 2 for H29 & H30)
    render_jobs: List[Dict[str, Any]] = []
    for kspec in NEW_SUBBOX_SPECS:
        render_jobs.append(kspec)
    for hspec in NEW_HEADLINE_SPECS[8:]:
        render_jobs.append({
            "kid": "K23" if hspec["hid"] == "H29" else "K30",
            "sid": hspec["sid"],
            "name": hspec["name"],
            "h_main_file": hspec["font_file"],
            "h_focal_file": hspec["focal_file"],
            "h_focal_style": hspec["focal_style"],
            "sub_med_file": hspec["sub_med_file"],
            "sub_bold_file": hspec["sub_bold_file"],
            "mono_file": hspec["mono_file"],
            "subbox_html": hspec["subbox_html"],
        })

    rendered_by_sid: Dict[str, Dict[str, Any]] = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for job in render_jobs:
            sid = job["sid"]
            hfile = PILOT_DIR / f"{sid}.html"
            hfile.write_text(build_banner_html(job), encoding="utf-8")
            page.goto(f"file://{hfile.resolve()}", wait_until="networkidle")
            page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(60)

            calc = page.evaluate("""() => {
              const h = document.querySelector('.headline');
              const lines = Array.from(document.querySelectorAll('.headline .line'));
              const hl = document.querySelector('.headline .hl');
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

              let hlXH = xH;
              if (hl) {
                const hlSt = getComputedStyle(hl);
                const hlSpec = (hlSt.fontStyle || 'normal') + ' ' + (hlSt.fontWeight || '700') + ' 90px ' + hlSt.fontFamily;
                hlXH = +measureGlyphRatio(hlSpec, 'x', 90).toFixed(3);
              }

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

              // Auto-fit sub-box inner elements using TreeWalker(SHOW_TEXT) + scrollWidth check (LAW_11)
              const sBox = document.querySelector('.sub-box');
              if (sBox) {
                sBox.style.width = '546px';
                sBox.style.maxWidth = '546px';
                const sRight = sBox.getBoundingClientRect().right - 22;
                for (let step = 0; step < 20; step++) {
                  let anyIssue = false;
                  const walker = document.createTreeWalker(sBox, NodeFilter.SHOW_TEXT, null);
                  let tNode;
                  while ((tNode = walker.nextNode())) {
                    if (!tNode.nodeValue || !tNode.nodeValue.trim()) continue;
                    const range = document.createRange();
                    range.selectNodeContents(tNode);
                    const rects = Array.from(range.getClientRects());
                    const parentRow = tNode.parentElement.closest('.step3-row, .step3-sub, .roi-row, .def-row, .notif-top, .notif-body, .cond3-row, .cond3-bot, .sc-1, .sc-2, .sp-val') || tNode.parentElement;
                    const overRight = rects.some(r => r.width > 0 && r.right > sRight);
                    const isMultiAllowed = tNode.parentElement.closest('.r-txt');
                    const wrappedInSingleRow = rects.length > 1 && parentRow && !isMultiAllowed;
                    if (overRight || wrappedInSingleRow) {
                      const curFs = parseFloat(getComputedStyle(parentRow).fontSize);
                      if (curFs > 18.5) {
                        anyIssue = true;
                        parentRow.style.fontSize = (curFs - 0.5).toFixed(1) + 'px';
                        if (tNode.parentElement !== parentRow) {
                          tNode.parentElement.style.fontSize = (curFs - 0.5).toFixed(1) + 'px';
                        }
                      }
                    }
                  }
                  const allSub = Array.from(sBox.querySelectorAll('*'));
                  for (const el of allSub) {
                    if (el.clientWidth > 0 && el.scrollWidth > el.clientWidth + 1) {
                      const curFs = parseFloat(getComputedStyle(el).fontSize);
                      if (curFs > 18.5) {
                        anyIssue = true;
                        el.style.fontSize = (curFs - 0.5).toFixed(1) + 'px';
                      }
                    }
                  }
                  if (!anyIssue) break;
                }
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

              // Calibrate vertical split boundary so hBottom <= 720 and sTop >= 734 (for 53.8% = 726.3px modal split)
              let hRect = h.getBoundingClientRect();
              let sEl = document.querySelector('.sub-box');
              let sRect = sEl.getBoundingClientRect();
              const zone = document.querySelector('.zone');
              if (hRect.bottom > 721) {
                const shiftUp = Math.ceil(hRect.bottom - 716);
                zone.style.top = (135 - shiftUp) + 'px';
                hRect = h.getBoundingClientRect();
                sRect = sEl.getBoundingClientRect();
              }
              if (sRect.top < 735) {
                const extraGap = Math.ceil(736 - sRect.top);
                h.style.marginBottom = (50 + extraGap) + 'px';
              }

              hRect = h.getBoundingClientRect();
              sRect = sEl.getBoundingClientRect();
              const mEl = document.querySelector('.meta');
              const mRect = mEl.getBoundingClientRect();

              return {
                fs, xH, hlXH, capH, lsEm, L_2D, L_rhythm, L_target, W_ratio,
                hTop: Math.round(hRect.top), hBottom: Math.round(hRect.bottom),
                sTop: Math.round(sRect.top), sBottom: Math.round(sRect.bottom),
                mBottom: Math.round(mRect.bottom)
              };
            }""")

            hfile.write_text(page.content(), encoding="utf-8")
            txt_png = PILOT_DIR / f"{sid}_text.png"
            page.screenshot(path=str(txt_png), omit_background=True)
            comp = Image.alpha_composite(bg_img, Image.open(txt_png).convert("RGBA")).convert("RGB")

            jpg_path = PILOT_DIR / f"{sid}.jpg"
            comp.save(jpg_path, quality=93)

            # 1. Crop Headline only (620x440) — strictly above sTop so sub-box never bleeds into headline crop
            y_h2 = min(calc["sTop"] - 12, calc["hBottom"] + 46)
            y_h1 = max(0, y_h2 - 440)
            crop_h = comp.crop((16, y_h1, 636, y_h2)).resize((620, 440), Image.Resampling.LANCZOS)
            crop_h_path = PILOT_DIR / f"crop_head_{sid}.jpg"
            crop_h.save(crop_h_path, quality=92)
            shutil.copy2(crop_h_path, BRAIN_DIR / f"crop_head_{sid}.jpg")

            # 2. Crop Subline + Meta (580x315)
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
            "min_2d_gap_px": g2["min_2d_ink_gap_px"],
            "rPad": g16["min_right_pad_px"],
            "lPad": g16["min_left_pad_px"],
            "sibGap": g16["min_sibling_gap_px"],
            "failed_gates": [k for k, v in audit_res["gates"].items() if not v.get("pass")],
        }
        print(
            f"[{sid:35s}] fs={calc['fs']}px LH={calc['L_target']} W={calc['W_ratio']}x "
            f"gap2D={g2['min_2d_ink_gap_px']}px rPad={g16['min_right_pad_px']}px sibGap={g16['min_sibling_gap_px']}px "
            f"hBot={calc['hBottom']} sTop={calc['sTop']} => {audit_res['score']} (PASS={audit_res['all_13_pass']})"
        )
        if not audit_res["all_13_pass"]:
            print("   FAILED GATES:", rendered_by_sid[sid]["failed_gates"])
            for fg in rendered_by_sid[sid]["failed_gates"]:
                print("   ", fg, audit_res["gates"][fg])

    # Build 2 composite overview grids:
    # 1) k23_k30_8subboxes_grid.jpg (4x2 grid of the 8 new subboxes)
    grid_k = Image.new("RGB", (580 * 2 + 36, 315 * 4 + 60), (7, 11, 20))
    for idx, kspec in enumerate(NEW_SUBBOX_SPECS):
        col = idx % 2
        row = idx // 2
        im = Image.open(PILOT_DIR / f"crop_sub_{kspec['sid']}.jpg")
        grid_k.paste(im, (12 + col * (580 + 12), 12 + row * (315 + 12)))
    grid_k.save(PILOT_DIR / "k23_k30_8subboxes_grid.jpg", quality=92)
    shutil.copy2(PILOT_DIR / "k23_k30_8subboxes_grid.jpg", BRAIN_DIR / "k23_k30_8subboxes_grid.jpg")

    # 2) h21_h30_10headlines_grid.jpg (2x5 grid of the 10 new headlines)
    grid_h = Image.new("RGB", (620 * 2 + 36, 440 * 5 + 72), (7, 11, 20))
    for idx, hspec in enumerate(NEW_HEADLINE_SPECS):
        col = idx % 2
        row = idx // 2
        im = Image.open(PILOT_DIR / f"crop_head_{hspec['sid']}.jpg")
        grid_h.paste(im, (12 + col * (620 + 12), 12 + row * (440 + 12)))
    grid_h.save(PILOT_DIR / "h21_h30_10headlines_grid.jpg", quality=92)
    shutil.copy2(PILOT_DIR / "h21_h30_10headlines_grid.jpg", BRAIN_DIR / "h21_h30_10headlines_grid.jpg")

    out_data = {
        "rendered_by_sid": rendered_by_sid,
        "new_subboxes": NEW_SUBBOX_SPECS,
        "new_headlines": NEW_HEADLINE_SPECS,
    }
    Path("/tmp/new_h21_h30_k23_k30_report.json").write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    render_all()
