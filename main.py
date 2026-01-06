import logging
import os
import traceback
from kivy.app import App
from kivy.uix.label import Label

# Setup logging agar bisa di-debug lewat logcat/file
logging.basicConfig(level=logging.DEBUG)

class SovereignApp(App):
    def build(self):
        try:
            print("🛡️ FEAC Sovereign: Menghidupkan sistem...")
            
            # Menerapkan Dynamic Path (Solusi Hardcoded Path)
            # Menggunakan direktori internal aplikasi agar tidak butuh izin manual di awal
            from android.storage import primary_external_storage_path # type: ignore
            base_dir = primary_external_storage_path()
        except:
            base_dir = os.path.expanduser("~")

        try:
            # Implementasi Try-Except sesuai saran Blackbox & Video
            from core.engine import NeoEngine
            
            engine_path = os.path.join(base_dir, "FauzanEngine/NeoEngine")
            if not os.path.exists(engine_path):
                os.makedirs(engine_path, exist_ok=True)
                
            self.engine = NeoEngine(root_path=engine_path)
            return self.engine.start_ui()
            
        except Exception as e:
            error_msg = f"CRITICAL FAILURE:\n{str(e)}\n\n{traceback.format_exc()}"
            logging.error(error_msg)
            return Label(text=f"FEAC SOVEREIGN ERROR:\n\n{error_msg}", 
                         font_size='12sp', color=(1, 0, 0, 1))

if __name__ == "__main__":
    SovereignApp().run()
