import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

# Replace the specific // comments I introduced
content = content.replace("// Update badge", "")
content = content.replace("// Inject accordion chevron & body", "")
content = content.replace("// Container for chevron", "")

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("Removed comments")
