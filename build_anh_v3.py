import json
import os
import html

json_path = '/Users/vietmac/Documents/CODE/k/all_unique_posters.json'
html_path = '/Users/vietmac/Documents/CODE/k/anh.html'

with open(json_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Sort them so newer ones might be at the top, or just keep json_data order
# Usually json_data is already ordered, let's reverse it if needed or keep it.
# all_unique_posters.json has them in some order.

cards_html = []
with_prompt_count = 0

def create_card(path, prompt):
    if not path.startswith("http") and not path.startswith("assets") and not path.startswith("/"):
        path = f"assets/covers/{path}"
    
    filename = os.path.basename(path)
    clean_filename = os.path.splitext(filename)[0]
    poem_id = clean_filename.replace("poster_", "")
    
    if prompt:
        escaped_prompt = html.escape(prompt)
        if prompt.startswith("POEM:"):
            parts = prompt.split('\n\n')
            title = parts[0].replace("POEM: ", "").strip()
            poem_text = parts[1].strip().replace('\n', '<br>') if len(parts) > 1 else ""
            
            return f'''<div class="card has-prompt poem-card" style="display: flex; flex-direction: column; background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.4); transition: transform 0.2s;">
  <div class="img-wrap" style="position: relative; overflow: hidden; width: 100%; aspect-ratio: 9/16; background: #334155;">
    <img src="{path}" loading="lazy" alt="Poster" style="width: 100%; height: 100%; object-fit: cover; display: block;">
    <button class="copy-btn" data-prompt="{escaped_prompt}" style="position: absolute; top: 8px; right: 8px; background: rgba(0,0,0,0.7); color: white; border: none; border-radius: 6px; padding: 6px 10px; font-size: 0.75rem; cursor: pointer; opacity: 0; transition: opacity 0.2s; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px);">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Prompt</span>
    </button>
  </div>
  <div class="poem-content" style="padding: 16px; display: flex; flex-direction: column; gap: 8px; flex: 1;">
    <div><span style="background: rgba(255,255,255,0.1); color: #94a3b8; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">{poem_id}</span></div>
    <div style="color: #60a5fa; font-weight: 800; font-size: 0.95rem; text-transform: uppercase; line-height: 1.3;">{html.escape(title)}</div>
    <div style="color: #e2e8f0; font-style: italic; font-size: 0.9rem; line-height: 1.5; margin-top: 4px;">{poem_text}</div>
  </div>
</div>'''
        else:
            return f'''<div class="card has-prompt" style="background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.4); transition: transform 0.2s;">
  <div class="img-wrap" style="position: relative; overflow: hidden; width: 100%; aspect-ratio: 9/16; background: #334155;">
    <img src="{path}" loading="lazy" alt="Poster" style="width: 100%; height: 100%; object-fit: cover; display: block;">
    <button class="copy-btn" data-prompt="{escaped_prompt}" style="position: absolute; top: 8px; right: 8px; background: rgba(0,0,0,0.7); color: white; border: none; border-radius: 6px; padding: 6px 10px; font-size: 0.75rem; cursor: pointer; opacity: 0; transition: opacity 0.2s; display: flex; align-items: center; gap: 4px; backdrop-filter: blur(4px);">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Prompt</span>
    </button>
  </div>
  <div class="card-label" style="padding: 8px 12px; font-size: 0.7rem; color: #94a3b8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{clean_filename}</div>
</div>'''
    else:
        return f'''<div class="card no-prompt" style="background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.4); transition: transform 0.2s;">
  <div class="img-wrap" style="position: relative; overflow: hidden; width: 100%; aspect-ratio: 9/16; background: #334155;">
    <img src="{path}" loading="lazy" alt="Poster" style="width: 100%; height: 100%; object-fit: cover; display: block;">
  </div>
  <div class="card-label" style="padding: 8px 12px; font-size: 0.7rem; color: #94a3b8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{clean_filename}</div>
</div>'''

for item in json_data:
    path = item.get("path", "")
    prompt = item.get("prompt", "")
    if prompt:
        with_prompt_count += 1
    cards_html.append(create_card(path, prompt))

total_cards = len(cards_html)

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thư Viện Ảnh Bìa Thơ & Prompt Toàn Tập</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: sans-serif; background-color: #0f172a; color: white; }}
        header {{ position: sticky; top: 0; z-index: 100; background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(8px); padding: 16px 32px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #334155; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
        .header-left h1 {{ margin: 0; font-size: 1.5rem; }}
        .header-left p {{ margin: 0; font-size: 0.9rem; color: #94a3b8; margin-top: 4px; }}
        
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; padding: 32px; }}
        
        .card:hover {{ transform: translateY(-4px); box-shadow: 0 8px 30px rgba(0,0,0,0.6) !important; }}
        .card:hover .copy-btn {{ opacity: 1 !important; }}
        .copy-btn.copied {{ background: rgba(16,185,129,0.9) !important; }}
    </style>
</head>
<body>
    <header>
        <div class="header-left">
            <h1>Thư Viện Ảnh Bìa Thơ & Prompt</h1>
            <p>Tổng cộng: {total_cards} concept độc bản (Đã lọc trùng lặp)</p>
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
    </script>
</body>
</html>
'''

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Done: anh.html updated with {total_cards} cards ({with_prompt_count} with prompt)")
