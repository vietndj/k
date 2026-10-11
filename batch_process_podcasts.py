#!/usr/bin/env python3
"""
batch_process_podcasts.py
Hệ thống tự động hóa xử lý batch 35 video podcast Raj Shamani:
1. Đọc danh sách video từ raj_35_queue.json (hỗ trợ checkpoint/resume).
2. Tải metadata & subtitle tiếng Anh qua yt-dlp.
3. Làm sạch subtitle.
4. Gọi Gemini API (google-genai SDK) với fallback pool để phân tích 8 insight Đơn sắc Thụy Sĩ.
5. Render file HTML chuẩn xuất bản fedu.vn/k.
6. Cập nhật thẻ .apple-card vào rajchannel.html.
7. Chạy build_feed.py và tự động git commit/push lên GitHub.
"""

import os
import sys
import re
import json
import time
import subprocess
import pathlib
from google import genai

# Đường dẫn thư mục
BASE_DIR = pathlib.Path("/Users/vietmac/Documents/CODE/k")
QUEUE_FILE = BASE_DIR / "raj_35_queue.json"
PROGRESS_FILE = BASE_DIR / "raj_35_progress.json"
HUB_FILE = BASE_DIR / "rajchannel.html"
LOG_FILE = BASE_DIR / "batch_process.log"

# API Key
CONFIG_KEY_FILE = pathlib.Path.home() / ".config" / "gemini" / "api_key"
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
if not API_KEY and CONFIG_KEY_FILE.exists():
    API_KEY = CONFIG_KEY_FILE.read_text().strip()

if not API_KEY:
    print("❌ Lỗi: Không tìm thấy GEMINI_API_KEY trong môi trường hoặc ~/.config/gemini/api_key")
    sys.exit(1)

client = genai.Client(api_key=API_KEY)

# Fallback pool các model Gemini đang hoạt động (ưu tiên các model tốc độ cao & ổn định)
MODEL_POOL = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-flash-latest",
    "gemini-3.5-flash",
    "gemini-flash-lite-latest"
]

def log(msg):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def clean_vtt(vtt_content):
    lines = vtt_content.splitlines()
    cleaned = []
    last = ""
    for line in lines:
        line = line.strip()
        if not line or line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line or re.match(r"^\d+$", line):
            continue
        text = re.sub(r"<[^>]+>", "", line).strip()
        if not text or text == last:
            continue
        cleaned.append(text)
        last = text
    return " ".join(cleaned)

def get_video_metadata_and_sub(yt_id):
    url = f"https://www.youtube.com/watch?v={yt_id}"
    log(f"[*] Đang lấy metadata & sub cho {yt_id}...")
    
    # 1. Metadata
    cmd_meta = [
        "yt-dlp",
        "--cookies-from-browser", "chrome",
        "--print", "%(upload_date>%d/%m/%Y)s|%(duration_string)s|%(title)s|%(upload_date)s",
        "--skip-download",
        url
    ]
    try:
        res_meta = subprocess.run(cmd_meta, capture_output=True, text=True, check=True)
    except Exception:
        # Fallback không cookies
        cmd_meta_fallback = [
            "yt-dlp",
            "--print", "%(upload_date>%d/%m/%Y)s|%(duration_string)s|%(title)s|%(upload_date)s",
            "--skip-download",
            url
        ]
        res_meta = subprocess.run(cmd_meta_fallback, capture_output=True, text=True, check=True)

    parts = res_meta.stdout.strip().split("|")
    publish_date = parts[0].strip() if len(parts) > 0 else "01/01/2026"
    duration = parts[1].strip() if len(parts) > 1 else "1:30:00"
    title_raw = parts[2].strip() if len(parts) > 2 else ""
    date_iso = parts[3].strip() if len(parts) > 3 else "2026-01-01"
    if len(date_iso) == 8:
        date_iso = f"{date_iso[:4]}-{date_iso[4:6]}-{date_iso[6:]}"

    # 2. Subtitles
    temp_prefix = BASE_DIR / f"temp_{yt_id}"
    cmd_sub = [
        "yt-dlp",
        "--cookies-from-browser", "chrome",
        "--write-auto-subs",
        "--sub-lang", "en",
        "--skip-download",
        "--sub-format", "vtt",
        "-o", str(temp_prefix),
        url
    ]
    try:
        subprocess.run(cmd_sub, capture_output=True, text=True, check=True)
    except Exception:
        # Fallback không cookies
        cmd_sub_fallback = [
            "yt-dlp",
            "--write-auto-subs",
            "--sub-lang", "en",
            "--skip-download",
            "--sub-format", "vtt",
            "-o", str(temp_prefix),
            url
        ]
        subprocess.run(cmd_sub_fallback, capture_output=True, text=True, check=True)
    
    vtt_file = BASE_DIR / f"temp_{yt_id}.en.vtt"
    transcript = ""
    if vtt_file.exists():
        vtt_content = vtt_file.read_text(encoding="utf-8")
        transcript = clean_vtt(vtt_content)
        vtt_file.unlink()
    else:
        log(f"[!] Cảnh báo: Không tìm thấy sub tiếng Anh cho {yt_id}")

    return {
        "yt_id": yt_id,
        "publish_date": publish_date,
        "date_iso": date_iso,
        "duration": duration,
        "title_raw": title_raw,
        "transcript": transcript
    }

SYSTEM_PROMPT = """Bạn là "Kiến Trúc Sư Trí Tuệ Hệ Thống" chuyên mổ xẻ podcast chuyên sâu cho fedu.vn.
Nhiệm vụ: Phân tích podcast dựa trên transcript, chiết xuất tri thức tối thượng theo triết lý "Đơn sắc Thụy Sĩ" (Swiss Monochrome) - Sắc bén, khách quan, không self-help sáo rỗng, 100% TIẾNG VIỆT đanh thép.

Yêu cầu xuất ra DUY NHẤT một chuỗi JSON hợp lệ (không kèm markdown ```json hay giải thích) theo schema sau:
{
  "vietnamese_title": "Tiêu đề tiếng Việt đanh thép, không thừa thãi",
  "speaker_name": "Tên khách mời / diễn giả chính",
  "speaker_role": "Vai trò, chức danh thực chiến",
  "category_section": "sec-tech", // BẮT BUỘC chọn 1 trong: "sec-tech", "sec-health", "sec-psychology", "sec-business", "sec-finance", "sec-arts-sports"
  "category_kicker": "TÊN NHÃN KICKER NGẮN IN HOA (ví dụ: TRÍ TUỆ NHÂN TẠO, QUẢN TRỊ VỐN, KHOA HỌC NÃO BỘ)",
  "slug": "ten-dien-gia-chu-de-chinh-podcast", // slug tiếng Anh không dấu, kết thúc bằng -podcast
  "editorial_hook": "Hai câu lục bát mở đầu đanh thép, phản ánh bài học lớn nhất",
  "lead_box": [
    "• Điểm nhấn 1: Tóm tắt thực trạng hoặc cạm bẫy đám đông hay mắc phải.",
    "• Điểm nhấn 2: Luận điểm cốt lõi và đòn bẩy thấu suốt của diễn giả."
  ],
  "card_bullets": [
    "Mô tả súc tích ý 1 cho thẻ Apple Card (dưới 120 ký tự)",
    "Mô tả súc tích ý 2 cho thẻ Apple Card (dưới 120 ký tự)"
  ],
  "delusion": {
    "quote": "Một câu tuyên ngôn sắc lạnh đập tan ảo tưởng đám đông",
    "crowd_myth_title": "ẢO TƯỞNG ĐÁM ĐÔNG",
    "crowd_myth_desc": "Mô tả chi tiết đám đông đang lầm tưởng điều gì",
    "truth_title": "SỰ THẬT HỆ THỐNG",
    "truth_desc": "Mô tả bản chất thực tế mà diễn giả bóc trần",
    "poem": "Hai câu lục bát đúc kết phần bóc trần lầm tưởng"
  },
  "insights": [
    // BẮT BUỘC ĐỦ ĐÚNG 8 INSIGHTS
    {
      "number": 1,
      "title": "Tóm tắt 1 câu sắc bén",
      "fact": "Dữ kiện gốc, nghiên cứu, số liệu hoặc câu chuyện thực tế được trích dẫn",
      "surface": "Hiện tượng bề mặt mà đa số người thường lầm tưởng hoặc làm sai",
      "nature": "Giải mã bản chất qua lăng kính vật lý / sinh học / hệ thống",
      "leverage": "Đòn bẩy thực chiến để tối ưu hóa quy trình / môi trường",
      "poem": "Hai câu thơ lục bát đúc kết sâu sắc"
    }
  ],
  "space_design": {
    "title": "THIẾT KẾ MÔI TRƯỜNG VẬT LÝ & QUY TRÌNH",
    "content": "Hướng dẫn cụ thể cách bài trí không gian làm việc, loại bỏ ma sát, thiết kế trigger để hiện thực hóa bài học.",
    "poem": "Hai câu lục bát đúc kết"
  },
  "emotion_protection": {
    "title": "BẢO TOÀN CẢM XÚC & QUẢN TRỊ TÂM THÁI",
    "content": "Khách quan hóa thất bại, xem rủi ro là dữ liệu game, giữ năng lượng và dopamine ổn định.",
    "poem": "Hai câu lục bát đúc kết"
  }
}
"""

def analyze_with_gemini(video_info, ep_code):
    prompt = f"""Thông tin podcast:
Mã tập: {ep_code}
Tiêu đề gốc: {video_info['title_raw']}
Thời lượng: {video_info['duration']}
Ngày phát hành: {video_info['publish_date']}
YouTube ID: {video_info['yt_id']}

Dưới đây là Transcript đầy đủ của video:
---
{video_info['transcript'][:70000]}
---
Hãy đọc kỹ transcript và trả về chuỗi JSON hoàn chỉnh theo đúng hướng dẫn hệ thống."""

    for model_name in MODEL_POOL:
        try:
            log(f"[*] Thử gọi Gemini model: {model_name}...")
            resp = client.models.generate_content(
                model=model_name,
                contents=[
                    {"role": "user", "parts": [{"text": SYSTEM_PROMPT + "\n\n" + prompt}]}
                ],
                config={"response_mime_type": "application/json"}
            )
            data = json.loads(resp.text)
            # Kiểm tra các trường quan trọng
            if "insights" in data and len(data["insights"]) >= 8 and "slug" in data:
                log(f"[+] Phân tích thành công bằng {model_name}!")
                return data
            else:
                log(f"[!] Dữ liệu từ {model_name} thiếu trường hoặc < 8 insights. Đang thử model khác...")
        except Exception as e:
            log(f"[!] Lỗi khi gọi {model_name}: {str(e)[:150]}. Thử model tiếp theo sau 3s...")
            time.sleep(3)

    raise RuntimeError(f"Không thể phân tích video {video_info['yt_id']} sau khi thử toàn bộ pool model.")

def generate_html_file(data, video_info, ep_code):
    slug = data.get("slug", f"podcast-{video_info['yt_id']}")
    if not slug.endswith("-podcast"):
        slug += "-podcast"
    
    speaker = data.get("speaker_name", "Raj Shamani")
    role = data.get("speaker_role", "Chuyên gia")
    title_vn = data.get("vietnamese_title", "Phân Tích Chuyên Sâu")
    kicker = data.get("category_kicker", "KIẾN TRÚC HỆ THỐNG")
    orig_title = video_info.get("title_raw", "")
    pub_date = video_info.get("publish_date", "01/01/2026")
    date_iso = video_info.get("date_iso", "2026-01-01")
    duration = video_info.get("duration", "1:30:00")
    yt_id = video_info.get("yt_id", "")
    yt_url = f"https://www.youtube.com/watch?v={yt_id}"

    # Render lead box
    lead_items = "\n".join([f"        <p>{p}</p>" for p in data.get("lead_box", [])])

    # Render insights
    insight_html_list = []
    for ins in data.get("insights", [])[:8]:
        num = ins.get("number", len(insight_html_list) + 1)
        ititle = ins.get("title", "")
        ifact = ins.get("fact", "")
        isurf = ins.get("surface", "")
        inature = ins.get("nature", "")
        ilev = ins.get("leverage", "")
        ipoem = ins.get("poem", "")

        ins_block = f"""          <!-- Insight {num} -->
          <div class="cb-item">
            <div class="insight-title">### 📌 Insight {num}: {ititle}</div>
            <div class="insight-quote">🎙️ <strong>Dữ kiện gốc:</strong> {ifact}</div>
            <div class="cb-layer">👁️ <strong>Hiện tượng bề mặt:</strong> {isurf}</div>
            <div class="cb-layer">🔬 <strong>Giải mã bản chất:</strong> {inature}</div>
            <div class="cb-layer">⚙️ <strong>Đòn bẩy thực chiến:</strong> {ilev}</div>
            <div class="cb-mantra">"{ipoem}"</div>
          </div>"""
        insight_html_list.append(ins_block)
    
    insights_rendered = "\n\n".join(insight_html_list)

    delusion = data.get("delusion", {})
    space = data.get("space_design", {})
    emotion = data.get("emotion_protection", {})

    html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{speaker}: {title_vn}</title>
  <meta property="article:published_time" content="{date_iso}" />
  <meta name="publish_date" content="{pub_date}" />
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <style>
    @font-face {{ font-family: 'FD Aeonik Extended'; src: url('./fonts/FDAeonikExtended-Regular.woff2?v=2') format('woff2'); font-weight: 400; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'FD Aeonik Extended'; src: url('./fonts/FDAeonikExtended-Bold.woff2?v=2') format('woff2'); font-weight: 700; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikRegular.ttf') format('truetype'); font-weight: 400; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikSemiBold.ttf') format('truetype'); font-weight: 600; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'FD Aeonik'; src: url('./fonts/FDAeonikBold.ttf') format('truetype'); font-weight: 700; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'Tiempos Text'; src: url('./fonts/FDTiemposText-Regular.woff2?v=2') format('woff2'); font-weight: 400; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'Tiempos Text'; src: url('./fonts/FDTiemposText-Bold.woff2?v=2') format('woff2'); font-weight: 700; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'Tiempos Text'; src: url('./fonts/FDTiemposText-Semibold.woff2?v=2') format('woff2'); font-weight: 600; font-style: normal; font-display: swap; }}
    @font-face {{ font-family: 'Tiempos Text'; src: url('./fonts/FDTiemposText-RegularItalic.woff2?v=2') format('woff2'); font-weight: 400; font-style: italic; font-display: swap; }}

    :root {{
      --cl-bg: #ffffff;
      --cl-tint: #f8fafc;
      --cl-card: #ffffff;
      --cl-accent: #1a73e8;
      --cl-line: rgba(0, 0, 0, 0.06);
      --cl-border-code: #e2e8f0;
      --cl-text-base: #090d16;
      --cl-text-body: #0f172a;
      --cl-text-muted: #475569;
      --cl-radius-md: 12px;
      --cl-radius-sm: 8px;
      --cl-radius-full: 9999px;
      --font-display-short: 'FD Aeonik Extended', sans-serif;
      --font-display-long: 'FD Aeonik', sans-serif;
      --font-body: 'FD Aeonik', sans-serif;
      --font-reading: 'Tiempos Text', serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
    body {{ background-color: var(--cl-bg); color: var(--cl-text-body); font-family: var(--font-body); line-height: 1.8; font-size: 16.5px; }}

    .read-section {{ padding: 72px 24px; width: 100%; }}
    .read-section--light {{ background-color: var(--cl-bg); }}
    .read-section--tint {{ background-color: var(--cl-tint); border-top: 1px solid var(--cl-line); border-bottom: 1px solid var(--cl-line); }}
    .read-container {{ max-width: 760px; margin: 0 auto; }}
    
    .cl-badge {{ display: inline-flex; align-items: center; gap: 8px; font-family: 'FD Aeonik', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.12em; text-transform: uppercase; color: var(--cl-text-muted); background: #f1f5f9; border: 1px solid var(--cl-border-code); padding: 5px 14px; border-radius: var(--cl-radius-full); margin-bottom: 18px; }}
    .title-hero {{ font-family: var(--font-display-short); font-weight: 700; font-size: clamp(26px, 3.8vw, 36px); line-height: 1.25; color: var(--cl-text-base); margin-bottom: 12px; text-transform: uppercase; }}
    .title-sub {{ font-family: var(--font-display-long); font-weight: 600; font-size: clamp(19px, 2.6vw, 24px); color: var(--cl-text-base); margin-bottom: 18px; }}
    .editorial-hook {{ font-family: var(--font-reading); font-style: italic; font-weight: 500; font-size: clamp(18px, 2.2vw, 22px); color: var(--cl-text-base); margin: 18px 0 24px; padding-left: 18px; border-left: 3px solid var(--cl-text-base); }}
    
    .lead-box {{ background: var(--cl-card); border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); padding: 22px 24px; margin-bottom: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }}
    .lead-box p {{ font-size: 16px; margin-bottom: 12px; }}
    .lead-box p:last-child {{ margin-bottom: 0; }}
    .lead-box strong {{ color: var(--cl-text-base); }}
    
    .podcast-meta-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; margin: 18px 0 28px; padding: 14px 18px; background: var(--cl-tint); border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); }}
    .meta-item {{ display: flex; flex-direction: column; gap: 2px; }}
    .meta-item__label {{ font-family: 'FD Aeonik', sans-serif; font-size: 10px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--cl-text-muted); }}
    .meta-item__val {{ font-size: 13.5px; font-weight: 600; color: var(--cl-text-base); }}

    .code-box {{ position: relative; background: #ffffff; border: 1px solid var(--cl-border-code); border-radius: 12px; padding: 24px 28px 22px; margin: 28px 0 36px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }}
    .cb-meta {{ font-family: 'FD Aeonik', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cl-text-muted); margin-bottom: 4px; }}
    .cb-title {{ font-family: 'FD Aeonik', sans-serif; font-size: 18px; font-weight: 700; color: var(--cl-text-base); margin-bottom: 18px; }}
    .cb-item {{ margin-bottom: 24px; padding-bottom: 24px; border-bottom: 1px solid var(--cl-line); }}
    .cb-item:last-child {{ margin-bottom: 0; padding-bottom: 0; border-bottom: none; }}
    
    .insight-title {{ font-family: 'FD Aeonik', sans-serif; font-size: 16px; font-weight: 700; color: var(--cl-text-base); margin-bottom: 12px; }}
    .insight-quote {{ background: var(--cl-tint); border-left: 3px solid var(--cl-accent); padding: 12px 16px; margin-bottom: 16px; font-family: var(--font-reading); font-style: italic; color: var(--cl-text-base); font-size: 15.5px; }}
    
    .cb-layer {{ margin-bottom: 10px; font-family: var(--font-reading); font-size: 16.5px; line-height: 1.75; color: var(--cl-text-body); }}
    .cb-layer strong {{ color: var(--cl-text-base); font-family: var(--font-body); font-weight: 600; }}
    
    .cb-mantra {{ margin-top: 18px; padding-top: 14px; border-top: 1px dashed var(--cl-border-code); font-family: var(--font-reading); font-style: italic; font-size: 16.5px; color: var(--cl-text-base); font-weight: 500; }}

    .compare-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 22px 0 30px; }}
    .compare-card {{ background: #ffffff; border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); padding: 22px 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }}
    .compare-card__badge {{ font-family: 'FD Aeonik', sans-serif; font-size: 10.5px; font-weight: 600; padding: 3px 8px; border-radius: var(--cl-radius-sm); display: inline-block; margin-bottom: 10px; letter-spacing: 0.08em; text-transform: uppercase; background: #f1f5f9; color: var(--cl-text-muted); border: 1px solid var(--cl-line); }}
    .compare-card__title {{ font-family: 'FD Aeonik', sans-serif; font-size: 16px; font-weight: 600; color: var(--cl-text-base); margin-bottom: 8px; }}
    .compare-card__text {{ font-size: 14.5px; color: var(--cl-text-body); }}
    
    .copy-btn {{ position: absolute; top: 14px; right: 14px; display: inline-flex; align-items: center; gap: 6px; background: #ffffff; color: var(--cl-text-muted); border: 1px solid var(--cl-border-code); border-radius: 6px; padding: 5px 11px; font-family: 'FD Aeonik', sans-serif; font-size: 11.5px; font-weight: 600; cursor: pointer; }}
    .copy-btn:hover {{ background: var(--cl-tint); color: var(--cl-text-base); }}
  </style>
</head>
<body>

  <!-- PHẦN 1: TỔNG QUAN & DỮ LIỆU GỐC -->
  <section class="read-section read-section--light">
    <div class="read-container">
      <div class="cl-badge">{ep_code} / {kicker}</div>
      <h1 class="title-hero">{speaker}<br>{title_vn}</h1>
      <h2 class="title-sub">{orig_title}</h2>
      
      <div class="editorial-hook">
        "{data.get('editorial_hook', '')}"
      </div>

      <div class="lead-box">
{lead_items}
      </div>

      <div class="podcast-meta-grid">
        <div class="meta-item"><span class="meta-item__label">Khách mời</span><span class="meta-item__val">{speaker}</span></div>
        <div class="meta-item"><span class="meta-item__label">Vai trò</span><span class="meta-item__val">{role}</span></div>
        <div class="meta-item"><span class="meta-item__label">Phát hành</span><span class="meta-item__val">{pub_date}</span></div>
        <div class="meta-item"><span class="meta-item__label">Thời lượng gốc</span><span class="meta-item__val">{duration}</span></div>
        <div class="meta-item"><span class="meta-item__label">Nền tảng</span><span class="meta-item__val"><a href="{yt_url}" target="_blank" style="color:var(--cl-accent);text-decoration:none;">YouTube (Raj Shamani)</a></span></div>
      </div>
    </div>
  </section>

  <!-- PHẦN 2: BÓC TRẦN LẦM TƯỞNG -->
  <section class="read-section read-section--tint">
    <div class="read-container">
      <div class="cl-badge">02 / BÓC TRẦN LẦM TƯỞNG</div>
      <h2 class="title-sub" style="font-family: var(--font-display-short); text-transform: uppercase;">ẢO TƯỞNG ĐÁM ĐÔNG & SỰ THẬT TỒN TẠI</h2>
      
      <blockquote>
        <p style="font-family: var(--font-reading); font-style: italic; font-size: 18px; margin-bottom: 24px; padding-left: 16px; border-left: 3px solid var(--cl-text-base);">
          "{delusion.get('quote', '')}"
        </p>
      </blockquote>

      <div class="compare-grid">
        <div class="compare-card">
          <span class="compare-card__badge">{delusion.get('crowd_myth_title', 'ẢO TƯỞNG ĐÁM ĐÔNG')}</span>
          <h3 class="compare-card__title">{delusion.get('crowd_myth_title', '')}</h3>
          <p class="compare-card__text">{delusion.get('crowd_myth_desc', '')}</p>
        </div>

        <div class="compare-card">
          <span class="compare-card__badge">{delusion.get('truth_title', 'SỰ THẬT HỆ THỐNG')}</span>
          <h3 class="compare-card__title">{delusion.get('truth_title', '')}</h3>
          <p class="compare-card__text">{delusion.get('truth_desc', '')}</p>
        </div>
      </div>
      
      <div style="text-align: center; font-family: var(--font-reading); font-style: italic; color: var(--cl-text-base); font-size: 17px; margin-top: 16px; font-weight: 500;">
        "{delusion.get('poem', '')}"
      </div>
    </div>
  </section>

  <!-- PHẦN 3: 8 DEEP INSIGHTS -->
  <section class="read-section read-section--light">
    <div class="read-container">
      <div class="cl-badge">03 / CHIẾT XUẤT 8 INSIGHT CỐT LÕI</div>
      
      <div class="code-box">
        <button class="copy-btn" onclick="navigator.clipboard.writeText(this.parentElement.innerText); this.innerText='Đã chép!'; setTimeout(()=>this.innerText='Sao chép', 2000);"><span>Sao chép</span></button>
        <div class="cb-inner">
          <div class="cb-meta">KHO TÀNG NHẬN THỨC // 8 DEEP INSIGHTS</div>
          <div class="cb-title">Giải mã bản chất từ {speaker}</div>

{insights_rendered}

        </div>
      </div>
    </div>
  </section>

  <!-- PHẦN 4: THIẾT KẾ KHÔNG GIAN -->
  <section class="read-section read-section--tint">
    <div class="read-container">
      <div class="cl-badge">04 / THIẾT KẾ KHÔNG GIAN</div>
      <h2 class="title-sub" style="font-family: var(--font-display-short); text-transform: uppercase;">{space.get('title', 'THIẾT KẾ MÔI TRƯỜNG VẬT LÝ & QUY TRÌNH')}</h2>
      
      <div style="font-family: var(--font-reading); font-size: 16.5px; line-height: 1.8; margin-bottom: 20px;">
        <p>{space.get('content', '')}</p>
      </div>

      <div style="text-align: center; font-family: var(--font-reading); font-style: italic; color: var(--cl-text-base); font-size: 17px; font-weight: 500;">
        "{space.get('poem', '')}"
      </div>
    </div>
  </section>

  <!-- PHẦN 5: BẢO TOÀN CẢM XÚC -->
  <section class="read-section read-section--light">
    <div class="read-container">
      <div class="cl-badge">05 / BẢO TOÀN CẢM XÚC</div>
      <h2 class="title-sub" style="font-family: var(--font-display-short); text-transform: uppercase;">{emotion.get('title', 'BẢO TOÀN CẢM XÚC & QUẢN TRỊ TÂM THÁI')}</h2>
      
      <div style="font-family: var(--font-reading); font-size: 16.5px; line-height: 1.8; margin-bottom: 20px;">
        <p>{emotion.get('content', '')}</p>
      </div>

      <div style="text-align: center; font-family: var(--font-reading); font-style: italic; color: var(--cl-text-base); font-size: 17px; font-weight: 500;">
        "{emotion.get('poem', '')}"
      </div>
    </div>
  </section>

</body>
</html>
"""
    output_path = BASE_DIR / f"{slug}.html"
    output_path.write_text(html_content, encoding="utf-8")
    log(f"[+] Đã tạo file HTML: {output_path.name}")
    return slug

def inject_apple_card_to_hub(data, video_info, ep_code, slug):
    section_id = data.get("category_section", "sec-business")
    kicker = data.get("category_kicker", "CHUYÊN ĐỀ")
    speaker = data.get("speaker_name", "Raj Shamani")
    role = data.get("speaker_role", "")
    speaker_display = f"{speaker} ({role})" if role else speaker
    title_vn = data.get("vietnamese_title", "")
    yt_id = video_info.get("yt_id", "")
    
    bullets = data.get("card_bullets", [])
    bullet_1 = bullets[0] if len(bullets) > 0 else "Phân tích bản chất cốt lõi từ chuyên gia."
    bullet_2 = bullets[1] if len(bullets) > 1 else "Ứng dụng đòn bẩy thực chiến để nhân bản năng suất."

    card_html = f"""<!-- Video {ep_code} -->
<div class="apple-card" style="--card-delay: 0ms;">
<div>
<div class="apple-card__ep">{ep_code} // {kicker} • 2026</div>
<h3 class="apple-card__title">{title_vn}</h3>
<div class="apple-card__speaker">👤 {speaker_display}</div>
<div class="apple-card__summary">
<p>• {bullet_1}</p>
<p>• {bullet_2}</p>
</div>
</div>
<div class="apple-card__actions">
<a class="apple-card__btn apple-card__btn--primary" href="./{slug}.html">ĐỌC BÀI PHÂN TÍCH →</a>
<a class="apple-card__btn apple-card__btn--secondary" href="https://www.youtube.com/watch?v={yt_id}" target="_blank">YOUTUBE ↗</a>
</div>
</div>"""

    with open(HUB_FILE, "r", encoding="utf-8") as f:
        hub_text = f.read()

    # Kiểm tra xem link hoặc slug đã tồn tại chưa
    if f"./{slug}.html" in hub_text or yt_id in hub_text:
        log(f"[*] Thẻ cho {ep_code} ({slug}) đã có trong rajchannel.html, bỏ qua.")
        return

    pattern = r'(<section[^>]*id="' + re.escape(section_id) + r'"[^>]*>.*?<div class="apple-cards-grid">)'
    if not re.search(pattern, hub_text, flags=re.DOTALL):
        # Fallback vào sec-business nếu section không tìm thấy
        section_id = "sec-business"
        pattern = r'(<section[^>]*id="' + re.escape(section_id) + r'"[^>]*>.*?<div class="apple-cards-grid">)'

    new_hub_text = re.sub(pattern, r'\1\n' + card_html, hub_text, count=1, flags=re.DOTALL)
    
    with open(HUB_FILE, "w", encoding="utf-8") as f:
        f.write(new_hub_text)
    
    log(f"[+] Đã chèn thẻ Apple Card [{ep_code}] vào section #{section_id} của rajchannel.html")

def run_build_and_deploy():
    log("[*] Đang chạy build_feed.py...")
    subprocess.run([sys.executable, str(BASE_DIR / "build_feed.py")], cwd=str(BASE_DIR), check=True)
    
    log("[*] Đang Git Add, Commit & Push...")
    subprocess.run(["git", "add", "."], cwd=str(BASE_DIR), check=True)
    subprocess.run(["git", "commit", "-m", "Batch add 35 Raj Shamani podcasts (Swiss Monochrome)"], cwd=str(BASE_DIR), check=True)
    subprocess.run(["git", "push", "origin", "main"], cwd=str(BASE_DIR), check=True)
    log("[🎉] HOÀN TẤT TOÀN BỘ QUY TRÌNH DEPLOY LÊN GITHUB!")

def main():
    if not QUEUE_FILE.exists():
        log(f"❌ Không tìm thấy file hàng đợi {QUEUE_FILE}")
        sys.exit(1)

    with open(QUEUE_FILE, "r", encoding="utf-8") as f:
        queue = json.load(f)

    # Đọc tiến độ đã hoàn thành
    processed = {}
    if PROGRESS_FILE.exists():
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                processed = json.load(f)
        except Exception:
            processed = {}

    total = len(queue)
    log(f"🚀 BẮT ĐẦU TIẾN TRÌNH XỬ LÝ BATCH {total} PODCASTS RAJ SHAMANI")
    log(f"Đã hoàn thành trước đó: {len(processed)}/{total}")

    for idx, item in enumerate(queue, 1):
        yt_id = item["id"]
        ep_code = item.get("ep", "PODCAST")
        raw_title = item.get("raw_title", "")

        if yt_id in processed:
            log(f"[{idx}/{total}] Đã xử lý trước đó: {ep_code} ({yt_id}) - Bỏ qua.")
            continue

        log(f"\n{'='*60}")
        log(f"[{idx}/{total}] ĐANG XỬ LÝ: {ep_code} | {raw_title[:60]}...")
        log(f"{'='*60}")

        try:
            # 1. Tải metadata & subtitle
            video_info = get_video_metadata_and_sub(yt_id)
            if not video_info["transcript"]:
                log(f"[!] Bỏ qua {yt_id} vì không có transcript khả dụng.")
                continue

            # 2. Gọi Gemini phân tích
            analysis_data = analyze_with_gemini(video_info, ep_code)

            # 3. Tạo file HTML
            slug = generate_html_file(analysis_data, video_info, ep_code)

            # 4. Inject vào rajchannel.html
            inject_apple_card_to_hub(analysis_data, video_info, ep_code, slug)

            # 5. Lưu checkpoint
            processed[yt_id] = {
                "ep": ep_code,
                "slug": slug,
                "title_vn": analysis_data.get("vietnamese_title", ""),
                "time": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
                json.dump(processed, f, ensure_ascii=False, indent=2)

            log(f"✅ Hoàn tất tập [{idx}/{total}]: {ep_code} -> {slug}.html")

            # Delay nhỏ để tránh rate limit
            time.sleep(2)

        except Exception as e:
            log(f"❌ LỖI KHI XỬ LÝ {ep_code} ({yt_id}): {e}")
            import traceback
            log(traceback.format_exc())
            time.sleep(5)

    log(f"\n{'='*60}")
    log(f"🎉 ĐÃ HOÀN THÀNH XỬ LÝ TẤT CẢ VIDEO TRONG HÀNG ĐỢI!")
    log(f"{'='*60}")

    # Chạy build feed và push Git
    try:
        run_build_and_deploy()
    except Exception as e:
        log(f"[!] Lỗi khi chạy build/deploy: {e}")

if __name__ == "__main__":
    main()
