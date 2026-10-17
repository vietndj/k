import re

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <audio>...</audio> with iframe placeholder
def yt_repl(match):
    filename = match.group(1)
    return f"""<div class="relative w-full overflow-hidden rounded-lg" style="padding-top: 56.25%;">
                            <iframe class="absolute top-0 left-0 w-full h-full border-0" 
                                src="https://www.youtube.com/embed/DUMMY_VIDEO_ID?rel=0" 
                                title="YouTube video player" 
                                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                                allowfullscreen>
                            </iframe>
                        </div>
                        <div class="mt-2 text-xs text-slate-500 text-center">
                            <em>*Thay DUMMY_VIDEO_ID bằng ID video YouTube của bài {filename}*</em>
                        </div>"""

content = re.sub(
    r'<audio controls class="w-full">\s*<source src="assets/audio/([^"]+)" type="audio/mpeg">\s*Trình duyệt của bạn không hỗ trợ thẻ audio\.\s*</audio>',
    yt_repl,
    content
)

with open('/Users/vietmac/Documents/CODE/k/nhac.html', 'w', encoding='utf-8') as f:
    f.write(content)

