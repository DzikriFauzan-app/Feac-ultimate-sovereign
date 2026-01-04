import cgitb; cgitb.enable(format='text') # Logger darurat
try:
    # --- MASUKKAN IMPORT DAN LOGIKA UTAMA KAMU DI SINI ---
    from kivy.app import App
    from kivy.uix.label import Label
    # Contoh sederhana untuk tes:
    class FEACSovereign(App):
        def build(self):
            return Label(text='Sovereign Online - Aries Connected')
    
    if __name__ == '__main__':
        FEACSovereign().run()
except Exception as e:
    # Jika crash, cetak error ke file agar bisa kita baca
    with open("crash_log.txt", "w") as f:
        f.write(str(e))
    raise e
