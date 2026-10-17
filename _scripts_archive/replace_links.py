import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. assets/covers -> media.fedu.vn/k_covers
    content = re.sub(r'assets/covers/([^"\'<>\s]+)\.(jpg|jpeg|png)', r'https://media.fedu.vn/k_covers/\1.webp', content)
    content = re.sub(r'assets/covers/([^"\'<>\s]+)\.webp', r'https://media.fedu.vn/k_covers/\1.webp', content)
    # Also handle ./assets/covers
    content = re.sub(r'\./assets/covers/([^"\'<>\s]+)\.(jpg|jpeg|png)', r'https://media.fedu.vn/k_covers/\1.webp', content)
    content = re.sub(r'\./assets/covers/([^"\'<>\s]+)\.webp', r'https://media.fedu.vn/k_covers/\1.webp', content)

    # 2. assets/anhloi -> media.fedu.vn/anhloi
    content = re.sub(r'assets/anhloi/([^"\'<>\s]+)\.(jpg|jpeg|png)', r'https://media.fedu.vn/anhloi/\1.webp', content)
    content = re.sub(r'assets/anhloi/([^"\'<>\s]+)\.webp', r'https://media.fedu.vn/anhloi/\1.webp', content)
    content = re.sub(r'\./assets/anhloi/([^"\'<>\s]+)\.(jpg|jpeg|png)', r'https://media.fedu.vn/anhloi/\1.webp', content)
    content = re.sub(r'\./assets/anhloi/([^"\'<>\s]+)\.webp', r'https://media.fedu.vn/anhloi/\1.webp', content)

    # 3. assets/images_gen_fixes -> media.fedu.vn/images_gen_fixes
    content = re.sub(r'assets/images_gen_fixes/([^"\'<>\s]+)\.(jpg|jpeg|png)', r'https://media.fedu.vn/images_gen_fixes/\1.webp', content)
    content = re.sub(r'assets/images_gen_fixes/([^"\'<>\s]+)\.webp', r'https://media.fedu.vn/images_gen_fixes/\1.webp', content)
    content = re.sub(r'\./assets/images_gen_fixes/([^"\'<>\s]+)\.(jpg|jpeg|png)', r'https://media.fedu.vn/images_gen_fixes/\1.webp', content)
    content = re.sub(r'\./assets/images_gen_fixes/([^"\'<>\s]+)\.webp', r'https://media.fedu.vn/images_gen_fixes/\1.webp', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.codegraph' in root or 'assets' in root or '__pycache__' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.json', '.py')):
            process_file(os.path.join(root, file))

print("All links replaced.")
