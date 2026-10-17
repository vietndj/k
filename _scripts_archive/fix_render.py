import os

with open('/Users/vietmac/Documents/CODE/k/render_gmail_showcase.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<style>svg{width:1024px!important;height:1024px!important;}</style>',
    '<style>svg{{width:1024px!important;height:1024px!important;}}</style>'
)

with open('/Users/vietmac/Documents/CODE/k/render_gmail_showcase.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated render_gmail_showcase.py with escaped curly braces")
