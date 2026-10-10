import re

with open('rebuild_anh_ui.py', 'r', encoding='utf-8') as f:
    content = f.read()

# I will write a regex to completely replace the filterData function
import re
new_func = """function removeAccents(str) {{
            if (!str) return '';
            return str.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase();
        }}

        function filterData() {{
            const rawSearch = document.getElementById('searchInput').value;
            const search = removeAccents(rawSearch).trim();
            const category = document.getElementById('categoryFilter').value;
            const style = document.getElementById('styleFilter').value;
            
            let synonyms = [search];
            if (search.includes('tuong') || search.includes('lien minh') || search.includes('lol')) {{
                synonyms.push('league of legends');
                synonyms.push('champion');
            }}
            if (search.includes('flow')) {{
                synonyms.push('google flow');
            }}

            const filtered = allPosters.filter(p => {{
                const fullText = removeAccents([
                    p.title, p.poem, p.id, p.prompt, p.category, p.style, p.movie_reference
                ].filter(Boolean).join(' '));
                
                const matchSearch = search === '' || synonyms.some(syn => fullText.includes(syn));
                const matchCategory = category === 'all' || p.category === category;
                const matchStyle = style === 'all' || p.style === style;
                
                return matchSearch && matchCategory && matchStyle;
            }});

            renderCards(filtered);
        }}"""

# Remove everything from function filterData() to just before document.getElementById('searchInput').addEventListener
content = re.sub(r'function filterData\(\).*?renderCards\(filtered\);\s*\}\s*document\.getElementById\(\'searchInput\'\)\.value\.toLowerCase\(\);.*?renderCards\(filtered\);\s*\}', new_func, content, flags=re.DOTALL)

with open('rebuild_anh_ui.py', 'w', encoding='utf-8') as f:
    f.write(content)
