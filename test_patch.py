import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8") as f:
    js = f.read()

# We need to find the definition of PV
idx_pv = js.find("PV({isOpen:e,")
print("Found PV at:", idx_pv)

# We need to find the root render
idx_render = js.find("c2(document.getElementById(\"root\")).render(")
print("Found render at:", idx_render)

if idx_render != -1:
    print(js[idx_render:idx_render+150])
