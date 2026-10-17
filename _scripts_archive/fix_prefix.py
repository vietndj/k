import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.replace('https://', 'https://')
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.codegraph' in root or '__pycache__' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.json', '.py')):
            process_file(os.path.join(root, file))

print("Done fixing prefixes.")
