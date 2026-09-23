content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
idx = content.find('z=L=>{')
if idx != -1:
    print(content[max(0, idx-100):idx+500])
else:
    print("Not found")
