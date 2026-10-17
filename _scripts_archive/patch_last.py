with open("generate_manifest.py", "r") as f:
    text = f.read()
text = text.replace('cover_mapping = {', 'cover_mapping = {\n            "kichbanoffline-kich-ban-bds-30-phut-dap-tan-su-tri-hoan.html": "https://khoai.fedu.vn/k_covers/cover_kich_ban_bds_1789517341819.jpg",')
with open("generate_manifest.py", "w") as f:
    f.write(text)
