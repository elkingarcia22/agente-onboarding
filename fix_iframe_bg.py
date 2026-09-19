import re

file_path = "panel-candidatos/chat-only.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("background: transparent;", "background: transparent !important;")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Iframe background fixed")
