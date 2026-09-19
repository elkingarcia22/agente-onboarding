import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

# Replace the specific // comment I introduced
content = content.replace("// Update main badge safely by checking text content", "/* Update main badge safely by checking text content */")

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("Removed comments")
