import re

with open("logic29.html", "r") as f:
    template = f.read()

with open("/tmp/logic30_content.html", "r") as f:
    content = f.read()

# Replace title
template = template.replace('<title>Logic 29', '<title>Logic 30')
template = template.replace('Logic 29', 'Logic 30')
template = template.replace('>29</text>', '>30</text>')

# Replace content
start_idx = template.find('<div class="ink-content-section" id="phan-1">')
end_idx = template.find('</script>', start_idx)

if start_idx != -1 and end_idx != -1:
    script_content = template[end_idx:]
    new_html = template[:start_idx] + content + '\n        </div>\n    </div>\n    ' + script_content
    with open("logic30.html", "w") as f:
        f.write(new_html)
else:
    print("Could not find replacement sections")
