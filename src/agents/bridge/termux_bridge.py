#!/usr/bin/env python3
import socketio
import os
import json
import time
from datetime import datetime

SERVER = os.environ.get("NEOENGINE_SERVER", "http://127.0.0.1:8080")
sio = socketio.Client()

@sio.event
def connect():
    print("[TermuxBridge] connected")
    sio.emit("register_termux", {"pid": os.getpid(), "time": datetime.utcnow().isoformat()})

@sio.event
def disconnect():
    print("[TermuxBridge] disconnected")

@sio.on("command")
def on_command(data):
    # This client only logs; heavy execution should be dispatched to ShellAgent via scheduler
    print("[TermuxBridge] command received:", data)

def run():
    sio.connect(SERVER)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sio.disconnect()

if __name__ == "__main__":
    run()
