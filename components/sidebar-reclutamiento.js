// El alto del rail lo resuelve el CSS (top/bottom con el mismo inset),
// así que no hace falta calcularlo ni recalcularlo al redimensionar.

// Sidebar Reclutamiento Component Loader
function loadSidebarReclutamiento(activeButton = null) {
    console.log('loadSidebarReclutamiento llamado con activeButton:', activeButton);
    
    // Buscar el contenedor del sidebar
    const sidebarContainer = document.getElementById('sidebar-container');
    console.log('Sidebar container encontrado:', sidebarContainer);
    
    if (!sidebarContainer) {
        console.error('No se encontró el contenedor sidebar-container');
        return;
    }
    
    // Markup del rail, copiado de la vista de candidatos
    // (Card candidato: src/components/sidebar/Sidebar.tsx + RailIcons.tsx)
    const sidebarHTML = `
        <nav class="rail" id="sidebar" aria-label="Navegación principal">
            <svg class="rail__logo" width="38" height="38" viewBox="0 0 32 32" fill="none" aria-label="UBITS">
                <path d="M 16 15 V 22 A 5 5 0 0 0 26 22 V 7" stroke="currentColor" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round" />
                <path d="M 11 15 A 5 5 0 0 1 16 10" stroke="currentColor" stroke-width="3.6" stroke-linecap="round" />
                <path d="M 6 15 A 10 10 0 0 1 16 5" stroke="currentColor" stroke-width="3.6" stroke-linecap="round" />
            </svg>

            <ul class="rail__nav">
                <li>
                    <button type="button" class="rail__item" data-section="aprendizaje" aria-label="Aprendizaje" title="Aprendizaje">
                        <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true">
                            <rect x="2.6" y="5.2" width="18.8" height="13.6" rx="2.6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.9" />
                            <rect x="6" y="8.6" width="2.2" height="2.2" rx="0.6" fill="currentColor" />
                            <rect x="6" y="13.2" width="2.2" height="2.2" rx="0.6" fill="currentColor" />
                            <path d="M10.4 9.7h7.2M10.4 14.3h7.2" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.7" />
                        </svg>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="organigrama" aria-label="Organigrama" title="Organigrama">
                        <i class="fas fa-sitemap"></i>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="personas" aria-label="Personas" title="Personas">
                        <i class="fas fa-users"></i>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="vacantes" aria-label="Vacantes" title="Vacantes" onclick="window.location.href='index.html'">
                        <i class="fas fa-briefcase"></i>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="plantillas" aria-label="Plantillas" title="Plantillas" onclick="window.location.href='home-plantillas.html'">
                        <i class="fas fa-file-alt"></i>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="serena" aria-label="Serena IA" title="Serena IA">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                            <circle cx="11" cy="11.3" r="7.7" />
                            <path d="M6.5 17.3a9 9 0 0 0 3.4 1.8l-4.7 2.7c-.7.4-1.5-.3-1.2-1.1z" />
                            <path d="M19.6 2.1c.16 0 .3.11.34.27l.44 1.52c.05.19.2.34.39.39l1.52.44a.35.35 0 0 1 0 .68l-1.52.44a.58.58 0 0 0-.39.39l-.44 1.52a.35.35 0 0 1-.68 0l-.44-1.52a.58.58 0 0 0-.39-.39l-1.52-.44a.35.35 0 0 1 0-.68l1.52-.44a.58.58 0 0 0 .39-.39l.44-1.52a.35.35 0 0 1 .34-.27Z" />
                        </svg>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="analitica" aria-label="Analítica" title="Analítica">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                            <rect x="3.7" y="7.8" width="4" height="8.4" rx="2" />
                            <rect x="10" y="3.6" width="4" height="16.8" rx="2" />
                            <rect x="16.3" y="6.2" width="4" height="11.6" rx="2" />
                        </svg>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="datos" aria-label="Datos" title="Datos">
                        <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
                            <ellipse cx="12" cy="6.1" rx="7.2" ry="2.35" />
                            <ellipse cx="12" cy="12" rx="7.2" ry="2.35" />
                            <ellipse cx="12" cy="17.9" rx="7.2" ry="2.35" />
                        </svg>
                    </button>
                </li>
                <li>
                    <button type="button" class="rail__item" data-section="enps" aria-label="eNPS" title="eNPS">
                        <svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true">
                            <path d="M4.4 5.2c0-1.2 1-2.2 2.2-2.2h7.2c.6 0 1.1.2 1.5.6l2.8 2.8c.4.4.6.9.6 1.5v3.5a5.9 5.9 0 0 0-7.4 7.4H6.6a2.2 2.2 0 0 1-2.2-2.2V5.2Z" fill="currentColor" />
                            <path fill-rule="evenodd" clip-rule="evenodd" d="M17.6 13.2a4.4 4.4 0 1 0 0 8.8 4.4 4.4 0 0 0 0-8.8Zm-2.2 4.4a2.2 2.2 0 0 1 3.3-1.9l-2.5 2.5a2.2 2.2 0 0 1-.8-.6Zm2.2 2.2c-.3 0-.5 0-.8-.1l2.5-2.5c.4.7.3 1.5-.2 2a2.2 2.2 0 0 1-1.5.6Z" fill="currentColor" />
                        </svg>
                    </button>
                </li>
            </ul>

            <span class="rail__spacer"></span>

            <button type="button" class="rail__logout" aria-label="Cerrar sesión" title="Cerrar sesión" onclick="handleLogout()">
                <i class="fas fa-right-from-bracket"></i>
            </button>

            <div class="rail__version">
                <span class="rail__version-name">UBITS</span>
                <span>1.4.0</span>
            </div>
        </nav>
    `;

    // Insertar el HTML
    sidebarContainer.innerHTML = sidebarHTML;
    console.log('HTML insertado en sidebar container');

    updateActiveSidebarReclutamientoButton(activeButton);

    console.log('Sidebar Reclutamiento cargado completamente');
}

// Función para actualizar el botón activo
function updateActiveSidebarReclutamientoButton(activeButton) {
    document.querySelectorAll('.rail__item').forEach(button => {
        button.classList.remove('active');
    });

    if (!activeButton) return;

    const button = document.querySelector(`.rail__item[data-section="${activeButton}"]`);
    if (button) {
        button.classList.add('active');
    }
}

// Función para manejar logout
function handleLogout() {
    console.log('Logout solicitado');
    // Implementar lógica de logout
}

// Exportar funciones al window global
window.loadSidebarReclutamiento = loadSidebarReclutamiento;
window.updateActiveSidebarReclutamientoButton = updateActiveSidebarReclutamientoButton;
window.handleLogout = handleLogout;
