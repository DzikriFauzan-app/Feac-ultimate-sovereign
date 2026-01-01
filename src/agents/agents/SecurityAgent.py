import hashlib

class SecurityAgent:
    def __init__(self):
        self.name = "SecurityAgent"
        self.secret_salt = "SOVEREIGN_FAUZAN_2025"

    async def execute(self, task):
        action = task.get("action")
        
        if action == "encrypt_stat":
            data = str(task.get("value"))
            # Membuat hash untuk validasi integritas data
            secure_hash = hashlib.sha256((data + self.secret_salt).encode()).hexdigest()
            return {"status": "SECURED", "value": data, "hash": secure_hash}

        if action == "validate_integrity":
            client_hash = task.get("hash")
            current_value = str(task.get("value"))
            expected_hash = hashlib.sha256((current_value + self.secret_salt).encode()).hexdigest()
            
            if client_hash == expected_hash:
                return {"status": "VALID", "msg": "Data murni, tidak ada cheat."}
            else:
                return {"status": "TAMPERED", "msg": "Deteksi Cheat! Resetting Player..."}
