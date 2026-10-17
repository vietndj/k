import re

with open("build_anh_v2.py", "r") as f:
    code = f.read()

new_create_card = r"""
def create_card(path, prompt):
    if not path.startswith("http") and not path.startswith("assets") and not path.startswith("/"):
        path = f"assets/covers/{path}"
    filename = os.path.basename(path)
    clean_filename = os.path.splitext(filename)[0]
    
    if prompt:
        escaped_prompt = html.escape(prompt)
        if prompt.startswith("POEM:"):
            poem_html = html.escape(prompt.replace("POEM: ", "")).replace("\n", "<br>")
            return f'''<div class="card has-prompt poem-card">
  <div class="img-wrap">
    <img src="{path}" loading="lazy" alt="Poster">
    <button class="copy-btn" data-prompt="{escaped_prompt}">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Prompt</span>
    </button>
  </div>
  <div class="card-label poem-content" style="white-space: normal; line-height: 1.5; padding: 12px; font-size: 0.85rem; color: #cbd5e1; background: #1e293b; text-align: left; border-top: 1px solid #334155;">
    {poem_html}
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

# Replace the old function
# Fix the broken code first by restoring from git if needed, or just finding the function.
# Since it's currently broken with a syntax error, let's just restore it first.
