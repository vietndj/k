with open('/Users/vietmac/Documents/CODE/k/logickenh-xaykenh.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix ./4tang.html to https://fedu.vn/course/4tang.html
html = html.replace('href="./4tang.html"', 'href="https://fedu.vn/course/4tang.html"')

# 2. Add the 3rd tool
html = html.replace('anh có sẵn 2 công cụ:', 'anh có sẵn 3 công cụ:')

third_tool_html = """      <div class="apple-card">
        <div class="apple-card__title">3. Bộ 3 Công Cụ AI Viết Kịch Bản: <a href="https://fedu.vn/course/miss-extensions.html" target="_blank" style="color: var(--cl-accent);">fedu.vn/course/miss-extensions.html</a></div>
        <p class="cl-body">
          Bộ 3 tiện ích AI (Miss Idea, Miss Vlog, Miss Video Ads) đã nạp sẵn bộ lọc văn phong thực chiến, tự động bóc tách tâm lý khách hàng và xuất kịch bản mộc mạc, hoàn toàn không dính văn mẫu.
        </p>
        <a href="https://fedu.vn/course/miss-extensions.html" target="_blank" class="btn-action">MỞ BỘ 3 CÔNG CỤ AI →</a>
      </div>

"""

# Insert the third tool after the second tool
# The second tool ends with <a href="https://ytuong.fedu.vn" target="_blank" class="btn-action">MỞ KHO Ý TƯỞNG QUỐC TẾ →</a>\n      </div>
target = '<a href="https://ytuong.fedu.vn" target="_blank" class="btn-action">MỞ KHO Ý TƯỞNG QUỐC TẾ →</a>\n      </div>'
if target in html:
    html = html.replace(target, target + '\n\n' + third_tool_html)

with open('logickenh-xaykenh.html', 'w', encoding='utf-8') as f:
    f.write(html)
