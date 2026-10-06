import re

with open('generate_manifest.py', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''        filepath = os.path.join(os.getcwd(), f)
        stat = os.stat(filepath)
        mod_time = datetime.fromtimestamp(stat.st_mtime).isoformat()'''

replacement = '''        filepath = os.path.join(os.getcwd(), f)
        stat = os.stat(filepath)
        try:
            mod_time = datetime.fromtimestamp(stat.st_birthtime).isoformat()
        except AttributeError:
            mod_time = datetime.fromtimestamp(stat.st_mtime).isoformat()'''

content = content.replace(target, replacement)

with open('generate_manifest.py', 'w', encoding='utf-8') as f:
    f.write(content)
