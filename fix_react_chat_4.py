import re

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_ev = r'EV=e=>`¡Listo! El plan de onboarding de \$\{e\} quedó creado y las tareas ya están asignadas en su plan.`'
new_ev = r'EV=e=>"Listo, ya quedó configurado el plan de onboarding y una vez se dé de alta al usuario en la plataforma se creará el plan de onboarding y se le notificará vía correo al usuario."'

content = re.sub(old_ev, new_ev, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done fixing final message.")
