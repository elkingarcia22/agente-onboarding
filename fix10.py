import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

# I will replace the b==="date" block with a custom array of buttons.
# original:
# b==="date"&&r.jsx("div",{className:"mb-3 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm",children:r.jsxs("button",{type:"button",onClick:()=>H(null),className:"flex w-full items-center gap-3 px-4 py-3 text-left transition-colors hover:bg-slate-50",children:[r.jsx("span",{className:"flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full border border-amber-200 text-[11px] font-semibold text-amber-500",children:"1"}),r.jsx("span",{className:"text-sm text-slate-700",children:Bv})]})})

old_block = r'b==="date"&&r\.jsx\("div",\{className:"mb-3 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm",children:r\.jsxs\("button",\{type:"button",onClick:\(\)=>H\(null\),className:"flex w-full items-center gap-3 px-4 py-3 text-left transition-colors hover:bg-slate-50",children:\[r\.jsx\("span",\{className:"flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full border border-amber-200 text-\[11px\] font-semibold text-amber-500",children:"1"\}\),r\.jsx\("span",\{className:"text-sm text-slate-700",children:Bv\}\)\]\}\)\}\)'

# We will create an array of buttons and map them
new_block = r'''b==="date"&&r.jsx("div",{className:"mb-3 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm",children:
  ["Lunes 21 de Septiembre", "Viernes 25 de Septiembre", "Lunes 28 de Septiembre", "Otra fecha — la escribo yo", null].map((dateOption, idx) => 
    r.jsxs("div", {
      className:"flex flex-col w-full text-left border-b border-gray-100 last:border-b-0",
      children: [
        r.jsxs("button", {
          type:"button",
          onClick: () => { if(dateOption !== "Otra fecha — la escribo yo") H(dateOption); },
          className:"flex w-full items-center gap-3 px-4 py-3 text-left transition-colors hover:bg-slate-50",
          children: [
            r.jsx("span", {className:"flex h-6 w-6 flex-shrink-0 items-center justify-center rounded-full border border-indigo-200 text-[11px] font-semibold text-indigo-500", children:idx+1}),
            r.jsx("span", {className:"text-sm text-slate-700 font-medium", children:dateOption || Bv})
          ]
        }),
        dateOption === "Otra fecha — la escribo yo" ? r.jsx("div", {
          className:"px-4 pb-3 pl-12",
          children: r.jsx("input", {
            type:"text",
            placeholder:"Escribe la fecha aquí y presiona Enter...",
            value: D,
            onChange: (e) => M(e.target.value),
            onKeyDown: (e) => { if(e.key==="Enter"){ e.preventDefault(); H(D); } },
            className:"w-full rounded border border-gray-300 bg-white px-3 py-2 text-sm text-slate-700 shadow-sm outline-none focus:border-indigo-400"
          })
        }) : null
      ]
    })
  )
})'''
new_block = new_block.replace('\n', '')

content = re.sub(old_block, new_block, content)

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("Applied date choices")
