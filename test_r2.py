import urllib.request
import urllib.error

domains = [
    "https://pub-447bd44dfdac4938912655c855b8631c.r2.dev",
    "https://media.fedu.vn",
    "https://khoai.fedu.vn",
    "https://go.fedu.vn"
]

paths = [
    "/images_gen/",
    "/k_covers/",
    "/covers/",
    "/anhloi/",
    "/"
]

files = [
    "poster_tho-0336.webp",
    "poster_tho-0336.jpg",
    "10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.webp",
    "10-protocols-andrew-huberman-toi-uu-nao-bo-the-chat-diary-of-a-ceo.jpg"
]

found = []

for domain in domains:
    for path in paths:
        for file in files:
            url = f"{domain}{path}{file}"
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
            try:
                response = urllib.request.urlopen(req, timeout=5)
                if response.status == 200:
                    print(f"[FOUND] {url}")
                    found.append(url)
            except Exception as e:
                pass # print(f"Failed: {url}")

if not found:
    print("NO FILES FOUND ON R2 WITH GUESSED URLS.")
