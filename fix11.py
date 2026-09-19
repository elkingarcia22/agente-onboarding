import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

old_choices = r'choices:\[\{id:"conexion-reto",label:"Activar el reto de conectividad",planLabel:"Reto de conectividad en el canal del equipo",reply:"Genial, activo el reto y preparo la notificación para el equipo\."\}\],datePrompt'

new_choices = r'choices:[{id:"conexion-reto",label:"Activar el reto de conectividad (Slack)",planLabel:"Reto de conectividad en Slack",reply:"Genial, activo el reto y preparo la notificación para el equipo."},{id:"conexion-reunion",label:"Presentarse en la reunión de equipo",planLabel:"Presentación en reunión de equipo",reply:"Perfecto, lo agendamos para la próxima reunión grupal."},{id:"conexion-cafes",label:"Cafés virtuales con compañeros",planLabel:"Cafés virtuales 1:1",reply:"Excelente idea, programaremos cafés cortos para que conozca a sus compañeros."}],datePrompt'

content = re.sub(old_choices, new_choices, content)

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("Added options")
