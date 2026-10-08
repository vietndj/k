import os
import json

def build():
    # Read the data directory
    data_dir = "/Users/vietmac/Documents/CODE/k/mridu_transitions/data/kieu1"
    if not os.path.exists(data_dir):
        print("Data dir not found!")
        return

    json_files = [f for f in os.listdir(data_dir) if f.endswith(".json")]
    
    transitions = []
    for f in json_files:
        with open(os.path.join(data_dir, f)) as jf:
            d = json.load(jf)
            transitions.extend(d.get("transitions", []))

    # Output file
    out_path = "/Users/vietmac/Documents/CODE/k/mridu.html"
    
    html = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phân tích @mridupawasharma - KIỂU 1 (Quay người)</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --cl-bg: #ffffff;
            --cl-tint: #f8fafc;
            --cl-card: #ffffff;
            --cl-accent: #1a73e8;
            --cl-accent-tint: rgba(26, 115, 232, 0.08);
            --cl-text-base: #090d16;
            --cl-text-body: #0f172a;
            --cl-text-muted: #475569;
            --cl-line: rgba(0, 0, 0, 0.06);
            --cl-line-strong: rgba(0, 0, 0, 0.12);
            --cl-radius-lg: 24px;
            --cl-radius-md: 16px;
            --cl-radius-sm: 10px;
            --cl-radius-full: 9999px;
            --font-ui: 'Inter', -apple-system, sans-serif;
            --font-mono: monospace;
        }

        body { margin: 0; background: var(--cl-bg); color: var(--cl-text-body); font-family: var(--font-ui); }
        .app-container { display: flex; min-height: 100vh; }

        .video-sidebar { width: 420px; max-width: 420px; position: sticky; top: 0; height: 100vh; background: var(--cl-tint); border-right: 1px solid var(--cl-line); padding: 24px; display: flex; flex-direction: column; gap: 16px; }
        .video-wrap { width: 100%; aspect-ratio: 9/16; border-radius: var(--cl-radius-md); overflow: hidden; background: #000; position: relative; }
        .video-wrap iframe, .video-wrap video { width: 100%; height: 100%; border: none; object-fit: contain; }
        
        .video-controls { display: flex; flex-direction: column; gap: 12px; }
        .speed-row, .action-row { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
        .ctrl-btn { font-family: var(--font-ui); font-size: 13px; font-weight: 500; padding: 6px 12px; border: 1px solid var(--cl-line-strong); background: var(--cl-card); border-radius: var(--cl-radius-full); cursor: pointer; }
        .ctrl-btn:hover { border-color: var(--cl-accent); color: var(--cl-accent); }
        #shotStatusTag { font-family: var(--font-mono); font-size: 12px; text-align: center; color: var(--cl-accent); background: var(--cl-accent-tint); padding: 6px 12px; border-radius: var(--cl-radius-full); }

        .content-column { flex: 1; padding: 32px 40px; overflow-y: auto; max-width: 1000px; }
        .header-badges span { background: var(--cl-accent-tint); color: var(--cl-accent); padding: 4px 10px; border-radius: var(--cl-radius-full); font-size: 12px; font-weight: 600; margin-right: 8px; }
        .report-title { font-size: 32px; font-weight: 700; margin: 16px 0; }
        
        .script-axis-card, .overview-card { background: var(--cl-tint); border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); padding: 20px; margin-bottom: 24px; }
        .script-axis-title { color: var(--cl-accent); font-weight: 700; margin-bottom: 12px; }

        .toolbar { display: flex; gap: 16px; margin-bottom: 24px; }
        .tab-btn { font-weight: 600; padding: 8px 16px; cursor: pointer; border: none; background: transparent; }
        .tab-btn.active { background: var(--cl-accent); color: white; border-radius: 20px; }

        .shot-card { display: flex; gap: 20px; padding: 20px; border: 1px solid var(--cl-line); border-radius: var(--cl-radius-md); margin-bottom: 16px; cursor: pointer; }
        .shot-card:hover { border-color: var(--cl-accent); }
        .shot-card.active-playing { border-color: var(--cl-accent); box-shadow: 0 0 0 2px var(--cl-accent-tint); }
        
        .shot-thumb { width: 130px; border-radius: var(--cl-radius-sm); overflow: hidden; display: flex; gap: 4px; }
        .shot-thumb img { width: 100%; aspect-ratio: 9/16; object-fit: cover; }
        
        .shot-body { flex: 1; }
        .shot-head { display: flex; gap: 10px; margin-bottom: 8px; align-items: center; }
        .shot-num { background: var(--cl-accent-tint); color: var(--cl-accent); padding: 4px 10px; border-radius: var(--cl-radius-full); font-weight: 700; font-size: 12px; }
        .shot-time-badge { font-family: var(--font-mono); font-size: 12px; font-weight: 600; }
        .shot-headline { font-size: 18px; font-weight: 600; margin: 0 0 8px; }
        .shot-insight { color: var(--cl-text-muted); margin-bottom: 12px; }
        .shot-details { background: var(--cl-tint); padding: 12px; border-radius: 8px; }
    </style>
</head>
<body>
<div class="app-container">
    <!-- Sidebar -->
    <div class="video-sidebar">
        <div id="playerContainer" class="video-wrap">
            <div id="ytPlayer"></div>
        </div>
        <div class="video-controls">
            <div class="speed-row">
                <button class="ctrl-btn" onclick="setSpeed(0.25)">0.25x</button>
                <button class="ctrl-btn" onclick="setSpeed(0.5)">0.5x</button>
                <button class="ctrl-btn active" onclick="setSpeed(1)">1x</button>
                <button class="ctrl-btn" onclick="setSpeed(1.5)">1.5x</button>
            </div>
            <div class="action-row">
                <button class="ctrl-btn" onclick="stepFrame(-1)">-1F</button>
                <button class="ctrl-btn" onclick="stepFrame(1)">+1F</button>
                <button class="ctrl-btn" onclick="toggleMute(this)">Âm thanh</button>
                <button class="ctrl-btn" onclick="toggleLoop(this)">Tắt Lặp đoạn</button>
            </div>
            <div id="shotStatusTag">Sẵn sàng</div>
        </div>
    </div>

    <!-- Content -->
    <div class="content-column">
        <div class="header-badges"><span>KIỂU 1</span></div>
        <h1 class="report-title">Phân tích chuyển cảnh Quay Người (@mridupawasharma)</h1>
        
        <div class="script-axis-card">
            <div class="script-axis-title">TRỤC: Chuẩn bị xoay → Điểm cắt giấu bằng vai/lưng → Match chuyển động</div>
            <div>Chủ thể xoay thân/đầu ở cảnh A, lợi dụng blur hoặc che khung hình để cắt sang cảnh B và tiếp tục xoay khớp với hướng đó.</div>
        </div>

        <div class="overview-card">
            <p><strong>Công thức K1a:</strong> Quay người rời camera rồi hiện ra ở bối cảnh mới.</p>
            <p><strong>Công thức K1b:</strong> Quay người hướng vào camera.</p>
        </div>

        <div class="toolbar">
            <div class="tab-group">
                <button class="tab-btn active">Chi tiết</button>
            </div>
        </div>

        <div id="storyboardView">
"""
    
    # Generate cards
    for idx, t in enumerate(transitions):
        igid = t["id"].rsplit("_", 1)[0]
        yt_id = "" # find yt_id
        for f in json_files:
            if igid in f:
                with open(os.path.join(data_dir, f)) as jf:
                    yt_id = json.load(jf).get("yt_id") or ""
                    break

        html += f"""
            <div class="shot-card" id="card-{idx}" onclick="playTransition('{yt_id}', {t['start']}, {t['end']}, 'SHOT {idx+1}', '{igid}')">
                <div class="shot-thumb">
                    <img src="mridu_transitions/{t['frames']['cut']}" alt="Cut frame">
                </div>
                <div class="shot-body">
                    <div class="shot-head">
                        <span class="shot-num">KIỂU 1 • {t.get('variant', 'K1a')}</span>
                        <span class="shot-time-badge">{t['start']:.2f}s – {t['end']:.2f}s (cut @{t['cut_time']:.2f}s)</span>
                    </div>
                    <h3 class="shot-headline">{t['scene_A']} → {t['scene_B']}</h3>
                    <p class="shot-insight">Giấu vết cắt: {t['hide_trick']}</p>
                    <details class="shot-details">
                        <summary>Chi tiết (Chất lượng match: {t['match_quality']}★)</summary>
                        <p><strong>Hướng:</strong> {t['direction']}</p>
                        <p><strong>Cách làm:</strong> {', '.join(t['how_to_replicate'])}</p>
                    </details>
                </div>
            </div>
"""

    html += """
        </div>
    </div>
</div>

<script src="https://www.youtube.com/iframe_api"></script>
<script>
    var ytPlayer;
    var currentYtId = '';
    var loopStart = 0;
    var loopEnd = 0;
    var isLooping = true;
    var checkInterval = null;
    var ytReady = false;

    function onYouTubeIframeAPIReady() {
        ytReady = true;
    }
    
    function toggleLoop(btn) {
        isLooping = !isLooping;
        btn.innerText = isLooping ? 'Tắt Lặp đoạn' : 'Bật Lặp đoạn';
    }
    
    function setSpeed(speed) {
        if(ytPlayer && ytPlayer.setPlaybackRate) {
            ytPlayer.setPlaybackRate(speed);
        }
    }

    function checkLoop() {
        if(!isLooping || !ytPlayer || !ytPlayer.getCurrentTime) return;
        var t = ytPlayer.getCurrentTime();
        if(loopEnd > 0 && t >= loopEnd) {
            ytPlayer.seekTo(loopStart, true);
        }
    }

    function playTransition(ytId, start, end, label, igid) {
        document.querySelectorAll('.shot-card').forEach(c => c.classList.remove('active-playing'));
        var card = Array.from(document.querySelectorAll('.shot-card')).find(c => c.innerHTML.includes(label));
        if(card) card.classList.add('active-playing');
        
        document.getElementById('shotStatusTag').innerText = label + ' • ' + igid + ' • ' + start.toFixed(2) + 's–' + end.toFixed(2) + 's';
        
        loopStart = start;
        loopEnd = end;
        
        if (!document.getElementById('ytPlayer')) {
            ytPlayer = null;
        }

        if (!ytId || ytId === 'None') {
            console.log("No YT id, fallback to video");
            ytPlayer = null;
            // Setup fallback <video>
            var container = document.getElementById('playerContainer');
            container.innerHTML = `<video id="htmlPlayer" src="mridu_transitions/lite/${igid}.mp4" autoplay playsinline muted></video>`;
            var vid = document.getElementById('htmlPlayer');
            vid.currentTime = start; vid.play();
            if(checkInterval) clearInterval(checkInterval);
            checkInterval = setInterval(() => {
                if(!isLooping) return;
                if(vid.currentTime >= end) {
                    vid.currentTime = start; vid.play();
                }
            }, 100);
            return;
        }

        if(!ytPlayer) {
            var container = document.getElementById('playerContainer');
            container.innerHTML = '<div id="ytPlayer"></div>';
            ytPlayer = new YT.Player('ytPlayer', {
                videoId: ytId,
                playerVars: { 'autoplay': 1, 'mute': 1, 'start': Math.floor(start) },
                events: {
                    'onReady': function(e) {
                        currentYtId = ytId;
                        e.target.seekTo(start, true);
                        e.target.playVideo();
                        if(checkInterval) clearInterval(checkInterval);
                        checkInterval = setInterval(checkLoop, 100);
                    },
                    'onError': function(e) {
                        console.log("YT error", e.data);
                        // Fallback
                        playTransition(null, start, end, label, igid);
                    }
                }
            });
        } else {
            if (currentYtId !== ytId) {
                currentYtId = ytId;
                ytPlayer.loadVideoById({videoId: ytId, startSeconds: start});
            } else {
                ytPlayer.seekTo(start, true);
                ytPlayer.playVideo();
            }
        }
    }
</script>
</body>
</html>
"""
    with open(out_path, "w") as f:
        f.write(html)
    print("Build complete.")

if __name__ == "__main__":
    build()
