import sys

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_str_1 = '«reto de conectividad»: que se presente en el canal general de Slack (o la herramienta que usen) compartiendo'
new_str_1 = '«reto de conectividad»: que se presente ante el equipo compartiendo'

old_str_2 = 'label:"Activar el reto de conectividad (Slack)"'
new_str_2 = 'label:"Activar el reto de conectividad"'

old_str_3 = 'planLabel:"Reto de conectividad en Slack"'
new_str_3 = 'planLabel:"Reto de conectividad"'

content = content.replace(old_str_1, new_str_1)
content = content.replace(old_str_2, new_str_2)
content = content.replace(old_str_3, new_str_3)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
