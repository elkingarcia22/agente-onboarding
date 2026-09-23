import re
content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
# Let's search for "EV="
idx = content.find('EV=')
if idx != -1:
    print(content[max(0, idx-50):idx+500])
