const fs = require('fs');

const path = 'components/sidebar-reclutamiento.js';
let content = fs.readFileSync(path, 'utf8');

const target = `<span class="rail__spacer"></span>

            <button type="button" class="rail__logout" aria-label="Cerrar sesión" title="Cerrar sesión" onclick="handleLogout()">
                <i class="fas fa-right-from-bracket"></i>
            </button>

            <div class="rail__version">
                <span class="rail__version-name">UBITS</span>
                <span>1.4.0</span>
            </div>`;

const replacement = `<span class="rail__spacer"></span>

            <div class="rail__profile" id="rail-profile-container" style="position: relative; width: 100%; display: flex; flex-direction: column; align-items: center; padding-bottom: 16px;">
                <button type="button" class="rail__profile-btn" onclick="toggleRailProfileMenu(event)" style="background: none; border: none; cursor: pointer; padding: 0; display: flex; flex-direction: column; align-items: center; gap: 4px; width: 100%;">
                    <div style="width: 32px; height: 32px; border-radius: 50%; background: var(--ubits-brand-primary, #0D6EFD); color: white; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: bold; margin-bottom: 2px;">
                        <img src="images/Profile-image.jpg" onerror="this.style.display='none'" alt="Usuario" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;" />
                    </div>
                    <span style="color: var(--ubits-fg-1, #111827); font-size: 10px; font-weight: 600; width: 64px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: center;">Juan Pérez</span>
                    <span style="color: var(--ubits-fg-2, #6B7280); font-size: 9px; width: 64px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: center;">juan@ubits.com</span>
                    <span style="color: var(--ubits-fg-2, #6B7280); font-size: 9px; width: 64px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: center; margin-top: 2px; line-height: 1.1;">Sucursal Norte</span>
                    <span style="color: var(--ubits-fg-2, #6B7280); font-size: 9px; width: 64px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; text-align: center; line-height: 1.1;">Admin</span>
                </button>
                
                <div id="rail-profile-menu" style="display: none; position: absolute; left: calc(100% + 12px); bottom: 0; background: var(--ubits-bg-1, #FFFFFF); border: 1px solid var(--ubits-border-color, #E5E7EB); border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); width: 220px; z-index: 100; overflow: hidden; text-align: left;">
                    <div style="padding: 8px 0;">
                        <button onclick="alert('Próximamente: Cambiar sucursal')" style="display: flex; align-items: center; width: 100%; padding: 10px 16px; background: none; border: none; cursor: pointer; color: var(--ubits-fg-1, #111827); font-size: 14px; text-align: left; transition: background 0.2s;" onmouseover="this.style.background='var(--ubits-bg-2, #F3F4F6)'" onmouseout="this.style.background='none'">
                            <i class="far fa-building" style="margin-right: 12px; width: 16px; text-align: center;"></i> Cambiar sucursal
                        </button>
                        <button onclick="alert('Próximamente: Cambiar rol')" style="display: flex; align-items: center; width: 100%; padding: 10px 16px; background: none; border: none; cursor: pointer; color: var(--ubits-fg-1, #111827); font-size: 14px; text-align: left; transition: background 0.2s;" onmouseover="this.style.background='var(--ubits-bg-2, #F3F4F6)'" onmouseout="this.style.background='none'">
                            <i class="far fa-user-tag" style="margin-right: 12px; width: 16px; text-align: center;"></i> Cambiar rol
                        </button>
                        <button id="rail-theme-toggle" style="display: flex; align-items: center; width: 100%; padding: 10px 16px; background: none; border: none; cursor: pointer; color: var(--ubits-fg-1, #111827); font-size: 14px; text-align: left; transition: background 0.2s;" onmouseover="this.style.background='var(--ubits-bg-2, #F3F4F6)'" onmouseout="this.style.background='none'">
                            <i class="far fa-moon" style="margin-right: 12px; width: 16px; text-align: center;"></i> Personalización
                        </button>
                        <div style="height: 1px; background: var(--ubits-border-color, #E5E7EB); margin: 4px 0;"></div>
                        <button onclick="handleLogout()" style="display: flex; align-items: center; width: 100%; padding: 10px 16px; background: none; border: none; cursor: pointer; color: var(--ubits-brand-red, #dc2626); font-size: 14px; text-align: left; transition: background 0.2s;" onmouseover="this.style.background='var(--ubits-bg-2, #F3F4F6)'" onmouseout="this.style.background='none'">
                            <i class="far fa-sign-out" style="margin-right: 12px; width: 16px; text-align: center;"></i> Cerrar sesión
                        </button>
                    </div>
                </div>
            </div>`;

if (content.includes('rail__logout')) {
    content = content.replace(target, replacement);
    
    // Add logic for toggle menu and theme toggle
    const jsAddition = `
// Función para el menú de perfil en el rail
window.toggleRailProfileMenu = function(event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    const menu = document.getElementById('rail-profile-menu');
    if (menu) {
        menu.style.display = menu.style.display === 'none' || menu.style.display === '' ? 'block' : 'none';
    }
};

// Cerrar dropdown al hacer click fuera
document.addEventListener('click', function(event) {
    const profileBtn = document.getElementById('rail-profile-btn');
    const menu = document.getElementById('rail-profile-menu');
    
    if (menu && menu.style.display === 'block') {
        if (!menu.contains(event.target) && (!profileBtn || !profileBtn.contains(event.target))) {
            menu.style.display = 'none';
        }
    }
});

// Inicializar dark mode en el rail
setTimeout(() => {
    const themeToggle = document.getElementById('rail-theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            if (typeof toggleDarkMode === 'function') {
                toggleDarkMode();
            } else if (typeof window.toggleDarkMode === 'function') {
                window.toggleDarkMode();
            }
        });
    }
}, 500);
`;
    content += jsAddition;
    fs.writeFileSync(path, content);
    console.log('Sidebar patched successfully.');
} else {
    console.log('Target not found.');
}
