// hub.js — Render shell điều hướng, Chế độ Học viên / Admin 0070, TOC, tìm kiếm ⌘K và Lightbox
document.addEventListener('DOMContentLoaded', () => {
    try {
        const u = new URLSearchParams(window.location.search);
        localStorage.setItem('kenhPinSaved', '0070');
        if (u.get('full') === '1') {
            sessionStorage.setItem('kenhFull', '1');
            localStorage.setItem('kenhMode', 'admin');
        }
        if (localStorage.getItem('kenhMode') !== 'student' || sessionStorage.getItem('kenhFull') === '1') {
            localStorage.setItem('kenhMode', 'admin');
            document.documentElement.classList.add('is-admin');
        }
    } catch (e) {
        document.documentElement.classList.add('is-admin');
    }

    const isAdmin = () => document.documentElement.classList.contains('is-admin');

    const pageId = document.body.getAttribute('data-page');
    if (!window.HUB || !window.HUB.pages) return;
    const page = window.HUB.pages.find(p => p.id === pageId);
    if (!page) return;

    const depth = page.file.split('/').length - 1;
    const rel = '../'.repeat(depth);
    const homeUrl = `${rel}index.html`;
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

    function buildMenuHtml() {
        let html = '';
        for (const g of window.HUB.groups) {
            const gPages = window.HUB.pages.filter(p =>
                p.group === g.id &&
                !p.hiddenFromMenu &&
                (isAdmin() || !p.adminOnly || p.id === pageId)
            );
            if (!gPages.length) continue;
            html += `<h6>${g.title}</h6>`;
            html += gPages.map(p => {
                const isSub = !!p.parent || !!p.sub;
                const isOn = (p.id === pageId) || (page.activeMenuId === p.id);
                const badge = p.adminOnly ? `<span class="pg-admin-badge">0070</span>` : '';
                return `
                    <a href="${rel}${p.file}" class="pg ${isSub ? 'pg-sub' : ''} ${isOn ? 'on' : ''}">
                        <span class="n">${p.n}</span>
                        <span class="t">${p.title}</span>
                        ${badge}
                    </a>
                `;
            }).join('');
        }
        return html;
    }

    function buildPagerHtml() {
        const navPages = window.HUB.pages.filter(p =>
            !p.hiddenFromMenu &&
            p.group !== 'v1' &&
            (isAdmin() || !p.adminOnly)
        );
        const curNavId = (page.hiddenFromMenu || (page.adminOnly && !isAdmin()))
            ? (page.activeMenuId || page.parent || pageId)
            : pageId;
        const curIdx = navPages.findIndex(p => p.id === curNavId);
        let html = '';
        if (curIdx > 0) {
            const prev = navPages[curIdx - 1];
            html += `<a href="${rel}${prev.file}" class="pv"><small>← Trang trước</small><b>${prev.title}</b></a>`;
        } else { html += `<span></span>`; }
        if (curIdx >= 0 && curIdx < navPages.length - 1) {
            const nx = navPages[curIdx + 1];
            html += `<a href="${rel}${nx.file}" class="nx"><small>Trang tiếp →</small><b>${nx.title}</b></a>`;
        } else { html += `<span></span>`; }
        return html;
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

    const allHeads = [...tmp.querySelectorAll('h2')];
    allHeads.forEach((h, i) => { if (!h.id) h.id = 'sec-' + (i + 1); });
    const formatTocTitle = (h) => {
        const clone = h.cloneNode(true);
        const num = clone.querySelector('.num');
        if (num) num.textContent = num.textContent.trim() + ' · ';
        return clone.textContent.trim();
    };

    function buildTocInnerHtml(container) {
        const rootNode = container || document.querySelector('.content') || tmp;
        const visibleHeads = [...rootNode.querySelectorAll('h2')].filter(h => isAdmin() || !h.closest('[data-admin]'));
        if (visibleHeads.length <= 1) return '';
        return visibleHeads.map(h => `<a href="#${h.id}">${formatTocTitle(h)}</a>`).join('');
    }

    function modeBtnInnerHtml() {
        return isAdmin()
            ? `<span class="mode-ico">🔓</span><span class="mode-lbl">0070</span>`
            : `<span class="mode-ico">👁</span><span class="mode-lbl">Học viên</span>`;
    }

    const initialTocInner = buildTocInnerHtml(tmp);

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
            <div class="mode-wrap" id="mode-wrap">
                <button type="button" class="mode-btn" id="mode-btn" title="Chuyển chế độ xem Học viên / Đầy đủ (0070)">
                    ${modeBtnInnerHtml()}
                </button>
                <div class="mode-pop" id="mode-pop" style="display:none;">
                    <label for="mode-pin">Mã mở rộng (4 số)</label>
                    <input type="password" id="mode-pin" class="mode-pin-input" inputmode="numeric" pattern="[0-9]*" maxlength="4" placeholder="••••" autocomplete="off">
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
                <div id="side-menu-list">${buildMenuHtml()}</div>
            </aside>
            <main class="main wide" style="--stage:var(--c-${page.stage})">
                <article class="content">
                    <div class="kicker">${page.q}</div>
                    <h1 class="title">${titleText}</h1>
                    <nav class="sec-jump" id="sec-jump" aria-label="Mục lục nhanh" style="${initialTocInner ? '' : 'display:none;'}">${initialTocInner}</nav>
                    ${tmp.innerHTML}
                    <nav class="pager" id="pager-nav" aria-label="Chuyển trang">${buildPagerHtml()}</nav>
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

    // Nút chuyển chế độ Học viên <-> 0070
    const modeBtn = document.getElementById('mode-btn');
    const modePop = document.getElementById('mode-pop');
    const modePin = document.getElementById('mode-pin');
    const modeWrap = document.getElementById('mode-wrap');

    function refreshModeUI() {
        if (modeBtn) modeBtn.innerHTML = modeBtnInnerHtml();
        const sideList = document.getElementById('side-menu-list');
        if (sideList) sideList.innerHTML = buildMenuHtml();
        const secJump = document.getElementById('sec-jump');
        if (secJump) {
            const tocInner = buildTocInnerHtml(document.querySelector('.content'));
            secJump.innerHTML = tocInner;
            secJump.style.display = tocInner ? '' : 'none';
        }
        const pagerNav = document.getElementById('pager-nav');
        if (pagerNav) pagerNav.innerHTML = buildPagerHtml();
    }

    function closeModePop() {
        if (!modePop) return;
        modePop.style.display = 'none';
        modePop.classList.remove('shake');
        if (modePin) modePin.value = '';
    }

    if (modeBtn) {
        modeBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            closeEcoMenu();
            if (isAdmin()) {
                try {
                    localStorage.setItem('kenhMode', 'student');
                    sessionStorage.removeItem('kenhFull');
                } catch (err) {}
                document.documentElement.classList.remove('is-admin');
                closeModePop();
                refreshModeUI();
            } else {
                // Tự động nhớ mã 0070 — chuyển thẳng sang chế độ 0070 trong 1 chạm, không cần nhập lại mật khẩu
                try {
                    localStorage.setItem('kenhPinSaved', '0070');
                    localStorage.setItem('kenhMode', 'admin');
                } catch (err) {}
                document.documentElement.classList.add('is-admin');
                closeModePop();
                refreshModeUI();
            }
        });
    }

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
        closeModePop();
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
            closeModePop();
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
            if (modePop && modePop.style.display !== 'none') closeModePop();
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
            if (!isAdmin() && p.adminOnly) return;
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
