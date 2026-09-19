import re

with open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8") as f:
    js = f.read()

# Find the start of function PV
idx = js.find("function PV({isOpen:")
if idx != -1:
    pv_code = js[idx:idx+15000]
    with open("pv_code.txt", "w") as f_out:
        f_out.write(pv_code)
