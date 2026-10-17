import re

with open("build_anh_v2.py", "r") as f:
    code = f.read()

new_func = r"""def create_card(path, prompt):
    import html
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
  <div class="img-wrap">
    <img src="{path}" loading="lazy" alt="Poster">
    <button class="copy-btn" data-prompt="{escaped_prompt}">
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
"""

# Try simple split and join instead of regex
parts = code.split('def create_card(path, prompt):')
if len(parts) == 2:
    tail_parts = parts[1].split('\nfor path in all_paths:')
    if len(tail_parts) >= 2:
        # success
        new_code = parts[0] + new_func + '\nfor path in all_paths:' + tail_parts[1]
        with open("build_anh_v2.py", "w") as f:
            f.write(new_code)
        print("Patched successfully")
    else:
        print("Failed to find tail")
else:
    print("Failed to find head")
