content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
idx = content.find('z=({stepId')
if idx != -1:
    print(content[max(0, idx-200):idx+400])
else:
    print("Not found")
