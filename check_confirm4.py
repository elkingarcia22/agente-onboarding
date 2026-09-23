import re
content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
match = re.search(r'.{0,300}z=\([^\)]*\)=>{.{0,400}', content)
if match:
    print(match.group(0))
