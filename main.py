import logging
try:
    from core.engine import NeoEngine
    engine = NeoEngine()
    engine.start()
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    # Tambahkan logging ke file agar bisa dicek di Android
    with open("error_log.txt", "a") as f:
        f.write(str(e))
