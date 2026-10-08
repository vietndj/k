import json

with open('brand_style.css', 'r', encoding='utf-8') as f:
    brand_css = f.read()

html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Posters Gallery • NGUYỄN VIỆT</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
    
    {brand_css}
    
    <style>
        body {{ background-color: var(--cl-bg); color: var(--cl-text-base); font-family: var(--cl-font-sub); margin: 0; padding: 0; -webkit-font-smoothing: antialiased; }}
        .gallery-header {{ position: sticky; top: 0; z-index: 100; background: rgba(7, 9, 14, 0.85); backdrop-filter: blur(12px); border-bottom: 1px solid var(--cl-line); padding: 24px 40px; display: flex; justify-content: space-between; align-items: center; }}
        .header-left h1 {{ font-family: var(--cl-font-head); font-size: 28px; font-weight: 700; letter-spacing: 1px; margin: 0 0 4px 0; color: var(--cl-text-base); }}
        .header-left p {{ font-family: var(--cl-font-mono); font-size: 13px; color: var(--cl-accent); margin: 0; }}
        .toolbar {{ padding: 24px 40px 0 40px; display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
        .toolbar input, .toolbar select {{ background: var(--cl-card); border: 1px solid var(--cl-line-strong); color: var(--cl-text-base); padding: 12px 20px; border-radius: var(--cl-radius-sm); font-family: var(--cl-font-sub); font-size: 14px; outline: none; transition: all 0.2s ease; }}
        .toolbar input:focus, .toolbar select:focus {{ border-color: var(--cl-accent); box-shadow: 0 0 0 3px var(--cl-accent-tint); }}
        .toolbar input {{ flex-grow: 1; min-width: 300px; }}
        .stats {{ padding: 20px 40px 0 40px; display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
        .stat-badge {{ background: var(--cl-card-muted); border: 1px solid var(--cl-line); padding: 6px 14px; border-radius: 20px; font-size: 12px; font-family: var(--cl-font-mono); color: var(--cl-text-muted); }}
        .style-a .grid-container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; padding: 32px 40px 60px 40px; }}
        .style-b .grid-container {{ columns: 4 300px; column-gap: 24px; padding: 32px 40px 60px 40px; }}
        .poster-card {{ background: var(--cl-card); border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); overflow: hidden; transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.3s ease; position: relative; margin-bottom: 24px; break-inside: avoid; }}
        .poster-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 32px rgba(0,0,0,0.4); border-color: var(--cl-line-strong); }}
        .poster-img-wrap {{ position: relative; width: 100%; overflow: hidden; }}
        .poster-img-wrap img {{ width: 100%; height: auto; display: block; cursor: zoom-in; transition: transform 0.5s ease; }}
        .poster-card:hover .poster-img-wrap img {{ transform: scale(1.03); }}
        .copy-btn {{ position: absolute; bottom: 12px; right: 12px; background: rgba(7, 9, 14, 0.7); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.1); color: white; padding: 8px 12px; border-radius: 8px; font-family: var(--cl-font-sub); font-size: 12px; font-weight: 600; display: flex; align-items: center; gap: 6px; cursor: pointer; opacity: 0; transform: translateY(10px); transition: all 0.2s ease; }}
        .poster-card:hover .copy-btn {{ opacity: 1; transform: translateY(0); }}
        .copy-btn:hover {{ background: var(--cl-accent); color: #07090e; }}
        .poster-info {{ padding: 20px; display: flex; flex-direction: column; gap: 12px; }}
        .poster-id {{ font-family: var(--cl-font-mono); font-size: 11px; color: var(--cl-accent); background: var(--cl-accent-tint); padding: 4px 8px; border-radius: 4px; display: inline-block; align-self: flex-start; }}
        .poster-title {{ font-family: var(--cl-font-head); font-size: 16px; font-weight: 700; line-height: 1.4; color: var(--cl-text-base); text-transform: uppercase; }}
        .poster-poem {{ font-family: var(--cl-font-serif); font-size: 14px; line-height: 1.6; color: var(--cl-text-muted); font-style: italic; }}
        .poster-meta {{ font-family: var(--cl-font-mono); font-size: 11px; color: var(--cl-text-faint); margin-top: 4px; display: flex; flex-wrap: wrap; gap: 8px; }}
        .lightbox {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.95); backdrop-filter: blur(10px); z-index: 9999; align-items: center; justify-content: center; }}
        .lightbox img {{ max-width: 90vw; max-height: 90vh; border-radius: 12px; box-shadow: 0 24px 64px rgba(0,0,0,0.6); }}
        .btn-toggle {{ background: var(--cl-card); border: 1px solid var(--cl-line); color: var(--cl-text-base); padding: 8px 16px; border-radius: var(--cl-radius-sm); font-family: var(--cl-font-sub); font-size: 13px; cursor: pointer; transition: 0.2s; }}
        .btn-toggle.active {{ background: var(--cl-accent); color: var(--cl-bg); border-color: var(--cl-accent); font-weight: 600; }}
        .just-image-label {{ position: absolute; top: 12px; left: 12px; font-family: var(--cl-font-mono); font-size: 11px; color: #fff; background: rgba(0,0,0,0.6); backdrop-filter: blur(4px); padding: 4px 8px; border-radius: 4px; }}
    </style>
</head>
<body class="style-b">
    <header class="gallery-header">
        <div class="header-left">
            <h1>THƯ VIỆN POSTER</h1>
            <p id="total-count">LOADING DATA...</p>
        </div>
        <div class="header-right" style="display:flex; gap:12px;">
            <button class="btn-toggle" data-style="style-a" onclick="setStyle('style-a')">GRID VIEW</button>
            <button class="btn-toggle active" data-style="style-b" onclick="setStyle('style-b')">MASONRY VIEW</button>
        </div>
    </header>
    <div class="toolbar">
        <input type="text" id="searchInput" placeholder="Tìm kiếm theo mã, tiêu đề, thơ, thẻ loại, phong cách...">
        <select id="categoryFilter">
            <option value="all">Tất cả thể loại</option>
            <option value="Chưa phân loại">Chưa phân loại</option>
            <option value="Phim Điện Ảnh">Phim Điện Ảnh</option>
            <option value="Anime">Anime</option>
            <option value="Game">Game</option>
        </select>
        <select id="styleFilter">
            <option value="all">Tất cả phong cách</option>
            <option value="Google Flow">Google Flow</option>
            <option value="Chưa phân loại">Chưa phân loại</option>
            <option value="Cinematic">Cinematic</option>
            <option value="Anime Style">Anime Style</option>
            <option value="3D Render">3D Render</option>
        </select>
    </div>
    <div id="statsContainer" class="stats"></div>
    <div id="grid" class="grid-container"></div>
    <div id="lightbox" onclick="closeLightbox(event)">
        <img id="lightbox-img" src="" alt="Zoomed Poster">
    </div>

    <script>
        let allPosters = [];

        async function init() {{
            try {{
                const res = await fetch('database.json');
                const data = await res.json();
                allPosters = data.posters;
                document.getElementById('total-count').textContent = `[ ${{data.metadata.total_images}} MASTERPIECES ]`;
                renderCards(allPosters);
                renderStats(allPosters);
            }} catch (err) {{
                console.error('Error loading data:', err);
                document.getElementById('grid').innerHTML = '<p style="padding:16px; color:#ef4444;">Lỗi tải dữ liệu. Cần chạy trên Live Server (localhost) do CORS.</p>';
            }}
        }}

        function copyPrompt(btn) {{
            const text = btn.dataset.prompt;
            navigator.clipboard.writeText(text).then(() => {{
                const span = btn.querySelector('span');
                span.textContent = 'COPIED!';
                btn.style.background = 'var(--cl-accent)';
                btn.style.color = 'var(--cl-bg)';
                setTimeout(() => {{ 
                    span.textContent = 'COPY PROMPT'; 
                    btn.style.background = '';
                    btn.style.color = '';
                }}, 2000);
            }});
        }}

        function renderCards(posters) {{
            const grid = document.getElementById('grid');
            grid.innerHTML = '';
            posters.forEach(p => {{
                const card = document.createElement('div');
                card.className = 'poster-card';
                let html = `<div class="poster-img-wrap"><img src="${{p.image}}" loading="lazy" alt="Poster" onclick="openLightbox('${{p.image}}')">`;
                
                if (p.has_prompt) {{
                    const safePrompt = (p.prompt || '').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                    html += `<button class="copy-btn" data-prompt="${{safePrompt}}" onclick="copyPrompt(this)">
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> 
                          <span>COPY PROMPT</span>
                        </button>`;
                }} else {{
                    html += `<div class="just-image-label">${{p.id}}</div>`;
                }}
                
                html += `</div>`;
                
                if (p.has_prompt) {{
                    html += `<div class="poster-info">
                        <div class="poster-id">${{p.id}}</div>
                        <div class="poster-title">${{p.title}}</div>
                        <div class="poster-poem">${{(p.poem || '').replace(/\\n/g, '<br>')}}</div>
                        <div class="poster-meta">
                            <span>${{p.movie_reference || 'N/A'}}</span> • 
                            <span>${{p.category || 'N/A'}}</span> • 
                            <span>${{p.style || 'N/A'}}</span>
                        </div>
                      </div>`;
                }}
                card.innerHTML = html;
                grid.appendChild(card);
            }});
        }}

        function renderStats(posters) {{
            const stats = document.getElementById('statsContainer');
            const counts = {{}};
            posters.forEach(p => {{
                const k = p.movie_reference || 'Khác';
                counts[k] = (counts[k] || 0) + 1;
            }});
            
            let html = '<strong style="color: var(--cl-text-base); font-family: var(--cl-font-head); font-size: 13px;">THỐNG KÊ:</strong> ';
            for (const [k, v] of Object.entries(counts)) {{
                html += `<span class="stat-badge">${{k}}: ${{v}}</span>`;
            }}
            stats.innerHTML = html;
        }}

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
        }}

        document.getElementById('searchInput').addEventListener('input', filterData);
        document.getElementById('categoryFilter').addEventListener('change', filterData);
        document.getElementById('styleFilter').addEventListener('change', filterData);

        function openLightbox(src) {{
            const lb = document.getElementById('lightbox');
            document.getElementById('lightbox-img').src = src;
            lb.style.display = 'flex';
        }}
        
        function closeLightbox(e) {{
            if (e.target.id === 'lightbox') {{
                document.getElementById('lightbox').style.display = 'none';
            }}
        }}
        
        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                document.getElementById('lightbox').style.display = 'none';
            }}
        }});

        function setStyle(s) {{ 
            document.body.className = s; 
            localStorage.setItem('poster_style', s); 
            document.querySelectorAll('.btn-toggle').forEach(b => b.classList.toggle('active', b.dataset.style === s)); 
        }}
        
        document.addEventListener('DOMContentLoaded', () => {{ 
            const s = localStorage.getItem('poster_style') || 'style-b'; 
            setStyle(s); 
        }});

        init();
    </script>
</body>
</html>
"""

with open('anh.html', 'w', encoding='utf-8') as f:
    f.write(html)
    
# Keep rewrite_k_html.py matched
with open('rewrite_k_html.py', 'w', encoding='utf-8') as f:
    f.write(open('rebuild_anh_ui.py', 'r').read())

print("anh.html rewritten and clean!")
