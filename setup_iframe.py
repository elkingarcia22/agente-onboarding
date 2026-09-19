import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I need to create the iframe element. It will be hidden by default.
iframe_html = """
    <!-- iframe for Onboarding Chat (Exact same React code) -->
    <iframe id="onboardingChatIframe" src="panel-candidatos/chat-only.html" style="position: fixed; inset: 0; width: 100vw; height: 100vh; border: none; z-index: 10000; display: none; background: transparent;"></iframe>
"""

if 'id="onboardingChatIframe"' not in content:
    content = content.replace("</body>", iframe_html + "\n</body>")

# Modify openOnboardingConfigDrawer to show the iframe instead of step 1!
# We also need an event listener for postMessage.
js_listener = """
        // Escuchar mensajes del iframe (React)
        window.addEventListener('message', function(event) {
            if (event.data && event.data.type === 'closePV') {
                document.getElementById('onboardingChatIframe').style.display = 'none';
            } else if (event.data && event.data.type === 'chatDone') {
                document.getElementById('onboardingChatIframe').style.display = 'none';
                
                // Abrir el Step 2 nativo de configurar-vacante
                const drawer = document.getElementById('onboardingConfigDrawer');
                const overlay = document.getElementById('drawerOverlay');
                if (drawer) drawer.classList.add('active');
                if (overlay) overlay.classList.add('active');
                
                document.getElementById('onboarding-step-1').style.display = 'none';
                document.getElementById('onboarding-drawer-title').innerHTML = '<i class="far fa-gear" style="color: var(--ubits-brand-primary);"></i> Configuración de Agente';
                document.getElementById('onboarding-step-2').style.display = 'flex';
                document.getElementById('onboarding-step-2-footer').style.display = 'flex';
                
                // Mostrar plan mock
                const planContainer = document.getElementById('onboarding-generated-plan');
                if(planContainer) {
                    planContainer.innerHTML = `
                        <div style="display: flex; align-items: flex-start; gap: 12px;">
                            <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #10b981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
                                <i class="far fa-check" style="color: #10b981; font-size: 12px;"></i>
                            </div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 14px; font-weight: 600; color: #111827;">Alta en la plataforma</span>
                                <span style="font-size: 13px; color: #6b7280; margin-top: 2px;">Datos confirmados</span>
                            </div>
                        </div>
                        <div style="display: flex; align-items: flex-start; gap: 12px;">
                            <div style="width: 24px; height: 24px; border-radius: 50%; border: 1px solid #10b981; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-top: 2px;">
                                <i class="far fa-check" style="color: #10b981; font-size: 12px;"></i>
                            </div>
                            <div style="display: flex; flex-direction: column;">
                                <span style="font-size: 14px; font-weight: 600; color: #111827;">Inmersión en cultura y OKRs</span>
                                <span style="font-size: 13px; color: #6b7280; margin-top: 2px;">Contenido asignado en el plan de tareas</span>
                            </div>
                        </div>
                    `;
                }
            }
        });
        
        window.openOnboardingConfigDrawer = function(stageId) {
            const iframe = document.getElementById('onboardingChatIframe');
            if (iframe) {
                // Reload iframe to reset React state
                iframe.src = 'panel-candidatos/chat-only.html';
                iframe.style.display = 'block';
            }
        }
"""

# Find openOnboardingConfigDrawer definition and replace it
# Because I might have multiple definitions due to previous scripts, I'll use regex carefully.
# The previous scripts replaced it completely, let's just replace the whole window.openOnboardingConfigDrawer definition until the next window.closeOnboardingConfigDrawer
pattern = re.compile(r"window\.openOnboardingConfigDrawer = function\(stageId\).*?window\.closeOnboardingConfigDrawer = function\(\) \{", re.DOTALL)

# But wait, there are also obChat logic that is now useless! We can leave it or remove it.
# Let's just find the exact block and replace it.
content = pattern.sub(js_listener + "\n\n        window.closeOnboardingConfigDrawer = function() {", content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Setup iframe logic in HTML")
