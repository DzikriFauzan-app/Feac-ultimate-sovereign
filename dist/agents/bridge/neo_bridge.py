#!/usr/bin/env python3
import sys, os, asyncio

# ===== PATH FIX =====
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ===== IMPORT ENGINE =====
from fastapi import FastAPI
import socketio
from core.engine import NeoEngine

# ===== SOCKET.IO SERVER =====
sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = FastAPI()
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

# ===== CREATE ENGINE EARLY =====
engine = NeoEngine()    # <-- ini memuat agents langsung

# ===== FASTAPI STARTUP =====
@app.on_event("startup")
async def startup_event():
    print("[BRIDGE] NeoBridge startup...")
    # Jalankan engine loop
    asyncio.create_task(engine.start())
    print("[BRIDGE] Engine start() scheduled")

# ===== WEBSOCKET EVENTS =====
@sio.event
async def connect(sid, environ):
    print("[WS] Client connected:", sid)

@sio.event
async def execute(sid, data):
    print("[WS] Exec:", data)
    try:
        result = await engine.dispatch_task(data)

        if result is None:
            result = {
                "id": data.get("id"),
                "agent": data.get("agent"),
                "status": "failed",
                "error": "no result"
            }

        print("[DEBUG] RESULT FROM ENGINE:", result)
        await sio.emit("result", result, to=sid)

    except Exception as e:
        err = {
            "id": data.get("id"),
            "agent": data.get("agent"),
            "status": "failed",
            "error": str(e)
        }
        print("[DEBUG] DISPATCH ERROR:", e)
        await sio.emit("result", err, to=sid)

@sio.event
async def disconnect(sid):
    print("[WS] Client disconnected:", sid)

# ===== UVICORN ENTRYPOINT =====
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(sio_app, host="0.0.0.0", port=8080)
