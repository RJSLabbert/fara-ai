import threading
import webbrowser
import os
import time
import sys
import subprocess
from http.server import HTTPServer, SimpleHTTPRequestHandler

# ---------------------
# Paths
# ---------------------
root_dir = os.path.dirname(os.path.abspath(__file__))
frontend_path = os.path.join(root_dir, "frontend")
backend_path = os.path.join(root_dir, "backend")

BACKEND_HOST = "127.0.0.1"
BACKEND_PORT = 8000
FRONTEND_PORT = 5500

MODEL_NAME = "phi3:mini"

# ---------------------
# Helper: generate text via Ollama CLI
# ---------------------
def generate_with_ollama(prompt):
    """Calls the Ollama CLI to generate text from the model."""
    try:
        result = subprocess.run(
            ["ollama", "generate", MODEL_NAME, prompt],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return f"[ERROR] Ollama CLI failed: {result.stderr.strip()}"
        return result.stdout.strip()
    except FileNotFoundError:
        return "[ERROR] Ollama CLI not found. Make sure Ollama is installed and in PATH."

# ---------------------
# Backend
# ---------------------
def start_backend():
    """Runs FastAPI backend using uvicorn programmatically."""
    try:
        import uvicorn
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uvicorn", "fastapi", "requests"])
        import uvicorn

    # Make sure backend.main exists
    main_file = os.path.join(backend_path, "main.py")
    if not os.path.exists(main_file):
        print(f"[ERROR] Backend file not found: {main_file}")
        input("Press Enter to exit...")
        sys.exit(1)

    uvicorn.run("backend.main:app", host=BACKEND_HOST, port=BACKEND_PORT, log_level="info")

# ---------------------
# Frontend
# ---------------------
def start_frontend():
    """Serves the frontend folder on FRONTEND_PORT."""
    os.chdir(frontend_path)
    server_address = ('', FRONTEND_PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Frontend started on http://localhost:{FRONTEND_PORT}")
    httpd.serve_forever()

# ---------------------
# Start backend and frontend threads
# ---------------------
backend_thread = threading.Thread(target=start_backend, daemon=True)
backend_thread.start()
time.sleep(1)  # wait for backend to start

frontend_thread = threading.Thread(target=start_frontend, daemon=True)
frontend_thread.start()

# ---------------------
# Open browser automatically
# ---------------------
webbrowser.open(f"http://localhost:{FRONTEND_PORT}")

# ---------------------
# Keep main thread alive
# ---------------------
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nShutting down...")
    sys.exit(0)
