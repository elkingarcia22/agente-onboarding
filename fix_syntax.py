import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the bad block
bad_code = """` : ''}` : ''}"""
fixed_code = """` : ''}"""

# Wait, the exact block is:
#                                 ` : ''}
#                                 ${isEditMode && stage.agentId === 'onboarding' ? `
#                                 <button class="ubits-button ubits-button--tertiary ubits-button--sm ubits-button--icon-only" onclick="openOnboardingConfigDrawer('${stage.id}')" title="Configurar Onboarding">
#                                     <i class="far fa-cog"></i>
#                                 </button>
#                                 ` : ''}` : ''}

# I should just remove that broken onboarding button from that location because it's not even a stage inside the flow there! It's the board header actions!! 
# Let's completely remove it.

# I'll use regex to remove it
pattern = re.compile(r"(\s*\$\{\s*isEditMode && stage\.agentId === 'onboarding'\s*\?\s*`\s*<button[^>]+onclick=\"openOnboardingConfigDrawer\('[^']+'\)\"[^>]*>[\s\S]*?` : ''\})` : ''\}")
content = pattern.sub("` : ''}", content)

# I should also fix the second error in script.js
with open("script.js", "r", encoding="utf-8") as f:
    script_content = f.read()

script_content = script_content.replace(
    "if (windowWidth <= 768) {",
    "if (windowWidth <= 768 && sidebar) {"
)
script_content = script_content.replace(
    "sidebar.style.width = '240px';",
    "if(sidebar) sidebar.style.width = '240px';"
)
script_content = script_content.replace(
    "sidebar.style.minWidth = '240px';",
    "if(sidebar) sidebar.style.minWidth = '240px';"
)
script_content = script_content.replace(
    "sidebar.style.left = '16px';",
    "if(sidebar) sidebar.style.left = '16px';"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(script_content)

print("Done")
