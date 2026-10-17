import re

with open("/tmp/logic30_raw.txt", "r") as f:
    text = f.read()

phan1_blocks = re.findall(r'Phần 1: HỆ THỐNG HÓA CÂU HỎI CỦA TÔI\n+(.*?)(?=\nPhần 2:|\Z)', text, re.DOTALL | re.IGNORECASE)
phan1_items = []
if phan1_blocks:
    for line in phan1_blocks[0].split('\n'):
        line = line.strip()
        if line.startswith('*') or (line and line[0].isdigit() and line[1:3] in ['. ', ') ']):
            item = line.lstrip('*)0123456789. ').strip()
            item = re.sub(r'^\*\*', '', item)
            item = item.replace('**', '')
            if item:
                phan1_items.append(item)

qa_blocks = []
current_qa = None

lines = text.split('\n')
for line in lines:
    line = line.strip()
    if re.match(r'^\[Ẩn dụ', line, re.IGNORECASE) or re.match(r'^\[Ví dụ', line, re.IGNORECASE) or re.match(r'^\[Khái niệm', line, re.IGNORECASE) or re.match(r'^\[Dẫn chứng', line, re.IGNORECASE):
        if current_qa and 'h' in current_qa and 'd' in current_qa:
            qa_blocks.append(current_qa)
        title = line.strip('[]*')
        current_qa = {'title': title, 'h': '', 'd': '', 't': []}
    elif current_qa is not None:
        if line.startswith('Hỏi:'):
            current_qa['h'] = line[4:].strip().replace('**', '')
        elif line.startswith('Đáp:'):
            current_qa['d'] = line[4:].strip().replace('**', '')
        elif line.startswith('Thơ:'):
            pass 
        elif line and current_qa['h'] and current_qa['d']:
            if not line.startswith('---') and not line.startswith('Phần') and not line.startswith('Dưới đây'):
                 current_qa['t'].append(line.replace('**', ''))

if current_qa and 'h' in current_qa and 'd' in current_qa:
    qa_blocks.append(current_qa)

unique_qas = []
seen_titles = set()
for qa in qa_blocks:
    if qa['title'] not in seen_titles:
        seen_titles.add(qa['title'])
        unique_qas.append(qa)

toc_html = f"""  <li style="margin-top: 14px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 11.5px; text-transform: uppercase;">
    <a class="ink-toc-link" style="font-weight: 700; color: var(--ink-text);" href="#phan-1">Phần 1: HỆ THỐNG HÓA CÂU HỎI CỦA TÔI</a>
  </li>
  <li style="margin-top: 14px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 11.5px; text-transform: uppercase;">
    <a class="ink-toc-link" style="font-weight: 700; color: var(--ink-text);" href="#phan-2">Phần 2: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG (Q&A)</a>
  </li>\n"""

for idx, qa in enumerate(unique_qas):
    title = qa['title']
    toc_title = title.replace('Ẩn dụ/Ví dụ:', 'Ẩn dụ:').replace('Khái niệm:', 'Khái niệm:').strip()
    toc_html += f"""  <li class="ink-toc-item" style="margin-bottom: 2px;">
    <a class="ink-toc-link" href="#p2_q{idx+1}" style="font-size: 12.5px; line-height: 1.4; padding: 6px 12px; display: block;">{idx+1}. {toc_title}</a>
  </li>\n"""

content_html = f"""<h1 class="is-long" id="phan-1">Phần 1: HỆ THỐNG HÓA CÂU HỎI CỦA TÔI</h1>
<p>Dưới lăng kính phản biện tàn nhẫn, toàn bộ sự hoang mang trong tâm trí bạn được bóc tách và chưng cất thành {len(phan1_items)} vấn đề cốt lõi sau:</p>
<ol style='font-size: 19.5px; line-height: 1.8; color: var(--ink-text); padding-left: 20px; margin-bottom: 40px;'>
"""
for item in phan1_items:
    content_html += f"  <li style='margin-bottom: 16px;'>{item}</li>\n"
content_html += "</ol>\n\n"

content_html += """<h1 class="is-long" id="phan-2">Phần 2: HỎI ĐÁP ĐẬP TAN LẦM TƯỞNG (Q&A)</h1>
<hr style="margin: 2rem 0 3rem; border: none; border-top: 1px solid var(--ink-border);"/>
"""

for idx, qa in enumerate(unique_qas):
    title = qa['title']
    h = qa['h']
    d = qa['d']
    t_lines = qa['t']
    
    content_html += f"""
<div class="dialogue-turn" id="p2_q{idx+1}">
  <h2 class="dialogue-prompt">❓ [{title}]<br/><span style="font-weight: 500; font-size: 17px; color: var(--ink-muted);">Hỏi:</span> {h}</h2>
  <div class="dialogue-response">
    <p><strong>🔪 Đáp:</strong> {d}</p>
"""
    if t_lines:
        content_html += "    <blockquote>\n      <p><strong>📜 Thơ:</strong><br/>\n"
        for i, line in enumerate(t_lines):
            if line.strip():
                words = line.strip().split()
                if words:
                    words[-1] = f"<strong>{words[-1]}</strong>"
                line_formatted = " ".join(words)
                content_html += f"      {line_formatted}" + ("<br/>\n" if i < len(t_lines)-1 else "\n")
        content_html += "      </p>\n    </blockquote>\n"
    content_html += "  </div>\n</div>\n"

with open("logic29.html", "r") as f:
    template = f.read()

template = template.replace('<title>Logic 29', '<title>Logic 30')
template = template.replace('Logic 29', 'Logic 30')
template = template.replace('>29</text>', '>30</text>')

start_toc = template.find('<li style="margin-top: 14px; font-weight: bold; color: var(--ink-text); font-family: var(--font-display-long); font-size: 11.5px; text-transform: uppercase;">\n    <a class="ink-toc-link" style="font-weight: 700; color: var(--ink-text);" href="#phan-1">Phần 1')
end_toc = template.find('</ul>\n    </div>\n    <div class="ink-right-col" id="content">')
if start_toc != -1 and end_toc != -1:
    template = template[:start_toc] + toc_html + template[end_toc:]

start_content = template.find('<h1 class="is-long" id="top">Phần 1: HỆ THỐNG HÓA CÂU HỎI CỦA TÔI</h1>')
if start_content == -1:
    start_content = template.find('<h1 class="is-long" id="phan-1">')

end_content = template.rfind('</div>\n    </div>\n\n<script>')
if end_content == -1:
    end_content = template.rfind('</div>\n  </div>\n\n<script>')
if end_content == -1:
    end_content = template.rfind('<script>') - 20 # Just cut before <script> somewhere

if start_content != -1 and end_content != -1:
    # Just to be safe, find the exact '</div>' sequence before script
    match = re.search(r'</div>\s*</div>\s*<script>', template[start_content:])
    if match:
        end_content = start_content + match.start()
        
    new_html = template[:start_content] + content_html + template[end_content:]
    with open("logic30.html", "w") as f:
        f.write(new_html)
    print("Successfully created logic30.html")
else:
    print("Could not find content sections")
