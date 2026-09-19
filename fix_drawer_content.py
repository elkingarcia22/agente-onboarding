import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_str = '<div class="drawer-content" onclick="event.stopPropagation();" style="display: flex; flex-direction: column; width: 420px; max-width: 90vw; background: white; height: 100%; position: absolute; right: 0; box-shadow: -4px 0 24px rgba(0,0,0,0.1);">'
new_str = '<div class="drawer-content" onclick="event.stopPropagation();" style="display: flex; flex-direction: column; height: 100%;">'

content = content.replace(old_str, new_str)

# wait, also the <div class="drawer-body"> doesn't need to be so complex if .drawer-body has styles, but display:flex is good to expand
# the drawer-content in serenaConfigDrawer doesn't have inline styles: 
# <div class="drawer-content" onclick="if(event.target === this) event.stopPropagation();">

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Cleaned up drawer content")
