import json
import os
import html

json_path = '/Users/vietmac/Documents/CODE/k/all_unique_posters.json'
covers_dir = '/Users/vietmac/Documents/CODE/k/assets/covers'
html_path = '/Users/vietmac/Documents/CODE/k/anh.html'

with open(json_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

json_dict = {item['path']: item['prompt'] for item in json_data}

all_covers = sorted([f for f in os.listdir(covers_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))], 
                    key=lambda x: os.path.getmtime(os.path.join(covers_dir, x)), reverse=True)
all_paths = [f'assets/covers/{f}' for f in all_covers]

cards_html = []
with_prompt_count = 0
processed_paths = set()

def create_card(path, prompt):
    if not path.startswith("http") and not path.startswith("assets") and not path.startswith("/"):
        path = f"assets/covers/{path}"
    filename = os.path.basename(path)
    clean_filename = os.path.splitext(filename)[0]
    
    if prompt:
        escaped_prompt = html.escape(prompt)
        return f'''<div class="card has-prompt">
  <div class="img-wrap">
    <img src="{path}" loading="lazy" alt="Poster">
    <button class="copy-btn" data-prompt="{escaped_prompt}">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Prompt</span>
    </button>
  </div>
  <div class="card-label">{clean_filename}</div>
</div>'''
    else:
        return f'''<div class="card no-prompt">
  <div class="img-wrap">
    <img src="{path}" loading="lazy" alt="Poster">
  </div>
  <div class="card-label">{clean_filename}</div>
</div>'''

for item in json_data:
    path = item['path']
    prompt = item['prompt']
    cards_html.append(create_card(path, prompt))
    processed_paths.add(path)
    with_prompt_count += 1

new_cards_html = []
for path in all_paths:
    if path not in processed_paths:
        new_cards_html.append(create_card(path, None))
        
cards_html = new_cards_html + cards_html

total_cards = len(cards_html)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Posters</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: sans-serif; background-color: #0f172a; color: white; }}
        header {{ position: sticky; top: 0; z-index: 100; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(8px); padding: 16px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; }}
        .header-left h1 {{ margin: 0; font-size: 1.5rem; }}
        .header-left p {{ margin: 0; font-size: 0.9rem; color: #94a3b8; }}
        .header-right button {{ background: #334155; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; margin-left: 8px; }}
        .header-right button.active {{ background: #3b82f6; }}
        
        
        
        /* Style A - Grid Compact */
        .style-a body {{ background-color: #0f172a; }}
        .style-a .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 8px; padding: 8px; }}
        .style-a .card-label {{ display: none; }}
        .style-a .card {{ overflow: hidden; }}
        
        /* Style B - Kanban/Notion (Default) */
        .style-b body {{ background-color: #1a1a2e; }}
        .style-b .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; padding: 16px; }}
        .style-b .card {{ background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.4); transition: transform 0.2s; }}
        .style-b .card:hover {{ transform: translateY(-4px); }}
        .style-b .card-label {{ padding: 8px 12px; font-size: 0.7rem; color: #94a3b8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

        /* Shared Image Wrap (Fix Safari Lazy Load Bug) */
        .img-wrap {{ position: relative; overflow: hidden; width: 100%; aspect-ratio: 9/16; background: #334155; }}
        .img-wrap img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
/* Copy Button */
        .copy-btn {{ position: absolute; top: 8px; right: 8px; background: rgba(0,0,0,0.7); color: white; border: none; border-radius: 6px; padding: 6px 10px; font-size: 0.75rem; cursor: pointer; opacity: 0; transition: opacity 0.2s; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px); }}
        .img-wrap {{ position: relative; overflow: hidden; }}
        .card:hover .copy-btn {{ opacity: 1; }}
        .copy-btn.copied {{ background: rgba(16,185,129,0.9); }}
    </style>
</head>
<body class="style-b">
    <header>
        <div class="header-left">
            <h1>Posters</h1>
            <p>{total_cards} images</p>
        </div>
        <div class="header-right">
            <button class="style-btn" data-style="style-a" onclick="setStyle('style-a')">Style A (Grid)</button>
            <button class="style-btn" data-style="style-b" onclick="setStyle('style-b')">Style B (Kanban)</button>
        </div>
    </header>
    
    <div class="grid">
        {''.join(cards_html)}
    </div>

    <script>
        function copyPrompt(btn) {{
            const text = btn.dataset.prompt;
            navigator.clipboard.writeText(text).then(() => {{
                const span = btn.querySelector('span');
                span.textContent = '✓ Copied!';
                btn.classList.add('copied');
                setTimeout(() => {{ span.textContent = 'Copy Prompt'; btn.classList.remove('copied'); }}, 2000);
            }});
        }}
        
        document.querySelectorAll('.copy-btn').forEach(btn => btn.addEventListener('click', () => copyPrompt(btn)));
        
        function setStyle(s) {{ 
            document.body.className = s; 
            localStorage.setItem('poster_style', s); 
            document.querySelectorAll('.style-btn').forEach(b => b.classList.toggle('active', b.dataset.style === s)); 
        }}
        
        document.addEventListener('DOMContentLoaded', () => {{ 
            const s = localStorage.getItem('poster_style') || 'style-b'; 
            setStyle(s); 
        }});
    </script>
</body>
</html>
'''

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Done: anh.html updated with {total_cards} cards ({with_prompt_count} with prompt)")
