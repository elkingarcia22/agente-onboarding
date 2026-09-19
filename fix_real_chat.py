import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# The entire JS logic to replace:
new_js = """        // ===== REAL ONBOARDING AI CHAT LOGIC =====
        const NV = [
            {
                id: "datos",
                title: "Verificación de datos y alta",
                stage: "Compliance",
                taskName: "Alta en la plataforma",
                message: "¡Hola! Vamos a configurar el plan de onboarding para el nuevo talento. Para empezar y poder darle acceso a la plataforma, tengo estos datos preliminares:\\n\\nNombre*: Mariana Suárez Londoño\\nCorreo*: mariana.suarez@email.com\\nIdentificación: SULM940213MDFRND04\\nTeléfono: +57 310 555 2048\\nCiudad: Ciudad de México\\nPaís: México\\n\\n(*) Nombre y correo son los obligatorios para darle acceso; el resto es opcional.\\n\\n¿Son correctos o necesitas actualizar/agregar algo más?",
                choices: [
                    {id: "datos-ok", label: "Los datos están correctos", planLabel: "Datos confirmados", reply: "Perfecto, dejo los datos confirmados para el alta."},
                    {id: "datos-editar", label: "Necesito corregir algo", planLabel: "Datos por corregir", reply: "Sin problema. Cuéntame qué hay que ajustar y lo dejo anotado para el alta.", needsDetail: true, detailPrompt: "Escribe el dato a corregir…"}
                ],
                datePrompt: "¿En qué fecha exacta te gustaría que le demos de alta en la plataforma para que reciba sus accesos? Si aún no la tienes, no te preocupes: lo podemos dejar abierto para más adelante."
            },
            {
                id: "cultura",
                title: "Cultura, OKRs y formación",
                stage: "Clarification & Culture",
                taskName: "Inmersión en cultura y OKRs",
                message: "¡Perfecto! Pasemos a la inmersión en la Cultura y los OKRs. He revisado nuestro catálogo y te sugiero asignarle el video «Nuestra Cultura Corporativa» y el módulo interactivo «Introducción a Objetivos».\\n\\nSi eliges la plataforma, el contenido queda asignado dentro de su plan de tareas: le aparece junto al resto de su onboarding, lo ve a su ritmo y tú puedes seguir el avance desde ahí. También podemos dejar este punto para una reunión 1:1 con su líder o una charla grupal con el CEO. ¿Qué modalidad prefieres?",
                choices: [
                    {id: "cultura-async", label: "Asignar el contenido en su plan de tareas", planLabel: "Contenido asignado en el plan de tareas", reply: "Buena elección: le asigno el video y el módulo interactivo en su plan de tareas, para que los vea a su ritmo y quede registro del avance."},
                    {id: "cultura-lider", label: "Reunión 1:1 con su líder", planLabel: "Reunión 1:1 con su líder", reply: "Listo, entonces este punto se aborda en una 1:1 con su líder."},
                    {id: "cultura-ceo", label: "Charla grupal con el CEO", planLabel: "Charla grupal con el CEO", reply: "Anotado: lo sumo a la próxima charla grupal con el CEO."}
                ],
                datePrompt: "¿Para qué fecha límite debería estar completada esta etapa?"
            },
            {
                id: "conexion",
                title: "Conexión social",
                stage: "Connection",
                taskName: "Reto de conectividad con el equipo",
                message: "Para que rompa el hielo rápidamente con el equipo, te propongo un pequeño «reto de conectividad»: que se presente en el canal general de Slack (o la herramienta que usen) compartiendo un dato curioso sobre sí mismo, o lanzando una breve encuesta interactiva.\\n\\n¿Te suena bien activar este reto o prefieres definir otra dinámica?",
                choices: [
                    {id: "conexion-reto", label: "Activar el reto de conectividad (Slack)", planLabel: "Reto de conectividad en Slack", reply: "Genial, activo el reto y preparo la notificación para el equipo."},
                    {id: "conexion-reunion", label: "Presentarse en la reunión de equipo", planLabel: "Presentación en reunión de equipo", reply: "Perfecto, lo agendamos para la próxima reunión grupal."},
                    {id: "conexion-cafes", label: "Cafés virtuales con compañeros", planLabel: "Cafés virtuales 1:1", reply: "Excelente idea, programaremos cafés cortos para que conozca a sus compañeros."}
                ],
                datePrompt: "¿Cuándo le enviamos la notificación para que lo haga?"
            },
            {
                id: "feedback",
                title: "Seguimiento y feedback",
                stage: "Check-back",
                taskName: "Medición de experiencia (días 15, 30 y 60)",
                message: "Finalmente, necesitamos medir cómo se siente durante sus primeros días. Para facilitarte el trabajo, te propongo usar nuestro módulo nativo de encuestas: podemos dejar programados envíos automáticos de feedback para sus días 15, 30 y 60.\\n\\n¿Te gustaría que automatice estas encuestas por la plataforma, o prefieres agendar reuniones de chequeo uno a uno?",
                choices: [
                    {id: "feedback-encuestas", label: "Automatizar las encuestas", planLabel: "Encuestas automáticas (días 15, 30 y 60)", reply: "Perfecto, programo las tres encuestas en el módulo nativo y te aviso con cada resultado."},
                    {id: "feedback-reuniones", label: "Agendar reuniones 1:1", planLabel: "Reuniones de chequeo 1:1", reply: "De acuerdo, entonces dejo creados los recordatorios de calendario para los chequeos."}
                ],
                datePrompt: "¿En qué fecha aproximada arrancamos con el primer chequeo?"
            }
        ];

        const dateOptions = ["Lunes 21 de Septiembre", "Viernes 25 de Septiembre", "Lunes 28 de Septiembre", "Otra fecha — la escribo yo"];
        
        let obState = { stepIndex: 0, phase: "choice", currentChoice: null, answers: [] };
        
        function scrollObChat() {
            const container = document.getElementById('onboarding-chat-messages');
            container.scrollTop = container.scrollHeight;
        }

        function obChatAddUserMessage(text) {
            const container = document.getElementById('onboarding-chat-messages');
            const msg = document.createElement('div');
            msg.className = 'tw-flex tw-justify-end';
            msg.innerHTML = `<div class="tw-flex tw-items-start tw-gap-3 tw-max-w-85"><div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-slate-100-80 tw-text-slate-800 tw-rounded-tr-none" style="background: rgba(241, 245, 249, 0.8);">${text}</div></div>`;
            container.appendChild(msg);
            scrollObChat();
        }

        function obChatAddAiMessage(text) {
            const container = document.getElementById('onboarding-chat-messages');
            const msg = document.createElement('div');
            msg.className = 'tw-flex tw-justify-start';
            msg.innerHTML = `<div class="tw-flex tw-items-start tw-gap-3 tw-max-w-95"><div class="tw-w-8 tw-h-8 tw-rounded-full tw-bg-gradient tw-shadow-lg tw-flex-shrink-0 tw-mt-1 tw-border tw-border-white" style="border-width: 2px; border-color: white;"></div><div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-white tw-border tw-border-gray-100 tw-text-slate-700 tw-rounded-tl-none">${text}</div></div>`;
            container.appendChild(msg);
            scrollObChat();
        }

        function obUpdateProgress() {
            const idx = obState.stepIndex;
            for(let i=0; i<4; i++) {
                const el = document.getElementById('ob-prog-' + (i+1));
                if(i < idx) el.style.background = '#6366f1';
                else if(i === idx) el.style.background = '#a5b4fc';
                else el.style.background = '#e5e7eb';
            }
        }

        function obRenderChoices() {
            const choicesBox = document.getElementById('onboarding-choices-box');
            if (obState.phase === "choice") {
                const step = NV[obState.stepIndex];
                let html = '';
                step.choices.forEach((c, idx) => {
                    html += `
                        <button type="button" onclick="obHandleChoice(${idx})" style="display: flex; width: 100%; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer;">
                            <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">${idx+1}</span>
                            <span style="font-size: 14px; color: #334155; font-weight: 500;">${c.label}</span>
                        </button>
                    `;
                });
                choicesBox.innerHTML = html;
                choicesBox.style.display = 'block';
                choicesBox.style.opacity = '1';
                choicesBox.style.pointerEvents = 'auto';
                document.getElementById('ob-main-textarea').placeholder = "Elige una opción o escribe tu respuesta...";
                document.getElementById('ob-main-textarea').disabled = false;
            } else if (obState.phase === "detail") {
                const c = NV[obState.stepIndex].choices[obState.currentChoice];
                choicesBox.innerHTML = `
                    <div style="display: flex; flex-direction: column; width: 100%; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white;">
                        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                            <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">!</span>
                            <span style="font-size: 14px; color: #334155; font-weight: 500;">${c.label}</span>
                        </div>
                        <input type="text" id="ob-custom-detail" placeholder="${c.detailPrompt}" style="margin-top: 4px; width: 100%; border-radius: 6px; border: 1px solid #d1d5db; background: white; padding: 8px 12px; font-size: 14px; color: #334155; outline: none;" onkeydown="if(event.key==='Enter' && this.value.trim()!==''){ obHandleDetail(this.value); }">
                    </div>
                `;
                document.getElementById('ob-main-textarea').placeholder = c.detailPrompt;
                setTimeout(() => document.getElementById('ob-custom-detail').focus(), 100);
            } else if (obState.phase === "date") {
                let html = '';
                dateOptions.forEach((d, idx) => {
                    html += `
                        <button type="button" onclick="obHandleDate('${d}')" style="display: flex; width: 100%; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer;">
                            <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">${idx+1}</span>
                            <span style="font-size: 14px; color: #334155; font-weight: 500;">${d}</span>
                        </button>
                    `;
                });
                choicesBox.innerHTML = html;
                document.getElementById('ob-main-textarea').placeholder = "Elige una fecha o escribe una...";
            } else if (obState.phase === "confirm") {
                choicesBox.innerHTML = `
                    <button type="button" onclick="obHandleConfirm(true)" style="display: flex; width: 100%; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer;">
                        <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">1</span>
                        <span style="font-size: 14px; color: #334155; font-weight: 500;">Generar mi plan</span>
                    </button>
                    <button type="button" onclick="obHandleConfirm(false)" style="display: flex; width: 100%; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer;">
                        <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">2</span>
                        <span style="font-size: 14px; color: #334155; font-weight: 500;">Quiero hacer un último ajuste</span>
                    </button>
                `;
                document.getElementById('ob-main-textarea').disabled = true;
                document.getElementById('ob-main-textarea').placeholder = "Esperando confirmación...";
            } else if (obState.phase === "generating" || obState.phase === "done") {
                choicesBox.style.display = 'none';
                document.getElementById('ob-main-textarea').disabled = true;
                document.getElementById('ob-main-textarea').placeholder = "Plan generado";
            }
        }

        function obHandleChoice(idx) {
            const step = NV[obState.stepIndex];
            const c = step.choices[idx];
            obState.currentChoice = idx;
            
            if (c.needsDetail) {
                obState.phase = "detail";
                obRenderChoices();
            } else {
                obChatAddUserMessage(c.label);
                obState.answers.push({ step: step.id, task: step.taskName, choice: c.planLabel });
                document.getElementById('onboarding-choices-box').style.opacity = '0.5';
                document.getElementById('onboarding-choices-box').style.pointerEvents = 'none';
                setTimeout(() => {
                    obChatAddAiMessage(c.reply + "\\n\\n" + step.datePrompt);
                    obState.phase = "date";
                    obRenderChoices();
                }, 800);
            }
        }

        function obHandleDetail(text) {
            const step = NV[obState.stepIndex];
            const c = step.choices[obState.currentChoice];
            obChatAddUserMessage(c.label + ": " + text);
            obState.answers.push({ step: step.id, task: step.taskName, choice: c.planLabel + " (" + text + ")" });
            document.getElementById('onboarding-choices-box').style.opacity = '0.5';
            document.getElementById('onboarding-choices-box').style.pointerEvents = 'none';
            setTimeout(() => {
                obChatAddAiMessage(c.reply + "\\n\\n" + step.datePrompt);
                obState.phase = "date";
                obRenderChoices();
            }, 800);
        }

        function obHandleDate(dateText) {
            if (dateText === "Otra fecha — la escribo yo") {
                document.getElementById('ob-main-textarea').focus();
                return;
            }
            obChatAddUserMessage(dateText);
            document.getElementById('onboarding-choices-box').style.opacity = '0.5';
            document.getElementById('onboarding-choices-box').style.pointerEvents = 'none';
            
            setTimeout(() => {
                obState.stepIndex++;
                if (obState.stepIndex < NV.length) {
                    obUpdateProgress();
                    obChatAddAiMessage(NV[obState.stepIndex].message);
                    obState.phase = "choice";
                    obRenderChoices();
                } else {
                    // All steps completed!
                    obUpdateProgress();
                    obChatAddAiMessage("¡Listo! Ya tengo todo el plan con las actividades de " + NV.map(n=>n.stage).join(', ') + ".\\n\\n¿Quieres generarlo o hacer un último ajuste?");
                    obState.phase = "confirm";
                    obRenderChoices();
                }
            }, 800);
        }

        function obHandleConfirm(generate) {
            if (generate) {
                obChatAddUserMessage("Generar mi plan");
                obState.phase = "generating";
                obRenderChoices();
                obChatAddAiMessage("Procesando información y generando el plan definitivo de onboarding...");
                
                // Show final output after 2 seconds
                setTimeout(() => {
                    obState.phase = "done";
                    obRenderChoices();
                    // Render the plan in step 2!
                    const planContainer = document.getElementById('onboarding-generated-plan');
                    let planHtml = '';
                    obState.answers.forEach(ans => {
                        planHtml += `
                        <div style="display: flex; align-items: flex-start; gap: 12px;">
                            <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #10b981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
                                <i class="far fa-check" style="color: #10b981; font-size: 12px;"></i>
                            </div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 14px; font-weight: 600; color: #111827;">${ans.task}</span>
                                <span style="font-size: 13px; color: #6b7280; margin-top: 2px;">${ans.choice}</span>
                            </div>
                        </div>`;
                    });
                    planContainer.innerHTML = planHtml;
                    
                    document.getElementById('onboarding-step-1').style.display = 'none';
                    document.getElementById('onboarding-drawer-title').innerHTML = '<i class="far fa-gear" style="color: var(--ubits-brand-primary);"></i> Configuración de Agente';
                    document.getElementById('onboarding-step-2').style.display = 'flex';
                    document.getElementById('onboarding-step-2-footer').style.display = 'flex';
                }, 2000);
            } else {
                obChatAddUserMessage("Quiero hacer un último ajuste");
                obChatAddAiMessage("Entendido. Cuéntame qué te gustaría ajustar.");
                document.getElementById('ob-main-textarea').disabled = false;
                document.getElementById('ob-main-textarea').placeholder = "Escribe tu ajuste...";
                document.getElementById('ob-main-textarea').focus();
            }
        }

        function obChatSendText() {
            const input = document.getElementById('ob-main-textarea');
            const text = input.value.trim();
            if (text === '') return;
            
            if (obState.phase === "choice") {
                // If they typed something manually instead of picking a choice
                const step = NV[obState.stepIndex];
                obState.answers.push({ step: step.id, task: step.taskName, choice: text });
                obChatAddUserMessage(text);
                document.getElementById('onboarding-choices-box').style.opacity = '0.5';
                document.getElementById('onboarding-choices-box').style.pointerEvents = 'none';
                setTimeout(() => {
                    obChatAddAiMessage(step.datePrompt);
                    obState.phase = "date";
                    obRenderChoices();
                }, 800);
            } else if (obState.phase === "detail") {
                obHandleDetail(text);
            } else if (obState.phase === "date") {
                obHandleDate(text);
            } else if (obState.phase === "confirm") {
                obChatAddUserMessage(text);
                obChatAddAiMessage("Ajuste registrado. ¿Podemos proceder a generar el plan?");
                // Keep it in confirm phase
            }
            input.value = '';
        }

        window.openOnboardingConfigDrawer = function(stageId) {
            const drawer = document.getElementById('onboardingConfigDrawer');
            const overlay = document.getElementById('drawerOverlay');
            if (drawer) drawer.classList.add('active');
            if (overlay) overlay.classList.add('active');
            
            // Reset state
            obState = { stepIndex: 0, phase: "choice", currentChoice: null, answers: [] };
            document.getElementById('onboarding-step-1').style.display = 'flex';
            document.getElementById('onboarding-step-2').style.display = 'none';
            document.getElementById('onboarding-step-2-footer').style.display = 'none';
            document.getElementById('onboarding-drawer-title').innerHTML = '<i class="far fa-sparkles" style="color: var(--ubits-brand-primary);"></i> Agente de Onboarding';
            
            document.getElementById('onboarding-chat-messages').innerHTML = '';
            
            obUpdateProgress();
            obChatAddAiMessage(NV[0].message);
            obRenderChoices();
        }

        window.closeOnboardingConfigDrawer = function() {
            const drawer = document.getElementById('onboardingConfigDrawer');
            const overlay = document.getElementById('drawerOverlay');
            if (drawer) drawer.classList.remove('active');
            if (overlay) overlay.classList.remove('active');
        }
        
        window.sendOnboardingMessage = function() {
            obChatSendText();
        }
"""

# Read and replace script section
old_js_pattern = re.compile(r"// Variables para el flujo de Onboarding Chat.*window\.sendOnboardingMessage = function\(\) \{\n            obChatSendText\(\);\n        \}", re.DOTALL)
content = old_js_pattern.sub(new_js, content)

# I also need to make sure the target div for generated plan exists in step 2.
# In my step 2 HTML, I had static tasks. I will give the container an ID.
old_plan = """<div style="background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
                    <div style="display: flex; flex-direction: column; gap: 16px;">
                        <!-- Task 1 -->"""

new_plan = """<div style="background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
                    <div id="onboarding-generated-plan" style="display: flex; flex-direction: column; gap: 16px;">
                        <!-- Plan will be rendered here dynamically -->"""

# Regex sub to replace the static tasks
old_tasks_pattern = re.compile(r'<div style="background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 24px;">.*?</div>\s*</div>\s*</div>', re.DOTALL)

# But wait, earlier I used a different regex. Let's just do a manual replace.
content = content.replace("""<div style="background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
                    <div style="display: flex; flex-direction: column; gap: 16px;">
                        <!-- Task 1 -->
                        <div style="display: flex; align-items: flex-start; gap: 12px;">
                            <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #10b981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
                                <i class="far fa-check" style="color: #10b981; font-size: 12px;"></i>
                            </div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 14px; font-weight: 600; color: #111827;">Alta en la plataforma</span>
                                <span style="font-size: 13px; color: #6b7280; margin-top: 2px;">Datos confirmados</span>
                            </div>
                        </div>
                        <!-- Task 2 -->
                        <div style="display: flex; align-items: flex-start; gap: 12px;">
                            <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #10b981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
                                <i class="far fa-check" style="color: #10b981; font-size: 12px;"></i>
                            </div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 14px; font-weight: 600; color: #111827;">Inmersión en cultura y OKRs</span>
                                <span style="font-size: 13px; color: #6b7280; margin-top: 2px;">Reunión 1:1 con su líder</span>
                            </div>
                        </div>
                        <!-- Task 3 -->
                        <div style="display: flex; align-items: flex-start; gap: 12px;">
                            <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #10b981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
                                <i class="far fa-check" style="color: #10b981; font-size: 12px;"></i>
                            </div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 14px; font-weight: 600; color: #111827;">Reto de conectividad</span>
                                <span style="font-size: 13px; color: #6b7280; margin-top: 2px;">Mensaje de presentación en el canal del equipo</span>
                            </div>
                        </div>
                    </div>
                </div>""", 
                """<div style="background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
                    <div id="onboarding-generated-plan" style="display: flex; flex-direction: column; gap: 16px;">
                        <!-- Contenido dinámico -->
                    </div>
                </div>""")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done with full state machine chat replacement")
