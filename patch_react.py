import re

file_path = "panel-candidatos/assets/index-BF1UmWzM.js"
with open(file_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace the render line
old_render = 'c2(document.getElementById("root")).render(r.jsx(x.StrictMode,{children:r.jsx(GV,{})}));'

# We pass window.__PV_PROPS__ into PV. We need to define PV component variable. In the minified code, PV is just PV.
# So we can do: r.jsx(PV, window.__PV_PROPS__)
new_render = """
if (window.__MOUNT_PV_ONLY__) {
    c2(document.getElementById("root")).render(r.jsx(x.StrictMode,{children:r.jsx(PV, window.__PV_PROPS__ || {})}));
} else {
    c2(document.getElementById("root")).render(r.jsx(x.StrictMode,{children:r.jsx(GV,{})}));
}
"""

if old_render in js:
    js = js.replace(old_render, new_render)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(js)
    print("Patched React build successfully")
else:
    print("Could not find the render line")

