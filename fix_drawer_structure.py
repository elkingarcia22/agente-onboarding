import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

old_start = """<div class="serena-config-drawer" id="onboardingConfigDrawer">
        <div class="drawer-header">"""

new_start = """<div class="serena-config-drawer" id="onboardingConfigDrawer">
    <div class="drawer-overlay" onclick="closeOnboardingConfigDrawer()"></div>
    <div class="drawer-content" onclick="event.stopPropagation();" style="display: flex; flex-direction: column; width: 420px; max-width: 90vw; background: white; height: 100%; position: absolute; right: 0; box-shadow: -4px 0 24px rgba(0,0,0,0.1);">
        <div class="drawer-header" style="flex-shrink: 0;">"""

content = content.replace(old_start, new_start)

# I also need to close the drawer-content div at the end
old_end = """        </div>
    </div>
    
    <!-- Modal -->"""

new_end = """        </div>
    </div>
    </div>
    
    <!-- Modal -->"""

content = content.replace(old_end, new_end)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed structure")
