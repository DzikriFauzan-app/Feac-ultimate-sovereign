import socketio
from fastapi import FastAPI
import uvicorn

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)

@sio.event
async def connect(sid, environ):
    print("[WS] Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("[WS] Client disconnected:", sid)

@sio.event
async def execute_command(sid, data):
    print("[WS] Received:", data)

if __name__ == "__main__":
    uvicorn.run(socket_app, host="0.0.0.0", port=8080)
