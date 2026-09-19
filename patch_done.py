import re

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    js = f.read()

old_str = 'b==="done"&&r.jsxs("a",{href:u,target:"_blank",rel:"noreferrer",'
new_str = 'b==="done"&&r.jsxs("button",{onClick:()=>{window.parent.postMessage({type:"chatDone"},"*")},'

if old_str in js:
    js = js.replace(old_str, new_str)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Patched done button successfully")
else:
    print("Could not find the done button string")
