import re

with open('/tmp/logic29_clean.txt', 'r') as f:
    text = f.read()

# Split into parts
parts = text.split("### Phần 2: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG (Q&A)")
part1 = parts[0].strip()
part2 = parts[1].strip() if len(parts) > 1 else ""

# Extract questions from Part 1
p1_lines = part1.split('\n')
p1_content = []
for line in p1_lines:
    if line.startswith("### Phần 1:"):
        continue
    if "tạo file logic29.html" in line:
        continue
    p1_content.append(line)
p1_text = '\n'.join(p1_content).strip()

# Convert p1_text into HTML
html_p1 = ""
for p in p1_text.split('\n\n'):
    p = p.strip()
    if not p: continue
    if p.startswith("1."):
        html_p1 += "<ol style='font-size: 19.5px; line-height: 1.8; color: var(--ink-text); padding-left: 20px; margin-bottom: 40px;'>\n"
        for item in p.split('\n'):
            item = item.strip()
            if re.match(r'^\d+\.', item):
                item = re.sub(r'^\d+\.\s*', '', item)
                item = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', item)
                html_p1 += f"  <li style='margin-bottom: 16px;'>{item}</li>\n"
        html_p1 += "</ol>\n"
    else:
        p = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', p)
        html_p1 += f"<p>{p}</p>\n"

# Process Part 2 Q&A blocks
q_blocks = []
current_block = []
for line in part2.split('\n'):
    if line.startswith("**[") or line.startswith("["):
        if current_block:
            q_blocks.append('\n'.join(current_block))
            current_block = []
    current_block.append(line)
if current_block:
    q_blocks.append('\n'.join(current_block))

q_blocks = [b.strip() for b in q_blocks if b.strip()]

qa_data = []
for b in q_blocks:
    lines = b.split('\n')
    title = lines[0].strip().replace('**', '')
    if title.startswith('[') and title.endswith(']'):
        title = title[1:-1]
    
    hoi = ""
    dap = ""
    tho = []
    
    state = None
    for line in lines[1:]:
        line = line.strip()
        if line.startswith('Hỏi:'):
            hoi = line[4:].strip()
            state = 'hoi'
        elif line.startswith('Đáp:'):
            dap = line[4:].strip()
            state = 'dap'
        elif line.startswith('Thơ:'):
            state = 'tho'
        else:
            if state == 'tho' and line:
                tho.append(line)
            elif state == 'hoi' and line:
                hoi += " " + line
            elif state == 'dap' and line:
                dap += " " + line
                
    qa_data.append({
        'title': title,
        'hoi': hoi,
        'dap': dap,
        'tho': tho
    })

# Read template
with open('logic28.html', 'r') as f:
    template = f.read()

head_part = template.split('</head>')[0]
css = template.split('<style>')[1].split('</style>')[0]

head_part = head_part.replace('Logic 28:', 'Logic 29:').replace('LOGICKENH #28', 'LOGICKENH #29')
head_part = head_part.replace('%3E28%3C', '%3E29%3C')

html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
{head_part.split('<head>')[1]}
</style>
<style>
{css}
</style>
</head>
<body>

<!-- MOBILE NAV -->
<div class="ink-mobile-nav">
<a class="ink-brand" href="logickenh.html">LOGICKENH #29</a>
<button class="ink-menu-btn" onclick="document.querySelector('.ink-sidebar').classList.add('is-open'); document.querySelector('.ink-overlay').classList.add('is-open');">MỤC LỤC</button>
</div>

<!-- MOBILE OVERLAY -->
<div class="ink-overlay" onclick="document.querySelector('.ink-sidebar').classList.remove('is-open'); this.classList.remove('is-open');"></div>

<!-- SIDEBAR TOC -->
<aside class="ink-sidebar">
<div class="ink-sidebar-header" style="display: flex; justify-content: space-between; align-items: center;">
<a class="ink-brand" href="logickenh.html">LOGICKENH #29</a>
<button class="ink-close-btn" onclick="document.querySelector('.ink-sidebar').classList.remove('is-open'); document.querySelector('.ink-overlay').classList.remove('is-open');">✕</button>
</div>

<div class="ink-search-box">
  <input type="text" id="inkSearch" class="ink-search-input" placeholder="🔍 Lọc câu hỏi nhanh..." onkeyup="filterTOC()">
</div>

<div class="ink-toc-title">CÁC CHƯƠNG CHÍNH</div>
<ul class="ink-toc-list" id="inkTocList">
  <li style="margin-top: 14px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 11.5px; text-transform: uppercase;">
    <a class="ink-toc-link" style="font-weight: 700; color: var(--ink-text);" href="#phan-1">Phần 1: HỆ THỐNG HÓA CÂU HỎI CỦA TÔI</a>
  </li>
  <li style="margin-top: 14px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 11.5px; text-transform: uppercase;">
    <a class="ink-toc-link" style="font-weight: 700; color: var(--ink-text);" href="#phan-2">Phần 2: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG (Q&A)</a>
  </li>
"""

for i, qa in enumerate(qa_data):
    html += f"""  <li class="ink-toc-item" style="margin-bottom: 2px;">
    <a class="ink-toc-link" href="#p2_q{i+1}" style="font-size: 12.5px; line-height: 1.4; padding: 6px 12px; display: block;">{i+1}. {qa['title']}</a>
  </li>
"""

html += """</ul>
<div style="margin-top: 30px; font-size: 12px; color: var(--ink-muted); text-align: center; border-top: 1px solid var(--ink-border); padding-top: 15px;">
    <i>Sử dụng mũi khoan Laser và Mỏ neo giấy bút để định tuyến thần kinh.</i>
</div>
</aside>

<main class="ink-main-wrapper">
<article class="ink-content ink-mode-dialogue">

<div class="ink-meta">
<span class="ink-badge">LOGIC #29</span>
<span>Nguyễn Việt</span>
<span>•</span>
<span>Hệ Thống Hóa Câu Hỏi & Đập Tan Lầm Tưởng</span>
</div>

<button class="ink-copy-btn" onclick="copyAll()">📋 Copy Toàn Bộ Bài Viết</button>

<h1 class="is-long" id="top">Phần 1: HỆ THỐNG HÓA CÂU HỎI CỦA TÔI</h1>
"""
html += html_p1
html += """
<hr style="margin: 3rem 0; border: none; border-top: 2px solid var(--ink-border);"/>

<h1 class="is-long" id="phan-2">Phần 2: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG (Q&A)</h1>
<hr style="margin: 2rem 0 3rem; border: none; border-top: 1px solid var(--ink-border);"/>
"""

for i, qa in enumerate(qa_data):
    tho_html = ""
    if qa['tho']:
        tho_lines = [re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', line) for line in qa['tho']]
        tho_html = f"""    <blockquote>
      <p><strong>📜 Thơ:</strong><br/>
      {'<br/>\n      '.join(tho_lines)}</p>
    </blockquote>"""
    
    html += f"""
<div class="dialogue-turn" id="p2_q{i+1}">
  <h2 class="dialogue-prompt">❓ [{qa['title']}]<br/><span style="font-weight: 500; font-size: 17px; color: var(--ink-muted);">Hỏi:</span> {qa['hoi']}</h2>
  <div class="dialogue-response">
    <p><strong>🔪 Đáp:</strong> {qa['dap']}</p>
{tho_html}
  </div>
</div>
"""

scripts = template.split('</article>')[1]
html += "</article>\n" + scripts

with open('logic29.html', 'w') as f:
    f.write(html)
print(f"Generated logic29.html with {len(qa_data)} questions.")
