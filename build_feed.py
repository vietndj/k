#!/usr/bin/env python3
"""
build_feed.py
Tự động đồng bộ và tái lập chỉ mục danh sách bài viết cho FEDU Podcast Intelligence (fedu.vn/k).
- Quét toàn bộ file *.html trong thư mục (trừ index.html).
- Trích xuất metadata: title, summary, category, size_kb, mtime.
- Lấy timestamp commit từ Git để sắp xếp chuẩn xác bài mới nhất lên đầu.
- Giữ nguyên các thông tin đã được tinh chỉnh thủ công trước đó.
- Xuất file articles_data.json.
"""

import os
import re
import json
import subprocess
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "articles_data.json")

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.in_title = False
        self.paragraphs = []
        self.in_p = False
        self.cur_p = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta" and attrs_dict.get("name", "").lower() == "description":
            self.description = attrs_dict.get("content", "")
        elif tag == "p":
            self.in_p = True
            self.cur_p = []

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "p":
            self.in_p = False
            text = "".join(self.cur_p).strip()
            if len(text) > 40 and not text.startswith("©") and len(self.paragraphs) < 3:
                self.paragraphs.append(text)

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_p:
            self.cur_p.append(data)

def clean_text(t):
    if not t:
        return ""
    return re.sub(r"\s+", " ", t).strip()

def infer_category(title, summary, slug):
    text = f"{title} {summary} {slug}".lower()
    
    # Ưu tiên 1: Kinh doanh, bán hàng, tăng trưởng view
    if any(k in text for k in ["bán hàng", "chốt sale", "chot sale", "xây kênh", "triệu view", "shorts", "kinh doanh", "đòn bẩy", "doanh nghiệp", "tài chính", "tiền bạc", "wealth", "ray dalio", "jun yuh", "shelby"]):
        return "Kinh Doanh & Đòn Bẩy"
    
    # Ưu tiên 2: Khoa học não bộ, thần kinh học, giấc ngủ, stress, tâm lý
    if any(k in text for k in ["huberman", "não bộ", "não", "thần kinh", "dopamine", "serotonin", "adhd", "stress", "sleep", "giấc ngủ", "tâm lý", "cảm xúc", "lo âu", "darby"]):
        return "Khoa Học Não Bộ"
    
    # Ưu tiên 3: Sinh học, đường ruột, tế bào, ung thư, dinh dưỡng
    if any(k in text for k in ["tế bào", "đường ruột", "ruột", "glucose", "insulin", "sinh học", "gan", "ung thư", "tiểu đường", "metabolism", "chuyển hóa", "ty thể"]):
        return "Sinh Học & Tế Bào"
    
    # Ưu tiên 4: AI & Công nghệ
    if any(k in text for k in ["ai", "chatgpt", "claude", "agent", "computer use", "prompt", "thuật toán", "code", "máy tính", "spacex", "kardashev", "motion design", "deepseek", "siêu máy tính"]):
        return "AI & Công Nghệ"
    
    # Ưu tiên 5: Triết học, khắc kỷ, thức tỉnh
    if any(k in text for k in ["khắc kỷ", "stoic", "triết học", "thức tỉnh", "ý thức", "thiền", "tâm trí", "hạnh phúc", "cái tôi", "vũ trụ"]):
        return "Triết Học & Thức Tỉnh"
    
    return "Hệ Thống & Tự Sự"

def get_git_timestamps():
    file_mtimes = {}
    try:
        res = subprocess.run(
            ["git", "log", "--format=COMMIT:%ct", "--name-only"],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        current_time = None
        for line in res.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("COMMIT:"):
                current_time = float(line.split(":")[1])
            else:
                if line.endswith(".html") and line not in file_mtimes:
                    file_mtimes[line] = current_time
    except Exception as e:
        print(f"[WARN] Không thể đọc Git commit timestamps: {e}")
    return file_mtimes

def main():
    existing_items = {}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    existing_items[item["slug"]] = item
        except Exception as e:
            print(f"[WARN] Lỗi đọc {DATA_FILE}: {e}")

    git_mtimes = get_git_timestamps()

    html_files = [
        f for f in os.listdir(BASE_DIR)
        if f.endswith(".html") and f != "index.html" and not f.startswith(".")
    ]

    print(f"[*] Tìm thấy {len(html_files)} bài viết HTML...")

    articles = []
    new_count = 0
    updated_count = 0

    for fname in html_files:
        fpath = os.path.join(BASE_DIR, fname)
        size_kb = round(os.path.getsize(fpath) / 1024, 1)

        # Lấy mtime từ git log hoặc filesystem
        mtime = git_mtimes.get(fname, os.path.getmtime(fpath))

        if fname in existing_items:
            item = existing_items[fname].copy()
            item["size_kb"] = size_kb
            item["mtime"] = mtime
            articles.append(item)
            updated_count += 1
        else:
            # Parse nội dung bài mới
            try:
                with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                    content_chunk = f.read(25000)
                parser = MetaParser()
                parser.feed(content_chunk)
                
                title = clean_text(parser.title)
                title = re.sub(r"\s*\|\s*Kiến Trúc Sư.*$", "", title, flags=re.I)
                title = re.sub(r"\s*\|\s*System Intelligence.*$", "", title, flags=re.I)
                if not title:
                    title = fname.replace("-", " ").replace(".html", "").title()

                summary = clean_text(parser.description)
                if not summary and parser.paragraphs:
                    summary = parser.paragraphs[0]
                if not summary:
                    summary = "Phân tích đa tầng từ Podcast chuyên sâu bởi Kiến trúc sư Trí tuệ Hệ thống."

                category = infer_category(title, summary, fname)

                new_item = {
                    "slug": fname,
                    "title": title,
                    "summary": summary,
                    "category": category,
                    "size_kb": size_kb,
                    "mtime": mtime
                }
                articles.append(new_item)
                new_count += 1
                print(f"  [+] Bài mới: {fname} -> [{category}] {title[:40]}...")
            except Exception as e:
                print(f"  [!] Lỗi parse {fname}: {e}")

    # Sắp xếp mới nhất lên đầu
    articles.sort(key=lambda x: x.get("mtime", 0), reverse=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

    print(f"[OK] Đã cập nhật {DATA_FILE}:")
    print(f"     - Tổng số bài: {len(articles)}")
    print(f"     - Bài mới thêm: {new_count}")
    print(f"     - Bài cập nhật: {updated_count}")

if __name__ == "__main__":
    main()
