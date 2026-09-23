content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
idx = content.find('h.length')
if idx != -1:
    print(content[max(0, idx-400):idx+400])
else:
    print("Not found")
