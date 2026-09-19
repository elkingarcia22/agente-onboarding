import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

match = re.search(r"(setInterval\(\(\)=>{  count\+\+;.*?250\); \},1600\))", content)
if match:
    print(match.group(1))
