import os
import subprocess

files_to_bump = [
    "logic08.html",
    "logic09.html",
    "logic10.html",
    "logic11.html",
    "logic12.html",
    "dom.html"
]

for html_file in files_to_bump:
    filepath = os.path.join("/Users/vietmac/Documents/CODE/k", html_file)
    if os.path.exists(filepath):
        os.utime(filepath, None)

subprocess.run(["python3", "generate_manifest.py"], cwd="/Users/vietmac/Documents/CODE/k")
