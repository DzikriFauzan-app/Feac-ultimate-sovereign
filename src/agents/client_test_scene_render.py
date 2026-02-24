import socketio
import time

SERVER_URL = "http://10.4.35.107:8080"  # HARD-CODED (ANDROID SAFE)

sio = socketio.Client()

@sio.event
def connect():
    print("[CLIENT] Connected")

@sio.event
def result(data):
    print("[CLIENT] RENDER RESULT RECEIVED:")
    print(data)

@sio.event
def error(data):
    print("[CLIENT] ERROR:", data)

sio.connect(SERVER_URL)

sio.emit("load_scene", {})
time.sleep(0.2)

sio.emit("set_pipeline", {})
time.sleep(0.2)

sio.emit("render_scene", {})
time.sleep(2)

sio.disconnect()
print("[CLIENT] Disconnected")
