import re

with open('/Users/vietmac/Documents/CODE/k/rewrite_k_html.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the select id="styleFilter" in the HTML string and add the Google Flow option
old_select = '''<select id="styleFilter">
            <option value="all">Tất cả phong cách</option>
            <option value="Chưa phân loại">Chưa phân loại</option>
            <option value="Cinematic">Cinematic</option>
            <option value="Anime Style">Anime Style</option>
            <option value="3D Render">3D Render</option>
        </select>'''

new_select = '''<select id="styleFilter">
            <option value="all">Tất cả phong cách</option>
            <option value="Google Flow">Google Flow</option>
            <option value="Chưa phân loại">Chưa phân loại</option>
            <option value="Cinematic">Cinematic</option>
            <option value="Anime Style">Anime Style</option>
            <option value="3D Render">3D Render</option>
        </select>'''

content = content.replace(old_select, new_select)

with open('/Users/vietmac/Documents/CODE/k/rewrite_k_html.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched rewrite_k_html.py")
