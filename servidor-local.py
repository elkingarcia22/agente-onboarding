#!/usr/bin/env python3
"""
Servidor HTTP simple para desarrollo local
Uso: python3 servidor-local.py
Luego abre: http://localhost:8000
"""

import http.server
import socketserver
import os

PORT = 8000

# Página de entrada del sitio. /index.html se sigue sirviendo tal cual para el
# dashboard de plantillas, al que apunta el rail de navegación.
ENTRY_PAGE = '/index.html'

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ('', '/'):
            self.send_response(302)
            self.send_header('Location', ENTRY_PAGE)
            self.end_headers()
            return
        super().do_GET()

    def end_headers(self):
        # Agregar headers CORS para desarrollo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        # Sin caché: en desarrollo el navegador debe ver siempre el archivo actual
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Log simplificado
        print(f"[{self.address_string()}] {format % args}")

if __name__ == "__main__":
    # Cambiar al directorio del script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor iniciado en http://localhost:{PORT}")
        print(f"📁 Directorio: {os.getcwd()}")
        print(f"🌐 Abre tu navegador en: http://localhost:{PORT}/index.html")
        print(f"⏹️  Presiona Ctrl+C para detener el servidor\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n⏹️  Servidor detenido")


