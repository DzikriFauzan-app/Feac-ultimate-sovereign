sed -i 's/result = await engine.dispatch_task(data)/print("[DEBUG] RESULT FROM ENGINE:", result := await engine.dispatch_task(data))/g' neo_bridge.py
sed -i 's/await sio.emit("result", result,/await sio.emit("result", result if result is not None else {"error": "no result"},/g' neo_bridge.py
