import re

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace FD Aeonik with FD Sectra
content = content.replace(
    "@font-face {\n            font-family: 'FD Aeonik';\n            src: local('Helvetica Neue'), local('Arial');\n        }",
    "@font-face {\n            font-family: 'FD Sectra';\n            src: local('FD Sectra'), local('GT Sectra'), local('Times New Roman');\n        }"
)
content = content.replace(
    ".font-display {\n            font-family: 'FD Aeonik', sans-serif;\n        }",
    ".font-display {\n            font-family: 'FD Sectra', serif;\n        }"
)

# Replace h2 tags with flex container and copy button
def repl_h2(match):
    h2_content = match.group(1)
    prompt_id = "prompt-" + h2_content.split('.')[0]
    return f"""<div class="flex items-center justify-between mb-6 pb-2 border-b border-slate-200">
                    <h2 class="font-display font-semibold text-2xl">{h2_content}</h2>
                    <button onclick="copyToClipboard('{prompt_id}', this)" class="shrink-0 inline-flex items-center gap-1 px-3 py-1.5 bg-slate-800 border border-transparent rounded-md text-xs font-medium text-white hover:bg-slate-700 transition-colors shadow-sm">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"></path></svg>
                        Copy Prompt
                    </button>
                </div>"""

content = re.sub(r'<h2 class="font-display font-semibold text-2xl mb-6 pb-2 border-b border-slate-200">(.*?)</h2>', repl_h2, content)

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'w', encoding='utf-8') as f:
    f.write(content)

