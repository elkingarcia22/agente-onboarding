import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8") as f:
    js = f.read()

idx = js.find("getElementById(\"root\")")
if idx != -1:
    print(js[idx-100:idx+200])
