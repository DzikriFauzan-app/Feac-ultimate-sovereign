import os
import sys

# Redirect error ke file agar kita bisa baca lewat file manager HP
sys.stderr = open("feac_error_log.txt", "w")
sys.stdout = sys.stderr

try:
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.scrollview import ScrollView
    
    class DiagnosticApp(App):
        def build(self):
            # Jika berhasil running, tampilkan pesan ini
            return Label(text="FEAC SOVEREIGN ONLINE\nAries & Neo Engine Ready")

    if __name__ == "__main__":
        DiagnosticApp().run()

except Exception as e:
    # Jika crash, ini akan tertulis di file feac_error_log.txt di folder data aplikasi
    print(f"CRITICAL ERROR: {e}")
    with open("/sdcard/FEAC_CRASH.txt", "w") as f:
        f.write(str(e))
