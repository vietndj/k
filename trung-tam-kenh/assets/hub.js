// hub.js — Render shell điều hướng, TOC, tìm kiếm ⌘K và Lightbox xem ảnh Timeline
document.addEventListener('DOMContentLoaded', () => {
    const pageId = document.body.getAttribute('data-page');
    if (!window.HUB || !window.HUB.pages) return;
    const page = window.HUB.pages.find(p => p.id === pageId);
    if (!page) return;

    const depth = page.file.split('/').length - 1;
    const rel = '../'.repeat(depth);
    const homeUrl = (window.location.protocol === 'file:') ? `${rel}index.html` : '/';
    const L = window.LINKS || {};

    // Topbar stepper (chỉ lấy các chặng chính của flow)
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

    // Sidebar menu
    let menuHtml = '';
    for (const g of window.HUB.groups) {
        menuHtml += `<h6>${g.title}</h6>`;
        const gPages = window.HUB.pages.filter(p => p.group === g.id && !p.hiddenFromMenu);
        menuHtml += gPages.map(p => {
            const isSub = !!p.parent || !!p.sub;
            const isOn = (p.id === pageId) || (page.activeMenuId === p.id);
            return `
                <a href="${rel}${p.file}" class="pg ${isSub ? 'pg-sub' : ''} ${isOn ? 'on' : ''}">
                    <span class="n">${p.n}</span>
                    <span class="t">${p.title}</span>
                </a>
            `;
        }).join('');
    }

    // Tách nội dung bài viết
    const mainEl = document.querySelector('.main');
    const tmp = document.createElement('div');
    if (mainEl) {
        const contentEl = mainEl.querySelector('.content');
        if (contentEl) {
            let combinedHtml = contentEl.innerHTML;
            let sibling = contentEl.nextElementSibling;
            while (sibling) {
                combinedHtml += sibling.outerHTML;
                sibling = sibling.nextElementSibling;
            }
            tmp.innerHTML = combinedHtml;
        } else {
            tmp.innerHTML = mainEl.innerHTML;
        }
    }
    tmp.querySelectorAll('p:empty').forEach(n => n.remove());
    const h1 = tmp.querySelector('h1');
    let titleText = h1 ? h1.textContent.trim() : page.title;
    titleText = titleText.charAt(0).toLocaleUpperCase('vi') + titleText.slice(1);
    if (h1) {
        const hero = h1.closest('.hero');
        const heroOnlyTitle = hero && hero.children.length === 1;
        (heroOnlyTitle ? hero : h1).remove();
    }

    // Bọc bảng cuộn ngang mượt trên điện thoại
    tmp.querySelectorAll('table').forEach(t => {
        if (!t.closest('.tw') && !t.closest('.matrix-wrap') && !t.closest('.rubric-interactive')) {
            const w = document.createElement('div');
            w.className = 'tw';
            t.replaceWith(w);
            w.appendChild(t);
        }
    });

    // Thanh mục lục nhanh đặt gọn ngay dưới tiêu đề (bỏ cột phải để mở rộng không gian xem ảnh)
    const heads = [...tmp.querySelectorAll('h2')];
    heads.forEach((h, i) => { if (!h.id) h.id = 'sec-' + (i + 1); });
    const formatTocTitle = (h) => {
        const clone = h.cloneNode(true);
        const num = clone.querySelector('.num');
        if (num) num.textContent = num.textContent.trim() + ' · ';
        return clone.textContent.trim();
    };
    const tocHtml = heads.length > 1
        ? `<nav class="sec-jump" aria-label="Mục lục nhanh">${heads.map(h => `<a href="#${h.id}">${formatTocTitle(h)}</a>`).join('')}</nav>`
        : '';

    // Pager chuyển trang
    const navPages = window.HUB.pages.filter(p => !p.hiddenFromMenu && p.group !== 'v1');
    const curNavId = page.hiddenFromMenu ? (page.activeMenuId || page.parent || pageId) : pageId;
    const curIdx = navPages.findIndex(p => p.id === curNavId);
    let pagerHtml = '<nav class="pager" aria-label="Chuyển trang">';
    if (curIdx > 0) {
        const prev = navPages[curIdx - 1];
        pagerHtml += `<a href="${rel}${prev.file}" class="pv"><small>← Trang trước</small><b>${prev.title}</b></a>`;
    } else { pagerHtml += `<span></span>`; }
    if (curIdx >= 0 && curIdx < navPages.length - 1) {
        const nx = navPages[curIdx + 1];
        pagerHtml += `<a href="${rel}${nx.file}" class="nx"><small>Trang tiếp →</small><b>${nx.title}</b></a>`;
    } else { pagerHtml += `<span></span>`; }
    pagerHtml += '</nav>';

    document.body.innerHTML = `
        <div class="topbar">
            <a href="${homeUrl}" class="brand" title="Trang chủ Logic Xây Kênh">
                <div class="logo">K</div>
                <div class="t">Logic Kênh<small>Nguyễn Đức Việt</small></div>
            </a>
            <div class="stepper">${stepperHtml}</div>
            <div class="ecosystem-wrap">
                <button type="button" class="ecosystem-btn" id="eco-btn" aria-haspopup="true" aria-expanded="false">
                    <span class="eco-btn-text-full">Công cụ &amp; Khóa học</span><span class="eco-btn-text-short">Công cụ</span>
                    <span class="eco-caret">▾</span>
                </button>
                <div class="ecosystem-menu" id="eco-menu" style="display:none;">
                    <div class="eco-header">
                        <div>
                            <div class="eco-title">Công Cụ Làm Kênh &amp; Đào Tạo</div>
                            <div class="eco-sub">Kho nguyên liệu thực hành và chương trình huấn luyện của Nguyễn Đức Việt</div>
                        </div>
                        <span class="eco-tag">NGUYỄN ĐỨC VIỆT</span>
                    </div>
                    <div class="eco-grid">
                        <div class="eco-group">
                            <div class="eco-gh">CÔNG CỤ THỰC HÀNH</div>
                            <a href="${L.ytuong || '#'}" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Kho Ý Tưởng &amp; Góc Quay</span>
                                <span class="eco-desc">Mẫu mở đầu 3 giây và cấu trúc video quốc tế</span>
                            </a>
                            <a href="${L.broll || '#'}" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Kho Cảnh Quay B-Roll</span>
                                <span class="eco-desc">Tư liệu cảnh chèn minh họa sắc nét</span>
                            </a>
                            <a href="${L.nhac || '#'}" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Kho Nhạc Nền &amp; Âm Thanh</span>
                                <span class="eco-desc">Nhạc nền giữ nhịp cảm xúc theo định dạng</span>
                            </a>
                        </div>
                        <div class="eco-group">
                            <div class="eco-gh">ĐÀO TẠO &amp; HỒ SƠ</div>
                            <a href="${L.offline || '#'}" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Huấn Luyện Trực Tiếp (Offline)</span>
                                <span class="eco-desc">Cầm tay chỉ việc quay dựng và định hướng kênh</span>
                            </a>
                            <a href="${L.online || '#'}" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Khóa Dựng Video Thực Chiến (Online)</span>
                                <span class="eco-desc">Tự quay dựng bằng điện thoại cho người bận rộn</span>
                            </a>
                            <a href="${L.profile || '#'}" target="_blank" rel="noopener noreferrer" class="eco-item">
                                <span class="eco-name">Hồ Sơ Nguyễn Đức Việt</span>
                                <span class="eco-desc">Kênh cá nhân và thông tin liên hệ trực tiếp</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
            <div class="searchbtn">TÌM KIẾM <kbd>⌘K</kbd></div>
            <div class="menubtn" aria-label="Mở danh mục">☰</div>
        </div>
        <div class="shell">
            <aside class="side">
                <div class="mh">
                    <b>${window.HUB.name}</b>
                    <p>${window.HUB.sub}</p>
                </div>
                ${menuHtml}
            </aside>
            <main class="main wide" style="--stage:var(--c-${page.stage})">
                <article class="content">
                    <div class="kicker">${page.q}</div>
                    <h1 class="title">${titleText}</h1>
                    ${tocHtml}
                    ${tmp.innerHTML}
                    ${pagerHtml}
                </article>
            </main>
        </div>
    `;

    // Kích hoạt lại các script nội tuyến bên trong .content
    document.querySelectorAll('.content script').forEach(oldScript => {
        const newScript = document.createElement('script');
        Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));
        newScript.textContent = oldScript.textContent;
        oldScript.parentNode.replaceChild(newScript, oldScript);
    });

    // Menu Drawer trên điện thoại
    const menuBtn = document.querySelector('.menubtn');
    if (menuBtn) {
        menuBtn.addEventListener('click', () => {
            document.body.classList.toggle('navopen');
        });
    }

    // Dropdown Công cụ & Khóa học
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
        if (modal && modal.style.display !== 'none') modal.style.display = 'none';
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
            if (ecoMenu.style.display !== 'none') closeEcoMenu();
            else openEcoMenu();
        });
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && ecoMenu.style.display !== 'none') closeEcoMenu();
        });
    }

    // Tìm kiếm nhanh ⌘K
    const searchBtn = document.querySelector('.searchbtn');
    document.body.insertAdjacentHTML('beforeend', `
        <div class="sm" id="search-modal" style="display:none;">
            <div class="box">
                <input type="text" id="sm-input" placeholder="Gõ từ khóa cần tìm (ví dụ: 7 giờ, lurker, góc máy, tầng 2.5)...">
                <div class="res" id="sm-results"></div>
            </div>
        </div>
        <div class="tl-lightbox" id="tl-lightbox" style="display:none;" role="dialog" aria-modal="true">
            <div class="tl-lightbox__inner">
                <img id="tl-lightbox-img" src="" alt="">
                <div class="tl-lightbox__cap" id="tl-lightbox-cap"></div>
            </div>
        </div>
    `);

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
    modal.addEventListener('click', (e) => { if (e.target === modal) toggleModal(); });

    document.addEventListener('keydown', (e) => {
        if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
            e.preventDefault();
            toggleModal();
        }
        if (e.key === 'Escape') {
            if (modal.style.display !== 'none') toggleModal();
            if (lb && lb.style.display !== 'none') lb.style.display = 'none';
        }
        if (modal.style.display !== 'none') {
            const items = smResults.querySelectorAll('a');
            if (!items.length) return;
            if (e.key === 'ArrowDown') {
                e.preventDefault();
                activeIndex = (activeIndex + 1) % items.length;
                items.forEach((it, idx) => it.classList.toggle('sel', idx === activeIndex));
            } else if (e.key === 'ArrowUp') {
                e.preventDefault();
                activeIndex = (activeIndex - 1 + items.length) % items.length;
                items.forEach((it, idx) => it.classList.toggle('sel', idx === activeIndex));
            } else if (e.key === 'Enter' && activeIndex >= 0 && items[activeIndex]) {
                items[activeIndex].click();
            }
        }
    });

    smInput.addEventListener('input', (e) => {
        const q = e.target.value.toLowerCase().trim();
        if (!q) { smResults.innerHTML = ''; return; }
        resultsData = [];
        window.HUB.pages.forEach(p => {
            if (p.title.toLowerCase().includes(q) || (p.q && p.q.toLowerCase().includes(q))) {
                resultsData.push({ title: `${p.n} · ${p.title}`, url: rel + p.file, context: p.q || '' });
            }
        });
        activeIndex = -1;
        smResults.innerHTML = resultsData.length
            ? resultsData.map(r => `<a href="${r.url}"><b>${r.title}</b><span>${r.context}</span></a>`).join('')
            : '<div class="dyn-empty" style="margin:8px;">Không tìm thấy bài phù hợp.</div>';
    });

    // Lightbox 1 chạm cho mọi thẻ ảnh trong Timeline (.tl__img)
    const lb = document.getElementById('tl-lightbox');
    const lbImg = document.getElementById('tl-lightbox-img');
    const lbCap = document.getElementById('tl-lightbox-cap');
    document.addEventListener('click', (e) => {
        const a = e.target.closest('a.tl__img');
        if (!a) return;
        e.preventDefault();
        const img = a.querySelector('img');
        const note = a.parentElement ? a.parentElement.querySelector('.tl__note') : null;
        const num = a.querySelector('.tl__n');
        lbImg.src = a.getAttribute('href') || (img ? img.src : '');
        lbCap.textContent = (num ? num.textContent + ' · ' : '') + (note ? note.textContent : (img ? img.alt : ''));
        lb.style.display = 'flex';
    });
    if (lb) {
        lb.addEventListener('click', () => { lb.style.display = 'none'; lbImg.src = ''; });
    }
});
