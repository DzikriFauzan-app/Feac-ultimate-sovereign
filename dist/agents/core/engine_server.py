#!/usr/bin/env python3
import os
from flask import Flask, jsonify
from flask_socketio import SocketIO
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/ping")
def ping():
    return jsonify({"engine":"Fauzan Engine","time":datetime.utcnow().isoformat()})

@socketio.on("connect")
def on_connect():
    print("[ENGINE] Client connected")

@socketio.on("disconnect")
def on_disconnect():
    print("[ENGINE] Client disconnected")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5050)
