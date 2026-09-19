import re

file_path = "configurar-vacante.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I need to move the footer OUTSIDE of drawer-body
bad_footer = """            <!-- Step 2 Footer (Save Button) -->
            <div id="onboarding-step-2-footer" class="drawer-footer" style="display: none; padding: 16px 24px; border-top: 1px solid var(--ubits-border-light); background: white;">
                <button class="ubits-button ubits-button--primary" style="width: 100%;" onclick="saveOnboardingConfig()">
                    Guardar configuración
                </button>
            </div>

        </div>
    </div>
    </div>"""

good_footer = """
        </div> <!-- End of drawer-body -->
        
        <!-- Step 2 Footer (Save Button) -->
        <div id="onboarding-step-2-footer" class="drawer-footer" style="display: none; padding: 16px 24px; border-top: 1px solid var(--ubits-border-light); background: white;">
            <button class="ubits-button ubits-button--primary" style="width: 100%;" onclick="saveOnboardingConfig()">
                Guardar configuración
            </button>
        </div>

    </div> <!-- End of drawer-content -->
    </div> <!-- End of serena-config-drawer -->"""

content = content.replace(bad_footer, good_footer)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Footer fixed")
