import logging
import traceback
import os

# Setup logging ke file agar bisa di-debug di Android
logging.basicConfig(filename='sovereign_debug.log', level=logging.DEBUG)

try:
    print("🚀 Menginisialisasi FEAC Sovereign Engine...")
    from core.engine import NeoEngine
    engine = NeoEngine()
    engine.start()
except Exception as e:
    error_msg = f"FATAL ERROR SAAT STARTUP: {str(e)}\n{traceback.format_exc()}"
    print(error_msg)
    logging.error(error_msg)
    # Tetap jalankan loop kosong agar app tidak langsung tertutup
    import time
    while True:
        time.sleep(1)
