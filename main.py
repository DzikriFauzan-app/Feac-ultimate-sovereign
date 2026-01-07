import logging
import os
import traceback
from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import platform

logging.basicConfig(level=logging.DEBUG)

class SovereignApp(App):
    def build(self):
        try:
            if platform == 'android':
                from android.storage import primary_external_storage_path
                base_dir = primary_external_storage_path()
            else:
                base_dir = os.path.expanduser("~")
            
            target_path = os.path.join(base_dir, "FauzanEngine/NeoEngine")
            os.makedirs(target_path, exist_ok=True)

            from core.engine import NeoEngine
            self.engine = NeoEngine(root_path=target_path)
            return self.engine.start_ui()
            
        except Exception as e:
            logging.error(traceback.format_exc())
            return Label(text=f"FEAC SYSTEM ERROR:\n{str(e)}", color=(1,0,0,1))

if __name__ == "__main__":
    SovereignApp().run()
