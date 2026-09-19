import re

with open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8") as f:
    content = f.read()

# Find App component
app_match = re.search(r'function \w+\(\)\{.*?(return[^}]+})', content)
if app_match:
    print(app_match.group(0)[:1000])
