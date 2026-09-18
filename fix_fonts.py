import os
import re

dir_path = '/Users/vietmac/Documents/CODE/k'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

# The standard font-face blocks
blocks = {
    'FD Aeonik': """
    @font-face {
      font-family: 'FD Aeonik';
      src: url('./fonts/FDAeonik-Regular.woff2') format('woff2'),
           url('./fonts/FDAeonik-Regular.ttf') format('truetype');
      font-weight: 400; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'FD Aeonik';
      src: url('./fonts/FDAeonik-Medium.woff2') format('woff2'),
           url('./fonts/FDAeonik-Medium.ttf') format('truetype');
      font-weight: 500; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'FD Aeonik';
      src: url('./fonts/FDAeonik-Bold.woff2') format('woff2'),
           url('./fonts/FDAeonik-Bold.ttf') format('truetype');
      font-weight: 600 700; font-style: normal; font-display: swap;
    }""",
    
    'FD Aeonik Extended': """
    @font-face {
      font-family: 'FD Aeonik Extended';
      src: url('./fonts/FDAeonikExtended-Regular.woff2') format('woff2'),
           url('./fonts/FDAeonikExtended-Regular.ttf') format('truetype');
      font-weight: 400; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'FD Aeonik Extended';
      src: url('./fonts/FDAeonikExtended-Bold.woff2') format('woff2'),
           url('./fonts/FDAeonikExtended-Bold.ttf') format('truetype');
      font-weight: 700; font-style: normal; font-display: swap;
    }""",
    
    'FD Integral': """
    @font-face {
      font-family: 'FD Integral';
      src: url('./fonts/SVN-IntegralCF-Regular.ttf') format('truetype');
      font-weight: 400; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'FD Integral';
      src: url('./fonts/SVN-IntegralCF-Bold.ttf') format('truetype');
      font-weight: 700; font-style: normal; font-display: swap;
    }""",
    
    'Tiempos Text': """
    @font-face {
      font-family: 'Tiempos Text';
      src: url('./fonts/FDTiemposText-Regular.woff2') format('woff2');
      font-weight: 400; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'Tiempos Text';
      src: url('./fonts/FDTiemposText-Bold.woff2') format('woff2');
      font-weight: 700; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'Tiempos Text';
      src: url('./fonts/FDTiemposText-Semibold.woff2') format('woff2');
      font-weight: 600; font-style: normal; font-display: swap;
    }
    @font-face {
      font-family: 'Tiempos Text';
      src: url('./fonts/FDTiemposText-RegularItalic.woff2') format('woff2');
      font-weight: 400; font-style: italic; font-display: swap;
    }"""
}

# Regex to check if font is used
usage_patterns = {
    'FD Aeonik': r"font-family:[^;]*'FD Aeonik'|font-family:[^;]*\"FD Aeonik\"",
    'FD Aeonik Extended': r"font-family:[^;]*'FD Aeonik Extended'|font-family:[^;]*\"FD Aeonik Extended\"",
    'FD Integral': r"font-family:[^;]*'FD Integral'|font-family:[^;]*\"FD Integral\"",
    'Tiempos Text': r"font-family:[^;]*'Tiempos Text'|font-family:[^;]*\"Tiempos Text\""
}

# Regex to check if @font-face is declared for the family
decl_patterns = {
    'FD Aeonik': r"@font-face\s*\{[^}]*font-family:\s*['\"]FD Aeonik['\"]",
    'FD Aeonik Extended': r"@font-face\s*\{[^}]*font-family:\s*['\"]FD Aeonik Extended['\"]",
    'FD Integral': r"@font-face\s*\{[^}]*font-family:\s*['\"]FD Integral['\"]",
    'Tiempos Text': r"@font-face\s*\{[^}]*font-family:\s*['\"]Tiempos Text['\"]"
}

fixed_count = 0

for file in html_files:
    file_path = os.path.join(dir_path, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    missing_blocks = []
    
    # 1. FD Aeonik Extended logic:
    # If FD Aeonik Extended is used, but not declared -> add block.
    # Wait, in standard 30ngayviral html skill, `--font-display-short` uses `'FD Aeonik Extended'`, 
    # so we should check for `--font-display-short:[^;]*'FD Aeonik Extended'` or just `FD Aeonik Extended` usage.
    if re.search(r"['\"]FD Aeonik Extended['\"]", content, re.IGNORECASE):
        if not re.search(decl_patterns['FD Aeonik Extended'], content, re.IGNORECASE):
            missing_blocks.append(blocks['FD Aeonik Extended'])

    # 2. FD Aeonik logic
    # If FD Aeonik is used but not declared:
    # BUT we must make sure we don't just match 'FD Aeonik Extended' when searching for 'FD Aeonik'.
    # A negative lookahead might be needed, or just strict match.
    if re.search(r"['\"]FD Aeonik['\"]", content, re.IGNORECASE):
        if not re.search(decl_patterns['FD Aeonik'], content, re.IGNORECASE):
            missing_blocks.append(blocks['FD Aeonik'])
            
    # 3. FD Integral
    if re.search(r"['\"]FD Integral['\"]", content, re.IGNORECASE):
        if not re.search(decl_patterns['FD Integral'], content, re.IGNORECASE):
            missing_blocks.append(blocks['FD Integral'])
            
    # 4. Tiempos Text
    if re.search(r"['\"]Tiempos Text['\"]", content, re.IGNORECASE):
        if not re.search(decl_patterns['Tiempos Text'], content, re.IGNORECASE):
            missing_blocks.append(blocks['Tiempos Text'])
            
    if missing_blocks:
        # We need to insert the missing blocks into the <style> tag.
        # Find the first <style> tag.
        style_match = re.search(r'<style>', content, re.IGNORECASE)
        if style_match:
            insert_pos = style_match.end()
            new_content = content[:insert_pos] + "\n" + "".join(missing_blocks) + content[insert_pos:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            fixed_count += 1
            print(f"Fixed {file}")
            
print(f"\nTotal files fixed: {fixed_count}")
