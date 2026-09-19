import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the chat HTML
old_chat = """                <!-- Chat de IA simulado -->
                <div class="ai-chat-interface" id="onboarding-chat-interface" style="display: flex; flex: 1; position: relative; bottom: auto; right: auto; width: 100%; height: auto; z-index: 1; box-shadow: none; border-radius: 0; border-top: 1px solid var(--ubits-border-light);">
                    <div class="chat-header">
                        <div class="chat-user-info">
                            <div class="chat-user-avatar" style="background-color: var(--ubits-feedback-accent-info); color: white; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 12px;">
                                <i class="far fa-user-plus"></i>
                            </div>
                            <div>
                                <h3 class="chat-user-name">Agente de Onboarding</h3>
                                <p class="chat-user-description">Asistente IA</p>
                            </div>
                        </div>
                    </div>
                    <div class="chat-messages" id="onboarding-chat-messages">
                        <div class="message ai-message">
                            <div class="message-content">
                                <p>¡Hola! Soy el agente de Onboarding. Te ayudaré a configurar las tareas y actividades para los nuevos colaboradores. ¿Qué te gustaría incluir en el plan de onboarding?</p>
                            </div>
                            <div class="message-actions">
                                <div class="message-time">10:00</div>
                            </div>
                        </div>
                    </div>
                    <div class="chat-input-container">
                        <div class="chat-input">
                            <input type="text" id="onboarding-chat-input-field" placeholder="Escribe tu mensaje...">
                            <button class="icon-btn" id="onboarding-send-message" onclick="sendOnboardingMessage()">
                                <i class="far fa-paper-plane"></i>
                            </button>
                        </div>
                    </div>
                </div>"""

new_chat = """
                <!-- Chat de IA simulado (Estilo React App Tailwind) -->
                <style>
                    /* Tailwind mimics */
                    .tw-flex { display: flex; }
                    .tw-flex-col { flex-direction: column; }
                    .tw-h-full { height: 100%; }
                    .tw-w-full { width: 100%; }
                    .tw-overflow-hidden { overflow: hidden; }
                    .tw-flex-shrink-0 { flex-shrink: 0; }
                    .tw-px-6 { padding-left: 1.5rem; padding-right: 1.5rem; }
                    .tw-py-5 { padding-top: 1.25rem; padding-bottom: 1.25rem; }
                    .tw-py-3 { padding-top: 0.75rem; padding-bottom: 0.75rem; }
                    .tw-border-b { border-bottom-width: 1px; border-bottom-style: solid; }
                    .tw-border-gray-100 { border-color: #f3f4f6; }
                    .tw-border-gray-200 { border-color: #e5e7eb; }
                    .tw-items-center { align-items: center; }
                    .tw-justify-between { justify-content: space-between; }
                    .tw-justify-end { justify-content: flex-end; }
                    .tw-justify-start { justify-content: flex-start; }
                    .tw-justify-center { justify-content: center; }
                    .tw-bg-white { background-color: #ffffff; }
                    .tw-z-10 { z-index: 10; }
                    .tw-gap-2 { gap: 0.5rem; }
                    .tw-gap-3 { gap: 0.75rem; }
                    .tw-w-4 { width: 1rem; }
                    .tw-h-4 { height: 1rem; }
                    .tw-w-8 { width: 2rem; }
                    .tw-h-8 { height: 2rem; }
                    .tw-w-9 { width: 2.25rem; }
                    .tw-h-9 { height: 2.25rem; }
                    .tw-text-indigo-500 { color: #6366f1; }
                    .tw-text-lg { font-size: 1.125rem; line-height: 1.75rem; }
                    .tw-font-bold { font-weight: 700; }
                    .tw-text-slate-800 { color: #1e293b; }
                    .tw-text-slate-700 { color: #334155; }
                    .tw-flex-1 { flex: 1 1 0%; }
                    .tw-overflow-y-auto { overflow-y: auto; }
                    .tw-space-y-4 > * + * { margin-top: 1rem; }
                    .tw-max-w-85 { max-width: 85%; }
                    .tw-max-w-95 { max-width: 95%; }
                    .tw-rounded-full { border-radius: 9999px; }
                    .tw-rounded-2xl { border-radius: 1rem; }
                    .tw-rounded-tr-none { border-top-right-radius: 0px; }
                    .tw-rounded-tl-none { border-top-left-radius: 0px; }
                    .tw-bg-gradient { background-image: linear-gradient(to top right, #60a5fa, #6366f1, #a855f7); }
                    .tw-shadow-lg { box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }
                    .tw-shadow-sm { box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05); }
                    .tw-mt-1 { margin-top: 0.25rem; }
                    .tw-p-4 { padding: 1rem; }
                    .tw-p-3 { padding: 0.75rem; }
                    .tw-text-sm { font-size: 0.875rem; line-height: 1.25rem; }
                    .tw-leading-relaxed { line-height: 1.625; }
                    .tw-whitespace-pre-line { white-space: pre-line; }
                    .tw-bg-slate-100-80 { background-color: rgba(241, 245, 249, 0.8); }
                    .tw-border { border-width: 1px; border-style: solid; }
                    
                    /* Form input mimicking Tailwind */
                    .tw-input-container { padding: 1rem; background-color: #fff; border-top: 1px solid #f3f4f6; }
                    .tw-input-wrapper { display: flex; align-items: flex-end; gap: 0.5rem; border-radius: 1rem; border: 1px solid #e5e7eb; background-color: #ffffff; padding: 0.75rem; box-shadow: 0 1px 2px 0 rgba(0,0,0,0.05); }
                    .tw-textarea { width: 100%; resize: none; border: 0; background: transparent; font-size: 0.875rem; color: #334155; outline: none; }
                    .tw-textarea::placeholder { color: #94a3b8; }
                    .tw-send-btn { display: flex; height: 2.25rem; width: 2.25rem; align-items: center; justify-content: center; border-radius: 9999px; background-image: linear-gradient(to top right, #818cf8, #a855f7); color: white; border: none; cursor: pointer; transition: opacity 0.2s; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
                    .tw-send-btn:hover { opacity: 0.9; }
                </style>

                <div class="tw-flex tw-flex-col tw-h-full tw-w-full tw-overflow-hidden" style="flex: 1;">
                    <!-- Header Chat -->
                    <div class="tw-flex-shrink-0 tw-px-6 tw-py-5 tw-border-b tw-border-gray-100 tw-flex tw-items-center tw-justify-between tw-bg-white tw-z-10">
                        <div class="tw-flex tw-items-center tw-gap-2">
                            <i class="far fa-user-plus tw-text-indigo-500 tw-w-4 tw-h-4"></i>
                            <h2 class="tw-text-lg tw-font-bold tw-text-slate-800" style="margin: 0;">Agente de Onboarding</h2>
                        </div>
                    </div>

                    <!-- Messages -->
                    <div class="tw-flex-1 tw-overflow-y-auto tw-px-6 tw-py-5 tw-space-y-4" id="onboarding-chat-messages">
                        <div class="tw-flex tw-justify-start">
                            <div class="tw-flex tw-items-start tw-gap-3 tw-max-w-95">
                                <div class="tw-w-8 tw-h-8 tw-rounded-full tw-bg-gradient tw-shadow-lg tw-flex-shrink-0 tw-mt-1 tw-border tw-border-white" style="border-width: 2px; border-color: white;"></div>
                                <div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-white tw-border tw-border-gray-100 tw-text-slate-700 tw-rounded-tl-none">¡Hola! Soy el agente de Onboarding. Te ayudaré a configurar las tareas y actividades para los nuevos colaboradores. ¿Qué te gustaría incluir en el plan de onboarding?</div>
                            </div>
                        </div>
                    </div>

                    <!-- Input -->
                    <div class="tw-input-container">
                        <div class="tw-input-wrapper">
                            <textarea rows="2" id="onboarding-chat-input-field" class="tw-textarea" placeholder="Escribe tu respuesta..."></textarea>
                            <div class="tw-flex tw-justify-end">
                                <button type="button" class="tw-send-btn" onclick="sendOnboardingMessage()">
                                    <i class="far fa-paper-plane" style="font-size: 0.875rem;"></i>
                                </button>
                            </div>
                        </div>
                        <p style="margin-top: 0.75rem; text-align: center; font-size: 10px; color: #9ca3af;">Agentes AI puede cometer errores, verifica las respuestas.</p>
                    </div>
                </div>"""

content = content.replace(old_chat, new_chat)

# Also update the JS that appends messages to use the Tailwind classes
old_js = """                const userMessage = document.createElement('div');
                userMessage.className = 'message user-message';
                userMessage.innerHTML = `<div class="message-content"><p>${message}</p></div>`;"""
new_js = """                const userMessage = document.createElement('div');
                userMessage.className = 'tw-flex tw-justify-end';
                userMessage.innerHTML = `<div class="tw-flex tw-items-start tw-gap-3 tw-max-w-85"><div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-slate-100-80 tw-text-slate-800 tw-rounded-tr-none">${message}</div></div>`;"""

old_js2 = """                    const aiMessage = document.createElement('div');
                    aiMessage.className = 'message ai-message';
                    aiMessage.innerHTML = `
                        <div class="message-content">
                            <p>¡Entendido! He agregado "${message}" al plan de onboarding.</p>
                        </div>
                    `;"""
new_js2 = """                    const aiMessage = document.createElement('div');
                    aiMessage.className = 'tw-flex tw-justify-start';
                    aiMessage.innerHTML = `<div class="tw-flex tw-items-start tw-gap-3 tw-max-w-95"><div class="tw-w-8 tw-h-8 tw-rounded-full tw-bg-gradient tw-shadow-lg tw-flex-shrink-0 tw-mt-1 tw-border tw-border-white" style="border-width: 2px; border-color: white;"></div><div class="tw-p-4 tw-rounded-2xl tw-text-sm tw-leading-relaxed tw-shadow-sm tw-whitespace-pre-line tw-bg-white tw-border tw-border-gray-100 tw-text-slate-700 tw-rounded-tl-none">¡Entendido! He agregado "${message}" al plan de onboarding.</div></div>`;"""

content = content.replace(old_js, new_js)
content = content.replace(old_js2, new_js2)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done replacing chat design")
