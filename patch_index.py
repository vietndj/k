import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Main Container max-width for Medium style
content = content.replace('max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full', 'max-w-[720px] mx-auto px-4 sm:px-6 py-10 w-full')

# 2. Update initFeed to remove GitHub API and only use posts-manifest.json
init_feed_old = """async function initFeed() {
            try {
                // 1. Fetch from static manifest (0ms latency, reliable)
                const res = await fetch(`./posts-manifest.json?t=${Date.now()}`);
                if (res.ok) {
                    const data = await res.json();
                    allPosts = data.posts || [];
                }
            } catch (err) {
                console.warn("Không tải được posts-manifest.json, thử fallback GitHub API...", err);
            }

            // 2. Background check GitHub API for live discovered files
            checkGitHubLiveUpdates();

            // 3. Render initial state
            updateCategoryCounts();
            filterAndRender();

            document.getElementById('skeleton-loader').classList.add('hidden');
        }"""

init_feed_new = """async function initFeed() {
            try {
                const res = await fetch(`./posts-manifest.json?t=${Date.now()}`);
                if (res.ok) {
                    const data = await res.json();
                    allPosts = data.posts || [];
                }
            } catch (err) {
                console.warn("Không tải được posts-manifest.json", err);
            }

            updateCategoryCounts();
            filterAndRender();

            document.getElementById('skeleton-loader').classList.add('hidden');
        }"""
content = content.replace(init_feed_old, init_feed_new)

# 3. Update createMediumFeedCard template to match Medium
old_card = """        function createMediumFeedCard(post) {
            const postUrl = `./${encodeURIComponent(post.filename)}`;
            const catInfo = CATEGORY_MAP[post.category_key] || CATEGORY_MAP['other'];
            const dateStr = formatDateVN(post.updated_at);

            return `
                <article class="story-card pt-8 first:pt-0 group">
                    <a href="${postUrl}" target="_blank" class="grid grid-cols-1 md:grid-cols-12 gap-6 items-start">
                        
                        <!-- Left Content Column -->
                        <div class="md:col-span-8 flex flex-col justify-between space-y-3">
                            
                            <!-- Author & Meta -->
                            <div class="flex items-center gap-2 text-xs text-gray-500 font-medium">
                                <div class="w-5 h-5 rounded-full bg-black text-white flex items-center justify-center font-serif text-[10px]">V</div>
                                <span class="font-semibold text-gray-800">VIDEO • Anh Việt</span>
                                <span>•</span>
                                <span>${dateStr}</span>
                            </div>

                            <!-- Title -->
                            <h2 class="story-title text-xl sm:text-2xl font-bold font-display text-gray-900 group-hover:text-emerald-700 leading-snug">
                                ${post.title}
                            </h2>

                            <!-- Excerpt -->
                            <p class="text-sm text-gray-600 font-sans line-clamp-2 leading-relaxed">
                                ${post.excerpt}
                            </p>

                            <!-- Bottom Meta & Tags -->
                            <div class="pt-2 flex items-center justify-between text-xs text-gray-500">
                                <div class="flex items-center gap-3">
                                    <span class="inline-block px-2.5 py-0.5 rounded-full text-[11px] font-medium border ${catInfo.color}">
                                        ${post.category_label}
                                    </span>
                                    <span>${post.read_time}</span>
                                    <span class="font-mono text-gray-400 hidden sm:inline">${post.file_size_kb} KB</span>
                                </div>
                                <div class="text-gray-400 group-hover:text-emerald-700 flex items-center gap-1 font-medium transition-colors">
                                    <span>Mở tab mới</span>
                                    <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                                </div>
                            </div>
                        </div>

                        <!-- Right Image Thumbnail -->
                        <div class="md:col-span-4 order-first md:order-last">
                            <div class="img-zoom-box rounded-xl overflow-hidden aspect-[16/10] bg-gray-100 border border-gray-100 shadow-sm relative">
                                <img src="${post.cover_image}" alt="${post.title}" loading="lazy" class="w-full h-full object-cover">
                            </div>
                        </div>

                    </a>
                </article>
            `;
        }"""

new_card = """        function createMediumFeedCard(post) {
            const postUrl = `./${encodeURIComponent(post.filename)}`;
            const catInfo = CATEGORY_MAP[post.category_key] || CATEGORY_MAP['other'];
            const dateStr = formatDateVN(post.updated_at);

            return `
                <article class="py-8 first:pt-0 border-b border-gray-100 group">
                    <a href="${postUrl}" target="_blank" class="flex justify-between items-center gap-6">
                        
                        <!-- Left Content Column -->
                        <div class="flex-1 flex flex-col justify-center space-y-2">
                            
                            <!-- Author & Meta -->
                            <div class="flex items-center gap-2 text-[13px] text-gray-500 mb-1">
                                <span class="font-semibold text-gray-900">VIDEO</span>
                                <span>·</span>
                                <span>${dateStr}</span>
                            </div>

                            <!-- Title -->
                            <h2 class="text-xl sm:text-[22px] font-bold font-display text-gray-900 leading-tight group-hover:text-emerald-700 transition-colors">
                                ${post.title}
                            </h2>

                            <!-- Excerpt -->
                            <p class="text-[15px] text-gray-600 font-sans line-clamp-2 leading-relaxed mt-1">
                                ${post.excerpt}
                            </p>

                            <!-- Bottom Meta & Tags -->
                            <div class="pt-3 flex items-center gap-3 text-[13px] text-gray-500">
                                <span class="inline-block px-2.5 py-0.5 rounded-full bg-gray-100 text-gray-600 font-medium border border-gray-200">
                                    ${post.category_label}
                                </span>
                                <span>${post.read_time}</span>
                            </div>
                        </div>

                        <!-- Right Image Thumbnail -->
                        <div class="w-[120px] h-[120px] sm:w-[140px] sm:h-[140px] shrink-0 bg-gray-100 overflow-hidden rounded-md border border-gray-100">
                            <img src="${post.cover_image}" alt="${post.title}" loading="lazy" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300">
                        </div>

                    </a>
                </article>
            `;
        }"""
content = content.replace(old_card, new_card)

# Update the container classes to remove divide spacing and apply plain margin if not using divide
content = content.replace("container.className = 'space-y-8 sm:space-y-10 divide-y divide-gray-100';", "container.className = 'flex flex-col';")


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
