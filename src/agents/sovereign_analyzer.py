import os
import ast

class SovereignAnalyzer:
    def __init__(self, projects):
        self.projects = projects
        self.report = []

    def scan_deep(self):
        print("🔍 SovereignAnalyzer: Memulai pemindaian mendalam Aries, FEAC, & Neo Engine...")
        for project_path in self.projects:
            if os.path.exists(project_path):
                self._analyze_dir(project_path)
            else:
                self.report.append(f"❌ Path tidak ditemukan: {project_path}")

    def _analyze_dir(self, path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    self._audit_code(os.path.join(root, file))

    def _audit_code(self, file_path):
        with open(file_path, "r") as f:
            code = f.read()
            try:
                tree = ast.parse(code)
                # Simulasi pengecekan kompleksitas & fitur self-build
                score = len(tree.body)
                if "buildozer" in code or "export" in code:
                    self.report.append(f"✅ {file_path}: Terdeteksi modul Export/Build (Ready for Self-Build).")
                if score > 50:
                    self.report.append(f"⚠️ {file_path}: Kode terlalu padat ({score} nodes). Sarankan Modularisasi.")
            except SyntaxError:
                self.report.append(f"🚨 {file_path}: ERROR SINTAKS DITEMUKAN!")

    def show_suggestions(self):
        print("\n--- 📜 HASIL AUDIT SOVEREIGN ---")
        for line in self.report:
            print(line)

if __name__ == "__main__":
    paths = [
        "/sdcard/Buku saya/Fauzan engine/Projects/Aries",
        "/sdcard/Buku saya/Fauzan engine/Projects/FEAC",
        "/sdcard/Buku saya/Fauzan engine/NeoEngine"
    ]
    analyzer = SovereignAnalyzer(paths)
    analyzer.scan_deep()
    analyzer.show_suggestions()
