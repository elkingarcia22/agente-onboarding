content = open("panel-candidatos/assets/index-BF1UmWzM.js", "r", encoding="utf-8").read()
idx = content.find('A=L=>{O&&(P("user",L),w({id:"custom",label:L,planLabel:L,reply:""}),y("date"),P("agent",O.datePrompt))}')
if idx != -1:
    print(content[max(0, idx-600):idx+100])
