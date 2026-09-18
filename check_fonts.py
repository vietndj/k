import os
import re

dir_path = '/Users/vietmac/Documents/CODE/k'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

missing_files = []

for file in html_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Check if they USE FD Aeonik or FD Integral or Tiempos Text
        uses_aeonik = re.search(r'font-family:[^;]*FD Aeonik', content, re.IGNORECASE)
        uses_integral = re.search(r'font-family:[^;]*FD Integral', content, re.IGNORECASE)
        uses_tiempos = re.search(r'font-family:[^;]*Tiempos Text', content, re.IGNORECASE)
        
        # Check if they DECLARE them
        declares_aeonik = re.search(r"@font-face\s*\{[^}]*font-family:\s*['\"]FD Aeonik['\"]", content, re.IGNORECASE)
        declares_integral = re.search(r"@font-face\s*\{[^}]*font-family:\s*['\"]FD Integral['\"]", content, re.IGNORECASE)
        declares_tiempos = re.search(r"@font-face\s*\{[^}]*font-family:\s*['\"]Tiempos Text['\"]", content, re.IGNORECASE)
        
        missing = []
        if uses_aeonik and not declares_aeonik:
            missing.append('FD Aeonik')
        if uses_integral and not declares_integral:
            missing.append('FD Integral')
        if uses_tiempos and not declares_tiempos:
            missing.append('Tiempos Text')
            
        if missing:
            missing_files.append((file, missing))

print(f"Checked {len(html_files)} HTML files.")
if missing_files:
    print("Files with missing @font-face:")
    for f, m in missing_files:
        print(f" - {f}: {', '.join(m)}")
else:
    print("All files have correct @font-face declarations.")
