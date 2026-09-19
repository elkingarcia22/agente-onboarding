import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace header
old_header = """<div class="drawer-header" style="flex-shrink: 0;">
            <h2 class="ubits-heading-h4" id="onboarding-drawer-title">
                <i class="far fa-sparkles" style="color: var(--ubits-brand-primary);"></i> Agente de Onboarding
            </h2>
            <button class="icon-btn" onclick="closeOnboardingConfigDrawer()">
                <i class="far fa-times"></i>
            </button>
        </div>"""

new_header = """<div class="drawer-header">
            <h3 class="drawer-title" id="onboarding-drawer-title">
                <i class="far fa-sparkles" style="color: var(--ubits-brand-primary);"></i> Agente de Onboarding
            </h3>
            <button class="ubits-button ubits-button--secondary ubits-button--sm ubits-button--icon-only" onclick="closeOnboardingConfigDrawer(); return false;" title="Cerrar">
                <i class="far fa-times"></i>
            </button>
        </div>"""

content = content.replace(old_header, new_header)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed drawer header")
