import subprocess

class UnrealAgent:
    def __init__(self):
        self.name = "UnrealAgent"

    async def execute(self, task):
        # Memanggil bridge yang kita buat di Proot
        try:
            res = subprocess.run(["proot-distro", "login", "ubuntu", "--", "ue_bridge"], capture_output=True, text=True)
            return {"status": "success", "agent": self.name, "output": res.stdout.strip()}
        except:
            return {"status": "error", "msg": "Unreal Bridge Failed"}
