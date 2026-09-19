import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# For Serena:
# ${isEditMode && stage.agentId === 'interview-ia' ? `
# <button class="ubits-button ubits-button--tertiary ubits-button--sm ubits-button--icon-only" onclick="openSerenaConfigDrawer('${stage.id}')" title="Configurar entrevista Serena">
#    <i class="far fa-cog"></i>
# </button>
# ` : ''}

onboarding_btn_code = """
                                ${isEditMode && stage.agentId === 'onboarding' ? `
                                <button class="ubits-button ubits-button--tertiary ubits-button--sm ubits-button--icon-only" onclick="openOnboardingConfigDrawer('${stage.id}')" title="Configurar Onboarding">
                                    <i class="far fa-cog"></i>
                                </button>
                                ` : ''}"""

# Find the Serena button and append the Onboarding button right after it
content = content.replace("openSerenaConfigDrawer('${stage.id}')", "openSerenaConfigDrawer('${stage.id}')") # dummy
if "stage.agentId === 'interview-ia'" in content:
    # Just a simple string replacement
    parts = content.split("` : ''}")
    for i, part in enumerate(parts):
        if "stage.agentId === 'interview-ia'" in part:
            parts[i] = part + "` : ''}" + onboarding_btn_code
            break
    content = "` : ''}".join(parts)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done btn")
