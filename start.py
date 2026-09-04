"""
BLUEGUN — 2026 Football Transfer Intelligence
Unified Application Launcher
"""

import os
import sys
import webbrowser
import subprocess
import time

def run_server():
    print("=" * 65)
    print("⚡ BLUEGUN — 2026 Football Transfer Intelligence Platform")
    print("=" * 65)
    print("Starting unified server (FastAPI Backend + Interactive Frontend)...")
    
    workspace = os.path.dirname(os.path.abspath(__file__))
    os.chdir(workspace)
    
    url = "http://localhost:8000/"
    
    # Open browser after 1.5 seconds
    def open_browser():
        time.sleep(1.5)
        print(f"Opening browser at: {url}")
        webbrowser.open(url)
    
    import threading
    t = threading.Thread(target=open_browser, daemon=True)
    t.start()
    
    try:
        import uvicorn
        # Add backend to sys.path
        sys.path.insert(0, os.path.join(workspace, "backend"))
        uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)
    except ImportError:
        print("Uvicorn not found, launching standard Python HTTP server on port 3000...")
        url = "http://localhost:3000/"
        import http.server
        import socketserver
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", 3000), Handler) as httpd:
            print("Serving BLUEGUN at http://localhost:3000/")
            httpd.serve_forever()

if __name__ == "__main__":
    run_server()
