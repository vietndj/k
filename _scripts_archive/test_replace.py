import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace for list view
target_list = '''<div class="flex gap-1 ml-auto overflow-hidden hidden sm:flex">${tagsHtml}</div>'''
replacement_list = '''<div class="flex items-center gap-2 ml-auto">
                                <span class="text-[9px] text-gray-300 font-mono hidden sm:inline-block">${post.filename.replace('.html', '')}</span>
                                <div class="flex gap-1 overflow-hidden hidden sm:flex">${tagsHtml}</div>
                            </div>'''

content = content.replace(target_list, replacement_list)

# Replace for grid view
target_grid = '''<div class="text-xs text-gray-400 flex items-center gap-1">
                                        ${readHtml}
                                    </div>'''
replacement_grid = '''<div class="text-[9px] text-gray-300 flex items-center gap-1 font-mono truncate max-w-[120px]" title="${post.filename}">
                                        ${post.filename.replace('.html', '')} ${readHtml}
                                    </div>'''

content = content.replace(target_grid, replacement_grid)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
