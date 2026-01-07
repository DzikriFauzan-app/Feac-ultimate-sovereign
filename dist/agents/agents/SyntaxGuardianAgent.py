import os
import shutil
import ast

class SyntaxGuardianAgent:
    def __init__(self):
        self.name = "SyntaxGuardianAgent"
        self.backup_dir = "/data/data/org.feac.ultimate.feac_sovereign/files/NeoEngine/backups_safe"
        os.makedirs(self.backup_dir, exist_ok=True)

    async def execute(self, task):
        file_path = task.get("file_path")
        action = task.get("action")

        if action == "validate_and_backup":
            try:
                with open(file_path, 'r') as f:
                    code = f.read()
                # Validasi Syntax Python
                ast.parse(code)
                
                # Jika valid, buat backup
                filename = os.path.basename(file_path)
                shutil.copy(file_path, f"{self.backup_dir}/{filename}.stable")
                return {"status": "GUARD_OK", "msg": f"Syntax {filename} valid & backed up."}
            except SyntaxError as e:
                return {"status": "GUARD_FAIL", "msg": f"CRITICAL: Syntax error at line {e.lineno}"}
