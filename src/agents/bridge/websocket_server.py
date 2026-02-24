#!/usr/bin/env python3
import os, sys, asyncio, json, uuid
import socketio
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from core.engine import NeoEngine

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)

engine = NeoEngine()

def ensure_id(task: dict):
    """Inject task id if missing."""
    if "id" not in task:
        task["id"] = str(uuid.uuid4())
    return task

@app.get("/ping")
async def ping():
    return {"status":"ok"}

@app.post("/api/task")
async def api_task(request: Request):
    payload = await request.json()
    payload = ensure_id(payload)
    print("[BRIDGE][HTTP] Received task:", payload)
    asyncio.create_task(engine.dispatch_task(payload))
    return {"status":"ok","accepted":True,"id":payload["id"]}

@sio.event
async def connect(sid, environ):
    print(f"[BRIDGE] Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"[BRIDGE] Client disconnected: {sid}")

@sio.event
async def task(sid, data):
    data = ensure_id(data)
    print(f"[BRIDGE][WS] Received 'task' from {sid}: {data}")
    await engine.dispatch_task(data)
    await sio.emit("task_ack", {"status":"accepted","id":data["id"]}, to=sid)

@sio.event
async def execute_command(sid, data):
    data = ensure_id(data)
    print(f"[BRIDGE][WS] Received 'execute_command' from {sid}: {data}")
    await engine.dispatch_task(data)
    await sio.emit("command_ack", {"status":"accepted","id":data["id"]}, to=sid)

@app.on_event("startup")
async def startup_event():
    print("[BRIDGE] Startup: initializing NeoEngine...")
    asyncio.create_task(engine.start())

def run():
    import uvicorn
    uvicorn.run(socket_app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    run()
