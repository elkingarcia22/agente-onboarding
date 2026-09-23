content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
idx = content.find('Anotado para el')
if idx != -1:
    print(content[max(0, idx-500):idx+500])
else:
    print("Not found")
