import uvicorn
# Import the app object from the bridge
from bridge.websocket_server import app

if __name__ == "__main__":
    print("🚀 Starting NeoEngine Backend...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
