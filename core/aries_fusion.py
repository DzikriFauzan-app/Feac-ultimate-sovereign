import os
import re

class AriesFusion:
    def __init__(self):
        self.pending_fixes = []

    def scan_and_report(self):
        """Memindai bug dan mengumpulkan daftar perbaikan"""
        self.pending_fixes = []
        report = ["⚡ ARIES FUSION SCAN REPORT"]
        
        # 1. Scan Negotiator (DNA Blackbox)
        neg_path = "src/core/negotiator.ts"
        if os.path.exists(neg_path):
            with open(neg_path, 'r') as f:
                content = f.read()
                if "source: 'emulator'" in content:
                    report.append("❌ [Bug Found] Deprecated argument in negotiator.ts")
                    self.pending_fixes.append(('file', neg_path, "source: 'emulator'", ""))

        # 2. Scan Permissions (DNA Genspark)
        spec_path = "buildozer.spec"
        if os.path.exists(spec_path):
            with open(spec_path, 'r') as f:
                content = f.read()
                if "INTERNET" not in content:
                    report.append("❌ [Bug Found] Permissions missing in buildozer.spec")
                    self.pending_fixes.append(('spec', spec_path, "android.permissions =", "android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,ACCESS_NETWORK_STATE"))

        if not self.pending_fixes:
            report.append("✅ No critical bugs found. System Stable.")
        
        return "\n".join(report)

    def apply_fix_automatically(self):
        """Tombol Eksekusi: Langsung memperbaiki semua bug yang ditemukan"""
        if not self.pending_fixes:
            return "🛡️ Aries: Nothing to fix, system is already Sovereign."

        results = []
        for fix_type, path, target, replacement in self.pending_fixes:
            try:
                with open(path, 'r') as f:
                    content = f.read()
                
                if fix_type == 'file':
                    new_content = content.replace(", { source: 'emulator' }", "")
                    new_content = new_content.replace(", {source:'emulator'}", "")
                elif fix_type == 'spec':
                    new_content = re.sub(r'^android.permissions =.*', replacement, content, flags=re.M)
                
                with open(path, 'w') as f:
                    f.write(new_content)
                results.append(f"✅ Fixed: {path}")
            except Exception as e:
                results.append(f"❌ Failed to fix {path}: {str(e)}")
        
        return "\n".join(results)

if __name__ == "__main__":
    fusion = AriesFusion()
    print(fusion.scan_and_report())
