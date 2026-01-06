import os
import sys
from kivy.app import App
from kivy.uix.label import Label

class FEACApp(App):
    def build(self):
        try:
            # Simulasi pengecekan koneksi ke Aries Gateway
            return Label(text="FEAC SOVEREIGN ONLINE\nSystem Status: Operational")
        except Exception as e:
            # Jika ada error budget/koneksi, tampilkan di layar, jangan Force Close
            return Label(text=f"Aries Connection Error: {str(e)}")

if __name__ == "__main__":
    FEACApp().run()
