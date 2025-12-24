import requests
import time
import os

url = "http://127.0.0.1:8080/api/task"
payload = {
    "tasks": [
        {"agent": "GenesisAgent", "instruction": "Initialize World Map Layer", "command": "process_task"},
        {"agent": "MapGeneratorAgent", "instruction": "Bake 3 Lane Pathing", "command": "process_task"},
        {"agent": "AssetAgent", "instruction": "Load Minion Mesh", "command": "process_task"},
        {"agent": "CodeAgent", "instruction": "Generate Skill System", "command": "process_task"},
        {"agent": "AISupervisor", "instruction": "Sync All Nodes", "command": "process_task"},
        {"agent": "RenderAgent", "instruction": "Setup Shader Pipeline", "command": "process_task"},
        {"agent": "UIAgent", "instruction": "Build HUD Canvas", "command": "process_task"},
        {"agent": "AudioAgent", "instruction": "Process Soundscape", "command": "process_task"},
        {"agent": "SecurityAgent", "instruction": "Validate Auth Keys", "command": "process_task"},
        {"agent": "OptiAgent", "instruction": "Memory Cleanup", "command": "process_task"}
    ]
}

start_time = time.time()
print("⚡ SIMULASI BUILD DIMULAI...")

try:
    r = requests.post(url, json=payload, timeout=10)
    end_time = time.time()
    
    duration = (end_time - start_time) * 1000
    print(f"\n🚀 BUILD COMPLETE!")
    print(f"⏱️  Kecepatan Build: {duration:.2f} ms")
    print(f"📊 Status Server: {r.status_code}")
except Exception as e:
    print(f"❌ Error: {e}")
