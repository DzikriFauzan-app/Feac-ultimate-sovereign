#!/usr/bin/env python3
import sys
import json
import time
import socketio

URL = "http://127.0.0.1:8080"  # sesuaikan

def send(agent, command, params=None):
    sio = socketio.Client()
    try:
        sio.connect(URL)
    except Exception as e:
        print("[ERROR] connect:", e)
        return
    payload = {"agent": agent, "command": command, "params": params or {}}
    # emit like the UI
    sio.emit("execute_command", payload)
    print("[SENT]", payload)
    time.sleep(1)
    sio.disconnect()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: send_command.py <AgentName> <Command> [json_params]")
        print('Example: send_command.py AssetGeneratorAgent batch_generate_sprites \'{"count":100,"size":[32,32],"name_prefix":"tree"}\'')
        sys.exit(1)
    agent = sys.argv[1]
    cmd = sys.argv[2]
    params = {}
    if len(sys.argv) >= 4:
        params = json.loads(sys.argv[3])
    send(agent, cmd, params)
