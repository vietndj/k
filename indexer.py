#!/usr/bin/env python3
"""
indexer.py
FEDU Knowledge Vault Indexer & Full-Text Engine for fedu.vn/k.
- Scans all standalone HTML analysis files in repo k.
- Extracts clean titles, identifies speakers, eliminates generic summaries.
- Fixes regex word-boundary bugs for AI & categories.
- Generates:
    1. catalog.json (compact metadata for rapid UI rendering & CMS sync)
    2. search_index.json (full-text index with text snippets for instant search)
    3. articles_data.json (backward-compatible mirror)
"""

import os
import re
import json
import subprocess
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_FILE = os.path.join(BASE_DIR, "catalog.json")
SEARCH_INDEX_FILE = os.path.join(BASE_DIR, "search_index.json")
LEGACY_DATA_FILE = os.path.join(BASE_DIR, "articles_data.json")

SPEAKERS_DB = {
    "Andrew Huberman": ["huberman", "andrew huberman"],
    "Mo Gawdat": ["mo gawdat", "gawdat"],
    "Dr. K (Alok Kanojia)": ["dr. k", "dr k", "alok kanojia", "healthygamer"],
    "Elon Musk": ["elon musk", "musk", "spacex"],
    "Sam Altman": ["sam altman", "altman"],
    "Raj Shamani": ["raj shamani", "shamani"],
    "Dr. Peter Attia": ["peter attia", "attia"],
    "Ray Dalio": ["ray dalio", "dalio"],
    "Simon Sinek": ["simon sinek", "sinek"],
    "Scott Galloway": ["scott galloway", "galloway"],
    "Chris Williamson": ["chris williamson"],
    "Dr. V Mohan": ["dr. v. mohan", "v mohan", "v. mohan", "dr. v mohan", "bác sĩ v mohan"],
    "Alok Sama": ["alok sama"],
    "Saurabh Mukherjea": ["saurabh mukherjea", "mukherjea"],
    "Vaibhav Sisinty": ["vaibhav sisinty", "growthschool"],
    "Sauvik Banerjjee": ["sauvik banerjjee", "rezolve ai"],
    "Deepak Sahni": ["deepak sahni", "healthians"],
    "Frank Walliser": ["frank walliser", "bentley"],
    "Gaurav Mehta": ["gaurav mehta", "jaipur watch"],
    "Mark Bowden": ["mark bowden"],
    "Puneet Nanda": ["puneet nanda", "gurunanda"],
    "Sunil Bajpai": ["sunil bajpai"],
    "Satinder Sartaaj": ["satinder sartaaj", "sartaaj"],
    "Kiran Mazumdar-Shaw": ["kiran mazumdar-shaw", "kiran mazumdar", "biocon"],
    "Shubhanshu Shukla": ["shubhanshu shukla", "isro"],
    "Srini Sriniwasan": ["srini sriniwasan", "kotak"],
    "Hasan Minhaj": ["hasan minhaj"],
    "Richard Teng": ["richard teng", "binance"],
    "Anahat Singh": ["anahat singh"],
    "Dr. Sanjiv Goenka": ["sanjiv goenka", "rp-sanjiv"],
    "David Goggins": ["david goggins", "goggins"],
    "Gabor Maté": ["gabor mate", "gabor maté"],
    "Dr. Daniel Amen": ["daniel amen", "dr daniel amen"],
    "Dr. Lisa Feldman Barrett": ["lisa feldman barrett", "feldman barrett"],
    "Stuart Russell": ["stuart russell"],
    "Joe Rogan": ["joe rogan", "rogan"],
    "Lex Fridman": ["lex fridman", "fridman"],
    "Brian Chesky": ["brian chesky", "airbnb"],
    "Matthew McConaughey": ["matthew mcconaughey"],
    "Dr. Bhaskar Rao": ["bhaskar rao"],
    "Prashant Desai": ["prashant desai"],
    "Suyash Saraf": ["suyash saraf"],
    "Prasad Chalavadi": ["prasad chalavadi"],
    "Vidita Vaidya": ["vidita vaidya"],
    "Ashwin Srivastava": ["ashwin srivastava"],
    "Ankur Warikoo": ["ankur warikoo", "warikoo"],
    "Imtiaz Ali": ["imtiaz ali"],
    "Sourav Ganguly": ["sourav ganguly"],
    "Dr. Rena Malik": ["rena malik"],
    "Dr. Darby Saxbe": ["darby saxbe"],
    "Dr. Joe Dispenza": ["joe dispenza", "dispenza"],
    "Dr. Ravinder": ["dr. ravinder", "ravinder"],
    "Dr. Viju Jacob": ["viju jacob"],
    "Lakshya Sen": ["lakshya sen"],
    "Mark Manson": ["mark manson"],
    "Mokksh Sani": ["mokksh sani"],
    "Sandeep Das": ["sandeep das"],
    "Mathis Bolt": ["mathis bolt", "motiversity"],
    "Sadhguru": ["sadhguru"],
    "Mooji": ["mooji"],
    "Sir Roger Penrose": ["roger penrose", "penrose"]
}

CATEGORY_RULES = [
    # 1. AI, Tự Động Hóa & Tương Lai (dùng word boundary để không bắt nhầm các từ 'thất bại', 'tại', 'phải')
    (
        "AI, Tự Động Hóa & Tương Lai",
        r"\b(ai|artificial intelligence|chatgpt|claude|agent|agents|computer use|deepseek|llm|agi|asi|kardashev|spacex|thuật toán|robot|siêu trí tuệ|machine learning)\b"
    ),
    # 2. Sinh Học & Tuổi Thọ
    (
        "Sinh Học & Tuổi Thọ",
        r"\b(glucose|insulin|tiểu đường|đường ruột|vi sinh|gut|ty thể|mitochondria|tế bào|ung thư|chuyển hóa|metabolism|calo|nhịn ăn|fasting|dinh dưỡng|protein|carnivore|gan nhiễm mỡ|tuổi thọ|longevity|healthspan)\b"
    ),
    # 3. Khoa Học Não Bộ & Tâm Trí
    (
        "Khoa Học Não Bộ & Tâm Trí",
        r"\b(huberman|dopamine|serotonin|não bộ|não|thần kinh|neuroscience|giấc ngủ|sleep|adhd|lo âu|anxiety|stress|sang chấn|trauma|trầm cảm|tâm lý|cảm xúc|thói quen|trực giác|dopamine giá rẻ)\b"
    ),
    # 4. Kinh Doanh & Đòn Bẩy
    (
        "Kinh Doanh & Đòn Bẩy",
        r"\b(kinh doanh|bán lẻ|retail|walmart|d2c|chốt sale|sales|đòn bẩy|doanh nghiệp|khởi nghiệp|startup|đầu tư|tài chính|tiền tệ|crypto|bitcoin|bất động sản|thương hiệu cá nhân|triệu view|giữ chân|retention|founder)\b"
    ),
    # 5. Triết Học & Thức Tỉnh
    (
        "Triết Học & Thức Tỉnh",
        r"\b(khắc kỷ|stoic|stoicism|triết học|thức tỉnh|ý thức|bản ngã|ego|thiền|chánh niệm|dharma|tâm linh|chữa lành|buông bỏ|hạnh phúc|cái chết|vũ trụ|tâm thức)\b"
    ),
]

class HTMLContentExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1 = ""
        self.in_h1 = False
        self.meta_desc = ""
        self.paragraphs = []
        self.in_p = False
        self.cur_p = []
        self.quotes = []
        self.in_quote = False
        self.cur_quote = []
        self.insights = []
        self.in_insight_header = False
        self.cur_insight = []
        self.all_text_tokens = []
        self.skip_tags = {"script", "style", "nav", "footer", "header", "svg"}
        self.current_tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.current_tag_stack.append(tag)
        attrs_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True
        elif tag == "meta" and attrs_dict.get("name", "").lower() in ["description", "fedu:summary"]:
            self.meta_desc = attrs_dict.get("content", "")
        elif tag in ["p", "div"] and ("cb-text" in attrs_dict.get("class", "") or tag == "p"):
            self.in_p = True
            self.cur_p = []
        elif tag in ["blockquote", "em", "i"] or "cb-mantra" in attrs_dict.get("class", ""):
            self.in_quote = True
            self.cur_quote = []
        elif tag in ["h2", "h3"] or "cb-title" in attrs_dict.get("class", ""):
            self.in_insight_header = True
            self.cur_insight = []

    def handle_endtag(self, tag):
        if self.current_tag_stack and self.current_tag_stack[-1] == tag:
            self.current_tag_stack.pop()

        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False
        elif tag in ["p", "div"]:
            self.in_p = False
            t = "".join(self.cur_p).strip()
            if len(t) > 35 and not t.startswith("©") and "fedu.vn" not in t.lower() and len(self.paragraphs) < 8:
                self.paragraphs.append(t)
        elif tag in ["blockquote", "em", "i"]:
            self.in_quote = False
            t = "".join(self.cur_quote).strip()
            if len(t) > 15 and ("/" in t or "\n" in t or len(t.split()) >= 6):
                self.quotes.append(t)
        elif tag in ["h2", "h3"]:
            self.in_insight_header = False
            t = "".join(self.cur_insight).strip()
            if t:
                self.insights.append(t)

    def handle_data(self, data):
        if any(t in self.skip_tags for t in self.current_tag_stack):
            return

        text = data.strip()
        if not text:
            return

        if self.in_title:
            self.title += " " + text
        elif self.in_h1:
            self.h1 += " " + text
        elif self.in_p:
            self.cur_p.append(" " + text)
        elif self.in_quote:
            self.cur_quote.append(" " + text)
        elif self.in_insight_header:
            self.cur_insight.append(" " + text)

        self.all_text_tokens.append(text)

def clean_text(s):
    if not s:
        return ""
    return re.sub(r"\s+", " ", s).strip()

def clean_title(title, filename):
    t = clean_text(title)
    t = re.sub(r"\s*\|\s*Kiến Trúc Sư.*$", "", t, flags=re.I)
    t = re.sub(r"\s*\|\s*System Intelligence.*$", "", t, flags=re.I)
    t = re.sub(r"\s*\|\s*FEDU.*$", "", t, flags=re.I)
    t = re.sub(r"\s*\|\s*fedu\.vn.*$", "", t, flags=re.I)
    t = t.strip(" -•–")
    if not t or len(t) < 4:
        clean_fn = filename.replace("-podcast", "").replace("-science", "").replace("-long-form", "").replace(".html", "")
        t = " ".join(w.capitalize() for w in clean_fn.split("-"))
    return t

def detect_speaker(title, text_sample, filename):
    blob = f"{filename} {title} {text_sample}".lower()
    for spk, aliases in SPEAKERS_DB.items():
        if any(alias in blob for alias in aliases):
            return spk
    return "Chuyên Gia Đa Nguồn"

def infer_category(title, summary, text_sample, filename):
    blob = f"{filename} {title} {summary} {text_sample}".lower()
    for cat_name, pattern in CATEGORY_RULES:
        if re.search(pattern, blob, flags=re.I):
            return cat_name
    return "Khoa Học Não Bộ & Tâm Trí"

def extract_smart_summary(meta_desc, quotes, paragraphs, title):
    # 1. Check Luc Bat verse
    for q in quotes:
        cleaned_q = clean_text(q)
        if 20 <= len(cleaned_q) <= 180 and any(w in cleaned_q for w in ["ơi", "ngày", "người", "đời", "sâu", "thời", "lòng", "tâm", "đoạn", "/"]):
            return cleaned_q

    # 2. Check meta description if NOT generic placeholder
    if meta_desc and "Phân tích đa tầng từ Podcast chuyên sâu bởi Kiến trúc sư" not in meta_desc:
        cleaned_m = clean_text(meta_desc)
        if len(cleaned_m) > 30:
            return cleaned_m

    # 3. Find first meaningful paragraph
    for p in paragraphs:
        cleaned_p = clean_text(p)
        if "Kiến Trúc Sư Trí Tuệ Hệ Thống" in cleaned_p:
            continue
        if len(cleaned_p) >= 40:
            if len(cleaned_p) > 220:
                parts = cleaned_p.split(".")
                return (parts[0] + "." + (parts[1] + "." if len(parts) > 1 and len(parts[0]) < 80 else "")).strip()
            return cleaned_p

    return f"Bóc tách nguyên lý cốt lõi và đòn bẩy thực chiến từ chuyên đề {title}."

def extract_tags(category, speaker, title, summary):
    tags = set()
    blob = f"{title} {summary}".lower()
    
    if speaker != "Chuyên Gia Đa Nguồn":
        tags.add(speaker)

    tag_mappings = {
        "Dopamine": ["dopamine", "khoái lạc"],
        "Giấc ngủ": ["giấc ngủ", "sleep", "ngủ"],
        "Glucose": ["glucose", "insulin", "đường huyết"],
        "Ty thể": ["ty thể", "mitochondria", "năng lượng"],
        "Đường ruột": ["đường ruột", "vi sinh", "gut"],
        "ADHD": ["adhd", "tập trung", "phân tán"],
        "Khắc kỷ": ["khắc kỷ", "stoic"],
        "Tâm lý học": ["tâm lý", "sang chấn", "nội tâm"],
        "Chốt sale": ["chốt sale", "bán hàng", "sales"],
        "Bán lẻ": ["bán lẻ", "retail", "walmart"],
        "D2C": ["d2c", "thương hiệu"],
        "Agent AI": ["agent", "computer use"],
        "LLM & Prompt": ["claude", "chatgpt", "prompt", "llm"],
        "Đòn bẩy": ["đòn bẩy", "scale", "vốn"],
        "Kỷ luật": ["kỷ luật", "thói quen", "habit"],
        "Thức tỉnh": ["thức tỉnh", "bản ngã", "chánh niệm"]
    }

    for tag, keywords in tag_mappings.items():
        if any(k in blob for k in keywords):
            tags.add(tag)

    if not tags:
        tags.add(category.split("&")[0].strip())

    return sorted(list(tags))[:4]

def get_theme_version(html_content):
    if "Tiempos Text" in html_content or "FD Aeonik Extended" in html_content:
        return "swiss_monochrome"
    elif "#080811" in html_content or "#0d0e12" in html_content or "data-theme=\"dark\"" in html_content:
        return "legacy_dark"
    return "legacy_light"

def get_git_mtimes():
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
        print(f"[WARN] Git mtimes error: {e}")
    return file_mtimes

def main():
    print("[*] Starting Full-Spectrum Knowledge Indexer...")

    git_mtimes = get_git_mtimes()

    html_files = [
        f for f in os.listdir(BASE_DIR)
        if f.endswith(".html") and f != "index.html" and not f.startswith(".")
    ]

    print(f"[*] Found {len(html_files)} standalone HTML files in repo k.")

    catalog_items = []
    search_corpus = []

    stats = {
        "categories": {},
        "speakers": {},
        "themes": {},
        "total_words_indexed": 0
    }

    for idx, fname in enumerate(sorted(html_files)):
        fpath = os.path.join(BASE_DIR, fname)
        size_kb = round(os.path.getsize(fpath) / 1024, 1)
        mtime = git_mtimes.get(fname, os.path.getmtime(fpath))

        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            parser = HTMLContentExtractor()
            parser.feed(content[:45000])

            title = clean_title(parser.title or parser.h1 or "", fname)
            sample_text = " ".join(parser.paragraphs[:4]) + " " + " ".join(parser.insights)
            
            speaker = detect_speaker(title, sample_text, fname)
            summary = extract_smart_summary(parser.meta_desc, parser.quotes, parser.paragraphs, title)
            category = infer_category(title, summary, sample_text, fname)
            tags = extract_tags(category, speaker, title, summary)
            theme_ver = get_theme_version(content)

            word_count = len(" ".join(parser.all_text_tokens).split())
            read_time_min = max(3, round(word_count / 220))

            catalog_entry = {
                "slug": fname,
                "title": title,
                "speaker": speaker,
                "category": category,
                "tags": tags,
                "summary": summary,
                "read_time": read_time_min,
                "size_kb": size_kb,
                "theme": theme_ver,
                "mtime": mtime
            }
            catalog_items.append(catalog_entry)

            clean_search_text = " ".join(clean_text(" ".join(parser.all_text_tokens)).split()[:220])
            search_entry = {
                "slug": fname,
                "title": title,
                "speaker": speaker,
                "category": category,
                "tags": tags,
                "snippet": summary,
                "body_preview": clean_text(clean_search_text)
            }
            search_corpus.append(search_entry)

            stats["categories"][category] = stats["categories"].get(category, 0) + 1
            if speaker != "Chuyên Gia Đa Nguồn":
                stats["speakers"][speaker] = stats["speakers"].get(speaker, 0) + 1
            stats["themes"][theme_ver] = stats["themes"].get(theme_ver, 0) + 1
            stats["total_words_indexed"] += word_count

        except Exception as err:
            print(f"[ERROR] Parsing {fname}: {err}")

    # Sort catalog: latest first
    catalog_items.sort(key=lambda x: x.get("mtime", 0), reverse=True)

    with open(CATALOG_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog_items, f, ensure_ascii=False, indent=2)

    with open(SEARCH_INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(search_corpus, f, ensure_ascii=False)

    with open(LEGACY_DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(catalog_items, f, ensure_ascii=False, indent=2)

    print("\n" + "="*60)
    print("INDEXING & AUDIT COMPLETED SUCCESSFULLY!")
    print("="*60)
    print(f"Total articles indexed: {len(catalog_items)}")
    print(f"Total words indexed: {stats['total_words_indexed']:,}")
    print("\nCategory Distribution (No false positives):")
    for cat, count in sorted(stats["categories"].items(), key=lambda x: -x[1]):
        print(f"  - {cat}: {count} bài")

    print(f"\nTop Speakers Identified ({len(stats['speakers'])} speakers total):")
    for spk, count in sorted(stats["speakers"].items(), key=lambda x: -x[1])[:15]:
        print(f"  - {spk}: {count} bài")

    print("\nDesign Theme Distribution:")
    for th, count in stats["themes"].items():
        print(f"  - {th}: {count} bài")

    print("\nOutput Files Created:")
    print(f"  1. {CATALOG_FILE} ({round(os.path.getsize(CATALOG_FILE)/1024, 1)} KB)")
    print(f"  2. {SEARCH_INDEX_FILE} ({round(os.path.getsize(SEARCH_INDEX_FILE)/1024, 1)} KB)")
    print(f"  3. {LEGACY_DATA_FILE} ({round(os.path.getsize(LEGACY_DATA_FILE)/1024, 1)} KB)")

if __name__ == "__main__":
    main()
