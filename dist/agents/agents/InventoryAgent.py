class InventoryAgent:
    def __init__(self):
        self.name = "InventoryAgent"
        self.storage = {
            "fresh_meat": 0,    # Daging segar hari ini
            "chilled_meat": 0,  # Daging di kulkas (tahan lama)
            "decaying_meat": 0  # Daging mulai layu
        }
        self.has_fridge = False

    async def execute(self, task):
        action = task.get("action")
        
        # Opsi Buang Stok yang sudah buruk
        if action == "discard_stock":
            target = task.get("target") # misal 'decaying_meat'
            qty = task.get("qty")
            self.storage[target] = max(0, self.storage[target] - qty)
            return {"status": "DISCARDED", "msg": f"Berhasil membuang {qty}kg {target}."}

        # Logika Pindah ke Kulkas
        if action == "move_to_fridge":
            if not self.has_fridge:
                return {"error": "Belum punya kulkas!"}
            qty = self.storage["fresh_meat"]
            self.storage["chilled_meat"] += qty
            self.storage["fresh_meat"] = 0
            return {"status": "STORED", "msg": f"Daging aman di kulkas selama 2 bulan."}

        if action == "buy_fridge":
            self.has_fridge = True
            return {"status": "SUCCESS", "msg": "Kulkas 2 Juta Coin Aktif!"}
