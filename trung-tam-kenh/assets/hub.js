// hub.js - Tự động render shell (menu, topbar, hệ sinh thái) cho trang
document.addEventListener('DOMContentLoaded', () => {
    const pageId = document.body.getAttribute('data-page');
    if (!window.HUB || !window.HUB.pages) return;
    const page = window.HUB.pages.find(p => p.id === pageId);
    if (!page) return;
    
    // Determine relative path depth
    const depth = page.file.split('/').length - 1;
    const rel = '../'.repeat(depth);
    const homeUrl = (window.location.protocol === 'file:') ? `${rel}index.html` : '/';
    
    // Build topbar stepper (chỉ lấy các chặng chính !p.parent để giữ stepper tinh gọn)
    const flowPages = window.HUB.pages.filter(p => p.group === 'flow' && !p.parent);
    const stepperHtml = flowPages.map(p => {
        const isActive = (p.id === pageId) || (page.parent === p.id);
        return `
            <a href="${rel}${p.file}" class="${isActive ? 'on' : ''}" title="${p.title}">
                <span class="n">${p.n}</span>
                <span class="t">${p.short}</span>
            </a>
        `;
    }).join('');

    // Build sidebar menu (hỗ trợ menu con pg-sub lồng thụt lề nhẹ)
    let menuHtml = '';
    for (const g of window.HUB.groups) {
        menuHtml += `<h6>${g.title}</h6>`;
        const gPages = window.HUB.pages.filter(p => p.group === g.id);
        menuHtml += gPages.map(p => {
            const isSub = !!p.parent || !!p.sub;
            return `
                <a href="${rel}${p.file}" class="pg ${isSub ? 'pg-sub' : ''} ${p.id === pageId ? 'on' : ''}">
                    <span class="n">${p.icon || p.n}</span>
                    <span class="t">${p.title}</span>
                </a>
            `;
        }).join('');
    }

    // Lấy nội dung gốc (bỏ vỏ <main> tạm), tách h1 gốc nếu có để không bị lặp tiêu đề
    const srcEl = document.querySelector('.main .content') || document.querySelector('.main');
    const tmp = document.createElement('div');
    if (srcEl) {
        tmp.innerHTML = srcEl.innerHTML;
    }
    tmp.querySelectorAll('p:empty').forEach(n => n.remove());
    let h1 = tmp.querySelector('h1');
    let titleText = h1 ? h1.textContent.trim() : page.title;
    titleText = titleText.charAt(0).toLocaleUpperCase('vi') + titleText.slice(1);
    if (h1) {
        const hero = h1.closest('.hero');
        const heroOnlyTitle = hero && hero.children.length === 1;
        (heroOnlyTitle ? hero : h1).remove();
    }
    // Viết hoa chữ đầu tiêu đề / đoạn mở đầu (nguồn đang viết thường)
    const cap = el => { const w=document.createTreeWalker(el,NodeFilter.SHOW_TEXT); let n; while((n=w.nextNode())){ if(n.nodeValue.trim()){ n.nodeValue=n.nodeValue.replace(/^(\s*)(\S)/,(m,a,b)=>a+b.toLocaleUpperCase('vi')); break; } } };
    tmp.querySelectorAll('h2,h3,h4,h5,.hero p,.hero h2').forEach(cap);
    tmp.querySelectorAll('table').forEach(t=>{ if(!t.closest('.tw')){ const w=document.createElement('div'); w.className='tw'; t.replaceWith(w); w.appendChild(t); } });
    // Viết hoa đầu câu trong đoạn văn (nguồn viết thường toàn bộ)
    const U=c=>c.toLocaleUpperCase('vi');
    tmp.querySelectorAll('p,li,td,.callout,blockquote,summary').forEach(blk=>{
        const w=document.createTreeWalker(blk,NodeFilter.SHOW_TEXT); let n,first=true;
        while((n=w.nextNode())){
            if(n.parentElement.closest('code,pre,a,kbd')) { if(n.nodeValue.trim()) first=false; continue; }
            let v=n.nodeValue;
            if(first && v.trim()){ v=v.replace(/^(\s*)(\S)/,(m,a,b)=>a+U(b)); first=false; }
            v=v.replace(/([.!?…]\s+)([a-zà-ỹ])/g,(m,a,b)=>a+U(b));
            n.nodeValue=v;
        }
    });
    // Mục lục "Trên trang này" cho cột phải: gán id cho h2/h3
    const heads = [...tmp.querySelectorAll('h2')];
    heads.forEach((h, i) => { if (!h.id) h.id = 'sec-' + (i + 1); });
    const tocHtml = heads.length > 1
        ? `<h6>Trên trang này</h6><nav class="otp">${heads.map(h => `<a href="#${h.id}">${h.textContent.trim()}</a>`).join('')}</nav>`
        : '';

    // Pager
    const curIdx = window.HUB.pages.findIndex(p => p.id === pageId);
    let pagerHtml = '<nav class="pager" aria-label="Chuyển trang">';
    if (curIdx > 0) {
        const prev = window.HUB.pages[curIdx - 1];
        pagerHtml += `<a href="${rel}${prev.file}" class="pv"><small>← Trang trước</small><b>${prev.title}</b></a>`;
    } else { pagerHtml += `<span></span>`; }
    if (curIdx < window.HUB.pages.length - 1) {
        const nx = window.HUB.pages[curIdx + 1];
        pagerHtml += `<a href="${rel}${nx.file}" class="nx"><small>Trang tiếp →</small><b>${nx.title}</b></a>`;
    } else { pagerHtml += `<span></span>`; }
    pagerHtml += '</nav>';

    // Topbar & Shell injection
    document.body.innerHTML = `
        <div class="topbar">
            <a href="${homeUrl}" class="brand" title="Trang chủ Kênh &amp; Nhận diện (kenh.fedu.vn)">
                <div class="logo">K</div>
                <div class="t">Hub<small>Kênh &amp; Nhận diện</small></div>
            </a>
            <div class="stepper">${stepperHtml}</div>
            <div class="ecosystem-wrap">
                <button type="button" class="ecosystem-btn" id="eco-btn" aria-haspopup="true" aria-expanded="false" title="Khám phá 14 nền tảng FEDU">
                    <span class="eco-btn-text-full">Hệ sinh thái FEDU</span><span class="eco-btn-text-short">🌐 FEDU</span>
                    <span class="eco-caret">▾</span>
                </button>
                <div class="ecosystem-menu" id="eco-menu" style="display:none;">
                    <div class="eco-header">
                        <div>
                            <div class="eco-title">Hệ Sinh Thái FEDU</div>
                            <div class="eco-sub">14 Nền tảng Đào tạo · Sáng tạo · Vận hành · Kênh</div>
                        </div>
                        <span class="eco-tag">FD ECOSYSTEM</span>
                    </div>
                    <div class="eco-grid">
                        <div class="eco-group">
                            <div class="eco-gh">🎓 ĐÀO TẠO</div>
                            <a href="https://offline.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Offline Thực Chiến</span>
                                <span class="eco-desc">offline.fedu.vn · Huấn luyện trực tiếp</span>
                            </a>
                            <a href="https://k3.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Giáo Trình K3</span>
                                <span class="eco-desc">k3.fedu.vn · Giáo trình video thực chiến</span>
                            </a>
                            <a href="https://video.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Online CapCut</span>
                                <span class="eco-desc">video.fedu.vn · Làm chủ dựng video</span>
                            </a>
                            <a href="https://30ngayviral.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">30 Ngày Viral</span>
                                <span class="eco-desc">30ngayviral.fedu.vn · Kỷ luật xây kênh</span>
                            </a>
                            <a href="https://ai.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">AI Sáng Tạo</span>
                                <span class="eco-desc">ai.fedu.vn · Đòn bẩy AI &amp; Tự động hoá</span>
                            </a>
                        </div>

                        <div class="eco-group">
                            <div class="eco-gh">⚡ SÁNG TẠO</div>
                            <a href="https://brollbank.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Kho B-Roll</span>
                                <span class="eco-desc">brollbank.fedu.vn · Footage bản quyền</span>
                            </a>
                            <a href="https://nhac.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Kho Nhạc &amp; SFX</span>
                                <span class="eco-desc">nhac.fedu.vn · Âm thanh &amp; Nhịp dựng</span>
                            </a>
                            <a href="https://ytuong.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Kho Ý Tưởng</span>
                                <span class="eco-desc">ytuong.fedu.vn · Hook &amp; Kịch bản</span>
                            </a>
                            <a href="https://offline.fedu.vn/research" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Research</span>
                                <span class="eco-desc">offline.fedu.vn/research · Thị trường</span>
                            </a>
                        </div>

                        <div class="eco-group">
                            <div class="eco-gh">⚙️ VẬN HÀNH</div>
                            <a href="https://led.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Lead Center</span>
                                <span class="eco-desc">led.fedu.vn · Quản trị chuyển đổi lead</span>
                            </a>
                            <a href="https://stu.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <div class="eco-name-row">
                                    <span class="eco-name">Student Hub</span>
                                    <span class="eco-badge">PIN 0070</span>
                                </div>
                                <span class="eco-desc">stu.fedu.vn · Dữ liệu học viên</span>
                            </a>
                        </div>

                        <div class="eco-group">
                            <div class="eco-gh">🌐 KÊNH &amp; AGENCY</div>
                            <a href="https://fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">FEDU Agency</span>
                                <span class="eco-desc">fedu.vn · Giải pháp video &amp; Kênh</span>
                            </a>
                            <a href="https://vietndj.github.io" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Profile Thầy Việt</span>
                                <span class="eco-desc">vietndj.github.io · Triết lý &amp; Kết nối</span>
                            </a>
                            <a href="https://kenh.fedu.vn" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Trung Tâm Kênh</span>
                                <span class="eco-desc">kenh.fedu.vn · Hub Logic xây kênh</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="searchbtn">TÌM KIẾM <kbd>⌘K</kbd></div>
            <div class="menubtn">☰</div>
        </div>
        <div class="shell">
            <aside class="side">
                <div class="mh">
                    <b>${window.HUB.name}</b>
                    <p>${window.HUB.sub}</p>
                </div>
                ${menuHtml}
            </aside>
            <main class="main${tocHtml ? '' : ' wide'}" style="--stage:var(--c-${page.stage})">
                <article class="content">
                    <div class="kicker">${page.q}</div>
                    <h1 class="title">${titleText}</h1>
                    ${tmp.innerHTML}
                    ${pagerHtml}
                </article>
                ${tocHtml ? `<aside class="rail">${tocHtml}</aside>` : ''}
            </main>
        </div>
    `;

    // --- Xử lý nút Menu Drawer trên Mobile ---
    const menuBtn = document.querySelector('.menubtn');
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            document.body.classList.toggle('navopen');
        });
    }

    // --- Xử lý Dropdown Hệ sinh thái FEDU ---
    const ecoBtn = document.getElementById('eco-btn');
    const ecoMenu = document.getElementById('eco-menu');
    let ecoBackdrop = null;

    function closeEcoMenu() {
        if (!ecoMenu) return;
        ecoMenu.style.display = 'none';
        if (ecoBtn) {
            ecoBtn.classList.remove('active');
            ecoBtn.setAttribute('aria-expanded', 'false');
        }
        if (ecoBackdrop) {
            ecoBackdrop.remove();
            ecoBackdrop = null;
        }
    }

    function openEcoMenu() {
        if (!ecoMenu) return;
        if (typeof modal !== 'undefined' && modal && modal.style.display !== 'none') {
            modal.style.display = 'none';
        }
        ecoMenu.style.display = 'block';
        if (ecoBtn) {
            ecoBtn.classList.add('active');
            ecoBtn.setAttribute('aria-expanded', 'true');
        }
        if (!ecoBackdrop) {
            ecoBackdrop = document.createElement('div');
            ecoBackdrop.className = 'eco-backdrop';
            ecoBackdrop.addEventListener('click', closeEcoMenu);
            document.body.appendChild(ecoBackdrop);
        }
    }

    if (ecoBtn && ecoMenu) {
        ecoBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (ecoMenu.style.display !== 'none') {
                closeEcoMenu();
            } else {
                openEcoMenu();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && ecoMenu.style.display !== 'none') {
                closeEcoMenu();
            }
        });
    }

    // --- Bổ sung Logic tìm kiếm CMD+K và Modal ---
    const searchBtn = document.querySelector('.searchbtn');
    const modalHtml = `
        <div class="sm" id="search-modal" style="display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.5); z-index:9999; align-items:flex-start; justify-content:center; padding-top:10vh;">
            <div style="background:#fff; width:90%; max-width:600px; border-radius:8px; box-shadow:0 10px 25px rgba(0,0,0,0.2); overflow:hidden; display:flex; flex-direction:column;">
                <input type="text" id="sm-input" placeholder="Tìm kiếm trang, bài học, giáo án..." style="width:100%; border:none; padding:15px; font-size:16px; outline:none; border-bottom:1px solid #eee;">
                <div id="sm-results" style="max-height:60vh; overflow-y:auto; padding:10px;"></div>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', modalHtml);
    
    const modal = document.getElementById('search-modal');
    const smInput = document.getElementById('sm-input');
    const smResults = document.getElementById('sm-results');
    
    let activeIndex = -1;
    let resultsData = [];
    
    function toggleModal() {
        if (modal.style.display === 'none') {
            closeEcoMenu();
            modal.style.display = 'flex';
            smInput.value = '';
            smResults.innerHTML = '';
            smInput.focus();
            activeIndex = -1;
            resultsData = [];
        } else {
            modal.style.display = 'none';
        }
    }
    
    if (searchBtn) searchBtn.addEventListener('click', toggleModal);
    
    document.addEventListener('keydown', (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
            e.preventDefault();
            toggleModal();
        }
        if (e.key === 'Escape' && modal.style.display !== 'none') {
            toggleModal();
        }
        
        if (modal.style.display !== 'none') {
            const items = smResults.querySelectorAll('.sm-item');
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = (activeIndex + 1) % items.length;
                updateActive(items);
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = (activeIndex - 1 + items.length) % items.length;
                updateActive(items);
            } else if (e.key === 'Enter' && activeIndex >= 0 && items[activeIndex]) {
                items[activeIndex].click();
            }
        }
    });
    
    function updateActive(items) {
        items.forEach((it, idx) => {
            if (idx === activeIndex) {
                it.style.background = '#f1f5f9';
            } else {
                it.style.background = 'transparent';
            }
        });
    }
    
    smInput.addEventListener('input', (e) => {
        const q = e.target.value.toLowerCase().trim();
        if (!q) {
            smResults.innerHTML = '';
            return;
        }
        
        resultsData = [];
        
        // Search in HUB pages
        if (window.HUB && window.HUB.pages) {
            window.HUB.pages.forEach(p => {
                if (p.title.toLowerCase().includes(q) || (p.q && p.q.toLowerCase().includes(q))) {
                    resultsData.push({ type: 'page', title: p.title, url: rel + p.file, context: 'Trang tài liệu' });
                }
            });
        }
        
        // Search in GIAO_AN if available
        if (window.GIAO_AN) {
            window.GIAO_AN.forEach(g => {
                if (g.tieude.toLowerCase().includes(q) || g.vande.toLowerCase().includes(q)) {
                    resultsData.push({ type: 'giao-an', title: g.tieude, url: rel + '11-giao-an.html', context: 'Giáo án' });
                }
            });
        }
        
        renderResults();
    });
    
    function renderResults() {
        activeIndex = -1;
        if (resultsData.length === 0) {
            smResults.innerHTML = '<div style="padding:15px; color:#64748b;">Không tìm thấy kết quả.</div>';
            return;
        }
        
        smResults.innerHTML = resultsData.map((r, i) => `
            <a href="${r.url}" class="sm-item" style="display:block; padding:10px 15px; text-decoration:none; color:#0f172a; border-radius:6px; margin-bottom:5px;">
                <div style="font-weight:600;">${r.title}</div>
                <div style="font-size:12px; color:#64748b;">${r.context}</div>
            </a>
        `).join('');
    }

});
