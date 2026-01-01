#!/usr/bin/env python3
"""
Bridge server (FastAPI + Socket.IO ASGI)
Mounts Socket.IO at /ws and serves static UI.
On startup, creates NeoEngine instance and runs start_async() as background task.
"""
import asyncio
import traceback
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import socketio
import uvicorn

# Import core engine (must be relative package import friendly)
from core.engine import NeoEngine

# Create FastAPI app
app = FastAPI(title="NeoEngine Bridge")

# Create python-socketio AsyncServer (ASGI mode)
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*', logger=False, engineio_logger=False)
sio_app = socketio.ASGIApp(sio, other_asgi_app=app)

# Mount static UI (assumes 'ui' dir exists alongside project root)
app.mount("/static", StaticFiles(directory="ui"), name="static")

# Globals (engine instance assigned on startup)
engine = None

@app.get("/ping")
async def ping():
    return JSONResponse({"status": "ok"})

@app.get("/")
async def index():
    return FileResponse("ui/index.html")

# ========== Socket.IO events ==========
@sio.event
async def connect(sid, environ):
    print(f"[BRIDGE] Client connected: {sid}")
    await sio.emit("system_status", {"status":"ONLINE"}, to=sid)

@sio.event
async def disconnect(sid):
    print(f"[BRIDGE] Client disconnected: {sid}")

@sio.event
async def execute_command(sid, data):
    """
    Expected data:
    {
      "agent": "ShellAgent",
      "command": "run_command",
      "params": {...}
    }
    """
    try:
        if engine is None:
            await sio.emit("command_ack", {"error": "engine_not_ready"}, to=sid)
            return

        agent = data.get("agent")
        command = data.get("command")
        params = data.get("params", {})

        # schedule task via engine.scheduler
        task_id = await engine.scheduler.schedule_task(agent, command, params)
        await sio.emit("command_ack", {"task_id": task_id}, to=sid)
    except Exception as e:
        await sio.emit("command_ack", {"error": str(e)}, to=sid)
        traceback.print_exc()

# ========== MessageBus forwarder ==========
def _make_forwarder(sid=None):
    """
    Returns an async function that forwards bus events to Socket.IO clients.
    If sid is None -> broadcast to all.
    """
    async def forwarder(data):
        try:
            # try to emit 'log' event (UI expects 'log')
            await sio.emit('log', data, to=sid) if sid else await sio.emit('log', data)
        except Exception:
            pass
    return forwarder

# Register per-connection subscriptions if needed (optional)
# But to keep it simple, we will broadcast bus task events to all connected clients.

# ========== FastAPI Lifespan: start engine on startup ==========
@app.on_event("startup")
async def startup_event():
    global engine
    print("[BRIDGE] Startup: initializing NeoEngine...")
    engine = NeoEngine()
    # register forwarders for core bus events to broadcast to clients
    engine.bus.subscribe("task_started", _make_forwarder())
    engine.bus.subscribe("task_completed", _make_forwarder())
    engine.bus.subscribe("task_failed", _make_forwarder())
    engine.bus.subscribe("system.heartbeat", _make_forwarder())

    # schedule engine.start_async as background task
    asyncio.create_task(engine.start_async())
    print("[BRIDGE] NeoEngine start_async scheduled.")

@app.on_event("shutdown")
async def shutdown_event():
    global engine
    print("[BRIDGE] Shutdown: stopping engine...")
    if engine:
        await engine.stop_async()
    print("[BRIDGE] Engine stopped.")

# ========== Run helper ==========
def run(host="0.0.0.0", port=8080):
    """
    Run uvicorn with the mounted ASGI app (socketio + fastapi).
    Usage: python -m bridge.bridge_server  OR  uvicorn bridge.bridge_server:app --port 8080
    But because socketio.ASGIApp wraps both, run uvicorn on 'bridge.bridge_server:sio_app' or the module.
    """
    # We instruct uvicorn to run the socketio ASGI app (sio_app)
    uvicorn.run(sio_app, host=host, port=port)

# If executed directly, run
if __name__ == "__main__":
    run()
