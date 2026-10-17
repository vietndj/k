with open('rebuild_anh_ui.py', 'r', encoding='utf-8') as f:
    content = f.read()

old_search_logic = """        function filterData() {
            const search = document.getElementById('searchInput').value.toLowerCase();
            const category = document.getElementById('categoryFilter').value;
            const style = document.getElementById('styleFilter').value;

            const filtered = allPosters.filter(p => {
                const matchSearch = (p.title && p.title.toLowerCase().includes(search)) || 
                                    (p.poem && p.poem.toLowerCase().includes(search)) || 
                                    (p.id && p.id.toLowerCase().includes(search)) ||
                                    (p.prompt && p.prompt.toLowerCase().includes(search));
                const matchCategory = category === 'all' || p.category === category;
                const matchStyle = style === 'all' || p.style === style;
                return matchSearch && matchCategory && matchStyle;
            });

            renderCards(filtered);
        }"""

new_search_logic = """        function removeAccents(str) {
            if (!str) return '';
            return str.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase();
        }

        function filterData() {
            const rawSearch = document.getElementById('searchInput').value;
            const search = removeAccents(rawSearch).trim();
            const category = document.getElementById('categoryFilter').value;
            const style = document.getElementById('styleFilter').value;
            
            // Keyword mapping for smart search
            let synonyms = [search];
            if (search.includes('tuong') || search.includes('lien minh') || search.includes('lol')) {
                synonyms.push('league of legend');
                synonyms.push('champion');
            }

            const filtered = allPosters.filter(p => {
                // Combine all searchable text
                const fullText = removeAccents([
                    p.title, p.poem, p.id, p.prompt, p.category, p.style, p.movie_reference
                ].filter(Boolean).join(' '));
                
                // Match search: true if search is empty OR if ANY of the synonyms are found in the full text
                const matchSearch = search === '' || synonyms.some(syn => fullText.includes(syn));
                
                const matchCategory = category === 'all' || p.category === category;
                const matchStyle = style === 'all' || p.style === style;
                
                return matchSearch && matchCategory && matchStyle;
            });

            renderCards(filtered);
        }"""

content = content.replace(old_search_logic, new_search_logic)

with open('rebuild_anh_ui.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched search logic!")
