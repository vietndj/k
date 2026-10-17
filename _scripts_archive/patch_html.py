import os

path = "build_anh_v2.py"
with open(path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. CSS
css_patch = """        .copy-btn.copied { background: rgba(16,185,129,0.9); }
        
        /* Lightbox Styles */
        .lightbox { display: none; position: fixed; z-index: 1000; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); align-items: center; justify-content: center; backdrop-filter: blur(5px); }
        .lightbox.active { display: flex; }
        .lightbox img { max-width: 90%; max-height: 95vh; object-fit: contain; border-radius: 8px; box-shadow: 0 10px 40px rgba(0,0,0,0.6); }
        .lightbox .close-btn { position: absolute; top: 20px; right: 30px; color: white; font-size: 40px; cursor: pointer; background: none; border: none; font-weight: 300; }
        .img-wrap img { cursor: zoom-in; }"""
code = code.replace(".copy-btn.copied { background: rgba(16,185,129,0.9); }", css_patch)

# 2. HTML
html_patch = """    <div class="grid">
        {''.join(cards_html)}
    </div>

    <!-- Lightbox -->
    <div class="lightbox" id="lightbox" onclick="closeLightbox(event)">
        <button class="close-btn">&times;</button>
        <img id="lightbox-img" src="" alt="Zoomed Poster">
    </div>

    <script>"""
code = code.replace("""    <div class="grid">
        {''.join(cards_html)}
    </div>

    <script>""", html_patch)

# 3. JS
js_patch = """        document.addEventListener('DOMContentLoaded', () => { 
            const s = localStorage.getItem('poster_style') || 'style-b'; 
            setStyle(s); 
        });
        
        // Lightbox Logic
        function openLightbox(src) {
            document.getElementById('lightbox-img').src = src;
            document.getElementById('lightbox').classList.add('active');
            document.body.style.overflow = 'hidden';
        }
        function closeLightbox(e) {
            if (e.target.tagName !== 'IMG') {
                document.getElementById('lightbox').classList.remove('active');
                document.body.style.overflow = '';
            }
        }
        document.querySelectorAll('.img-wrap img').forEach(img => {
            img.addEventListener('click', (e) => {
                openLightbox(e.target.src);
            });
        });"""
code = code.replace("""        document.addEventListener('DOMContentLoaded', () => { 
            const s = localStorage.getItem('poster_style') || 'style-b'; 
            setStyle(s); 
        });""", js_patch)

with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Patched build_anh_v2.py successfully!")
