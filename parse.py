with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()
start = content.find("function Sz({")
if start != -1:
    print(content[start+3000:start+6000])
