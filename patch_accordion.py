import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

old_str = r'\{id:"onboarding",title:"Onboarding",category:"Onboarding",icon:ph,iconColor:"text-gray-500",number:10,children:null\}'

new_children = """r.jsx("div", {
  className: "p-6 border-t border-gray-100 bg-white",
  children: r.jsxs("div", {
    className: "flex flex-col gap-6",
    children: [
      r.jsx("div", {
        className: "flex items-center gap-2 mb-2",
        children: r.jsx("h4", {className: "text-[11px] font-bold text-gray-500 tracking-wider uppercase", children: "Plan de onboarding creado"})
      }),
      ...[
      {name: "Alta en la plataforma", desc: "Datos confirmados"},
      {name: "Inmersión en cultura y OKRs", desc: "Reunión 1:1 con su líder"},
      {name: "Reto de conectividad con el equipo", desc: "Reto de conectividad en el canal del equipo"},
      {name: "Medición de experiencia (días 15, 30 y 60)", desc: "Encuestas automáticas"}
    ].map((t,i) => r.jsxs("div", {
      className: "flex items-start gap-4",
      key: i,
      children: [
        r.jsx("div", {className: "w-6 h-6 rounded-full border border-emerald-500 flex items-center justify-center flex-shrink-0 mt-0.5", children: r.jsx("svg", {xmlns: "http://www.w3.org/2000/svg", viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className: "w-3.5 h-3.5 text-emerald-600", children: r.jsx("path", {d: "M20 6 9 17l-5-5"})})}),
        r.jsxs("div", {
          className: "flex flex-col",
          children: [
            r.jsx("span", {className: "text-sm font-semibold text-gray-900", children: t.name}),
            r.jsx("span", {className: "text-[13px] text-gray-500 mt-0.5", children: t.desc}),
            r.jsxs("span", {className: "text-[10.5px] font-bold bg-amber-50 text-amber-700 px-2.5 py-0.5 rounded-md mt-2 w-fit flex items-center gap-1.5 border border-amber-200", children: [
              r.jsxs("svg", {xmlns: "http://www.w3.org/2000/svg", viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2.5", strokeLinecap: "round", strokeLinejoin: "round", className: "w-3 h-3", children: [r.jsx("rect", {width: "18", height: "18", x: "3", y: "4", rx: "2", ry: "2"}), r.jsx("line", {x1: "16", x2: "16", y1: "2", y2: "6"}), r.jsx("line", {x1: "8", x2: "8", y1: "2", y2: "6"}), r.jsx("line", {x1: "3", x2: "21", y1: "10", y2: "10"})]}),
              "Sin fecha asignada"
            ]})
          ]
        })
      ]
    }))]
  })
})"""

# replace newlines in new_children to keep it single line if needed, or leave it
new_children_flat = new_children.replace('\n', '')

new_str = '{id:"onboarding",title:"Onboarding",category:"Onboarding",icon:ph,iconColor:"text-gray-500",number:10,children:' + new_children_flat + '}'

new_content = re.sub(old_str, new_str, content)
with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(new_content)

print("Done")
