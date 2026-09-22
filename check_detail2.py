import re
content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()

# Let's find X= or X = where X is the function
# We know it's near "A=" or "H="
match = re.search(r'.{0,300}b==="detail"\?X\(L\)', content)
if match:
    print(match.group(0))

