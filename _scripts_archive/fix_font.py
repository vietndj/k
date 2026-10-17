import re

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the faulty @font-face block
content = re.sub(
    r'@font-face\s*{\s*font-family:\s*\'FD Sectra\';\s*src:\s*local\([^)]+\),\s*local\([^)]+\),\s*local\([^)]+\);\s*}',
    '',
    content
)

# Replace .font-display font-family
content = re.sub(
    r'\.font-display\s*{\s*font-family:\s*\'FD Sectra\',\s*serif;\s*}',
    '.font-display {\n            font-family: "GT Sectra LCGV Display", "GT Sectra Display", "GT Sectra LCGV", "GT Sectra", "GR Sectra Display", "GR Sectra", serif;\n        }',
    content
)

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'w', encoding='utf-8') as f:
    f.write(content)

