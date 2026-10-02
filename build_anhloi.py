import os
import html
import json

covers_dir = '/Users/vietmac/Documents/CODE/k/assets/anhloi'
html_path = '/Users/vietmac/Documents/CODE/k/anhloi.html'
old_json_path = '/tmp/old_unique_posters.json'

# Load old prompts
prompt_map = {}
if os.path.exists(old_json_path):
    try:
        with open(old_json_path, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            for item in old_data:
                p = item.get("path", item.get("image_path", ""))
                filename = os.path.basename(p)
                prompt_map[filename] = item.get("prompt", "")
    except Exception as e:
        print("Could not load old prompts:", e)

all_covers = sorted([f for f in os.listdir(covers_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.webp'))], 
                    key=lambda x: os.path.getmtime(os.path.join(covers_dir, x)), reverse=True)
all_paths = [f'assets/anhloi/{f}' for f in all_covers]

cards_html = []
with_prompt_count = 0

def create_card(path):
    global with_prompt_count
    filename = os.path.basename(path)
    clean_filename = os.path.splitext(filename)[0]
    prompt = prompt_map.get(filename, "")
    
    if prompt:
        with_prompt_count += 1
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

for path in all_paths:
    cards_html.append(create_card(path))

total_cards = len(cards_html)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ảnh Lỗi / Ảnh Rác (Old Experiments)</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: sans-serif; background-color: #2a0a0a; color: white; }}
        header {{ position: sticky; top: 0; z-index: 100; background: rgba(42, 10, 10, 0.9); backdrop-filter: blur(8px); padding: 16px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #552222; }}
        .header-left h1 {{ margin: 0; font-size: 1.5rem; color: #ff6b6b; }}
        .header-left p {{ margin: 0; font-size: 0.9rem; color: #ff9999; }}
        .header-right button {{ background: #552222; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer; margin-left: 8px; }}
        .header-right button.active {{ background: #e63946; }}
        
        .style-a body {{ background-color: #2a0a0a; }}
        .style-a .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 8px; padding: 8px; }}
        .style-a .card-label {{ display: none; }}
        .style-a .card {{ overflow: hidden; }}
        
        .style-b body {{ background-color: #1a0505; }}
        .style-b .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 16px; padding: 16px; }}
        .style-b .card {{ background: #2b1111; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.4); transition: transform 0.2s; }}
        .style-b .card:hover {{ transform: translateY(-4px); }}
        .style-b .card-label {{ padding: 8px 12px; font-size: 0.7rem; color: #ff9999; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}

        .img-wrap {{ position: relative; overflow: hidden; width: 100%; aspect-ratio: 9/16; background: #331111; }}
        .img-wrap img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
        
        .copy-btn {{ position: absolute; top: 8px; right: 8px; background: rgba(0,0,0,0.7); color: white; border: none; border-radius: 6px; padding: 6px 10px; font-size: 0.75rem; cursor: pointer; opacity: 0; transition: opacity 0.2s; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px); }}
        .card:hover .copy-btn {{ opacity: 1; }}
        .copy-btn.copied {{ background: rgba(16,185,129,0.9); }}
    </style>
</head>
<body class="style-b">
    <header>
        <div class="header-left">
            <h1>Kho Ảnh Lỗi (Đã Xóa)</h1>
            <p>{total_cards} images ({with_prompt_count} with prompt)</p>
        </div>
        <div class="header-right">
            <button class="style-btn" data-style="style-a" onclick="setStyle('style-a')">Style A (Grid)</button>
            <button class="style-btn active" data-style="style-b" onclick="setStyle('style-b')">Style B (Kanban)</button>
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
            document.querySelectorAll('.style-btn').forEach(b => b.classList.toggle('active', b.dataset.style === s)); 
        }}
    </script>
</body>
</html>
'''

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Done: anhloi.html created with {total_cards} cards ({with_prompt_count} with prompt)")
