import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

# I want to:
# 1. Add id:"datos-editar" to the Hv object in the confirm block
# 2. Change the onKeyDown in the confirm block's map so it calls P("user",...),y("adjust"),P("agent",Uv)

# Let's find the confirm block:
old_confirm_arr = r'\[\{label:\$v,onClick:k\},\{label:Hv,onClick:F\}\]'
new_confirm_arr = r'[{label:$v,onClick:k},{label:Hv,onClick:F,id:"datos-editar"}]'
content = re.sub(old_confirm_arr, new_confirm_arr, content)

# Now find the second onKeyDown logic which is currently:
# onKeyDown:e=>{if(e.key==="Enter"&&e.target.value.trim()!==""){e.stopPropagation();e.preventDefault();U({...L,label:e.target.value,needsDetail:!1})}}

parts = content.split('onKeyDown:e=>{if(e.key==="Enter"&&e.target.value.trim()!==""){e.stopPropagation();e.preventDefault();')
if len(parts) == 3:
    # parts[0] is everything before the first one
    # parts[1] is between the first and second one
    # parts[2] is after the second one
    
    # The first one should stay U({...L,label:e.target.value,needsDetail:!1})}}
    # The second one should become P("user",e.target.value),y("adjust"),P("agent",Uv)}}
    
    second_rest = parts[2]
    second_rest = second_rest.replace('U({...L,label:e.target.value,needsDetail:!1})}}', 'P("user",e.target.value),y("adjust"),P("agent",Uv)}}', 1)
    
    content = parts[0] + 'onKeyDown:e=>{if(e.key==="Enter"&&e.target.value.trim()!==""){e.stopPropagation();e.preventDefault();' + parts[1] + 'onKeyDown:e=>{if(e.key==="Enter"&&e.target.value.trim()!==""){e.stopPropagation();e.preventDefault();' + second_rest
    
    with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
        f.write(content)
    print("Successfully patched!")
else:
    print(f"Error splitting, found {len(parts)} parts")
