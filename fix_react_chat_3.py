import re

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_slack = r'\{id:"conexion-slack",label:"Reto de conectividad \(Slack\)",planLabel:"Reto de conectividad en Slack",reply:"Genial, preparo la notificación para Slack.",needsDetail:!0,detailPrompt:"¿Cómo se llama el canal específico\?"\}'
new_slack = r'{id:"conexion-slack",label:"Reto de conectividad (Slack)",planLabel:"Reto de conectividad en Slack",reply:"Genial, preparo la notificación para Slack. ¿Cómo se llama el canal específico donde haremos el reto?",needsDetail:!0,detailPrompt:"Escribe el nombre del canal..."}'
content = re.sub(old_slack, new_slack, content)

old_teams = r'\{id:"conexion-teams",label:"Reto de conectividad \(Teams\)",planLabel:"Reto de conectividad en Teams",reply:"Genial, preparo la notificación para Teams.",needsDetail:!0,detailPrompt:"¿Cómo se llama el canal o grupo específico\?"\}'
new_teams = r'{id:"conexion-teams",label:"Reto de conectividad (Teams)",planLabel:"Reto de conectividad en Teams",reply:"Genial, preparo la notificación para Teams. ¿Cómo se llama el canal o grupo específico donde haremos el reto?",needsDetail:!0,detailPrompt:"Escribe el nombre del canal o grupo..."}'
content = re.sub(old_teams, new_teams, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done fixing chat replies.")
