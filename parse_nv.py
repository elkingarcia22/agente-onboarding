with open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8") as f:
    js = f.read()

idx = js.find("NV=[{id:\"datos\"")
if idx != -1:
    print(js[idx:idx+4000])
