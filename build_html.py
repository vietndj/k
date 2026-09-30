import re
import os

FILES = [
    "/Users/vietmac/Documents/CODE/Kich ban quang cao/SHOT_LIST_QUAY_LAI.md",
    "/Users/vietmac/Documents/CODE/Kich ban quang cao/SHOT_LIST_KY_NGUYEN.md",
    "/Users/vietmac/Documents/CODE/Kich ban quang cao/CANH_VAN_NANG_5_MOI.md",
    "/Users/vietmac/Documents/CODE/Kich ban quang cao/CANH_BAN_CONG_3H.md"
]

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def markdown_to_html(md_text):
    html_lines = []
    toc = []
    
    lines = md_text.split('\n')
    i = 0
    in_table = False
    table_headers = []
    
    in_scene = False
    in_spec_block = False
    in_timeline = False
    in_ul = False
    
    def close_blocks():
        nonlocal in_spec_block, in_timeline, in_ul, html_lines
        if in_timeline:
            html_lines.append('</div>')
            in_timeline = False
        if in_spec_block:
            html_lines.append('</div>')
            in_spec_block = False
        if in_ul:
            html_lines.append('</ul>')
            in_ul = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Headings
        h_match = re.match(r'^(#{1,3})\s+(.*)', stripped)
        if h_match:
            close_blocks()
            level = len(h_match.group(1))
            title = h_match.group(2)
            title_clean = re.sub(r'\*\*(.*?)\*\*', r'\1', title)
            title_clean = re.sub(r'\[(.*?)\]', r'\1', title_clean)
            
            # check if scene card
            scene_match = re.match(r'\*\*(CẢNH.*?[^\*]*)\*\*\s+`?(\[.*?\])?(.*)`?', title)
            if not scene_match:
                scene_match = re.match(r'\*\*(CẢNH.*?[^\*]*)\*\*(.*)', title)
            if not scene_match and title.startswith('**CẢNH'):
                scene_match = re.match(r'\*\*(CẢNH.*?)\*\*\s*(.*)', title)
                
            if title.startswith('**CẢNH') and scene_match:
                if in_scene:
                    html_lines.append('</div>')
                in_scene = True
                
                scene_num = scene_match.group(1)
                rest = scene_match.group(2) if len(scene_match.groups()) == 2 else f"{scene_match.group(2) or ''} {scene_match.group(3) or ''}"
                
                badge_type = ""
                if '[' in rest and ']' in rest:
                    t_match = re.search(r'(\[.*?\])', rest)
                    if t_match:
                        badge_type = f'<span class="shot-type-badge">{t_match.group(1)}</span>'
                        rest = rest.replace(t_match.group(1), '')
                
                rest = rest.replace('`', '').strip()
                html_lines.append(f'<div class="scene-card">')
                html_lines.append(f'<div class="scene-badge">{scene_num}</div> {badge_type} <strong>{rest}</strong>')
                i += 1
                continue
                
            sid = slugify(title_clean)
            if level == 2:
                toc.append({'level': 2, 'title': title_clean, 'id': sid})
            elif level == 3:
                toc.append({'level': 3, 'title': title_clean, 'id': sid})
            html_lines.append(f'<h{level} id="{sid}">{title_clean}</h{level}>')
            i += 1
            continue

        # Scene titles that are not headers (e.g. bold text)
        if stripped.startswith('**CẢNH'):
            close_blocks()
            scene_match = re.match(r'\*\*(CẢNH.*?[^\*]*)\*\*\s+`?(\[.*?\])?(.*)`?', stripped)
            if not scene_match:
                scene_match = re.match(r'\*\*(CẢNH.*?[^\*]*)\*\*(.*)', stripped)
            if scene_match:
                if in_scene:
                    html_lines.append('</div>')
                in_scene = True
                scene_num = scene_match.group(1)
                rest = scene_match.group(2) if len(scene_match.groups()) == 2 else f"{scene_match.group(2) or ''} {scene_match.group(3) or ''}"
                
                badge_type = ""
                if '[' in rest and ']' in rest:
                    t_match = re.search(r'(\[.*?\])', rest)
                    if t_match:
                        badge_type = f'<span class="shot-type-badge">{t_match.group(1)}</span>'
                        rest = rest.replace(t_match.group(1), '')
                
                rest = rest.replace('`', '').strip()
                html_lines.append(f'<div class="scene-card">')
                html_lines.append(f'<div><span class="scene-badge">{scene_num}</span> {badge_type} <strong>{rest}</strong></div>')
                i += 1
                continue

        # Blockquote
        if stripped.startswith('>'):
            close_blocks()
            bq_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                bq_lines.append(lines[i].strip()[1:].strip())
                i += 1
            html_lines.append('<blockquote>' + '<br>'.join(bq_lines) + '</blockquote>')
            continue

        # Table
        if stripped.startswith('|') and '|' in stripped:
            close_blocks()
            html_lines.append('<table>')
            # Header
            headers = [x.strip() for x in stripped.split('|') if x.strip()]
            html_lines.append('<tr>' + ''.join(f'<th>{h}</th>' for h in headers) + '</tr>')
            i += 1
            if i < len(lines) and lines[i].strip().startswith('|') and '-' in lines[i]:
                i += 1 # skip separator
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [x.strip() for x in lines[i].strip().split('|') if x.strip() or x == '']
                # remove first and last empty elements if they exist due to split
                if lines[i].strip().startswith('|'):
                    cells = lines[i].strip()[1:-1].split('|')
                cells = [c.strip() for c in cells]
                html_lines.append('<tr>' + ''.join(f'<td>{c}</td>' for c in cells) + '</tr>')
                i += 1
            html_lines.append('</table>')
            continue

        # Specs & Timeline (List items)
        if stripped.startswith('- **'):
            if not in_spec_block and not in_timeline and in_scene:
                html_lines.append('<div class="spec-block">')
                in_spec_block = True
            
            match = re.match(r'-\s+\*\*(.*?)\*\*(.*)', stripped)
            if match:
                label = match.group(1)
                val = match.group(2).strip()
                if val.startswith(':'):
                    val = val[1:].strip()
                
                if 'Action' in label:
                    if in_spec_block:
                        html_lines.append('</div>')
                        in_spec_block = False
                    
                    html_lines.append('<div class="timeline">')
                    in_timeline = True
                    if val:
                        html_lines.append(f'<div class="tl-item"><p class="tl-desc"><strong>{label}:</strong> {val}</p></div>')
                    
                    # check next lines for numbered lists or timeline items
                    i += 1
                    while i < len(lines):
                        nxt = lines[i].strip()
                        if nxt.startswith('- [') or nxt.startswith('- ['): # - [0s-1s]: ...
                            tl_match = re.match(r'-\s+\[(.*?)\]:?\s*(.*)', nxt)
                            if tl_match:
                                time = tl_match.group(1)
                                desc = tl_match.group(2)
                                html_lines.append(f'<div class="tl-item"><span class="time-badge">{time}</span><p class="tl-desc">{desc}</p></div>')
                            else:
                                html_lines.append(f'<div class="tl-item"><p class="tl-desc">{nxt}</p></div>')
                        elif re.match(r'^\d+\.\s+', nxt):
                            desc = re.sub(r'^\d+\.\s+', '', nxt)
                            html_lines.append(f'<div class="tl-item"><p class="tl-desc">{desc}</p></div>')
                        elif nxt.startswith('- '):
                            break
                        elif nxt == '':
                            pass
                        else:
                            break
                        i += 1
                    continue
                else:
                    if in_timeline:
                        html_lines.append('</div>')
                        in_timeline = False
                        html_lines.append('<div class="spec-block">')
                        in_spec_block = True
                    
                    if not in_spec_block:
                        if in_ul:
                            html_lines.append(f'<li><strong>{label}</strong>: {val}</li>')
                        else:
                            html_lines.append('<ul>')
                            in_ul = True
                            html_lines.append(f'<li><strong>{label}</strong>: {val}</li>')
                    else:
                        html_lines.append(f'<div class="spec-row"><div class="spec-label">{label}</div><div class="spec-value">{val}</div></div>')
            else:
                if in_spec_block:
                    html_lines.append(f'<div class="spec-row"><div class="spec-value">{stripped[1:].strip()}</div></div>')
                elif in_timeline:
                    html_lines.append(f'<div class="tl-item"><p class="tl-desc">{stripped[1:].strip()}</p></div>')
                else:
                    if not in_ul:
                        html_lines.append('<ul>')
                        in_ul = True
                    html_lines.append(f'<li>{stripped[1:].strip()}</li>')
            i += 1
            continue
            
        # Normal list items
        if stripped.startswith('- '):
            if in_spec_block:
                html_lines.append('</div>')
                in_spec_block = False
            if in_timeline:
                html_lines.append('</div>')
                in_timeline = False
            if not in_ul:
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f'<li>{stripped[1:].strip()}</li>')
            i += 1
            continue

        # hr
        if stripped == '---':
            close_blocks()
            if in_scene:
                html_lines.append('</div>')
                in_scene = False
            html_lines.append('<hr>')
            i += 1
            continue
            
        # Empty line
        if stripped == '':
            close_blocks()
            i += 1
            continue
            
        # Paragraph
        close_blocks()
        
        # Link rendering
        stripped = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" class="text-blue-600 underline">\1</a>', stripped)
        # Bold
        stripped = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', stripped)
        # Italic
        stripped = re.sub(r'\*(.*?)\*', r'<em>\1</em>', stripped)
        
        html_lines.append(f'<p>{stripped}</p>')
        i += 1
        
    close_blocks()
    if in_scene:
        html_lines.append('</div>')
        
    return '\n'.join(html_lines), toc


def main():
    all_html = []
    all_toc = []
    
    for f in FILES:
        content = parse_markdown_file(f)
        html, toc = markdown_to_html(content)
        all_html.append(html)
        all_toc.extend(toc)
        
    # Generate TOC HTML
    toc_html = []
    for item in all_toc:
        if item['level'] == 2:
            toc_html.append(f'<li><a href="#{item["id"]}">{item["title"]}</a></li>')
            # optionally handle ul for sub-toc, but simpler flat list is ok or nested
        elif item['level'] == 3:
            toc_html.append(f'<ul class="sub-toc"><li><a href="#{item["id"]}">{item["title"]}</a></li></ul>')
            
    # Load images if any, the prompt mentioned adding specific images AI storyboard. Let's append them to the end or somewhere?
    # "Ảnh AI Storyboard → Giữ lại đúng src: ./assets/img/scene_1_balcony_1790756482763.jpg..."
    # If they are not in the text, we don't have to guess. The parser preserves any existing <img> or we can manually insert them if they match.
    
    full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Shot-List Master — 2 Kịch Bản</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
/* === FONTS === */
@font-face {{ font-family: 'FD Aeonik'; src: url('https://fedu.vn/k/fonts/FDAeonikRegular.ttf'); font-weight: 400; }}
@font-face {{ font-family: 'FD Aeonik'; src: url('https://fedu.vn/k/fonts/FDAeonikMedium.ttf'); font-weight: 600; }}
@font-face {{ font-family: 'FD Aeonik Extended'; src: url('https://fedu.vn/k/fonts/FDAeonikExtended-Bold.woff2'); font-weight: 700; }}
@font-face {{ font-family: 'Tiempos Text'; src: url('https://fedu.vn/k/fonts/FDTiemposText-Regular.woff2'); font-weight: 400; }}

html {{ scroll-behavior: auto; font-size: 16px; }}
body {{ background: #fff; color: #1a1a1a; margin: 0; display: flex; min-height: 100vh; }}

/* === LAYOUT === */
.sidebar {{ width: 260px; min-height: 100vh; background: #f8fafc; border-right: 1px solid #e2e8f0; padding: 32px 0; position: fixed; top: 0; left: 0; overflow-y: auto; }}
.sidebar-title {{ font-family: 'FD Aeonik', sans-serif; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.12em; color: #94a3b8; padding: 0 20px 16px; }}
.main {{ margin-left: 260px; padding: 56px 80px; max-width: 1060px; }}
.content-body {{ max-width: 760px; }}

/* === TOC === */
.toc {{ list-style: none; padding: 0; margin: 0; }}
.toc li {{ margin: 0; }}
.toc > li > a {{ display: block; padding: 8px 20px; font-family: 'FD Aeonik', sans-serif; font-size: 13.5px; font-weight: 500; color: #475569; text-decoration: none; border-left: 3px solid transparent; transition: none; }}
.toc > li > a:hover, .toc > li > a.active {{ color: #0f172a; background: #f1f5f9; border-left-color: #3b82f6; font-weight: 600; }}
.sub-toc {{ list-style: none; padding: 0; margin: 0; }}
.sub-toc li a {{ display: block; padding: 5px 20px 5px 36px; font-family: 'FD Aeonik', sans-serif; font-size: 12.5px; color: #94a3b8; text-decoration: none; }}
.sub-toc li a:hover, .sub-toc li a.active {{ color: #475569; }}

/* === TYPOGRAPHY === */
h1 {{ font-family: 'FD Aeonik Extended', sans-serif; font-size: 32px; font-weight: 700; text-transform: uppercase; letter-spacing: -0.02em; color: #0f172a; margin: 0 0 8px 0; }}
h2 {{ font-family: 'FD Aeonik', sans-serif; font-size: 24px; font-weight: 700; color: #0f172a; margin: 64px 0 24px; padding-bottom: 12px; border-bottom: 2px solid #e5e7eb; scroll-margin-top: 32px; }}
h3 {{ font-family: 'FD Aeonik', sans-serif; font-size: 20px; font-weight: 600; color: #0f172a; margin: 48px 0 20px; scroll-margin-top: 32px; }}
p {{ font-family: 'Tiempos Text', Georgia, serif; font-size: 18px; line-height: 1.78; color: #374151; margin: 0 0 22px; }}
blockquote {{ margin: 28px 0; padding: 16px 20px; background: #fffbeb; border-left: 4px solid #f59e0b; border-radius: 0 8px 8px 0; font-family: 'Tiempos Text', Georgia, serif; font-style: italic; color: #78350f; font-size: 17px; line-height: 1.7; }}
ul, ol {{ font-family: 'Tiempos Text', Georgia, serif; font-size: 17px; line-height: 1.7; color: #374151; padding-left: 24px; margin: 0 0 20px; }}
li {{ margin-bottom: 8px; }}
li strong {{ font-family: 'FD Aeonik', sans-serif; color: #1e293b; }}
hr {{ border: none; border-top: 1px solid #e5e7eb; margin: 48px 0; }}

/* === SPEC BLOCK === */
.spec-block {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px 24px; margin: 24px 0; display: flex; flex-direction: column; gap: 10px; }}
.spec-row {{ display: flex; gap: 16px; align-items: baseline; }}
.spec-label {{ font-family: 'FD Aeonik', sans-serif; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #64748b; min-width: 130px; flex-shrink: 0; }}
.spec-value {{ font-size: 15px; color: #1e293b; line-height: 1.55; font-family: -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif; }}

/* === TIMELINE === */
.timeline {{ border-left: 2px solid #fed7aa; margin: 24px 0 24px 6px; padding: 4px 0 4px 24px; display: flex; flex-direction: column; gap: 18px; }}
.tl-item {{ position: relative; }}
.tl-item::before {{ content: ''; position: absolute; left: -30px; top: 7px; width: 8px; height: 8px; border-radius: 50%; background: #fb923c; border: 2px solid #fff; box-shadow: 0 0 0 2px #fb923c; }}
.time-badge {{ font-family: 'Courier New', monospace; font-size: 11.5px; font-weight: 700; background: #fff7ed; color: #c2410c; padding: 3px 10px; border-radius: 20px; border: 1px solid #fed7aa; display: inline-block; margin-bottom: 5px; }}
.time-badge.cut {{ background: #fef2f2; color: #dc2626; border-color: #fca5a5; }}
.tl-desc {{ font-family: -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif; font-size: 14.5px; color: #475569; line-height: 1.6; margin: 0; }}

/* === TABLE === */
table {{ width: 100%; border-collapse: collapse; margin: 32px 0; font-size: 15px; }}
th {{ background: #f1f5f9; font-family: 'FD Aeonik', sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #475569; padding: 12px 16px; border: 1px solid #e2e8f0; text-align: left; }}
td {{ padding: 14px 16px; border: 1px solid #e2e8f0; color: #334155; line-height: 1.6; vertical-align: top; font-size: 15px; }}
tr:nth-child(even) td {{ background: #f8fafc; }}

/* === SCENE CARD === */
.scene-card {{ margin: 40px 0 56px; }}
.scene-badge {{ display: inline-flex; align-items: center; gap: 8px; background: #0f172a; color: #fff; font-family: 'FD Aeonik', sans-serif; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; padding: 6px 14px; border-radius: 20px; margin-bottom: 16px; }}
.shot-type-badge {{ background: #3b82f6; color: #fff; font-family: 'Courier New', monospace; font-size: 11px; font-weight: 700; padding: 2px 8px; border-radius: 4px; display: inline-block; margin-bottom: 16px; vertical-align: middle;}}

/* === KICKER === */
.kicker {{ font-family: 'FD Aeonik', sans-serif; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #94a3b8; margin: 36px 0 12px; padding-bottom: 8px; border-bottom: 1px solid #f1f5f9; }}

/* === STORYBOARD IMG === */
.storyboard-img {{ width: 100%; border-radius: 10px; margin: 32px 0 8px; border: 1px solid #e2e8f0; }}
.img-caption {{ text-align: center; font-family: 'FD Aeonik', sans-serif; font-size: 13px; color: #94a3b8; margin-bottom: 32px; }}

/* === PRIORITY BADGE === */
.priority-fire {{ background: #fef2f2; color: #dc2626; border: 1px solid #fca5a5; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 700; font-family: 'FD Aeonik', sans-serif; }}
.priority-bolt {{ background: #fffbeb; color: #d97706; border: 1px solid #fde68a; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 700; font-family: 'FD Aeonik', sans-serif; }}
</style>
</head>
<body>
  <aside class="sidebar">
    <div class="sidebar-title">MỤC LỤC</div>
    <ul class="toc">
      {chr(10).join(toc_html)}
    </ul>
  </aside>
  <main class="main">
    <div class="content-body">
      {'<br><hr><br>'.join(all_html)}
    </div>
  </main>
<script>
const headings = document.querySelectorAll('h2[id], h3[id]');
const tocLinks = document.querySelectorAll('.toc a, .sub-toc a');
const obs = new IntersectionObserver((entries) => {{
  entries.forEach(e => {{
    if (e.isIntersecting) {{
      tocLinks.forEach(a => a.classList.remove('active'));
      const link = document.querySelector(`.toc a[href="#${{e.target.id}}"], .sub-toc a[href="#${{e.target.id}}"]`);
      if (link) link.classList.add('active');
    }}
  }});
}}, {{ rootMargin: '-15% 0px -70% 0px' }});
headings.forEach(h => obs.observe(h));
</script>
</body>
</html>
"""

    os.makedirs('/Users/vietmac/Documents/CODE/k', exist_ok=True)
    with open('/Users/vietmac/Documents/CODE/k/shot-list-v2.html', 'w', encoding='utf-8') as f:
        f.write(full_html)

if __name__ == "__main__":
    main()
