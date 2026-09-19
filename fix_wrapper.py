import re

file_path = "panel-candidatos/chat-only.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace body to add backdrop and right-align root
new_body = """  <body>
    <div id="backdrop" class="fixed inset-0 bg-slate-900/20 backdrop-blur-sm transition-opacity duration-300 opacity-100" onclick="window.parent.postMessage({type: 'closePV'}, '*')"></div>
    <div id="root" class="fixed inset-y-0 right-0 flex justify-end h-full"></div>
  </body>"""

content = re.sub(r'<body>.*?</body>', new_body, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Fixed chat-only.html wrapper")
