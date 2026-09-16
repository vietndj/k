import json

with open('posts-manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# These already have custom covers
mapped = [
    "kichbanoffline.html",
    "kichbanoffline-kich-ban-08-chuyen-mon-vung-nhung-vang-khach.html",
    "kichbanoffline-phan-tich-video-fb-ads-6.html",
    "kichbanoffline-phan-tich-video-fb-ads-5.html",
    "kichbanoffline-phan-tich-video-fb-ads-4.html",
    "an-toan-ai-02-podcast.html",
    "hau-qua-cua-nhin-linh-tinh-science.html",
    "complex-5-anxiety-is-not-what-you-think.html",
    "suyash-saraf-d2c-branding-gen-z-marketing-podcast.html",
    "law-5-stress-is-not-what-happens-to-you.html"
]

targets = []
for p in data['posts']:
    if p['filename'] not in mapped:
        targets.append(p)
    if len(targets) == 25:
        break

with open('25_targets.json', 'w', encoding='utf-8') as f:
    json.dump(targets, f, indent=2, ensure_ascii=False)

print(f"Found {len(targets)} targets.")
