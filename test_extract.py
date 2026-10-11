import sys
from bs4 import BeautifulSoup
import markdownify

def process(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    main_content = soup.find('article') or soup.find('main') or soup.body
    
    if main_content:
        # Xóa các thẻ script, style
        for script in main_content(['script', 'style', 'nav', 'header']):
            script.decompose()
            
        md = markdownify.markdownify(str(main_content), heading_style="ATX")
        print(md[:500])

process('logickenh-baohiem.html')
