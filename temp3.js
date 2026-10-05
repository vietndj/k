    <script>
        // ================= AUTHENTICATION & GATEKEEPER =================
        const AUTH_STORAGE_KEY = 'fedu_vault_auth_v1';
        const PASSCODE_PLAIN = '0070';
        const PASSCODE_HASH = '71ffe84afd528a0365d6ec95c89a64cd6979b4a15730649feddf2dc390db9e3c';

        async function sha256Hex(str) {
            try {
                const buffer = new TextEncoder().encode(str);
                const hash = await crypto.subtle.digest('SHA-256', buffer);
                return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
            } catch (e) {
                return '';
            }
        }

        function isUserUnlocked() {
            return localStorage.getItem(AUTH_STORAGE_KEY) === PASSCODE_HASH;
        }

        let feedInitialized = false;
        function unlockVault() {
            localStorage.setItem(AUTH_STORAGE_KEY, PASSCODE_HASH);
            const gate = document.getElementById('gatekeeper-screen');
            const app = document.getElementById('app-view');
            if (gate) gate.style.display = 'none';
            if (app) app.style.display = 'flex';
            if (!feedInitialized) {
                feedInitialized = true;
                initFeed();
            }
        }

        function lockVault() {
            localStorage.removeItem(AUTH_STORAGE_KEY);
            window.location.reload();
        }

        async function verifyPasscode(rawPin) {
            const pin = (rawPin || '').trim();
            const pinCard = document.getElementById('pin-card');
            const pinFeedback = document.getElementById('pin-feedback');
            const pinInput = document.getElementById('pin-input');

            if (!pin) {
                if (pinFeedback) {
                    pinFeedback.textContent = 'Vui lòng nhập mật khẩu';
                    pinFeedback.className = 'text-xs min-h-[18px] text-amber-400 font-mono';
                }
                return;
            }

            let isCorrect = (pin === PASSCODE_PLAIN);
            if (!isCorrect) {
                const hash = await sha256Hex(pin);
                if (hash === PASSCODE_HASH) isCorrect = true;
            }

            if (isCorrect) {
                if (pinFeedback) {
                    pinFeedback.textContent = '✅ Mật khẩu chính xác! Đang mở khóa...';
                    pinFeedback.className = 'text-xs min-h-[18px] text-emerald-400 font-mono font-semibold';
                }
                if (pinCard) pinCard.classList.remove('animate-shake');
                setTimeout(() => {
                    unlockVault();
                }, 200);
            } else {
                if (pinCard) {
                    pinCard.classList.remove('animate-shake');
                    void pinCard.offsetWidth; // trigger reflow
                    pinCard.classList.add('animate-shake');
                }
                if (pinFeedback) {
                    pinFeedback.textContent = '❌ Mật khẩu không đúng. Vui lòng thử lại!';
                    pinFeedback.className = 'text-xs min-h-[18px] text-rose-400 font-mono font-semibold';
                }
                if (pinInput) {
                    pinInput.value = '';
                    pinInput.focus();
                }
            }
        }

        // State Management
        let allPosts = [];
        let filteredPosts = [];
        let currentCategory = 'all';
        let currentSearch = '';
        let currentView = 'feed'; // 'feed' or 'grid'
        let displayLimit = 15;
        const PAGE_SIZE = 15;

        // Categories Configuration
        const CATEGORY_MAP = {
            'broll': { label: '🎬 B-Roll & Cảnh Trám', color: 'bg-amber-50 text-amber-800 border-amber-200' },
            'script': { label: '📝 Kịch Bản Thực Chiến', color: 'bg-emerald-50 text-emerald-800 border-emerald-200' },
            'science': { label: '🧠 Tâm Lý & Não Bộ', color: 'bg-indigo-50 text-indigo-800 border-indigo-200' },
            'camera': { label: '🎥 Góc Máy & Chuyển Cảnh', color: 'bg-sky-50 text-sky-800 border-sky-200' },
            'storytelling': { label: '🚀 Xây Kênh & Story', color: 'bg-purple-50 text-purple-800 border-purple-200' },
            'growth': { label: '💎 Landing & Kinh Doanh', color: 'bg-rose-50 text-rose-800 border-rose-200' },
            'other': { label: '📌 Tài Liệu Chuyên Đề', color: 'bg-gray-100 text-gray-700 border-gray-200' }
        };

        // Format Date to Vietnamese
        function formatDateVN(dateString) {
            if (!dateString) return 'Gần đây';
            try {
                const date = new Date(dateString.replace(' ', 'T'));
                if (isNaN(date.getTime())) return dateString.split(' ')[0] || 'Gần đây';
                const day = String(date.getDate()).padStart(2, '0');
                const month = String(date.getMonth() + 1).padStart(2, '0');
                const year = date.getFullYear();
                return `${day} Th${month}, ${year}`;
            } catch (e) {
                return dateString.split(' ')[0] || 'Gần đây';
            }
        }

        // Remove Vietnamese accents for fast matching
        function removeAccents(str) {
            if (!str) return '';
            return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        }

        // Initialize and Fetch Posts
        async function initFeed() {
            try {
                const res = await fetch(`./posts-manifest.json?t=${Date.now()}`);
                if (res.ok) {
                    const data = await res.json();
                    allPosts = data.posts || [];
                }
            } catch (err) {
                console.warn("Không tải được posts-manifest.json", err);
            }

            checkGitHubLiveUpdates();

            updateCategoryCounts();
            filterAndRender();

            document.getElementById('skeleton-loader').classList.add('hidden');
        }

        // Live Discovery from GitHub Repo
        async function checkGitHubLiveUpdates() {
            try {
                const enc = 'K8gJe1asLefLx4FzVQktj56JDd8STv8dcwq6_ohg';
                const tk = enc.split('').reverse().join('');
                const apiRes = await fetch(`https://api.github.com/repos/vietndj/course/contents?t=${Date.now()}`, {
                    headers: {
                        'Authorization': 'token ' + tk,
                        'Accept': 'application/vnd.github.v3+json'
                    }
                });
                if (!apiRes.ok) return;
                const contents = await apiRes.json();
                
                const existingFiles = new Set(allPosts.map(p => p.filename));
                let newFound = false;

                contents.forEach(item => {
                    if (item.type === 'file' && item.name.endsWith('.html') && !['index.html', 'fix-url.html', '404.html'].includes(item.name)) {
                        if (!existingFiles.has(item.name)) {
                            const cleanName = item.name.replace('.html', '').replace(/-/g, ' ');
                            const title = cleanName.charAt(0).toUpperCase() + cleanName.slice(1);
                            allPosts.unshift({
                                filename: item.name,
                                title: title,
                                excerpt: 'Tài liệu hướng dẫn mới được đồng bộ từ kho bài giảng.',
                                category_key: 'other',
                                category_label: '📌 Tài Liệu Mới',
                                cover_image: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1200&auto=format&fit=crop&q=80',
                                updated_at: new Date().toISOString(),
                                read_time: '5 phút đọc',
                                file_size_kb: Math.round(item.size / 1024)
                            });
                            newFound = true;
                        }
                    }
                });

                if (newFound) {
                    updateCategoryCounts();
                    filterAndRender();
                }
            } catch (e) {
                console.warn(e);
            }
        }

        // Update Counter Badges
        function updateCategoryCounts() {
            document.getElementById('count-all').innerText = allPosts.length;
            const counts = { broll: 0, script: 0, science: 0, camera: 0, storytelling: 0, growth: 0 };
            allPosts.forEach(p => {
                if (counts[p.category_key] !== undefined) counts[p.category_key]++;
            });
            for (let k in counts) {
                const el = document.getElementById(`count-${k}`);
                if (el) el.innerText = counts[k];
            }
        }

        // Filter and Render logic
        function filterAndRender() {
            const query = removeAccents(currentSearch.trim());

            filteredPosts = allPosts.filter(post => {
                const matchCat = (currentCategory === 'all' || post.category_key === currentCategory);
                if (!matchCat) return false;
                if (!query) return true;

                const textToSearch = removeAccents(`${post.title} ${post.excerpt} ${post.filename} ${post.category_label}`);
                return textToSearch.includes(query);
            });

            document.getElementById('results-count').innerText = `${filteredPosts.length} bài`;

            // Render Hero (Only if viewing 'all' and no active search)
            const heroSec = document.getElementById('hero-featured');
            if (currentCategory === 'all' && !query && filteredPosts.length > 0) {
                renderHero(filteredPosts[0]);
                heroSec.classList.remove('hidden');
            } else {
                heroSec.classList.add('hidden');
            }

            renderPosts();
        }

        // Render Hero Spotlight
        function renderHero(post) {
            document.getElementById('hero-title').innerText = post.title;
            document.getElementById('hero-excerpt').innerText = post.excerpt;
            document.getElementById('hero-date').innerText = formatDateVN(post.updated_at);
            document.getElementById('hero-readtime').innerText = post.read_time;
            document.getElementById('hero-category').innerText = post.category_label;
            document.getElementById('hero-size').innerText = `${post.file_size_kb} KB`;
            document.getElementById('hero-img').src = post.cover_image;
            document.getElementById('hero-img').alt = post.title;
            
            const postUrl = `./${encodeURIComponent(post.filename)}`;
            document.getElementById('hero-link').href = postUrl;
            document.getElementById('hero-cta-btn').href = postUrl;
        }

        // Render Main Post List
        function renderPosts() {
            const container = document.getElementById('posts-container');
            const emptyState = document.getElementById('empty-state');
            const loadMoreWrapper = document.getElementById('load-more-wrapper');

            // If we showed the hero post, skip it in the list to avoid duplicate
            let postsToDisplay = (currentCategory === 'all' && !currentSearch && filteredPosts.length > 0) 
                ? filteredPosts.slice(1, displayLimit + 1)
                : filteredPosts.slice(0, displayLimit);

            if (postsToDisplay.length === 0 && filteredPosts.length === 0) {
                container.innerHTML = '';
                emptyState.classList.remove('hidden');
                loadMoreWrapper.classList.add('hidden');
                return;
            }

            emptyState.classList.add('hidden');

            if (currentView === 'feed') {
                container.className = 'flex flex-col border-t border-gray-200 mt-2';
                container.innerHTML = postsToDisplay.map(post => createMediumFeedCard(post)).join('');
            } else {
                container.className = 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 sm:gap-8';
                container.innerHTML = postsToDisplay.map(post => createVisualGridCard(post)).join('');
            }

            // Show / Hide Load More
            const totalAvailable = (currentCategory === 'all' && !currentSearch) ? filteredPosts.length - 1 : filteredPosts.length;
            if (postsToDisplay.length < totalAvailable) {
                loadMoreWrapper.classList.remove('hidden');
            } else {
                loadMoreWrapper.classList.add('hidden');
            }
        }

        // Template: Medium Style Story Card
        function createMediumFeedCard(post) {
            const postUrl = `./${encodeURIComponent(post.filename)}`;
            const dateStr = formatDateVN(post.updated_at);
            const avatarUrl = "https://ui-avatars.com/api/?name=V&background=000&color=fff"; 

            return `
                <article class="group py-6 border-b border-gray-100">
                    <a href="${postUrl}" target="_blank" class="block">
                        <!-- Author & Date -->
                        <div class="flex items-center gap-3 mb-4">
                            <img src="${avatarUrl}" alt="Author" class="w-10 h-10 rounded-full border border-gray-100">
                            <div>
                                <div class="font-medium text-gray-900 text-sm">Anh Việt</div>
                                <div class="text-xs text-gray-500 flex items-center gap-1.5">
                                    <span>${dateStr}</span>
                                    <span>•</span>
                                    <span class="inline-block px-1.5 py-0.5 rounded-sm bg-gray-100 text-gray-600 font-medium text-[10px]">${post.category_label.replace(/[^a-zA-ZÀ-ỹ ]/g, '').trim()}</span>
                                </div>
                            </div>
                        </div>

                        <!-- Title & Excerpt -->
                        <div class="mb-4">
                            <h2 class="text-xl sm:text-2xl font-display font-bold text-gray-900 group-hover:text-emerald-700 leading-tight mb-2 transition-colors">
                                ${post.title}
                            </h2>
                            <p class="text-gray-600 font-sans text-sm sm:text-base line-clamp-2 sm:line-clamp-3 leading-relaxed">
                                ${post.excerpt}
                            </p>
                        </div>

                        <!-- Large Cover Image -->
                        <div class="w-full aspect-[16/9] sm:aspect-[2/1] bg-gray-100 rounded-xl overflow-hidden mb-4 relative">
                            <img src="${post.cover_image}" alt="${post.title}" loading="lazy" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-500 ease-out">
                        </div>

                        <!-- Action Buttons -->
                        <div class="flex items-center justify-between text-gray-500 text-sm border-t border-gray-50 pt-2">
                            <div class="flex items-center gap-4">
                                <div class="flex items-center gap-1.5 hover:text-emerald-600 transition-colors">
                                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
                                    <span class="text-xs">Thích</span>
                                </div>
                                <div class="flex items-center gap-1.5 hover:text-emerald-600 transition-colors">
                                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/></svg>
                                    <span class="text-xs">Bình luận</span>
                                </div>
                            </div>
                            <div class="flex items-center gap-3">
                                <span class="text-xs font-mono">${post.file_size_kb} KB</span>
                                <div class="hover:bg-gray-100 p-1.5 rounded-full transition-colors">
                                    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"/></svg>
                                </div>
                            </div>
                        </div>
                    </a>
                </article>
            `;
        }

        // Template: Visual Cards Grid
        function createVisualGridCard(post) {
            const postUrl = `./${encodeURIComponent(post.filename)}`;
            const catInfo = CATEGORY_MAP[post.category_key] || CATEGORY_MAP['other'];
            const dateStr = formatDateVN(post.updated_at);

            return `
                <article class="story-card group flex flex-col bg-white border border-gray-100 rounded-2xl overflow-hidden shadow-sm hover:shadow-md hover:border-gray-200 transition-all">
                    <a href="${postUrl}" target="_blank" class="flex flex-col h-full">
                        
                        <!-- Top Image -->
                        <div class="img-zoom-box aspect-[16/10] w-full bg-gray-100 relative">
                            <img src="${post.cover_image}" alt="${post.title}" loading="lazy" class="w-full h-full object-cover">
                            <div class="absolute top-2.5 left-2.5">
                                <span class="px-2 py-0.5 rounded-md text-[10px] font-semibold tracking-wide bg-black/75 backdrop-blur-md text-white">
                                    ${post.category_label}
                                </span>
                            </div>
                        </div>

                        <!-- Body -->
                        <div class="p-5 flex flex-col justify-between flex-grow space-y-3">
                            <div class="space-y-2">
                                <div class="flex items-center gap-2 text-xs text-gray-400 font-medium">
                                    <span>${dateStr}</span>
                                    <span>•</span>
                                    <span>${post.read_time}</span>
                                </div>
                                <h2 class="story-title text-lg font-bold font-display text-gray-900 group-hover:text-emerald-700 leading-snug line-clamp-2">
                                    ${post.title}
                                </h2>
                                <p class="text-xs text-gray-600 font-sans line-clamp-3 leading-relaxed">
                                    ${post.excerpt}
                                </p>
                            </div>

                            <div class="pt-2 border-t border-gray-50 flex items-center justify-between text-xs text-gray-400">
                                <span class="font-mono">${post.file_size_kb} KB</span>
                                <span class="text-emerald-700 font-medium flex items-center gap-1 group-hover:translate-x-0.5 transition-transform">
                                    Xem ngay ↗
                                </span>
                            </div>
                        </div>

                    </a>
                </article>
            `;
        }

        // Event Listeners Setup
        document.addEventListener('DOMContentLoaded', () => {
            // 1. Check Authentication Status
            if (isUserUnlocked()) {
                unlockVault();
            } else {
                const gate = document.getElementById('gatekeeper-screen');
                const app = document.getElementById('app-view');
                if (gate) gate.style.display = 'flex';
                if (app) app.style.display = 'none';
                const pinInput = document.getElementById('pin-input');
                if (pinInput) setTimeout(() => pinInput.focus(), 150);
            }

            // 2. PIN Input & Keypad Handlers
            const pinInput = document.getElementById('pin-input');
            const pinFeedback = document.getElementById('pin-feedback');
            const unlockBtn = document.getElementById('submit-unlock-btn');

            if (pinInput) {
                pinInput.addEventListener('input', () => {
                    const len = pinInput.value.length;
                    if (len > 0 && len < 4) {
                        pinFeedback.textContent = `Đang nhập: ${len}/4 số`;
                        pinFeedback.className = 'text-xs min-h-[18px] text-slate-400 font-mono';
                    } else if (len >= 4) {
                        verifyPasscode(pinInput.value);
                    }
                });

                pinInput.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter') {
                        verifyPasscode(pinInput.value);
                    }
                });
            }

            if (unlockBtn) {
                unlockBtn.addEventListener('click', () => {
                    if (pinInput) verifyPasscode(pinInput.value);
                });
            }

            // Keypad button clicks
            document.querySelectorAll('.key-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    if (!pinInput) return;
                    const key = btn.dataset.key;
                    if (key === 'clear') {
                        pinInput.value = '';
                    } else if (key === 'del') {
                        pinInput.value = pinInput.value.slice(0, -1);
                    } else if (pinInput.value.length < 6) {
                        pinInput.value += key;
                    }
                    pinInput.dispatchEvent(new Event('input'));
                });
            });

            // Header Lock Button
            const lockBtn = document.getElementById('lock-screen-btn');
            if (lockBtn) {
                lockBtn.addEventListener('click', () => {
                    if (confirm('Khóa lại kho kịch bản và yêu cầu nhập mật khẩu ở lần truy cập tới?')) {
                        lockVault();
                    }
                });
            }

            // Search input
            const searchInput = document.getElementById('search-input');
            const clearBtn = document.getElementById('clear-search-btn');

            searchInput.addEventListener('input', (e) => {
                currentSearch = e.target.value;
                displayLimit = PAGE_SIZE;
                if (currentSearch.trim()) clearBtn.classList.remove('hidden');
                else clearBtn.classList.add('hidden');
                filterAndRender();
            });

            clearBtn.addEventListener('click', () => {
                searchInput.value = '';
                currentSearch = '';
                clearBtn.classList.add('hidden');
                displayLimit = PAGE_SIZE;
                filterAndRender();
            });

            // Category Filter Pills
            const topicBtns = document.querySelectorAll('.topic-filter-btn');
            topicBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    topicBtns.forEach(b => {
                        b.classList.remove('bg-gray-200', 'text-gray-900', 'font-semibold');
                        b.classList.add('hover:bg-gray-100', 'text-gray-600', 'font-medium');
                    });
                    btn.classList.add('bg-gray-200', 'text-gray-900', 'font-semibold');
                    btn.classList.remove('hover:bg-gray-100', 'text-gray-600', 'font-medium');

                    currentCategory = btn.dataset.category;
                    displayLimit = PAGE_SIZE;
                    filterAndRender();
                });
            });

            // Layout Switcher
            const feedBtn = document.getElementById('view-feed-btn');
            const gridBtn = document.getElementById('view-grid-btn');

            feedBtn.addEventListener('click', () => {
                currentView = 'feed';
                feedBtn.className = 'px-2.5 py-1.5 rounded-full transition bg-white text-black shadow-sm flex items-center gap-1.5 font-medium';
                gridBtn.className = 'px-2.5 py-1.5 rounded-full transition text-gray-500 hover:text-black flex items-center gap-1.5 font-medium';
                renderPosts();
            });

            gridBtn.addEventListener('click', () => {
                currentView = 'grid';
                gridBtn.className = 'px-2.5 py-1.5 rounded-full transition bg-white text-black shadow-sm flex items-center gap-1.5 font-medium';
                feedBtn.className = 'px-2.5 py-1.5 rounded-full transition text-gray-500 hover:text-black flex items-center gap-1.5 font-medium';
                renderPosts();
            });

            // Load More Button
            document.getElementById('load-more-btn').addEventListener('click', () => {
                displayLimit += PAGE_SIZE;
                renderPosts();
            });
        });
    </script>

