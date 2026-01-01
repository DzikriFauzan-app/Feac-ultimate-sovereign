import socketio
from core.engine import NeoEngine

# Setup
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)
engine = NeoEngine()

@sio.event
async def connect(sid, environ):
    print(f"[BRIDGE] Client connected: {sid}")
    await sio.emit('log', {"agent": "SYSTEM", "message": "Backend Connected", "type": "success"})
    await engine.start()

@sio.event
async def execute_command(sid, data):
    agent = data.get('agent')
    cmd = data.get('command')
    params = data.get('params', {})
    
    print(f"[BRIDGE] Received: {agent} -> {cmd}")
    task_id = await engine.execute_command(agent, cmd, params)
    await sio.emit('log', {"agent": "SCHEDULER", "message": f"Task {task_id} started", "type": "info"})

# Forward internal bus events to UI
async def forward_to_ui(data):
    await sio.emit('log', data)

engine.bus.subscribe("task_completed", forward_to_ui)
engine.bus.subscribe("task_failed", forward_to_ui)

# For Uvicorn to find 'app'
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
