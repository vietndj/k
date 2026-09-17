with open("/Users/vietmac/Documents/CODE/k/anh.html", "r") as f:
    code = f.read()

css_addition = """
        /* Lightbox */
        #lightbox { display: none; position: fixed; z-index: 9999; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0, 0, 0, 0.9); align-items: center; justify-content: center; }
        #lightbox.active { display: flex; }
        #lightbox img { max-width: 90vw; max-height: 90vh; object-fit: contain; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        .lb-btn { position: absolute; background: rgba(255,255,255,0.1); color: white; border: none; width: 50px; height: 50px; border-radius: 50%; font-size: 24px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: background 0.2s; z-index: 10000; }
        .lb-btn:hover { background: rgba(255,255,255,0.3); }
        #lb-prev { left: 20px; }
        #lb-next { right: 20px; }
        #lb-close { top: 20px; right: 20px; }
        .card img { cursor: zoom-in; }
"""
if "/* Lightbox */" not in code:
    code = code.replace("    </style>", css_addition + "    </style>")

js_addition = """
    <!-- Lightbox Modal -->
    <div id="lightbox">
        <button id="lb-close" class="lb-btn">&times;</button>
        <button id="lb-prev" class="lb-btn">&larr;</button>
        <img id="lb-img" src="" alt="Lightbox Image">
        <button id="lb-next" class="lb-btn">&rarr;</button>
    </div>
    <script>
        const images = Array.from(document.querySelectorAll('.card img'));
        const lightbox = document.getElementById('lightbox');
        const lbImg = document.getElementById('lb-img');
        let currentIndex = 0;
        function openLightbox(index) { currentIndex = index; lbImg.src = images[currentIndex].src; lightbox.classList.add('active'); document.body.style.overflow = 'hidden'; }
        function closeLightbox() { lightbox.classList.remove('active'); document.body.style.overflow = ''; }
        function showNext() { currentIndex = (currentIndex + 1) % images.length; lbImg.src = images[currentIndex].src; }
        function showPrev() { currentIndex = (currentIndex - 1 + images.length) % images.length; lbImg.src = images[currentIndex].src; }
        images.forEach((img, index) => { img.addEventListener('click', () => openLightbox(index)); });
        document.getElementById('lb-close').addEventListener('click', closeLightbox);
        document.getElementById('lb-next').addEventListener('click', showNext);
        document.getElementById('lb-prev').addEventListener('click', showPrev);
        lightbox.addEventListener('click', (e) => { if (e.target === lightbox) closeLightbox(); });
        document.addEventListener('keydown', (e) => {
            if (!lightbox.classList.contains('active')) return;
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowRight') showNext();
            if (e.key === 'ArrowLeft') showPrev();
        });
    </script>
"""

if "<!-- Lightbox Modal -->" not in code:
    code = code.replace("    </div>\n</body>\n</html>", js_addition + "    </div>\n</body>\n</html>")

with open("/Users/vietmac/Documents/CODE/k/anh.html", "w") as f:
    f.write(code)

