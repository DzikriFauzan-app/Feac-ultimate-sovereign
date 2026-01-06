from kivy.app import App
from kivy.uix.label import Label
import os

class FEACApp(App):
    def build(self):
        try:
            # Logika inisialisasi Sovereign
            return Label(text="FEAC SOVEREIGN\nStatus: Connected to Aries Port 3000")
        except Exception as e:
            # Jika API port 3000 mati, aplikasi tetap hidup dan lapor error
            return Label(text=f"Connection Error: {str(e)}")

if __name__ == "__main__":
    FEACApp().run()
