import re

with open('/Users/vietmac/Documents/CODE/k/index.html', 'r') as f:
    content = f.read()

# 1. Update Collection Banner Buttons
banner_old = '''                        <div class="flex gap-2">
                            <button onclick="saveSharedCollection()" class="px-3 py-1 bg-indigo-600 text-white text-xs rounded hover:bg-indigo-700">Lưu vào BST</button>
                            <button onclick="exitSharedView()" class="px-3 py-1 bg-white border border-indigo-200 text-indigo-700 text-xs rounded hover:bg-indigo-50">Xem tất cả</button>
                        </div>'''
banner_new = '''                        <div class="flex gap-2">
                            <button onclick="openAddPostModal()" class="px-3 py-1 bg-indigo-100 text-indigo-700 text-xs rounded hover:bg-indigo-200 font-bold" title="Thêm bài viết">+</button>
                            <button onclick="renameSharedCollection()" class="px-3 py-1 bg-indigo-100 text-indigo-700 text-xs rounded hover:bg-indigo-200" title="Đổi tên">✏️</button>
                            <button onclick="saveSharedCollection()" id="btn-save-col" class="px-3 py-1 bg-indigo-600 text-white text-xs rounded hover:bg-indigo-700">Lưu vào BST</button>
                            <button onclick="exitSharedView()" class="px-3 py-1 bg-white border border-indigo-200 text-indigo-700 text-xs rounded hover:bg-indigo-50">Xem tất cả</button>
                        </div>'''
content = content.replace(banner_old, banner_new)

# 2. Add 'x' button to cards when in shared collection
list_card_anchor_old = '''<a href="./${post.filename}" target="_blank" onclick="markAsRead('${post.filename}')" class="flex-1 min-w-0 flex items-center gap-2 cursor-pointer">'''
list_card_anchor_new = '''${sharedCollectionData ? `<button onclick="removeFromCollection('${post.filename}'); event.preventDefault(); event.stopPropagation();" class="shrink-0 w-6 h-6 bg-gray-100 hover:bg-rose-100 hover:text-rose-600 rounded text-gray-400 flex items-center justify-center transition mr-2" title="Xóa khỏi BST">×</button>` : ''}
                        <a href="./${post.filename}" target="_blank" onclick="markAsRead('${post.filename}')" class="flex-1 min-w-0 flex items-center gap-2 cursor-pointer">'''
content = content.replace(list_card_anchor_old, list_card_anchor_new)

grid_card_badge_old = '''${badgeHtml}'''
grid_card_badge_new = '''${badgeHtml}
                        ${sharedCollectionData ? `<div class="absolute top-2 left-2 z-20"><button onclick="removeFromCollection('${post.filename}'); event.preventDefault(); event.stopPropagation();" class="w-6 h-6 bg-white/90 backdrop-blur hover:bg-rose-100 hover:text-rose-600 rounded text-gray-500 shadow flex items-center justify-center transition font-bold" title="Xóa khỏi BST">×</button></div>` : ''}'''
content = content.replace(grid_card_badge_old, grid_card_badge_new)

# 3. Add Right Sidebar Widget
widget_old = '''<!-- Suggestions Widget -->'''
widget_new = '''<!-- Custom Links Right Widget -->
                <div class="widget bg-gray-50 p-4 rounded-xl border border-gray-100 cursor-move" draggable="true" data-id="customlinks">
                    <h3 class="text-xs font-bold text-gray-500 uppercase tracking-widest mb-3 flex items-center justify-between">
                        Liên Kết Tùy Chỉnh
                        <div>
                            <button id="add-right-link-btn" class="text-gray-400 hover:text-black mr-2 px-1 hover:bg-gray-200 rounded" title="Thêm liên kết"><svg class="w-3.5 h-3.5 inline" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg></button>
                            <span class="text-gray-300">⣿</span>
                        </div>
                    </h3>
                    <div id="right-links-list" class="space-y-1.5"></div>
                </div>
                
                <!-- Suggestions Widget -->'''
content = content.replace(widget_old, widget_new)

# 4. Add Search Modal HTML
modals_marker = '''<!-- Modals -->'''
add_post_modal = '''<!-- Modals -->
    <div id="add-post-modal" class="hidden fixed inset-0 z-[100] bg-black/50 flex items-center justify-center p-4 backdrop-blur-sm">
        <div class="bg-white rounded-xl shadow-xl w-full max-w-md p-6 flex flex-col max-h-[80vh]">
            <h3 class="font-bold text-lg mb-4 text-gray-900">Thêm bài viết vào BST</h3>
            <div class="relative mb-4">
                <input type="text" id="post-search-input" placeholder="Tìm kiếm bài viết..." class="w-full p-2.5 pl-9 border border-gray-200 rounded-lg focus:ring-2 focus:ring-indigo-100 focus:border-indigo-400 outline-none transition">
                <svg class="w-4 h-4 text-gray-400 absolute left-3 top-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            </div>
            <div id="post-search-results" class="flex-1 overflow-y-auto space-y-1 mb-4 min-h-[200px]">
                <div class="text-sm text-gray-400 text-center mt-8">Gõ từ khóa để tìm...</div>
            </div>
            <div class="flex justify-end gap-2 mt-auto border-t border-gray-100 pt-4">
                <button onclick="closeAddPostModal()" class="px-4 py-2 text-gray-600 bg-gray-100 hover:bg-gray-200 rounded-lg text-sm font-medium transition">Đóng</button>
            </div>
        </div>
    </div>'''
content = content.replace(modals_marker, add_post_modal)

# 5. Add JS Logic
js_init_marker = '''// Initial renders'''
js_init_new = '''document.getElementById('add-right-link-btn')?.addEventListener('click', (e) => {
                e.stopPropagation();
                const url = prompt('Nhập URL liên kết:');
                if(!url) return;
                const name = prompt('Nhập tên liên kết:') || url.split('/').pop() || 'Link mới';
                rightCustomLinks.push({ name, url });
                localStorage.setItem('fedu_right_custom_links', JSON.stringify(rightCustomLinks));
                renderRightLinks();
            });
            
            document.getElementById('post-search-input')?.addEventListener('input', (e) => {
                const q = removeAccents(e.target.value.trim());
                const c = document.getElementById('post-search-results');
                if(!q) { c.innerHTML = '<div class="text-sm text-gray-400 text-center mt-8">Gõ từ khóa để tìm...</div>'; return; }
                let results = allPosts.filter(p => !sharedCollectionData.f.includes(p.filename) && removeAccents(p.title + ' ' + p.filename).includes(q)).slice(0, 15);
                if(results.length === 0) { c.innerHTML = '<div class="text-sm text-gray-400 text-center mt-8">Không tìm thấy bài nào</div>'; return; }
                c.innerHTML = results.map(p => `
                    <div class="p-2 hover:bg-indigo-50 border border-transparent hover:border-indigo-100 rounded-lg flex justify-between items-center cursor-pointer group transition" onclick="addToCollection('${p.filename}')">
                        <span class="text-sm text-gray-700 line-clamp-1 flex-1 min-w-0 pr-2">${p.title}</span>
                        <button class="text-[10px] bg-white border border-indigo-200 text-indigo-600 px-2 py-1 rounded shadow-sm opacity-0 group-hover:opacity-100 font-bold uppercase tracking-wide">Thêm</button>
                    </div>
                `).join('');
            });

            // Initial renders'''
content = content.replace(js_init_marker, js_init_new)

js_render_marker = '''function renderCollections() {'''
js_render_new = '''let rightCustomLinks = JSON.parse(localStorage.getItem('fedu_right_custom_links') || '[]');
        
        function renderRightLinks() {
            const c = document.getElementById('right-links-list');
            if(!c) return;
            c.innerHTML = rightCustomLinks.map((link, idx) => `
                <div class="flex justify-between items-center p-2 rounded-lg hover:bg-white border border-transparent hover:border-gray-200 hover:shadow-sm group transition bg-gray-50/50">
                    <a href="${link.url}" target="_blank" class="text-xs text-gray-700 font-medium truncate flex-1 min-w-0">🔗 ${link.name}</a>
                    <div class="flex gap-1 ml-1 shrink-0 opacity-0 group-hover:opacity-100 transition">
                        <button class="text-gray-400 hover:text-indigo-500 w-5 h-5 flex items-center justify-center bg-gray-100 rounded" onclick="editRightLink(${idx})" title="Sửa">✏️</button>
                        <button class="text-gray-400 hover:text-rose-500 w-5 h-5 flex items-center justify-center bg-gray-100 rounded font-bold" onclick="deleteRightLink(${idx})" title="Xóa">×</button>
                    </div>
                </div>
            `).join('');
            if(rightCustomLinks.length === 0) {
                c.innerHTML = `<div class="text-[10px] text-gray-400 text-center py-2 italic">Chưa có liên kết</div>`;
            }
        }

        window.editRightLink = function(idx) {
            const link = rightCustomLinks[idx];
            const newName = prompt('Tên liên kết:', link.name);
            if(newName === null) return;
            const newUrl = prompt('URL liên kết:', link.url);
            if(newUrl === null) return;
            rightCustomLinks[idx] = { name: newName.trim() || 'Link', url: newUrl.trim() };
            localStorage.setItem('fedu_right_custom_links', JSON.stringify(rightCustomLinks));
            renderRightLinks();
        };

        window.deleteRightLink = function(idx) {
            if(confirm('Xóa liên kết này?')) {
                rightCustomLinks.splice(idx, 1);
                localStorage.setItem('fedu_right_custom_links', JSON.stringify(rightCustomLinks));
                renderRightLinks();
            }
        };

        function renderCollections() {'''
content = content.replace(js_render_marker, js_render_new)

js_init_render_marker = '''renderWidgets();'''
js_init_render_new = '''renderWidgets();\n            renderRightLinks();'''
content = content.replace(js_init_render_marker, js_init_render_new)

js_actions_marker = '''window.openCollection = function(idx) {'''
js_actions_new = '''window.openAddPostModal = function() {
            if(!sharedCollectionData) return;
            document.getElementById('add-post-modal').classList.remove('hidden');
            document.getElementById('post-search-input').value = '';
            document.getElementById('post-search-results').innerHTML = '<div class="text-sm text-gray-400 text-center mt-8">Gõ từ khóa để tìm...</div>';
            setTimeout(() => document.getElementById('post-search-input').focus(), 100);
        };

        window.closeAddPostModal = function() {
            document.getElementById('add-post-modal').classList.add('hidden');
        };

        window.addToCollection = function(filename) {
            if(!sharedCollectionData) return;
            sharedCollectionData.f.unshift(filename); // Add to top
            updateCollectionState();
            closeAddPostModal();
        };

        window.removeFromCollection = function(filename) {
            if(!sharedCollectionData) return;
            if(!confirm('Xóa bài này khỏi bộ sưu tập?')) return;
            sharedCollectionData.f = sharedCollectionData.f.filter(f => f !== filename);
            updateCollectionState();
        };

        window.renameSharedCollection = function() {
            if(!sharedCollectionData) return;
            const newName = prompt('Nhập tên mới cho Bộ Sưu Tập:', sharedCollectionData.n);
            if(newName && newName.trim()) {
                const oldName = sharedCollectionData.n;
                sharedCollectionData.n = newName.trim();
                
                // Update in customCollections if it exists
                const idx = customCollections.findIndex(c => c.name === oldName);
                if(idx !== -1) {
                    customCollections[idx].name = sharedCollectionData.n;
                    localStorage.setItem('fedu_custom_collections', JSON.stringify(customCollections));
                    renderCollections();
                }
                
                updateCollectionState();
            }
        };

        function updateCollectionState() {
            // Check if saved
            const idx = customCollections.findIndex(c => c.name === sharedCollectionData.n);
            if(idx !== -1) {
                customCollections[idx].files = sharedCollectionData.f;
                localStorage.setItem('fedu_custom_collections', JSON.stringify(customCollections));
                renderCollections();
            }
            
            // Update UI & URL hash
            const hash = encodeCollection(sharedCollectionData.n, sharedCollectionData.f);
            window.location.hash = 'c=' + hash;
            showSharedCollectionView(sharedCollectionData.n, sharedCollectionData.f);
        }

        window.openCollection = function(idx) {'''
content = content.replace(js_actions_marker, js_actions_new)

with open('/Users/vietmac/Documents/CODE/k/index.html', 'w') as f:
    f.write(content)

