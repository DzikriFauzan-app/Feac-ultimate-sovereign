import logging
import traceback
import os

# Konfigurasi Logging agar kita bisa debug lewat logcat
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("FEAC_SOVEREIGN")

try:
    from kivy.app import App
    from kivy.utils import platform
    from core.engine import NeoEngine

    # Fix Hardcoded Path sesuai Laporan Kedua
    if platform == 'android':
        from android.storage import app_storage_path
        project_root = app_storage_path()
    else:
        project_root = os.path.abspath(".")

    class FeacSovereignApp(App):
        def build(self):
            try:
                logger.info(f"Starting NeoEngine at {project_root}")
                self.engine = NeoEngine(root=project_root)
                self.engine.start()
                # Di sini kamu bisa return root widget dashboard kamu
                return None 
            except Exception as e:
                logger.error(f"Engine Failure: {e}")
                traceback.print_exc()

    if __name__ == "__main__":
        FeacSovereignApp().run()

except Exception as fatal_e:
    logger.error(f"FATAL BOOT ERROR: {fatal_e}")
    traceback.print_exc()
