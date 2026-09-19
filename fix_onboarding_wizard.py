import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I need to find the <div class="serena-config-drawer" id="onboardingConfigDrawer"> and replace it completely.
# I'll use regex to replace everything from id="onboardingConfigDrawer" to the end of the drawer.
# It's better to just replace the whole drawer string since I know what I generated.

drawer_start = '<div class="serena-config-drawer" id="onboardingConfigDrawer">'
drawer_end_pattern = r'<div class="serena-config-drawer" id="onboardingConfigDrawer">.*?</div>\s*</div>\s*</div>'

new_drawer = """<div class="serena-config-drawer" id="onboardingConfigDrawer">
        <div class="drawer-header">
            <h2 class="ubits-heading-h4" id="onboarding-drawer-title">
                <i class="far fa-sparkles" style="color: var(--ubits-brand-primary);"></i> Agente de Onboarding
            </h2>
            <button class="icon-btn" onclick="closeOnboardingConfigDrawer()">
                <i class="far fa-times"></i>
            </button>
        </div>
        <div class="drawer-body" style="padding: 0; display: flex; flex-direction: column; background: #fafafa;">
            
            <!-- STEP 1: CHAT EXPERIENCE -->
            <div id="onboarding-step-1" style="display: flex; flex-direction: column; flex: 1; height: 100%;">
                
                <!-- Progress Bars -->
                <div style="flex-shrink: 0; padding: 12px 24px; border-bottom: 1px solid #f3f4f6; display: flex; align-items: center; gap: 6px; background: white;">
                    <div style="flex: 1;">
                        <div style="height: 4px; border-radius: 9999px; background: #6366f1; transition: background 0.3s;" id="ob-prog-1"></div>
                        <p style="margin-top: 6px; font-size: 10px; color: #9ca3af; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Compliance</p>
                    </div>
                    <div style="flex: 1;">
                        <div style="height: 4px; border-radius: 9999px; background: #e5e7eb; transition: background 0.3s;" id="ob-prog-2"></div>
                        <p style="margin-top: 6px; font-size: 10px; color: #9ca3af; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Clarification & Culture</p>
                    </div>
                    <div style="flex: 1;">
                        <div style="height: 4px; border-radius: 9999px; background: #e5e7eb; transition: background 0.3s;" id="ob-prog-3"></div>
                        <p style="margin-top: 6px; font-size: 10px; color: #9ca3af; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Connection</p>
                    </div>
                    <div style="flex: 1;">
                        <div style="height: 4px; border-radius: 9999px; background: #e5e7eb; transition: background 0.3s;" id="ob-prog-4"></div>
                        <p style="margin-top: 6px; font-size: 10px; color: #9ca3af; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">Check-back</p>
                    </div>
                </div>

                <!-- Messages Area -->
                <div style="flex: 1; overflow-y: auto; padding: 20px 24px; display: flex; flex-direction: column; gap: 16px;" id="onboarding-chat-messages">
                    <!-- Initial AI Message -->
                    <div style="display: flex; justify-content: flex-start;">
                        <div style="display: flex; align-items: flex-start; gap: 12px; max-width: 95%;">
                            <div style="width: 32px; height: 32px; border-radius: 50%; background-image: linear-gradient(to top right, #60a5fa, #6366f1, #a855f7); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); flex-shrink: 0; margin-top: 4px; border: 2px solid white;"></div>
                            <div style="padding: 16px; border-radius: 16px; border-top-left-radius: 0; font-size: 14px; line-height: 1.6; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); white-space: pre-line; background: white; border: 1px solid #f3f4f6; color: #334155;">¡Hola! Vamos a configurar el plan de onboarding para el nuevo talento. Para empezar y poder darle acceso a la plataforma, tengo estos datos preliminares:

Nombre*: Mariana Suárez Londoño
Correo*: mariana.suarez@email.com
Identificación: SULM940213MDFRND04
Teléfono: +57 310 555 2048
Ciudad: Ciudad de México
País: México

(*) Nombre y correo son los obligatorios para darle acceso; el resto es opcional.

¿Son correctos o necesitas actualizar/agregar algo más?</div>
                        </div>
                    </div>
                </div>

                <!-- Input / Choices Area -->
                <div style="padding: 16px 24px; background: white; border-top: 1px solid #f3f4f6;" id="onboarding-chat-input-area">
                    
                    <!-- Choices Box -->
                    <div id="onboarding-choices-box" style="margin-bottom: 12px; border-radius: 16px; border: 1px solid #e5e7eb; background: white; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); overflow: hidden;">
                        <button type="button" onclick="obChatSelectChoice(1, 'Los datos están correctos')" style="display: flex; width: 100%; items-center; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer; transition: background 0.2s;" onmouseover="this.style.background='#f8fafc'" onmouseout="this.style.background='white'">
                            <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">1</span>
                            <span style="font-size: 14px; color: #334155; font-weight: 500;">Los datos están correctos</span>
                        </button>
                        <div style="display: flex; flex-direction: column; width: 100%; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white;">
                            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                                <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">2</span>
                                <span style="font-size: 14px; color: #334155; font-weight: 500;">Necesito corregir algo</span>
                            </div>
                            <input type="text" id="ob-custom-input-1" placeholder="Escribe tu propia respuesta aquí" style="margin-top: 4px; width: 100%; border-radius: 6px; border: 1px solid #d1d5db; background: white; padding: 8px 12px; font-size: 14px; color: #334155; outline: none;" onkeydown="if(event.key==='Enter' && this.value.trim()!==''){ obChatSelectChoice(2, this.value); }">
                        </div>
                    </div>

                    <!-- Main Textarea Input -->
                    <div style="display: flex; flex-direction: column; border-radius: 16px; border: 1px solid #e5e7eb; background: white; padding: 12px; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05);">
                        <textarea rows="2" id="ob-main-textarea" placeholder="Elige una opción o escribe tu respuesta..." style="width: 100%; resize: none; border: none; background: transparent; font-size: 14px; color: #334155; outline: none; margin-bottom: 8px;"></textarea>
                        <div style="display: flex; justify-content: flex-end;">
                            <button type="button" onclick="obChatSendText()" style="display: flex; height: 36px; width: 36px; items-center; justify-content: center; border-radius: 50%; background-image: linear-gradient(to top right, #818cf8, #a855f7); color: white; border: none; cursor: pointer; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); opacity: 0.5;" id="ob-send-btn">
                                <i class="far fa-arrow-up" style="font-size: 14px;"></i>
                            </button>
                        </div>
                    </div>
                    <p style="margin-top: 12px; text-align: center; font-size: 10px; color: #9ca3af;">Agentes AI puede cometer errores, verifica las respuestas.</p>
                </div>
            </div>

            <!-- STEP 2: CONFIGURATION SETTINGS (HIDDEN INITIALLY) -->
            <div id="onboarding-step-2" style="display: none; flex-direction: column; flex: 1; height: 100%; padding: 24px; overflow-y: auto;">
                
                <h3 class="ubits-heading-h6" style="margin-bottom: 16px;">¿Cómo quieres que se active este agente?</h3>
                
                <div class="radio-group" style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 32px;">
                    <label class="radio-label" style="display: flex; align-items: flex-start; gap: 12px; cursor: pointer;">
                        <input type="radio" name="onboarding-activation" value="auto" checked style="margin-top: 3px;">
                        <div>
                            <span class="ubits-body-md-medium" style="display: block;">Automáticamente</span>
                            <span class="ubits-body-sm-regular" style="color: var(--ubits-fg-2-medium);">Cuando el candidato llegue a esta etapa</span>
                        </div>
                    </label>
                    <label class="radio-label" style="display: flex; align-items: flex-start; gap: 12px; cursor: pointer;">
                        <input type="radio" name="onboarding-activation" value="manual" style="margin-top: 3px;">
                        <div>
                            <span class="ubits-body-md-medium" style="display: block;">Manualmente</span>
                            <span class="ubits-body-sm-regular" style="color: var(--ubits-fg-2-medium);">Tú decides cuándo activarlo desde el tablero</span>
                        </div>
                    </label>
                </div>

                <div style="height: 1px; background: #e5e7eb; margin-bottom: 24px;"></div>

                <h3 class="ubits-heading-h6" style="margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
                    <i class="far fa-list-check" style="color: #6366f1;"></i> Plan de Onboarding Generado
                </h3>

                <!-- Generated Plan Preview -->
                <div style="background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; margin-bottom: 24px;">
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
                </div>

            </div>
            
            <!-- Step 2 Footer (Save Button) -->
            <div id="onboarding-step-2-footer" class="drawer-footer" style="display: none; padding: 16px 24px; border-top: 1px solid var(--ubits-border-light); background: white;">
                <button class="ubits-button ubits-button--primary" style="width: 100%;" onclick="saveOnboardingConfig()">
                    Guardar configuración
                </button>
            </div>

        </div>
    </div>"""

# Replace the drawer HTML using regex
pattern = re.compile(r'<div class="serena-config-drawer" id="onboardingConfigDrawer">.*?</div>\s*</div>\s*</div>', re.DOTALL)
content = pattern.sub(new_drawer, content)

# Also, update the JS scripts associated with it
js_to_add = """
        // Variables para el flujo de Onboarding Chat
        let obChatStep = 0;
        
        function obChatAddUserMessage(text) {
            const container = document.getElementById('onboarding-chat-messages');
            const msg = document.createElement('div');
            msg.style.display = 'flex';
            msg.style.justifyContent = 'flex-end';
            msg.innerHTML = `
                <div style="display: flex; align-items: flex-start; gap: 12px; max-width: 85%;">
                    <div style="padding: 16px; border-radius: 16px; border-top-right-radius: 0; font-size: 14px; line-height: 1.6; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); white-space: pre-line; background: rgba(241, 245, 249, 0.8); color: #1e293b;">${text}</div>
                </div>
            `;
            container.appendChild(msg);
            container.scrollTop = container.scrollHeight;
        }

        function obChatAddAiMessage(text) {
            const container = document.getElementById('onboarding-chat-messages');
            const msg = document.createElement('div');
            msg.style.display = 'flex';
            msg.style.justifyContent = 'flex-start';
            msg.innerHTML = `
                <div style="display: flex; align-items: flex-start; gap: 12px; max-width: 95%;">
                    <div style="width: 32px; height: 32px; border-radius: 50%; background-image: linear-gradient(to top right, #60a5fa, #6366f1, #a855f7); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); flex-shrink: 0; margin-top: 4px; border: 2px solid white;"></div>
                    <div style="padding: 16px; border-radius: 16px; border-top-left-radius: 0; font-size: 14px; line-height: 1.6; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); white-space: pre-line; background: white; border: 1px solid #f3f4f6; color: #334155;">${text}</div>
                </div>
            `;
            container.appendChild(msg);
            container.scrollTop = container.scrollHeight;
        }

        function obChatUpdateChoices(step) {
            const choicesBox = document.getElementById('onboarding-choices-box');
            if(step === 1) {
                document.getElementById('ob-prog-2').style.background = '#6366f1';
                choicesBox.innerHTML = `
                    <button type="button" onclick="obChatSelectChoice(1, 'Sí, generar plan')" style="display: flex; width: 100%; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer;">
                        <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">1</span>
                        <span style="font-size: 14px; color: #334155; font-weight: 500;">Sí, generar plan</span>
                    </button>
                    <div style="display: flex; flex-direction: column; width: 100%; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white;">
                        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                            <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">2</span>
                            <span style="font-size: 14px; color: #334155; font-weight: 500;">Agregar más contexto</span>
                        </div>
                        <input type="text" id="ob-custom-input-2" placeholder="Escribe tu contexto aquí" style="margin-top: 4px; width: 100%; border-radius: 6px; border: 1px solid #d1d5db; background: white; padding: 8px 12px; font-size: 14px; color: #334155; outline: none;" onkeydown="if(event.key==='Enter' && this.value.trim()!==''){ obChatSelectChoice(2, this.value); }">
                    </div>
                `;
            } else if (step === 2) {
                document.getElementById('ob-prog-3').style.background = '#6366f1';
                document.getElementById('ob-prog-4').style.background = '#6366f1';
                choicesBox.style.display = 'none';
                document.getElementById('ob-main-textarea').disabled = true;
                document.getElementById('ob-main-textarea').placeholder = 'Plan generado';
                document.getElementById('ob-send-btn').style.opacity = '0.4';
                document.getElementById('ob-send-btn').disabled = true;
            }
        }

        function obChatSelectChoice(idx, text) {
            obChatAddUserMessage(text);
            document.getElementById('onboarding-choices-box').style.pointerEvents = 'none';
            document.getElementById('onboarding-choices-box').style.opacity = '0.6';
            
            setTimeout(() => {
                obChatStep++;
                if(obChatStep === 1) {
                    obChatAddAiMessage('¡Perfecto! Con estos datos procederé a estructurar el plan inicial. ¿Quieres que genere el plan ahora o deseas agregar algún contexto especial sobre la cultura de la empresa?');
                    document.getElementById('onboarding-choices-box').style.pointerEvents = 'auto';
                    document.getElementById('onboarding-choices-box').style.opacity = '1';
                    obChatUpdateChoices(1);
                } else if(obChatStep === 2) {
                    obChatAddAiMessage('¡Entendido! Generando plan de onboarding...\n\n✅ Tareas de compliance creadas\n✅ Entrevistas 1:1 agendadas\n✅ Retos de cultura definidos\n\nEl plan de onboarding ha sido generado exitosamente.');
                    obChatUpdateChoices(2);
                    
                    // TRANSITION TO STEP 2 (Config screen)
                    setTimeout(() => {
                        document.getElementById('onboarding-step-1').style.display = 'none';
                        document.getElementById('onboarding-drawer-title').innerHTML = '<i class="far fa-gear" style="color: var(--ubits-brand-primary);"></i> Configuración de Agente';
                        document.getElementById('onboarding-step-2').style.display = 'flex';
                        document.getElementById('onboarding-step-2-footer').style.display = 'flex';
                    }, 2000);
                }
            }, 800);
        }

        function obChatSendText() {
            const input = document.getElementById('ob-main-textarea');
            if(input.value.trim() !== '') {
                obChatSelectChoice(3, input.value);
                input.value = '';
            }
        }
        
        // Ensure textarea enables the button
        document.addEventListener('input', function(e) {
            if(e.target && e.target.id === 'ob-main-textarea') {
                const btn = document.getElementById('ob-send-btn');
                if(e.target.value.trim() !== '') {
                    btn.style.opacity = '1';
                } else {
                    btn.style.opacity = '0.5';
                }
            }
        });

        function saveOnboardingConfig() {
            closeOnboardingConfigDrawer();
            showSuccessAlert('Configuración del Agente de Onboarding guardada correctamente.');
        }
"""

# I need to insert `js_to_add` right after `window.openOnboardingConfigDrawer = function(stageId) {`
# Or better, just append it to the end of my previous script block.

js_replacement = """        window.openOnboardingConfigDrawer = function(stageId) {
            const drawer = document.getElementById('onboardingConfigDrawer');
            const overlay = document.getElementById('drawerOverlay');
            if (drawer) drawer.classList.add('active');
            if (overlay) overlay.classList.add('active');
            
            // Reset state
            obChatStep = 0;
            document.getElementById('onboarding-step-1').style.display = 'flex';
            document.getElementById('onboarding-step-2').style.display = 'none';
            document.getElementById('onboarding-step-2-footer').style.display = 'none';
            document.getElementById('onboarding-drawer-title').innerHTML = '<i class="far fa-sparkles" style="color: var(--ubits-brand-primary);"></i> Agente de Onboarding';
            document.getElementById('ob-prog-2').style.background = '#e5e7eb';
            document.getElementById('ob-prog-3').style.background = '#e5e7eb';
            document.getElementById('ob-prog-4').style.background = '#e5e7eb';
            document.getElementById('ob-main-textarea').disabled = false;
            document.getElementById('ob-main-textarea').placeholder = 'Elige una opción o escribe tu respuesta...';
            document.getElementById('ob-main-textarea').value = '';
            document.getElementById('onboarding-choices-box').style.display = 'block';
            document.getElementById('onboarding-choices-box').style.pointerEvents = 'auto';
            document.getElementById('onboarding-choices-box').style.opacity = '1';
            
            // Re-render initial choices
            document.getElementById('onboarding-choices-box').innerHTML = `
                <button type="button" onclick="obChatSelectChoice(1, 'Los datos están correctos')" style="display: flex; width: 100%; gap: 12px; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white; cursor: pointer;">
                    <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">1</span>
                    <span style="font-size: 14px; color: #334155; font-weight: 500;">Los datos están correctos</span>
                </button>
                <div style="display: flex; flex-direction: column; width: 100%; border-bottom: 1px solid #f3f4f6; padding: 12px 16px; text-align: left; background: white;">
                    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
                        <span style="display: flex; height: 24px; width: 24px; flex-shrink: 0; align-items: center; justify-content: center; border-radius: 50%; border: 1px solid #c7d2fe; font-size: 11px; font-weight: 600; color: #6366f1;">2</span>
                        <span style="font-size: 14px; color: #334155; font-weight: 500;">Necesito corregir algo</span>
                    </div>
                    <input type="text" id="ob-custom-input-1" placeholder="Escribe tu propia respuesta aquí" style="margin-top: 4px; width: 100%; border-radius: 6px; border: 1px solid #d1d5db; background: white; padding: 8px 12px; font-size: 14px; color: #334155; outline: none;" onkeydown="if(event.key==='Enter' && this.value.trim()!==''){ obChatSelectChoice(2, this.value); }">
                </div>
            `;
            
            // Clear messages and add first msg
            const messagesContainer = document.getElementById('onboarding-chat-messages');
            messagesContainer.innerHTML = `
                <div style="display: flex; justify-content: flex-start;">
                    <div style="display: flex; align-items: flex-start; gap: 12px; max-width: 95%;">
                        <div style="width: 32px; height: 32px; border-radius: 50%; background-image: linear-gradient(to top right, #60a5fa, #6366f1, #a855f7); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); flex-shrink: 0; margin-top: 4px; border: 2px solid white;"></div>
                        <div style="padding: 16px; border-radius: 16px; border-top-left-radius: 0; font-size: 14px; line-height: 1.6; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); white-space: pre-line; background: white; border: 1px solid #f3f4f6; color: #334155;">¡Hola! Vamos a configurar el plan de onboarding para el nuevo talento. Para empezar y poder darle acceso a la plataforma, tengo estos datos preliminares:

Nombre*: Mariana Suárez Londoño
Correo*: mariana.suarez@email.com
Identificación: SULM940213MDFRND04
Teléfono: +57 310 555 2048
Ciudad: Ciudad de México
País: México

(*) Nombre y correo son los obligatorios para darle acceso; el resto es opcional.

¿Son correctos o necesitas actualizar/agregar algo más?</div>
                    </div>
                </div>
            `;
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
        
        """ + js_to_add

# I'll replace my old JS logic completely.
# Find old JS logic:
old_js_start = r"window\.openOnboardingConfigDrawer = function\(stageId\) \{.*?\n        \}"
old_js_pattern = re.compile(r"window\.openOnboardingConfigDrawer = function\(stageId\).*?window\.sendOnboardingMessage = function\(\) \{.*?\n        \}", re.DOTALL)
content = old_js_pattern.sub(js_replacement, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing wizard logic")
