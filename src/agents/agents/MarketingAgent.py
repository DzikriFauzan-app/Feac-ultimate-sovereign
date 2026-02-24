class MarketingAgent:
    def __init__(self):
        self.name = "MarketingAgent"
        self.total_reviews = 0
        self.positive_reviews = 0
        self.negative_reviews = 0

    async def execute(self, task):
        action = task.get("action")
        
        if action == "generate_review":
            daging = task.get("daging_ratio", 1)
            tepung = task.get("tepung_ratio", 1)
            is_fresh = task.get("is_fresh", True)
            
            # Logika Penentuan Rating
            if daging > tepung and is_fresh:
                rating = 5
                comment = "Gila, ini bakso urat paling mantap! Berasa banget dagingnya."
            elif daging == tepung and is_fresh:
                rating = 5
                comment = "Pas banget rasanya, langganan terus di sini."
            elif not is_fresh:
                rating = 1
                comment = "Aduh, perut langsung mules abis makan di sini. Baunya agak aneh."
            else:
                rating = 3
                comment = "Kebanyakan tepung, kayak makan cilok kuah."

            # Update Statistik
            self.total_reviews += 1
            if rating >= 4: self.positive_reviews += 1
            else: self.negative_reviews += 1
            
            return {"rating": rating, "comment": comment, "total_stats": f"{self.positive_reviews}/{self.total_reviews}"}

        if action == "get_traffic_multiplier":
            # Sesuai instruksi Master: 10 rating jelek dari 500 hanya turun 1%
            if self.total_reviews == 0: return 1.0
            failure_rate = self.negative_reviews / self.total_reviews
            # Jika 10/500 = 0.02 (2%), maka penurunan traffic minimal
            impact = 1.0 - (failure_rate * 0.5) 
            return {"multiplier": max(0.1, impact)}
