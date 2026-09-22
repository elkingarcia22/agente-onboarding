import re

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Restore the `datePrompt`
old_date = r'datePrompt:"¿Por qué medio o herramienta se realizará \(ej\. Slack, Teams, WhatsApp\), cómo se llama el canal o grupo, y para cuándo debería estar completada esta etapa\?"\}'
new_date = r'datePrompt:"¿Cuándo le enviamos la notificación para que lo haga?"}'
content = re.sub(old_date, new_date, content)

# 2. Add `needsDetail:!0,detailPrompt:"..."` to the first choice
old_choice = r'\{id:"conexion-reto",label:"Activar el reto de conectividad",planLabel:"Reto de conectividad",reply:"Genial, activo el reto y preparo la notificación para el equipo."\}'
new_choice = r'{id:"conexion-reto",label:"Activar el reto de conectividad",planLabel:"Reto de conectividad",reply:"Genial, activo el reto y preparo la notificación para el equipo.",needsDetail:!0,detailPrompt:"¿Por qué medio o herramienta se realizará (ej. Slack, Teams, WhatsApp) y cómo se llama el canal o grupo?"}'
content = re.sub(old_choice, new_choice, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
