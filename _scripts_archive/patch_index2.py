import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove checkGitHubLiveUpdates completely
func_pattern = re.compile(r'// Live Discovery from GitHub Repo.*?async function checkGitHubLiveUpdates\(\) \{.*?\}\s*', re.DOTALL)
content = func_pattern.sub('', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
