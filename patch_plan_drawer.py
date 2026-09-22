import sys

file_path = "components/plan-drawer.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("Reto de conectividad en el canal del equipo", "Reto de conectividad")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
