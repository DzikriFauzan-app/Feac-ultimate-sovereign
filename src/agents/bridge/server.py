import os
import sys
import uvicorn

# Set PYTHONPATH dynamically
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, ".."))

sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "core"))
sys.path.insert(0, os.path.join(ROOT, "agents"))
sys.path.insert(0, os.path.join(ROOT, "bridge"))

print("[LAUNCHER] PYTHONPATH:", sys.path)

# Import websocket server (FastAPI + Socket.IO)
import websocket_server  # This defines `app`

if __name__ == "__main__":
    uvicorn.run(
        websocket_server.app,
        host="0.0.0.0",
        port=8080,
        reload=False
    )
