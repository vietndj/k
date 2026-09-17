with open("/Users/vietmac/Documents/CODE/Quản gia/build_anh_html.py", "r") as f:
    code = f.read()

# Fix grid
code = code.replace('''        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }''', '''        .grid {
            column-count: 4;
            column-width: 350px;
            column-gap: 30px;
        }''')

code = code.replace('''        .card {
            background: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            display: flex;
            flex-direction: column;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }''', '''        .card {
            background: #ffffff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
            display: flex;
            flex-direction: column;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            break-inside: avoid;
            margin-bottom: 30px;
        }''')

code = code.replace('''        .img-container {
            width: 100%;
            padding-top: 100%; /* 1:1 Aspect Ratio */
            position: relative;
            background: #f1f5f9;
        }
        .card img {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }''', '''        .img-container {
            width: 100%;
            background: #f1f5f9;
        }
        .card img {
            width: 100%;
            height: auto;
            display: block;
        }''')

with open("/Users/vietmac/Documents/CODE/Quản gia/build_anh_html.py", "w") as f:
    f.write(code)
