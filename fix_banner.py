import re
with open("/Users/vietmac/Documents/CODE/k/banner.html", "r") as f:
    html = f.read()
html = re.sub(r"\./assets/banner/([^/\"'>]+)", r"https://media.fedu.vn/banner/\1", html)
with open("/Users/vietmac/Documents/CODE/k/banner.html", "w") as f:
    f.write(html)
print("Updated banner.html!")
