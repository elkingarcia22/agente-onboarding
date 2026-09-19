import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8") as f:
    js = f.read()

idx = js.find("function GV()")
if idx != -1:
    print(js[idx:idx+2000])
