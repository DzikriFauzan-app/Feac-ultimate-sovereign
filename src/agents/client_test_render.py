#!/usr/bin/env python3
import socketio, time, json

sio = socketio.Client(logger=True, engineio_logger=True)

@sio.event
def connect():
    print("CLIENT CONNECTED")

@sio.on("result")
def on_result(data):
    print("RESULT:", json.dumps(data, indent=2))

@sio.event
def disconnect():
    print("CLIENT DISCONNECTED")

def main():
    sio.connect("http://127.0.0.1:8080", transports=["websocket"])
    # 1) build pipeline
    sio.emit("execute", {
        "agent": "RenderAgent",
        "command": "build_pipeline",
        "params": {"name": "deferred_pbr", "config": {"passes": ["gbuffer", "lighting", "post"]}}
    })
    # 2) compile shader (will attempt GPU compile if available)
    sio.emit("execute", {
        "agent": "RenderAgent",
        "command": "compile_shader",
        "params": {"name": "pbr_frag", "source": "// simple fragment shader placeholder\nvoid main(){}", "stage": "fragment"}
    })
    # 3) request a render_frame (may fallback to snapshot)
    time.sleep(1)
    sio.emit("execute", {
        "agent": "RenderAgent",
        "command": "render_frame",
        "params": {"pipeline": "deferred_pbr", "camera": {"position": [0,0,0]}, "width": 640, "height": 360}
    })
    # wait results
    time.sleep(2)
    sio.disconnect()

if __name__ == "__main__":
    main()
