import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Original part:
#                                     ` : agentData.hasConfig && stage.agentId === 'interview-ia' ? `
#                                         <button class="ubits-button ubits-button--tertiary ubits-button--sm ubits-button--icon-only" onclick="openSerenaConfigDrawer('${stage.id}')" title="Configurar entrevista Serena">
#                                             <i class="far fa-gear"></i>
#                                         </button>
#                                     ` : agentData.hasConfig && stage.agentId !== 'psychometric-analyst' && stage.agentId !== 'interview-ia' ? `

target = "` : agentData.hasConfig && stage.agentId !== 'psychometric-analyst' && stage.agentId !== 'interview-ia' ? `"
replacement = """` : agentData.hasConfig && stage.agentId === 'onboarding' ? `
                                        <button class="ubits-button ubits-button--tertiary ubits-button--sm ubits-button--icon-only" onclick="openOnboardingConfigDrawer('${stage.id}')" title="Configurar Onboarding">
                                            <i class="far fa-gear"></i>
                                        </button>
                                    ` : agentData.hasConfig && stage.agentId !== 'psychometric-analyst' && stage.agentId !== 'interview-ia' && stage.agentId !== 'onboarding' ? `"""

content = content.replace(target, replacement)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done btn2")
