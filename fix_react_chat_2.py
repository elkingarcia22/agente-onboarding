import re

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_choices = r'choices:\[\{id:"conexion-reto",label:"Activar el reto de conectividad",planLabel:"Reto de conectividad",reply:"Genial, activo el reto y preparo la notificación para el equipo.",needsDetail:!0,detailPrompt:"¿Por qué medio o herramienta se realizará \(ej\. Slack, Teams, WhatsApp\) y cómo se llama el canal o grupo\?"\},\{id:"conexion-reunion",label:"Presentarse en la reunión de equipo",planLabel:"Presentación en reunión de equipo",reply:"Perfecto, lo agendamos para la próxima reunión grupal."\},\{id:"conexion-cafes",label:"Cafés virtuales con compañeros",planLabel:"Cafés virtuales 1:1",reply:"Excelente idea, programaremos cafés cortos para que conozca a sus compañeros."\}\]'

new_choices = r'choices:[{id:"conexion-slack",label:"Reto de conectividad (Slack)",planLabel:"Reto de conectividad en Slack",reply:"Genial, preparo la notificación para Slack.",needsDetail:!0,detailPrompt:"¿Cómo se llama el canal específico?"},{id:"conexion-teams",label:"Reto de conectividad (Teams)",planLabel:"Reto de conectividad en Teams",reply:"Genial, preparo la notificación para Teams.",needsDetail:!0,detailPrompt:"¿Cómo se llama el canal o grupo específico?"},{id:"conexion-reunion",label:"Presentarse en la reunión de equipo",planLabel:"Presentación en reunión de equipo",reply:"Perfecto, lo agendamos para la próxima reunión grupal."},{id:"conexion-cafes",label:"Cafés virtuales con compañeros",planLabel:"Cafés virtuales 1:1",reply:"Excelente idea, programaremos cafés cortos para que conozca a sus compañeros."}]'

content = re.sub(old_choices, new_choices, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing choices.")
