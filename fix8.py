import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

# 1. Filter out CV from choices if O.choices has 'datos-ok'
# Find: [...O.choices,CV].map((L,B)=>r.jsxs("button"
old_map = r'\[\.\.\.O\.choices,CV\]\.map\(\(L,B\)=>r\.jsxs\("button"'
new_map = r'[...O.choices,CV].filter(L => !(L.id === "otro" && O.choices.some(c => c.id === "datos-ok"))).map((L,B)=>r.jsxs("button"'
content = re.sub(old_map, new_map, content)

# 2. Add input to "datos-editar"
# Find: L.label.includes("escribo yo")?
old_input = r'L\.label\.includes\("escribo yo"\)\?'
new_input = r'(L.label.includes("escribo yo") || L.id === "datos-editar")?'
content = re.sub(old_input, new_input, content)

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("Changes applied")
