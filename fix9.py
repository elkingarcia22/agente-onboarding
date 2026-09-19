import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

old_input = r'\(L\.id==="otro"\?'
new_input = r'((L.id==="otro" || L.id==="datos-editar")?'
content = re.sub(old_input, new_input, content)

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("Applied ternary fix")
