#!/usr/bin/env python3
import socketio
import time
import json

sio = socketio.Client()

@sio.event
def connect():
    print("[WS-Client] Connected to NeoEngine")

@sio.event
def disconnect():
    print("[WS-Client] Disconnected")

@sio.on('log')
def on_log(data):
    print("[LOG]", json.dumps(data, indent=2, default=str))

def run(url="http://127.0.0.1:8080/ws"):
    try:
        sio.connect(url)
    except Exception as e:
        print("[ERROR] Failed to connect:", e)
        return

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sio.disconnect()

if __name__ == "__main__":
    run()
