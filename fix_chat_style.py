import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the style for the chat interface in the drawer
old_style = 'id="onboarding-chat-interface" style="display: flex; flex: 1; position: relative; bottom: 0; right: 0; width: 100%; height: 100%; z-index: 1;"'
new_style = 'id="onboarding-chat-interface" style="display: flex; flex: 1; position: relative; bottom: auto; right: auto; width: 100%; height: auto; z-index: 1; box-shadow: none; border-radius: 0; border-top: 1px solid var(--ubits-border-light);"'

content = content.replace(old_style, new_style)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done style")
