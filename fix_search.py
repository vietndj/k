with open('rebuild_anh_ui.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the filterData function properly
import re
new_logic = """
        function removeAccents(str) {{
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
                synonyms.push('league of legend');
                synonyms.push('champion');
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
        }}
"""

# Replace between "function filterData() {{" and "        document.getElementById('searchInput').addEventListener"
content = re.sub(r'function filterData\(\).*?renderCards\(filtered\);\s*\}\}', new_logic.strip(), content, flags=re.DOTALL)

with open('rebuild_anh_ui.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed rebuild_anh_ui.py")
