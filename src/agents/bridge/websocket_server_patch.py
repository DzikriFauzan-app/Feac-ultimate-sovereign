import sys, os

# Tambahkan root NeoEngine ke PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Lanjutkan load server asli
import websocket_server
websocket_server.main()
