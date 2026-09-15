import os
import glob
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup

def generate():
    files = glob.glob("*.html")
    exclude = ["index.html", "404.html", "rajchannel.html", "fix-url.html", "skills.html"]
    posts = []

    for f in files:
        if f in exclude:
            continue
            
        filepath = os.path.join(os.getcwd(), f)
        stat = os.stat(filepath)
        mod_time = datetime.fromtimestamp(stat.st_mtime).isoformat()
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            soup = BeautifulSoup(content, 'html.parser')
            title_tag = soup.find('title')
            title = title_tag.text.strip() if title_tag else f.replace('.html', '').replace('-', ' ').title()
            
            # Simple excerpt (first paragraph with text > 50 chars)
            excerpt = "Bài viết chuyên sâu từ kho dữ liệu Antigravity."
            for p in soup.find_all('p'):
                text = p.text.strip()
                if len(text) > 50:
                    excerpt = text[:150] + "..."
                    break
                    
            # Determine category based on filename keywords
            fname_lower = f.lower()
            if 'broll' in fname_lower or 'quay' in fname_lower:
                cat = "broll"
                cat_label = "🎬 B-Roll & Cảnh Trám"
            elif 'podcast' in fname_lower:
                cat = "science"
                cat_label = "🧠 Tâm Lý & Não Bộ"
            elif 'science' in fname_lower:
                cat = "science"
                cat_label = "🧠 Khoa Học"
            else:
                cat = "other"
                cat_label = "📌 Bài Viết"
                
        posts.append({
            "filename": f,
            "title": title,
            "excerpt": excerpt,
            "category_key": cat,
            "category_label": cat_label,
            "cover_image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80",
            "updated_at": mod_time,
            "read_time": "5 phút đọc",
            "file_size_kb": round(stat.st_size / 1024)
        })

    # Sort by updated_at descending
    posts.sort(key=lambda x: x['updated_at'], reverse=True)

    with open('posts-manifest.json', 'w', encoding='utf-8') as out:
        json.dump({"posts": posts}, out, ensure_ascii=False, indent=2)
        
    print(f"Generated manifest with {len(posts)} posts.")

if __name__ == "__main__":
    generate()
