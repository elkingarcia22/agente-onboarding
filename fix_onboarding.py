import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add the drawer HTML right after serenaConfigDrawer
drawer_html = """    <div class="serena-config-drawer" id="onboardingConfigDrawer">
        <div class="drawer-overlay" onclick="closeOnboardingConfigDrawer()"></div>
        <div class="drawer-content" onclick="if(event.target === this) event.stopPropagation();">
            <div class="drawer-header">
                <h3 class="drawer-title" id="onboardingDrawerTitle">Configurar Onboarding IA</h3>
                <button class="ubits-button ubits-button--secondary ubits-button--sm ubits-button--icon-only" onclick="closeOnboardingConfigDrawer(); return false;" title="Cerrar">
                    <i class="far fa-times"></i>
                </button>
            </div>
            <div class="drawer-body" style="display: flex; flex-direction: column; height: 100%;">
                
                <!-- Opciones de activación -->
                <div style="padding: 20px; border-bottom: 1px solid var(--ubits-border-light);">
                    <h4 style="margin-bottom: 12px; font-size: 14px;">¿Cómo quieres que se active este agente?</h4>
                    <div style="display: flex; gap: 16px; flex-direction: column;">
                        <label style="display: flex; align-items: center; gap: 8px;">
                            <input type="radio" name="onboarding_activation" value="auto" checked>
                            <span>Automáticamente (cuando el candidato llegue a esta etapa)</span>
                        </label>
                        <label style="display: flex; align-items: center; gap: 8px;">
                            <input type="radio" name="onboarding_activation" value="manual">
                            <span>Manualmente (tú decides cuándo activarlo)</span>
                        </label>
                    </div>
                </div>

                <!-- Chat de IA simulado -->
                <div class="ai-chat-interface" id="onboarding-chat-interface" style="display: flex; flex: 1; position: relative; bottom: 0; right: 0; width: 100%; height: 100%; z-index: 1;">
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
                </div>

            </div>
            <div class="drawer-footer">
                <div class="drawer-footer-actions">
                    <button class="ubits-button ubits-button--primary" onclick="closeOnboardingConfigDrawer()">Guardar configuración</button>
                </div>
            </div>
        </div>
    </div>"""

# Replace in HTML
content = content.replace('<div class="serena-config-drawer" id="serenaConfigDrawer">', drawer_html + '\n\n    <div class="serena-config-drawer" id="serenaConfigDrawer">')

# Modify addAgentToFlow
# Add the check for onboarding
add_agent_code = """            // Si es entrevista Serena, abrir drawer de configuración automáticamente
            if (agentId === 'interview-ia') {
                setTimeout(() => {
                    if (typeof window.openSerenaConfigDrawer === 'function') {
                        window.openSerenaConfigDrawer(newAgentStage.id);
                    }
                }, 300);
            }
            
            // Si es Onboarding, abrir drawer de onboarding
            if (agentId === 'onboarding') {
                setTimeout(() => {
                    if (typeof window.openOnboardingConfigDrawer === 'function') {
                        window.openOnboardingConfigDrawer(newAgentStage.id);
                    }
                }, 300);
            }"""
content = content.replace("""            // Si es entrevista Serena, abrir drawer de configuración automáticamente
            if (agentId === 'interview-ia') {
                setTimeout(() => {
                    if (typeof window.openSerenaConfigDrawer === 'function') {
                        window.openSerenaConfigDrawer(newAgentStage.id);
                    }
                }, 300);
            }""", add_agent_code)

# Add openOnboardingConfigDrawer and closeOnboardingConfigDrawer functions
# and the chat logic
onboarding_js = """
        window.openOnboardingConfigDrawer = function(stageId) {
            const drawer = document.getElementById('onboardingConfigDrawer');
            if (drawer) {
                drawer.classList.add('active');
            }
        };

        window.closeOnboardingConfigDrawer = function() {
            const drawer = document.getElementById('onboardingConfigDrawer');
            if (drawer) {
                drawer.classList.remove('active');
            }
        };

        window.sendOnboardingMessage = function() {
            const inputField = document.getElementById('onboarding-chat-input-field');
            const chatMessages = document.getElementById('onboarding-chat-messages');
            const message = inputField.value.trim();
            if (message) {
                const userMessage = document.createElement('div');
                userMessage.className = 'message user-message';
                userMessage.innerHTML = `<div class="message-content"><p>${message}</p></div>`;
                chatMessages.appendChild(userMessage);
                inputField.value = '';
                
                setTimeout(() => {
                    const aiMessage = document.createElement('div');
                    aiMessage.className = 'message ai-message';
                    aiMessage.innerHTML = `
                        <div class="message-content">
                            <p>¡Entendido! He agregado "${message}" al plan de onboarding.</p>
                        </div>
                    `;
                    chatMessages.appendChild(aiMessage);
                    chatMessages.scrollTop = chatMessages.scrollHeight;
                }, 1000);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }
        };

        // Escuchar Enter en el input
        setTimeout(() => {
            const inputField = document.getElementById('onboarding-chat-input-field');
            if(inputField) {
                inputField.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') {
                        window.sendOnboardingMessage();
                    }
                });
            }
        }, 1000);
"""

# Insert js somewhere inside <script>
content = content.replace("window.openSerenaConfigDrawer = function(stageId) {", onboarding_js + "\n        window.openSerenaConfigDrawer = function(stageId) {")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
