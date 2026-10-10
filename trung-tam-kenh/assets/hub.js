
// hub.js - Tự động render shell (menu, topbar) cho trang
document.addEventListener('DOMContentLoaded', () => {
    const pageId = document.body.getAttribute('data-page');
    const page = window.HUB.pages.find(p => p.id === pageId);
    if(!page) return;
    
    // Determine relative path depth
    const depth = page.file.split('/').length - 1;
    const rel = '../'.repeat(depth);
    
    // Build topbar stepper
    const flowPages = window.HUB.pages.filter(p => p.group === 'flow');
    const stepperHtml = flowPages.map(p => `
        <a href="${rel}${p.file}" class="${p.id === pageId ? 'on' : ''}">
            <span class="n">${p.n}</span>
            <span class="t">${p.short}</span>
        </a>
    `).join('');

    // Build sidebar menu
    let menuHtml = '';
    for(const g of window.HUB.groups) {
        menuHtml += `<h6>${g.title}</h6>`;
        const gPages = window.HUB.pages.filter(p => p.group === g.id);
        menuHtml += gPages.map(p => `
            <a href="${rel}${p.file}" class="pg ${p.id === pageId ? 'on' : ''}">
                <span class="n">${p.icon}</span>
                <span class="t">${p.title}</span>
            </a>
        `).join('');
    }

    // Lấy nội dung gốc (bỏ vỏ <main> tạm), tách h1 gốc nếu có để không bị lặp tiêu đề
    const srcEl = document.querySelector('.main .content') || document.querySelector('.main');
    const tmp = document.createElement('div');
    tmp.innerHTML = srcEl.innerHTML;
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

    document.body.innerHTML = `
        <div class="topbar">
            <a href="${rel}index.html" class="brand">
                <div class="logo">K</div>
                <div class="t">Hub<small>Kênh &amp; Nhận diện</small></div>
            </a>
            <div class="stepper">${stepperHtml}</div>
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
    // --- Bổ sung Logic tìm kiếm CMD+K và Menu Toggle ---
    const searchBtn = document.querySelector('.searchbtn');
    const menuBtn = document.querySelector('.menubtn');
    
    if(menuBtn) {
        menuBtn.addEventListener('click', () => {
            document.body.classList.toggle('navopen');
        });
    }

    // Modal Template
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
        if(modal.style.display === 'none') {
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
    
    if(searchBtn) searchBtn.addEventListener('click', toggleModal);
    
    document.addEventListener('keydown', (e) => {
        if((e.metaKey || e.ctrlKey) && e.key === 'k') {
            e.preventDefault();
            toggleModal();
        }
        if(e.key === 'Escape' && modal.style.display !== 'none') {
            toggleModal();
        }
        
        if(modal.style.display !== 'none') {
            const items = smResults.querySelectorAll('.sm-item');
            if(e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = (activeIndex + 1) % items.length;
                updateActive(items);
            } else if(e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = (activeIndex - 1 + items.length) % items.length;
                updateActive(items);
            } else if(e.key === 'Enter' && activeIndex >= 0 && items[activeIndex]) {
                items[activeIndex].click();
            }
        }
    });
    
    function updateActive(items) {
        items.forEach((it, idx) => {
            if(idx === activeIndex) {
                it.style.background = '#f1f5f9';
            } else {
                it.style.background = 'transparent';
            }
        });
    }
    
    smInput.addEventListener('input', (e) => {
        const q = e.target.value.toLowerCase().trim();
        if(!q) {
            smResults.innerHTML = '';
            return;
        }
        
        resultsData = [];
        
        // Search in HUB pages
        if(window.HUB && window.HUB.pages) {
            window.HUB.pages.forEach(p => {
                if(p.title.toLowerCase().includes(q) || (p.q && p.q.toLowerCase().includes(q))) {
                    resultsData.push({ type: 'page', title: p.title, url: rel + p.file, context: 'Trang tài liệu' });
                }
            });
        }
        
        // Search in GIAO_AN if available
        if(window.GIAO_AN) {
            window.GIAO_AN.forEach(g => {
                if(g.tieude.toLowerCase().includes(q) || g.vande.toLowerCase().includes(q)) {
                    resultsData.push({ type: 'giao-an', title: g.tieude, url: rel + '11-giao-an.html', context: 'Giáo án' });
                }
            });
        }
        
        renderResults();
    });
    
    function renderResults() {
        activeIndex = -1;
        if(resultsData.length === 0) {
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
