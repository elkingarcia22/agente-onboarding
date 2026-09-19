import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I will replace the newlines inside the string with literal \n or change to backticks.
bad_str = "obChatAddAiMessage('¡Entendido! Generando plan de onboarding...\n\n✅ Tareas de compliance creadas\n✅ Entrevistas 1:1 agendadas\n✅ Retos de cultura definidos\n\nEl plan de onboarding ha sido generado exitosamente.');"
fixed_str = "obChatAddAiMessage(`¡Entendido! Generando plan de onboarding...\\n\\n✅ Tareas de compliance creadas\\n✅ Entrevistas 1:1 agendadas\\n✅ Retos de cultura definidos\\n\\nEl plan de onboarding ha sido generado exitosamente.`);"

content = content.replace(bad_str, fixed_str)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Done fix quotes")
