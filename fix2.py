import re
with open("panel-candidatos/assets/index-BF1UmWzM.js", "r") as f:
    content = f.read()

# I will find my PREVIOUS setInterval hack and completely replace it with a new one that does everything!
old_timeout_hack = r'''let count=0; let intv = setInterval\(\(\)=>\{ count\+\+; if\(count>20\) clearInterval\(intv\); document\.querySelectorAll\("\.cand__status--waiting, \.cand__status--actionable"\)\.forEach\(el => \{ if\(el\.textContent\.includes\("Esperando"\) \|\| el\.textContent\.includes\("acción"\)\) \{ el\.className = "cand__status cand__status--success"; el\.innerHTML = "<span class=\\"cand__status-dot\\" aria-hidden=\\"true\\"></span>Completado"; \} \}\); document\.querySelectorAll\("div\.rounded-xl\.border\.overflow-hidden"\)\.forEach\(card => \{ if\(card\.textContent\.includes\("Esperando acción manual"\)\) \{ const badge = card\.querySelector\("span\.bg-amber-50"\); if\(badge\) \{ badge\.className = badge\.className\.replace\("text-amber-700", "text-emerald-700"\)\.replace\("border-amber-400", "border-emerald-300"\)\.replace\("bg-amber-50", "bg-emerald-50"\); badge\.textContent = "Completado"; \} const amberText = card\.querySelector\("\.text-amber-600"\); if\(amberText\) \{ amberText\.style\.display = "none"; \} card\.querySelectorAll\("button"\)\.forEach\(b => \{ if\(b\.textContent\.includes\("Activar"\)\) \{ b\.style\.display = "none"; \} \}\); const numBadge = card\.querySelector\("\.w-8\.h-8, \.w-9\.h-9"\); if\(numBadge\) \{ numBadge\.className = numBadge\.className\.replace\("bg-gray-100", "bg-emerald-50"\)\.replace\("border-gray-200", "border-emerald-200"\)\.replace\("text-gray-500", "text-emerald-600"\); numBadge\.innerHTML = "<svg xmlns=\\"http://www.w3.org/2000/svg\\" width=\\"24\\" height=\\"24\\" viewBox=\\"0 0 24 24\\" fill=\\"none\\" stroke=\\"currentColor\\" stroke-width=\\"2\\" stroke-linecap=\\"round\\" stroke-linejoin=\\"round\\" class=\\"lucide lucide-check w-4 h-4 text-emerald-600\\"><path d=\\"M20 6 9 17l-5-5\\"></path></svg>"; \} \} \}\); \}, 250\);'''

# Note: In the new setInterval, I will make the accordion HTML dynamic and attach a listener.
new_timeout_hack = r'''let count=0; let intv = setInterval(()=>{
  count++; if(count>20) clearInterval(intv);
  document.querySelectorAll(".cand__status--waiting, .cand__status--actionable").forEach(el => {
    if(el.textContent.includes("Esperando") || el.textContent.includes("acción")) {
      el.className = "cand__status cand__status--success";
      el.innerHTML = "<span class=\"cand__status-dot\" aria-hidden=\"true\"></span>Completado";
    }
  });
  document.querySelectorAll("div.rounded-xl.border.overflow-hidden").forEach(card => {
    if(card.textContent.includes("Esperando acción manual") || card.dataset.hacked === "true") {
      card.dataset.hacked = "true";
      // Update badge
      const badge = card.querySelector("span.bg-amber-50");
      if(badge) {
        badge.className = badge.className.replace("text-amber-700", "text-emerald-700").replace("border-amber-400", "border-emerald-300").replace("bg-amber-50", "bg-emerald-50");
        badge.textContent = "Completado";
      }
      const amberText = card.querySelector(".text-amber-600");
      if(amberText) { amberText.style.display = "none"; }
      card.querySelectorAll("button").forEach(b => {
        if(b.textContent.includes("Activar")) { b.style.display = "none"; }
      });
      const numBadge = card.querySelector(".w-8.h-8, .w-9.h-9");
      if(numBadge && !numBadge.classList.contains("bg-emerald-50")) {
        numBadge.className = numBadge.className.replace("bg-gray-100", "bg-emerald-50").replace("border-gray-200", "border-emerald-200").replace("text-gray-500", "text-emerald-600");
        numBadge.innerHTML = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"lucide lucide-check w-4 h-4 text-emerald-600\"><path d=\"M20 6 9 17l-5-5\"></path></svg>";
      }
      
      // Inject accordion chevron & body
      let accordionBody = card.querySelector(".custom-accordion-body");
      if (!accordionBody) {
        // Container for chevron
        let flexContainer = card.querySelector(".flex.items-center.gap-2.flex-wrap");
        if(flexContainer && !flexContainer.querySelector(".custom-chevron")) {
          let chevronBtn = document.createElement("button");
          chevronBtn.className = "flex-shrink-0 p-2 hover:opacity-70 transition-opacity custom-chevron";
          chevronBtn.innerHTML = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\" height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\" class=\"w-5 h-5 text-gray-400 transition-transform duration-200\"><path d=\"m18 15-6-6-6 6\"></path></svg>";
          flexContainer.appendChild(chevronBtn);
          
          let bodyDiv = document.createElement("div");
          bodyDiv.className = "border-t border-gray-200 bg-gray-50 custom-accordion-body";
          bodyDiv.style.display = "none";
          
          bodyDiv.innerHTML = `
            <div class="p-6 border-t border-gray-100 bg-white">
              <div class="flex flex-col gap-6">
                <div class="flex items-center gap-2 mb-2">
                  <h4 class="text-[11px] font-bold text-gray-500 tracking-wider uppercase">Plan de onboarding creado</h4>
                </div>
                <!-- Task 1 -->
                <div class="flex items-start gap-4">
                  <div class="w-6 h-6 rounded-full border border-emerald-500 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <svg class="w-3.5 h-3.5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>
                  </div>
                  <div class="flex flex-col">
                    <span class="text-sm font-semibold text-gray-900">Alta en la plataforma</span>
                    <span class="text-[13px] text-gray-500 mt-0.5">Datos confirmados</span>
                    <span class="text-[10.5px] font-bold bg-amber-50 text-amber-700 px-2.5 py-0.5 rounded-md mt-2 w-fit flex items-center gap-1.5 border border-amber-200">
                      <svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
                      Sin fecha asignada
                    </span>
                  </div>
                </div>
                <!-- Task 2 -->
                <div class="flex items-start gap-4">
                  <div class="w-6 h-6 rounded-full border border-emerald-500 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <svg class="w-3.5 h-3.5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>
                  </div>
                  <div class="flex flex-col">
                    <span class="text-sm font-semibold text-gray-900">Inmersión en cultura y OKRs</span>
                    <span class="text-[13px] text-gray-500 mt-0.5">Reunión 1:1 con su líder</span>
                    <span class="text-[10.5px] font-bold bg-amber-50 text-amber-700 px-2.5 py-0.5 rounded-md mt-2 w-fit flex items-center gap-1.5 border border-amber-200">
                      <svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
                      Sin fecha asignada
                    </span>
                  </div>
                </div>
                <!-- Task 3 -->
                <div class="flex items-start gap-4">
                  <div class="w-6 h-6 rounded-full border border-emerald-500 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <svg class="w-3.5 h-3.5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>
                  </div>
                  <div class="flex flex-col">
                    <span class="text-sm font-semibold text-gray-900">Reto de conectividad con el equipo</span>
                    <span class="text-[13px] text-gray-500 mt-0.5">Reto de conectividad en el canal del equipo</span>
                    <span class="text-[10.5px] font-bold bg-amber-50 text-amber-700 px-2.5 py-0.5 rounded-md mt-2 w-fit flex items-center gap-1.5 border border-amber-200">
                      <svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
                      Sin fecha asignada
                    </span>
                  </div>
                </div>
                <!-- Task 4 -->
                <div class="flex items-start gap-4">
                  <div class="w-6 h-6 rounded-full border border-emerald-500 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <svg class="w-3.5 h-3.5 text-emerald-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"></path></svg>
                  </div>
                  <div class="flex flex-col">
                    <span class="text-sm font-semibold text-gray-900">Medición de experiencia (días 15, 30 y 60)</span>
                    <span class="text-[13px] text-gray-500 mt-0.5">Encuestas automáticas</span>
                    <span class="text-[10.5px] font-bold bg-amber-50 text-amber-700 px-2.5 py-0.5 rounded-md mt-2 w-fit flex items-center gap-1.5 border border-amber-200">
                      <svg class="w-3 h-3" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect><line x1="16" x2="16" y1="2" y2="6"></line><line x1="8" x2="8" y1="2" y2="6"></line><line x1="3" x2="21" y1="10" y2="10"></line></svg>
                      Sin fecha asignada
                    </span>
                  </div>
                </div>
              </div>
            </div>
          `;
          card.appendChild(bodyDiv);
          
          let isOpen = false;
          chevronBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            isOpen = !isOpen;
            bodyDiv.style.display = isOpen ? "block" : "none";
            let svg = chevronBtn.querySelector("svg");
            if (isOpen) {
              svg.classList.add("rotate-180");
            } else {
              svg.classList.remove("rotate-180");
            }
          });
          
          let mainDiv = card.querySelector(".flex-1.flex.items-center");
          if (mainDiv) {
             mainDiv.style.cursor = "pointer";
             mainDiv.classList.add("hover:opacity-70");
             mainDiv.addEventListener("click", (e) => {
                chevronBtn.click();
             });
          }
        }
      }
    }
  });
}, 250);'''

new_timeout_flat = new_timeout_hack.replace('\n', '')

content = re.sub(old_timeout_hack, new_timeout_flat, content)

with open("panel-candidatos/assets/index-BF1UmWzM.js", "w") as f:
    f.write(content)
print("DOM Hack Updated")
