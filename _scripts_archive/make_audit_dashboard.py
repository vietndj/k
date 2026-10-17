import json
import re
import html

with open("generate_manifest.py", "r", encoding="utf-8") as f: content = f.read()
mapping = dict(re.findall(r'"([^"]+\.html)"\s*:\s*"([^"]+)"', content))

with open("master_poster_tasks.json", "r", encoding="utf-8") as f:
    master_tasks = json.load(f)

html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nghiệm Thu Toàn Bộ 640 Poster Face Clone</title>
    <style>
        body { font-family: -apple-system, system-ui, sans-serif; background: #0f172a; color: white; margin: 0; padding: 10px; }
        .header { text-align: center; margin-bottom: 20px; position: sticky; top: 0; background: rgba(15, 23, 42, 0.9); padding: 10px; z-index: 100; border-bottom: 1px solid #334155; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 10px; width: 100%; }
        .card { background: #1e293b; border-radius: 6px; overflow: hidden; position: relative; border: 2px solid transparent; transition: border-color 0.2s; }
        .card.error { border-color: #ef4444; }
        .card img { width: 100%; height: auto; aspect-ratio: 9/16; object-fit: cover; display: block; background: #334155; cursor: pointer; }
        .card .info { padding: 8px; font-size: 11px; }
        .card .info h3 { margin: 0 0 4px 0; font-size: 12px; color: #38bdf8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .card .info p { margin: 0 0 6px 0; color: #94a3b8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .actions { display: flex; gap: 5px; flex-wrap: wrap; }
        button { background: #3b82f6; color: white; border: none; padding: 5px 8px; border-radius: 4px; cursor: pointer; font-size: 11px; font-weight: bold; }
        button:hover { background: #2563eb; }
        button.btn-error { background: #ef4444; }
        button.btn-error:hover { background: #dc2626; }
        .stats { display: flex; justify-content: center; gap: 10px; margin-bottom: 10px; font-size: 14px; font-weight: bold; align-items: center; }
        .stat-box { background: #1e293b; padding: 8px 15px; border-radius: 6px; border: 1px solid #334155; }
        .toast { position: fixed; bottom: 20px; right: 20px; background: #22c55e; color: white; padding: 10px 20px; border-radius: 5px; opacity: 0; transition: opacity 0.3s; z-index: 1000; pointer-events: none; }
    </style>
</head>
<body>
    <div class="header">
        <h2 style="margin: 0 0 10px 0;">Nghiệm Thu Face Clone</h2>
        <div class="stats">
            <div class="stat-box">Tổng: <span id="total-count">0</span></div>
            <div class="stat-box" style="color: #ef4444;">Lỗi: <span id="error-count">0</span></div>
            <button onclick="exportErrors()" style="padding: 8px 15px; font-size: 14px; background: #10b981;">Xuất Data Lỗi & Câu Lệnh Fix</button>
        </div>
    </div>
    <div class="grid">
"""

for t in master_tasks:
    html_file = t.get("target_html", "")
    url = mapping.get(html_file, "")
    movie = t.get("movie", "Unknown")
    prompt = t.get("prompt", "")
    escaped_prompt = html.escape(prompt)
    
    html_content += f"""
        <div class="card" id="card-{t['index']}">
            <img src="{url}" loading="lazy" alt="{movie}" onclick="toggleError({t['index']})">
            <div class="info">
                <h3>{movie}</h3>
                <p>{html_file}</p>
                <div class="actions">
                    <button onclick="copyPrompt({t['index']})">Copy Prompt</button>
                    <button class="btn-error" onclick="toggleError({t['index']})" id="btn-err-{t['index']}">Đánh dấu Lỗi</button>
                </div>
                <div id="prompt-data-{t['index']}" style="display:none;">{escaped_prompt}</div>
                <div id="raw-task-{t['index']}" style="display:none;">{html.escape(json.dumps(t))}</div>
            </div>
        </div>
    """

html_content += """
    </div>
    
    <div id="toast" class="toast">Đã copy prompt!</div>

    <script>
        let errorList = [];
        let totalCount = document.querySelectorAll('.card').length;
        document.getElementById('total-count').innerText = totalCount;

        function toggleError(index) {
            const card = document.getElementById('card-' + index);
            const btn = document.getElementById('btn-err-' + index);
            const taskData = JSON.parse(document.getElementById('raw-task-' + index).innerText);
            
            if (card.classList.contains('error')) {
                card.classList.remove('error');
                btn.innerText = 'Đánh dấu Lỗi';
                errorList = errorList.filter(t => t.index !== index);
            } else {
                card.classList.add('error');
                btn.innerText = 'Bỏ Lỗi';
                errorList.push(taskData);
            }
            document.getElementById('error-count').innerText = errorList.length;
        }

        function copyPrompt(index) {
            const promptText = document.getElementById('prompt-data-' + index).innerText;
            navigator.clipboard.writeText(promptText).then(() => {
                showToast("Đã copy Prompt!");
            });
        }

        function showToast(msg) {
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.style.opacity = 1;
            setTimeout(() => { toast.style.opacity = 0; }, 2000);
        }

        function exportErrors() {
            if (errorList.length === 0) {
                alert("Chưa có ảnh nào bị đánh dấu lỗi!");
                return;
            }
            const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(errorList, null, 2));
            const dlAnchorElem = document.createElement('a');
            dlAnchorElem.setAttribute("href", dataStr);
            dlAnchorElem.setAttribute("download", "error_tasks.json");
            dlAnchorElem.click();
            
            alert("Đã tải xuống error_tasks.json! Bạn có thể dùng file này để chạy câu lệnh sửa lỗi.");
        }
    </script>
</body>
</html>
"""

with open("nghiem_thu_640_posters.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated nghiem_thu_640_posters.html")
