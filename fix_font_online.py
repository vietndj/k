import re

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to insert the @font-face rules
font_face_css = """
        @font-face {
            font-family: 'GT Sectra';
            src: url('assets/fonts/GT-Sectra-Display-Regular.otf') format('opentype');
            font-weight: 400;
            font-style: normal;
        }
        @font-face {
            font-family: 'GT Sectra';
            src: url('assets/fonts/GT-Sectra-Display-Bold.otf') format('opentype');
            font-weight: 600;
            font-style: normal;
        }
        @font-face {
            font-family: 'GT Sectra';
            src: url('assets/fonts/GT-Sectra-Display-Bold.otf') format('opentype');
            font-weight: 700;
            font-style: normal;
        }"""

# Insert before body
content = re.sub(
    r'(\s*)(body {)',
    rf'\1{font_face_css}\1\2',
    content
)

# Replace .font-display to use just GT Sectra
content = re.sub(
    r'\.font-display\s*{\s*font-family:\s*"GT Sectra LCGV Display", "GT Sectra Display", "GT Sectra LCGV", "GT Sectra", "GR Sectra Display", "GR Sectra", serif;\s*}',
    '.font-display {\n            font-family: "GT Sectra", serif;\n        }',
    content
)

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'w', encoding='utf-8') as f:
    f.write(content)

