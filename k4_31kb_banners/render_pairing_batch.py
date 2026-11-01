#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HỆ THỐNG KẾT XUẤT & KIỂM ĐỊNH 12 TỔ HỢP PHỐI CHỮ GIẢI PHẪU THƯỢNG TẦNG (P01 -> P12)
Theo 6 Quy Luật Kết Hợp Typography Thế Giới (LAW_10_TYPOGRAPHIC_PAIRING_MATRIX — CLAUDE2 Opus 5.5):
- L1: Đồng Khung Xương Đa Nhánh (Superfamily Shared-Skeleton Synthesis) -> P01, P02
- L2: Đối Trọng Ductus Bút Cọ / Dao Khắc × Grotesque Thụy Sĩ (Calligraphic/Chiseled vs Swiss Grotesque) -> P03, P04
- L3: Cực Tính Tương Phản Nét (Extreme Contrast Didone/Flare × Monolinear Technical Mono) -> P05, P06
- L4: Chuyển Giọng Nội Bộ Tiêu Đề Có Bù Trừ Quang Học (Intra-Headline Dual-Voice Synthesis) -> P07, P08
- L5: Đối Cực Kiến Trúc Chiều Rộng & Bẫy Mực (Architectural Width Polarity & Inktrap Tension) -> P09, P10
- L6: Giao Thoa Di Sản Cổ Điển & Chuẩn Mực Hiện Đại (Classical/Heritage Authority × Contemporary Sans) -> P11, P12

Hỗ trợ chạy theo từng Lô độc lập (--batch A|B|C|ALL) để 3 Subagent batch-builder thực thi song song.
Mỗi mẫu tự động đo xH, capH, 2D Ink Profile (LAW_09 + LAW_10), xuất:
1. Ảnh nguyên tấm 1080x1350: {sid}.jpg
2. Ảnh cắt cận cảnh Phối Chữ 3 Tầng (Headline + Subline + Meta, 620x740px): crop_pair_{sid}.jpg
3. Ảnh cắt cận cảnh Tiêu đề (620x440px): crop_head_{sid}.jpg
4. Ảnh cắt cận cảnh Hộp chữ bé (580x315px): crop_sub_{sid}.jpg
Và chấm qua 15/15 Cổng uiux_auditor.py (G1..G15).
"""
import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, List
from PIL import Image
from playwright.sync_api import sync_playwright

sys.path.insert(0, "/Users/vietmac/Documents/CODE/k/k4_31kb_banners")
from uiux_auditor import audit_v3_banner

PILOT_DIR = Path("/Users/vietmac/Documents/CODE/k/k4_31kb_banners/v2_pilots")
BG_PATH = PILOT_DIR / "kb_15_v22_bg.png"
FONT_DIR = "/Users/vietmac/Documents/CODE/fedu-font/fonts"

PAIRING_SPECS: List[Dict[str, Any]] = [
    # ==================== BATCH A: L1 (P01, P02) & L2 (P03, P04) ====================
    {
        "pid": "P01",
        "batch": "A",
        "law_code": "L1",
        "law_name": "Luật L1 • Đồng Khung Xương Đa Nhánh (Superfamily Skeleton)",
        "sid": "p01_l1_domaine_superfamily",
        "title": "Klim Domaine Superfamily (Baroque Serif × Flared Sans)",
        "foundry": "Klim Type Foundry + Dinamo",
        "h_main_file": "FDDomaineDisplay-Bold.woff2",
        "h_main_name": "Domaine Display Bold",
        "h_focal_file": "FDDomaineDisplay-BoldItalic.woff2",
        "h_focal_name": "Domaine Display Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDDomaineSansDisplay-Medium.woff2",
        "sub_bold_file": "FDDomaineSansDisplay-Bold.woff2",
        "sub_name": "Domaine Sans Display",
        "mono_file": "FDMonumentGroteskMono-Bold.woff2",
        "mono_name": "Monument Grotesk Mono Bold",
        "k_code": "K01",
        "k_name": "Hai Vế Đối Lập (× / ✓)",
        "anatomy_axes": "Giữ nguyên: Skeleton Klim, xH=0.500, Aperture | Đối lập: Baroque Bracketed Serif ↔ High-Contrast Sans",
        "use_case": "Bất động sản cao cấp, Đầu tư, Thương hiệu Chủ doanh nghiệp",
        "subbox_html": """
        <div class="sub-box box-k01">
          <div class="row-old"><span class="ic-bad">×</span><span class="num-tag">10 CLIP</span><span>quay vội: khách xem rồi lướt</span></div>
          <div class="div-line"></div>
          <div class="row-new"><span class="ic-good">✓</span><span class="num-tag gold">01 BÀI</span><span>trúng việc: khách tự nhắn</span></div>
        </div>
        """,
    },
    {
        "pid": "P02",
        "batch": "A",
        "law_code": "L1",
        "law_name": "Luật L1 • Đồng Khung Xương Đa Nhánh (Superfamily Skeleton)",
        "sid": "p02_l1_lock_stencil_superfamily",
        "title": "CoType Lock Superfamily (Editorial Serif + Stencil × Lock Sans)",
        "foundry": "CoType Foundry (London)",
        "h_main_file": "FDLockSerif-Bold.woff2",
        "h_main_name": "Lock Serif Bold",
        "h_focal_file": "FDLockSerifStencil-Bold.woff2",
        "h_focal_name": "Lock Serif Stencil Bold",
        "h_focal_style": "normal",
        "sub_med_file": "FDLockSans-Medium.woff2",
        "sub_bold_file": "FDLockSans-Bold.woff2",
        "sub_name": "Lock Sans Medium/Bold",
        "mono_file": "FDRMMono-Bold.woff2",
        "mono_name": "RM Mono Bold",
        "k_code": "K18",
        "k_name": "Phương Trình Đóng Khung ([A] + [B] = C)",
        "anatomy_axes": "Giữ nguyên: Khung xương Lock (xH=0.522) | Đối lập: Nét liền Solid ↔ Nét cắt khe Stencil công nghiệp",
        "use_case": "Hệ thống AI, Tự động hóa, Quy trình kỹ thuật, Khóa học thực chiến",
        "subbox_html": """
        <div class="sub-box box-k18">
          <div class="eq-row">
            <span class="eq-pill"><b class="mono">01</b> Bài kỹ/tuần</span>
            <span class="eq-op">+</span>
            <span class="eq-pill">Đúng nỗi đau</span>
            <span class="eq-op">=</span>
            <span class="eq-res">Khách tự nhắn</span>
          </div>
          <div class="eq-sub">Vận hành tự nhiên, không cần gồng đăng mỗi ngày.</div>
        </div>
        """,
    },
    {
        "pid": "P03",
        "batch": "A",
        "law_code": "L2",
        "law_name": "Luật L2 • Đối Trọng Ductus Dao Khắc × Grotesque Thụy Sĩ",
        "sid": "p03_l2_sectra_founders",
        "title": "Grilli Sectra Scalpel × Klim Founders Grotesk & Pitch Mono",
        "foundry": "Grilli Type × Klim Type Foundry",
        "h_main_file": "GRSectraDisplay-Bold.woff2",
        "h_main_name": "GT Sectra Display Bold",
        "h_focal_file": "GRSectraDisplay-BoldItalic.woff2",
        "h_focal_name": "GT Sectra Display Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDFoundersGrotesk-Medium.woff2",
        "sub_bold_file": "FDFoundersGrotesk-Bold.woff2",
        "sub_name": "Founders Grotesk",
        "mono_file": "FDPitch-Bold.woff2",
        "mono_name": "Pitch Typewriter Mono Bold",
        "k_code": "K06",
        "k_name": "Định Nghĩa Âm Bản (KHÔNG PHẢI A – MÀ LÀ B)",
        "anatomy_axes": "Giữ nguyên: xH (~0.48) & Mật độ mực | Đối lập: Góc dao khắc nghiêng Calligraphic ↔ Grotesque trục đứng",
        "use_case": "Giải mã cơ chế, Tư vấn chiến lược, Pháp lý, Phản biện chuyên gia",
        "subbox_html": """
        <div class="sub-box box-k06">
          <div class="def-row old"><span class="badge-muted">KHÔNG PHẢI</span><span>quay <b class="mono">10</b> clip ồn ào mỗi tuần</span></div>
          <div class="div-line"></div>
          <div class="def-row new"><span class="badge-gold">MÀ LÀ</span><span><b class="mono">01</b> bài gãi đúng chỗ ngứa của khách</span></div>
        </div>
        """,
    },
    {
        "pid": "P04",
        "batch": "A",
        "law_code": "L2",
        "law_name": "Luật L2 • Đối Trọng Ductus Bút Cọ × Grotesque Thụy Sĩ",
        "sid": "p04_l2_plantijn_sohne",
        "title": "Klim Martina Plantijn × Söhne (Akzidenz Heir) & Aeonik Mono",
        "foundry": "Klim Type Foundry × CoType",
        "h_main_file": "FDMartinaPlantijn-Bold.woff2",
        "h_main_name": "Martina Plantijn Bold",
        "h_focal_file": "FDMartinaPlantijn-BoldItalic.woff2",
        "h_focal_name": "Martina Plantijn Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDSohne-Halbfett.woff2",
        "sub_bold_file": "FDSohne-Dreiviertelfett.woff2",
        "sub_name": "Söhne (Halbfett / Dreiviertelfett)",
        "mono_file": "FDAeonikMono-Bold.woff2",
        "mono_name": "Aeonik Mono Bold",
        "k_code": "K20",
        "k_name": "Thẻ Chẩn Đoán ([BỆNH] → [THUỐC])",
        "anatomy_axes": "Giữ nguyên: Lòng chữ mở thoáng (xH=0.49) | Đối lập: Serif Phục hưng Hà Lan ấm áp ↔ Söhne kỷ luật Thụy Sĩ",
        "use_case": "Y khoa, Nha khoa, Giáo dục chuyên sâu, Đào tạo nghề chuẩn mực",
        "subbox_html": """
        <div class="sub-box box-k20">
          <div class="def-row old"><span class="badge-muted">BỆNH KÊNH</span><span>Đăng đều <b class="mono">07/07</b> ngày nhưng vắng khách</span></div>
          <div class="div-line"></div>
          <div class="def-row new"><span class="badge-gold">PHÁC ĐỒ</span><span><b class="mono">01</b> bài trúng bệnh → khách tự nhắn</span></div>
        </div>
        """,
    },

    # ==================== BATCH B: L3 (P05, P06) & L4 (P07, P08) ====================
    {
        "pid": "P05",
        "batch": "B",
        "law_code": "L3",
        "law_name": "Luật L3 • Cực Tính Tương Phản Nét (High-Contrast × Mono/Clean Sans)",
        "sid": "p05_l3_epicene_national2",
        "title": "Klim Epicene Baroque Opulence × National 2 & Pitch Mono",
        "foundry": "Klim Type Foundry",
        "h_main_file": "FDEpiceneDisplay-Bold.woff2",
        "h_main_name": "Epicene Display Bold",
        "h_focal_file": "FDEpiceneDisplay-BoldItalic.woff2",
        "h_focal_name": "Epicene Display Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDNational2-Medium.woff2",
        "sub_bold_file": "FDNational2-Bold.woff2",
        "sub_name": "National 2 Medium/Bold",
        "mono_file": "FDPitch-Bold.woff2",
        "mono_name": "Pitch Mono Bold",
        "k_code": "K09",
        "k_name": "Bong Bóng Tin Nhắn Khách Hàng",
        "anatomy_axes": "Giữ nguyên: Độ đầm khối chính | Đối lập cực đại: Nét thanh-đậm giọt lệ Baroque (≥5:1) ↔ Nét đơn đều cơ khí (1:1)",
        "use_case": "Spa, Thẩm mỹ viện, Thời trang, Mỹ phẩm, Làm đẹp cao cấp",
        "subbox_html": """
        <div class="sub-box box-k09">
          <div class="chat-head"><span class="live-dot"></span><span class="mono">TIN NHẮN KHÁCH HÀNG • 21:15</span></div>
          <div class="chat-msg">“Xem đúng <b class="gold">01 bài phân tích</b> của anh là em nhắn đặt lịch luôn.”</div>
        </div>
        """,
    },
    {
        "pid": "P06",
        "batch": "B",
        "law_code": "L3",
        "law_name": "Luật L3 • Cực Tính Tương Phản Nét (Sculptural Flare × Industrial Mono)",
        "sid": "p06_l3_orlando_monument",
        "title": "Commercial Type Orlando Flare × Dinamo Monument Grotesk",
        "foundry": "Commercial Type × Dinamo",
        "h_main_file": "FDOrlando-Bold.woff2",
        "h_main_name": "Orlando Bold (Flare Sculpture)",
        "h_focal_file": "FDOrlando-BoldItalic.woff2",
        "h_focal_name": "Orlando Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDMonumentGrotesk-Medium.woff2",
        "sub_bold_file": "FDMonumentGrotesk-Bold.woff2",
        "sub_name": "Monument Grotesk",
        "mono_file": "FDMonumentGroteskMono-Bold.woff2",
        "mono_name": "Monument Grotesk Mono Bold",
        "k_code": "K03",
        "k_name": "Con Số Bằng Chứng Lớn (1/10)",
        "anatomy_axes": "Giữ nguyên: xH cực đại (0.544) | Đối lập: Chân chữ loe điêu khắc La Mã ↔ Grotesque công nghiệp thô ráp",
        "use_case": "Kiến trúc, Nội thất, Nghệ thuật điêu khắc, Sự kiện, F&B Thượng lưu",
        "subbox_html": """
        <div class="sub-box box-k03">
          <div class="big-metric mono">1/10</div>
          <div class="metric-copy">
            <div class="mc-top">Làm <b>1 bài kỹ</b> giá trị bằng 10 clip vội.</div>
            <div class="mc-bot">Khách đọc xong tự nhắn hỏi lịch học.</div>
          </div>
        </div>
        """,
    },
    {
        "pid": "P07",
        "batch": "B",
        "law_code": "L4",
        "law_name": "Luật L4 • Chuyển Giọng Nội Bộ Tiêu Đề (Intra-Headline Dual-Voice)",
        "sid": "p07_l4_tiempos_untitled",
        "title": "Klim Tiempos Roman+Italic × Untitled Sans (Super-Normal)",
        "foundry": "Klim Type Foundry × CoType",
        "h_main_file": "FDTiemposHeadline-Bold.woff2",
        "h_main_name": "Tiempos Headline Bold",
        "h_focal_file": "FDTiemposHeadline-BoldItalic.woff2",
        "h_focal_name": "Tiempos Headline Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDUntitledSans-Medium.woff2",
        "sub_bold_file": "FDUntitledSans-Bold.woff2",
        "sub_name": "Untitled Sans Medium/Bold",
        "mono_file": "FDRMMono-SemiBold.woff2",
        "mono_name": "RM Mono SemiBold",
        "k_code": "K14",
        "k_name": "Thay Thói Quen Cũ ([CŨ] → Mới)",
        "anatomy_axes": "Giữ nguyên: Baseline & xH=0.544 trùng khít 100% | Đối lập: Trục đứng đĩnh đạc ↔ Trục nghiêng 12° nhấn cảm xúc",
        "use_case": "Kể chuyện nghề (Storytelling), Xây kênh chuyên gia, Podcast, Bản tin",
        "subbox_html": """
        <div class="sub-box box-k14">
          <div class="def-row old"><span class="badge-muted">CŨ</span><span>Ngày nào cũng phải gồng quay đủ <b class="mono">07</b> clip</span></div>
          <div class="div-line"></div>
          <div class="def-row new"><span class="badge-gold">MỚI</span><span>Đăng ít mà trúng việc → khách nhớ & nhắn</span></div>
        </div>
        """,
    },
    {
        "pid": "P08",
        "batch": "B",
        "law_code": "L4",
        "law_name": "Luật L4 • Chuyển Giọng Nội Bộ Tiêu Đề (Cross-Genre Sans + Serif Italic)",
        "sid": "p08_l4_monument_domaine_mix",
        "title": "Pentagram Cross-Genre: Monument Grotesk × Domaine Bold Italic",
        "foundry": "Dinamo × Klim Type Foundry",
        "h_main_file": "FDMonumentGrotesk-Bold.woff2",
        "h_main_name": "Monument Grotesk Bold (Sans Frame)",
        "h_focal_file": "FDDomaineDisplay-BoldItalic.woff2",
        "h_focal_name": "Domaine Display Bold Italic (Serif Focal)",
        "h_focal_style": "italic",
        "sub_med_file": "FDMonumentGrotesk-Medium.woff2",
        "sub_bold_file": "FDMonumentGrotesk-Bold.woff2",
        "sub_name": "Monument Grotesk",
        "mono_file": "FDMonumentGroteskSemiMono-Bold.woff2",
        "mono_name": "Monument Grotesk SemiMono",
        "k_code": "K05",
        "k_name": "Chuỗi Mũi Tên Nhân Quả ([A] → B)",
        "anatomy_axes": "Giữ nguyên: Cỡ chữ đồng nhất & xH (~0.51) | Đối lập nội dòng: Khung Grotesque hiện đại ↔ Từ khóa Serif Italic cổ điển",
        "use_case": "Sáng tạo nội dung, Marketing hiện đại, Agency, Khởi nghiệp, Thiết kế",
        "subbox_html": """
        <div class="sub-box box-k05">
          <div class="def-row old"><span class="badge-muted">QUAY VỘI</span><span>→ Khách lướt qua trong <b class="mono">0.5s</b></span></div>
          <div class="div-line"></div>
          <div class="def-row new"><span class="badge-gold">TRÚNG VIỆC</span><span>→ Khách dừng đọc & nhắn đăng ký</span></div>
        </div>
        """,
    },

    # ==================== BATCH C: L5 (P09, P10) & L6 (P11, P12) ====================
    {
        "pid": "P09",
        "batch": "C",
        "law_code": "L5",
        "law_name": "Luật L5 • Đối Cực Kiến Trúc & Bẫy Mực (Inktrap Tension)",
        "sid": "p09_l5_flexa_walsheim",
        "title": "Grilli Flexa Inktrap Architecture × Walsheim Pro & Aeonik Fono",
        "foundry": "Grilli Type × CoType",
        "h_main_file": "GRFlexaBold.woff2",
        "h_main_name": "GT Flexa Bold (Inktrap)",
        "h_focal_file": "GRFlexaBoldItalic.woff2",
        "h_focal_name": "GT Flexa Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "GRWalsheimPro-Medium.woff2",
        "sub_bold_file": "GRWalsheimPro-Bold.woff2",
        "sub_name": "GT Walsheim Pro",
        "mono_file": "FDAeonikFono-Bold.woff2",
        "mono_name": "Aeonik Fono Bold",
        "k_code": "K10",
        "k_name": "Thanh Đo Độ Nhớ (10% vs 95%)",
        "anatomy_axes": "Giữ nguyên: Độ dày nét Bold | Đối lập: Khe bẫy mực Inktrap khoét sâu góc giao ↔ Hình học tròn trịa Walsheim",
        "use_case": "Công nghệ, Phần mềm, Hiệu suất làm việc, Quảng cáo ra đơn thực tế",
        "subbox_html": """
        <div class="sub-box box-k10">
          <div class="meter-row"><span class="m-lbl">Clip quay vội</span><div class="m-track"><div class="m-fill low"></div></div><span class="mono m-val">10% nhớ</span></div>
          <div class="meter-row"><span class="m-lbl gold">1 Bài trúng đích</span><div class="m-track"><div class="m-fill high"></div></div><span class="mono m-val gold">95% nhắn</span></div>
        </div>
        """,
    },
    {
        "pid": "P10",
        "batch": "C",
        "law_code": "L5",
        "law_name": "Luật L5 • Đối Cực Chiều Rộng (Tall Condensed Tower × Engineered Sans)",
        "sid": "p10_l5_americangrotesk_calibre",
        "title": "Klim American Grotesk Condensed (96px Tower) × Calibre & Karbon Slab",
        "foundry": "Klim Type Foundry",
        "h_main_file": "FDAmericanGroteskCondensed-Bold.woff2",
        "h_main_name": "American Grotesk Condensed Bold",
        "h_focal_file": "FDAmericanGroteskCondensed-BoldItalic.woff2",
        "h_focal_name": "American Grotesk Condensed Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDCalibre-Medium.woff2",
        "sub_bold_file": "FDCalibre-Bold.woff2",
        "sub_name": "Calibre Medium/Bold",
        "mono_file": "FDKarbonSlabStencil-Bold.woff2",
        "mono_name": "Karbon Slab Stencil Bold",
        "k_code": "K21",
        "k_name": "Bộ Lọc 3 Giây Đầu (03s LƯỚT XEM)",
        "anatomy_axes": "Giữ nguyên: Trục đứng Grotesque | Đối lập chiều rộng: Thân chữ nén cao 96px (Condensed) ↔ Chữ ngang mở rộng Calibre",
        "use_case": "Sự kiện Offline, Tuyển sinh khóa học, Chiến dịch tốc độ, Thể thao",
        "subbox_html": """
        <div class="sub-box box-k21">
          <div class="big-metric mono">03s</div>
          <div class="metric-copy">
            <div class="mc-top">Bộ lọc <b>3 giây đầu</b> trên bảng tin:</div>
            <div class="mc-bot">Bài vội: khách lướt • Bài trúng: dừng & nhắn</div>
          </div>
        </div>
        """,
    },
    {
        "pid": "P11",
        "batch": "C",
        "law_code": "L6",
        "law_name": "Luật L6 • Giao Thoa Di Sản Báo Chí × Lưới Thụy Sĩ Hiện Đại",
        "sid": "p11_l6_financier_rmneue",
        "title": "Financial Times Authority (Financier 95px) × CoType RM Neue & Mono",
        "foundry": "Klim Type Foundry × CoType",
        "h_main_file": "FDFinancierDisplay-Bold.woff2",
        "h_main_name": "Financier Display Bold",
        "h_focal_file": "FDFinancierDisplay-BoldItalic.woff2",
        "h_focal_name": "Financier Display Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDRMNeue-Regular.woff2",
        "sub_bold_file": "FDRMNeue-Bold.woff2",
        "sub_name": "RM Neue Regular/Bold",
        "mono_file": "FDRMMono-Bold.woff2",
        "mono_name": "RM Mono Bold",
        "k_code": "K02",
        "k_name": "Khối Trích Dẫn Tối Sâu (Viền Đỉnh Vàng)",
        "anatomy_axes": "Giữ nguyên: Khí chất quyền lực điềm tĩnh | Đối lập: Serif cổ điển Anh Quốc (xH=0.444) ↔ Swiss Grid RM Neue (xH=0.520)",
        "use_case": "Tài chính, Chứng khoán, Quản trị doanh nghiệp, BĐS Vốn lớn",
        "subbox_html": """
        <div class="sub-box box-k02">
          <div class="q-line1"><b class="mono">10</b> clip quay vội khách chỉ xem rồi lướt qua.</div>
          <div class="q-line2">Chỉ cần <span class="gold"><b class="mono">01</b> bài đúng việc</span> làm khách tự nhắn.</div>
        </div>
        """,
    },
    {
        "pid": "P12",
        "batch": "C",
        "law_code": "L6",
        "law_name": "Luật L6 • Giao Thoa Khắc Đá Cổ Điển × Neo-Geometric Mềm Mại",
        "sid": "p12_l6_zirkon_aeonik_soft",
        "title": "Grilli Zirkon Chiseled Serif × CoType Aeonik Soft & Pitch Mono",
        "foundry": "Grilli Type × CoType & Klim",
        "h_main_file": "GRZirkonBold.woff2",
        "h_main_name": "GT Zirkon Bold",
        "h_focal_file": "GRZirkonBoldItalic.woff2",
        "h_focal_name": "GT Zirkon Bold Italic",
        "h_focal_style": "italic",
        "sub_med_file": "FDAeonikSoft-Medium.woff2",
        "sub_bold_file": "FDAeonikSoft-Bold.woff2",
        "sub_name": "Aeonik Soft (Rounded Terminal)",
        "mono_file": "FDPitch-Bold.woff2",
        "mono_name": "Pitch Typewriter Mono Bold",
        "k_code": "K15",
        "k_name": "Lịch Tuần 7 Ô (T2–CN)",
        "anatomy_axes": "Giữ nguyên: Lòng chữ rộng dễ đọc | Đối lập đầu nét: Chân chữ vát góc cạnh Zirkon ↔ Đầu nét bo tròn ấm áp Aeonik Soft",
        "use_case": "Văn hóa, Ẩm thực/F&B truyền thống, Du lịch, Đời sống, Quà tặng",
        "subbox_html": """
        <div class="sub-box box-k15">
          <div class="cal-grid mono">
            <span class="day">T2</span><span class="day">T3</span><span class="day on">T4 ✓</span><span class="day">T5</span><span class="day">T6</span><span class="day on">T7 ✓</span><span class="day">CN</span>
          </div>
          <div class="cal-caption">Tuần <b class="mono gold">02 bài</b> kỹ (T4 & T7) → khách nhớ & tự nhắn.</div>
        </div>
        """,
    },
]


def build_pairing_html(spec: Dict[str, Any]) -> str:
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
    width: 536px;
    max-width: 536px;
    background: rgba(5, 9, 18, 0.82);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 16px;
    padding: 20px 22px;
    margin-bottom: 44px;
    box-shadow: 0 22px 48px rgba(0, 0, 0, 0.48);
    font-family: "SubMed", sans-serif;
    color: #F8FAFC;
  }}
  .mono, .num-tag {{
    font-family: "MetaMono", monospace;
    letter-spacing: -0.02em;
  }}
  .gold {{ color: #FACC15 !important; font-family: "SubBold", sans-serif; }}
  .div-line {{ height: 1px; background: rgba(255, 255, 255, 0.11); width: 100%; margin: 13px 0; }}

  /* K01 */
  .row-old {{ font-size: 23.5px; color: #94A3B8; display: flex; align-items: baseline; gap: 10px; line-height: 1.32; }}
  .row-old .ic-bad {{ color: #F87171; font-family: "SubBold", sans-serif; font-size: 25px; flex-shrink: 0; }}
  .row-new {{ font-family: "SubBold", sans-serif; font-size: 24px; color: #FFFFFF; display: flex; align-items: baseline; gap: 10px; line-height: 1.32; }}
  .row-new .ic-good {{ color: #FACC15; font-size: 26px; flex-shrink: 0; }}
  .num-tag {{ background: rgba(148,163,184,0.16); padding: 2px 7px; border-radius: 6px; font-size: 20px; color: #CBD5E1; white-space: nowrap; flex-shrink: 0; }}
  .num-tag.gold {{ background: rgba(250,204,21,0.18); border: 1px solid rgba(250,204,21,0.45); color: #FACC15; font-family: "MetaMono", monospace; white-space: nowrap; flex-shrink: 0; }}

  /* K18 Equation */
  .eq-row {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; flex-wrap: wrap; }}
  .eq-pill {{ background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.16); padding: 5px 10px; border-radius: 8px; font-size: 20.5px; font-family: "SubBold", sans-serif; white-space: nowrap; }}
  .eq-op {{ color: #FACC15; font-family: "MetaMono", monospace; font-size: 22px; font-weight: 700; flex-shrink: 0; }}
  .eq-res {{ color: #FACC15; font-family: "SubBold", sans-serif; font-size: 21px; white-space: nowrap; }}
  .eq-sub {{ font-size: 20.5px; color: #CBD5E1; line-height: 1.34; white-space: normal; overflow-wrap: break-word; }}

  /* K06, K14, K20, K05 Rows */
  .def-row {{ display: flex; align-items: baseline; gap: 12px; font-size: 22.5px; line-height: 1.34; }}
  .def-row > span:last-child {{ min-width: 0; white-space: normal; overflow-wrap: break-word; text-wrap: pretty; }}
  .def-row b.mono {{ white-space: nowrap; }}
  .def-row.old {{ color: #94A3B8; font-size: 22px; }}
  .def-row.new {{ color: #FFFFFF; font-family: "SubBold", sans-serif; font-size: 23px; }}
  .badge-muted {{ font-family: "MetaMono", monospace; font-size: 16px; color: #94A3B8; background: rgba(148,163,184,0.15); border: 1px solid rgba(148,163,184,0.3); padding: 2px 8px; border-radius: 6px; white-space: nowrap; flex-shrink: 0; }}
  .badge-gold {{ font-family: "MetaMono", monospace; font-size: 16px; color: #070B14; background: #FACC15; padding: 2px 8px; border-radius: 6px; font-weight: 800; white-space: nowrap; flex-shrink: 0; }}

  /* K09 Chat */
  .chat-head {{ display: flex; align-items: center; gap: 10px; font-size: 18px; color: #94A3B8; margin-bottom: 9px; }}
  .live-dot {{ width: 9px; height: 9px; border-radius: 50%; background: #22C55E; flex-shrink: 0; }}
  .chat-msg {{ font-family: "SubBold", sans-serif; font-size: 24px; line-height: 1.34; color: #FFFFFF; white-space: normal; overflow-wrap: break-word; }}

  /* K03 & K21 Big Metric */
  .box-k03, .box-k21 {{ display: flex; align-items: center; gap: 16px; }}
  .big-metric {{ font-size: 56px; color: #FACC15; background: rgba(250,204,21,0.12); border: 1.5px solid rgba(250,204,21,0.40); padding: 6px 12px; border-radius: 12px; line-height: 1; white-space: nowrap; flex-shrink: 0; }}
  .metric-copy {{ display: flex; flex-direction: column; gap: 6px; min-width: 0; flex: 1; }}
  .mc-top {{ font-size: 21px; color: #CBD5E1; line-height: 1.32; white-space: normal; overflow-wrap: break-word; text-wrap: pretty; }}
  .mc-top b {{ color: #FFFFFF; font-family: "SubBold", sans-serif; white-space: nowrap; }}
  .mc-bot {{ font-size: 21.5px; color: #FACC15; font-family: "SubBold", sans-serif; line-height: 1.32; white-space: normal; overflow-wrap: break-word; text-wrap: pretty; }}

  /* K10 Meter */
  .meter-row {{ display: grid; grid-template-columns: max-content minmax(90px, 1fr) max-content; align-items: center; gap: 14px; margin-bottom: 12px; font-size: 21.5px; }}
  .meter-row:last-child {{ margin-bottom: 0; }}
  .m-lbl {{ min-width: 156px; color: #94A3B8; white-space: nowrap; }}
  .m-track {{ width: 100%; min-width: 0; height: 12px; background: rgba(255,255,255,0.10); border-radius: 99px; overflow: hidden; }}
  .m-fill.low {{ width: 16%; height: 100%; background: #64748B; border-radius: 99px; }}
  .m-fill.high {{ width: 94%; height: 100%; background: #FACC15; border-radius: 99px; }}
  .m-val {{ min-width: 96px; text-align: right; font-size: 20px; color: #94A3B8; white-space: nowrap; }}

  /* K02 Callout */
  .box-k02 {{ border-top: 3px solid #FACC15; }}
  .q-line1 {{ font-size: 23px; color: #94A3B8; margin-bottom: 10px; line-height: 1.34; white-space: normal; overflow-wrap: break-word; }}
  .q-line2 {{ font-family: "SubBold", sans-serif; font-size: 24px; color: #FFFFFF; line-height: 1.34; white-space: normal; overflow-wrap: break-word; }}

  /* K15 Calendar */
  .cal-grid {{ display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px; margin-bottom: 12px; }}
  .day {{ text-align: center; padding: 6px 0; border-radius: 7px; background: rgba(255,255,255,0.06); color: #64748B; font-size: 18.5px; white-space: nowrap; }}
  .day.on {{ background: rgba(250,204,21,0.22); border: 1px solid #FACC15; color: #FACC15; font-weight: 800; }}
  .cal-caption {{ font-family: "SubBold", sans-serif; font-size: 22px; color: #FFFFFF; line-height: 1.34; white-space: normal; overflow-wrap: break-word; }}

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


def run_batch(batch_filter: str, out_json: str):
    bg_img = Image.open(BG_PATH).convert("RGBA")
    selected = [s for s in PAIRING_SPECS if batch_filter == "ALL" or s["batch"] == batch_filter]
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)

        for spec in selected:
            sid = spec["sid"]
            hfile = PILOT_DIR / f"{sid}.html"
            hfile.write_text(build_pairing_html(spec), encoding="utf-8")
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

              // Measure focal span xH and apply font-size-adjust if needed so intra-line xH matches within +-2%
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

              // Auto-fit sub-box inner elements using TreeWalker(SHOW_TEXT) + scrollWidth check (CLAUDE2 LAW_11)
              const sBox = document.querySelector('.sub-box');
              if (sBox) {
                sBox.style.width = '546px';
                sBox.style.maxWidth = '546px';
                const sRight = sBox.getBoundingClientRect().right - 22;
                for (let step = 0; step < 18; step++) {
                  let anyIssue = false;
                  const walker = document.createTreeWalker(sBox, NodeFilter.SHOW_TEXT, null);
                  let tNode;
                  while ((tNode = walker.nextNode())) {
                    if (!tNode.nodeValue || !tNode.nodeValue.trim()) continue;
                    const range = document.createRange();
                    range.selectNodeContents(tNode);
                    const rects = Array.from(range.getClientRects());
                    const parentRow = tNode.parentElement.closest('.def-row, .row-old, .row-new, .mc-top, .mc-bot, .cal-caption, .eq-row, .eq-sub, .q-line1, .q-line2, .meter-row') || tNode.parentElement;
                    const overRight = rects.some(r => r.width > 0 && r.right > sRight);
                    const wrappedInSingleRow = rects.length > 1 && parentRow && !parentRow.classList.contains('chat-msg');
                    if (overRight || wrappedInSingleRow) {
                      const curFs = parseFloat(getComputedStyle(parentRow).fontSize);
                      if (curFs > 19.8) {
                        anyIssue = true;
                        parentRow.style.fontSize = (curFs - 0.6).toFixed(1) + 'px';
                        if (tNode.parentElement !== parentRow) {
                          tNode.parentElement.style.fontSize = (curFs - 0.6).toFixed(1) + 'px';
                        }
                      }
                    }
                  }
                  const allSub = Array.from(sBox.querySelectorAll('*'));
                  for (const el of allSub) {
                    if (el.clientWidth > 0 && el.scrollWidth > el.clientWidth + 1) {
                      const curFs = parseFloat(getComputedStyle(el).fontSize);
                      if (curFs > 19.8) {
                        anyIssue = true;
                        el.style.fontSize = (curFs - 0.6).toFixed(1) + 'px';
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

              const hRect = h.getBoundingClientRect();
              const sEl = document.querySelector('.sub-box');
              const sRect = sEl.getBoundingClientRect();
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

            # 1. Crop Headline only (620x440)
            y_h1 = max(0, calc["hTop"] - 36)
            crop_h = comp.crop((16, y_h1, 636, min(1350, y_h1 + 440))).resize((620, 440), Image.Resampling.LANCZOS)
            crop_h_path = PILOT_DIR / f"crop_head_{sid}.jpg"
            crop_h.save(crop_h_path, quality=92)

            # 2. Crop Subline + Meta (580x315)
            y_s1 = max(0, calc["sTop"] - 26)
            crop_s = comp.crop((20, y_s1, 600, min(1350, y_s1 + 315))).resize((580, 315), Image.Resampling.LANCZOS)
            crop_s_path = PILOT_DIR / f"crop_sub_{sid}.jpg"
            crop_s.save(crop_s_path, quality=92)

            # 3. Crop Full 3-Tier Typographic Pairing (Headline + Subline + Meta, 620x740)
            y_p1 = max(0, calc["hTop"] - 36)
            y_p2 = min(1350, max(y_p1 + 680, calc["mBottom"] + 36))
            crop_pair = comp.crop((16, y_p1, 636, y_p2)).resize((620, 740), Image.Resampling.LANCZOS)
            crop_pair_path = PILOT_DIR / f"crop_pair_{sid}.jpg"
            crop_pair.save(crop_pair_path, quality=93)

            results.append((spec, calc, hfile, jpg_path))

        browser.close()

    final_results = []
    for spec, calc, hfile, jpg_path in results:
        sid = spec["sid"]
        audit_res = audit_v3_banner(hfile, jpg_path, expected_lines=3, person_side="right")
        rec = {
            **spec,
            "calc": calc,
            "score": audit_res["score"],
            "all_pass": audit_res["all_13_pass"],
            "min_2d_gap_px": audit_res["gates"]["G2_LAW09_per_font_optical_leading"]["min_2d_ink_gap_px"],
            "intra_xh_ratio": audit_res["gates"]["G15_LAW10_typographic_pairing_harmony"]["intra_line_xh_ratio"],
            "hier_xh_ratio": audit_res["gates"]["G15_LAW10_typographic_pairing_harmony"]["headline_to_subline_xh_hierarchy"],
            "full_img": f"k4_31kb_banners/v2_pilots/{sid}.jpg",
            "crop_pair_img": f"k4_31kb_banners/v2_pilots/crop_pair_{sid}.jpg",
            "crop_head_img": f"k4_31kb_banners/v2_pilots/crop_head_{sid}.jpg",
            "crop_sub_img": f"k4_31kb_banners/v2_pilots/crop_sub_{sid}.jpg",
        }
        final_results.append(rec)
        print(f"[{spec['pid']} | {sid:32s}] fs={calc['fs']}px LH={calc['L_target']} W={calc['W_ratio']}x gap2D={rec['min_2d_gap_px']}px intraXH={rec['intra_xh_ratio']} hierXH={rec['hier_xh_ratio']} => {audit_res['score']} (PASS={audit_res['all_13_pass']})")

    if out_json:
        Path(out_json).write_text(json.dumps(final_results, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=str, default="ALL", choices=["A", "B", "C", "ALL"])
    parser.add_argument("--out-json", type=str, default="/tmp/pairing_batch_all.json")
    args = parser.parse_args()
    run_batch(args.batch, args.out_json)
