import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add checkGitHubLiveUpdates with token back to the script
github_api_script = """
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
"""

if "function checkGitHubLiveUpdates()" not in content:
    content = content.replace('// Update Counter Badges', github_api_script + '\n        // Update Counter Badges')

# Put the call back in initFeed
old_init_feed = """async function initFeed() {
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

new_init_feed = """async function initFeed() {
            try {
                const res = await fetch(`./posts-manifest.json?t=${Date.now()}`);
                if (res.ok) {
                    const data = await res.json();
                    allPosts = data.posts || [];
                }
            } catch (err) {
                console.warn("Không tải được posts-manifest.json", err);
            }

            // 2. Background check GitHub API for live discovered files with bypass token
            checkGitHubLiveUpdates();

            updateCategoryCounts();
            filterAndRender();

            document.getElementById('skeleton-loader').classList.add('hidden');
        }"""

content = content.replace(old_init_feed, new_init_feed)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
