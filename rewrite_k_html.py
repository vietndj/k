import re

with open('/Users/vietmac/Documents/CODE/k/anh.html', 'r', encoding='utf-8') as f:
    content = f.read()

head_match = re.search(r'(<!DOCTYPE html>.*?</style>\s*</head>\s*<body[^>]*>)', content, re.DOTALL)
if not head_match:
    print("Could not find <head>")
    exit(1)
head_content = head_match.group(1)

additional_styles = """
    .toolbar { background: #1e293b; padding: 16px; display: flex; gap: 16px; align-items: center; border-bottom: 1px solid #334155; flex-wrap: wrap; }
    .toolbar input, .toolbar select { padding: 8px 16px; border-radius: 8px; border: 1px solid #475569; background: #0f172a; color: white; outline: none; font-size: 0.95rem; }
    .toolbar input:focus, .toolbar select:focus { border-color: #3b82f6; }
    .toolbar input { flex-grow: 1; min-width: 200px; }
    .stats { padding: 16px 16px 0 16px; color: #94a3b8; font-size: 0.9rem; display: flex; gap: 16px; flex-wrap: wrap; }
    .stat-badge { background: #334155; padding: 4px 12px; border-radius: 12px; font-weight: 500; color: #e2e8f0; }
"""
head_content = head_content.replace('</style>', additional_styles + '\n</style>')

new_body = """
    <header>
        <div class="header-left">
            <h1>Posters</h1>
            <p id="total-count">Đang tải dữ liệu...</p>
        </div>
        <div class="header-right">
            <button class="style-btn" data-style="style-a" onclick="setStyle('style-a')">Style A (Grid)</button>
            <button class="style-btn" data-style="style-b" onclick="setStyle('style-b')">Style B (Kanban)</button>
        </div>
    </header>

    <div class="toolbar">
        <input type="text" id="searchInput" placeholder="Tìm kiếm theo mã, tiêu đề, nội dung thơ hoặc prompt...">
        <select id="categoryFilter">
            <option value="all">Tất cả thể loại</option>
            <option value="Chưa phân loại">Chưa phân loại</option>
            <option value="Phim Điện Ảnh">Phim Điện Ảnh</option>
            <option value="Anime">Anime</option>
            <option value="Game">Game</option>
        </select>
        <select id="styleFilter">
            <option value="all">Tất cả phong cách</option>
            <option value="Chưa phân loại">Chưa phân loại</option>
            <option value="Cinematic">Cinematic</option>
            <option value="Anime Style">Anime Style</option>
            <option value="3D Render">3D Render</option>
        </select>
    </div>

    <div class="stats" id="statsContainer"></div>

    <div class="grid" id="grid">
        <!-- Cards will be rendered here by JS -->
    </div>

    <!-- Lightbox -->
    <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
        <button class="close-btn" style="position: absolute; top: 20px; right: 20px; font-size: 2rem; background: none; border: none; color: white; cursor: pointer;">&times;</button>
        <img id="lightbox-img" src="" alt="Zoomed Poster" style="max-width: 90%; max-height: 90%; object-fit: contain;">
    </div>

    <script>
        let allPosters = [];

        async function init() {
            try {
                const res = await fetch('database.json');
                const data = await res.json();
                allPosters = data.posters;
                document.getElementById('total-count').textContent = `${data.metadata.total_images} images`;
                renderCards(allPosters);
                renderStats(allPosters);
            } catch (err) {
                console.error('Error loading data:', err);
                document.getElementById('grid').innerHTML = '<p style="padding:16px">Lỗi tải dữ liệu. Cần chạy trên Live Server do lỗi CORS với file JSON cục bộ.</p>';
            }
        }

        function copyPrompt(btn) {
            const text = btn.dataset.prompt;
            navigator.clipboard.writeText(text).then(() => {
                const span = btn.querySelector('span');
                span.textContent = '✓ Copied!';
                btn.classList.add('copied');
                setTimeout(() => { span.textContent = 'Copy Prompt'; btn.classList.remove('copied'); }, 2000);
            });
        }

        function renderCards(posters) {
            const grid = document.getElementById('grid');
            grid.innerHTML = '';
            
            posters.forEach(p => {
                const card = document.createElement('div');
                card.className = p.has_prompt ? 'card has-prompt poem-card' : 'card no-prompt';
                if(p.has_prompt) {
                    card.style.cssText = "display: flex; flex-direction: column; background: #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.4); transition: transform 0.2s;";
                }
                
                let html = `
                  <div class="img-wrap">
                    <img src="${p.image}" loading="lazy" alt="Poster" onclick="openLightbox('${p.image}')" style="cursor:pointer">
                `;
                
                if (p.has_prompt) {
                    // Escape prompt properly for attribute
                    const safePrompt = p.prompt.replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                    html += `
                        <button class="copy-btn" data-prompt="${safePrompt}" onclick="copyPrompt(this)">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg> <span>Copy Prompt</span>
                        </button>
                    `;
                }
                
                html += `</div>`;
                
                if (p.has_prompt) {
                    html += `
                      <div class="poem-content" style="padding: 16px; display: flex; flex-direction: column; gap: 8px; flex: 1;">
                        <div><span style="background: rgba(255,255,255,0.1); color: #94a3b8; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: bold;">${p.id}</span></div>
                        <div style="color: #60a5fa; font-weight: 800; font-size: 0.95rem; text-transform: uppercase; line-height: 1.3;">${p.title}</div>
                        <div style="color: #e2e8f0; font-style: italic; font-size: 0.9rem; line-height: 1.5; margin-top: 4px;">${p.poem.replace(/\\n/g, '<br>')}</div>
                        <div style="margin-top: 12px; font-size: 0.8rem; color: #64748b;">Phim: ${p.movie_reference} | ${p.category} | ${p.style}</div>
                      </div>
                    `;
                } else {
                    html += `<div class="card-label">${p.id}</div>`;
                }
                
                card.innerHTML = html;
                grid.appendChild(card);
            });
        }

        function renderStats(posters) {
            const stats = document.getElementById('statsContainer');
            const movieCounts = {};
            posters.forEach(p => {
                movieCounts[p.movie_reference] = (movieCounts[p.movie_reference] || 0) + 1;
            });
            
            let html = '<strong>Thống kê phim:</strong> ';
            for (const [movie, count] of Object.entries(movieCounts)) {
                html += `<span class="stat-badge">${movie}: ${count}</span>`;
            }
            stats.innerHTML = html;
        }

        function filterData() {
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
        }

        document.getElementById('searchInput').addEventListener('input', filterData);
        document.getElementById('categoryFilter').addEventListener('change', filterData);
        document.getElementById('styleFilter').addEventListener('change', filterData);

        function openLightbox(src) {
            const lb = document.getElementById('lightbox');
            const lbImg = document.getElementById('lightbox-img');
            lbImg.src = src;
            lb.style.display = 'flex';
        }
        
        function closeLightbox(e) {
            if (e.target.id === 'lightbox' || e.target.classList.contains('close-btn')) {
                document.getElementById('lightbox').style.display = 'none';
            }
        }
        
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                document.getElementById('lightbox').style.display = 'none';
            }
        });

        function setStyle(s) { 
            document.body.className = s; 
            localStorage.setItem('poster_style', s); 
            document.querySelectorAll('.style-btn').forEach(b => b.classList.toggle('active', b.dataset.style === s)); 
        }
        
        document.addEventListener('DOMContentLoaded', () => { 
            const s = localStorage.getItem('poster_style') || 'style-b'; 
            setStyle(s); 
            
            // Lightbox initial style
            document.getElementById('lightbox').style.display = 'none';
            document.getElementById('lightbox').style.position = 'fixed';
            document.getElementById('lightbox').style.zIndex = '9999';
            document.getElementById('lightbox').style.top = '0';
            document.getElementById('lightbox').style.left = '0';
            document.getElementById('lightbox').style.width = '100%';
            document.getElementById('lightbox').style.height = '100%';
            document.getElementById('lightbox').style.backgroundColor = 'rgba(0,0,0,0.9)';
            document.getElementById('lightbox').style.alignItems = 'center';
            document.getElementById('lightbox').style.justifyContent = 'center';
        });

        init();
    </script>
</body>
</html>
"""

final_html = head_content + new_body

with open('/Users/vietmac/Documents/CODE/k/anh.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Updated anh.html successfully.")
