class SentienceEvaluatorAgent:
    def __init__(self):
        self.name = "SentienceEvaluatorAgent"

    async def execute(self, task):
        # Kriteria Penilaian: Ekonomi, Biaya Hidup, Risiko, Skala Waktu
        score = 0
        criteria = []
        
        if task.get("has_inflation"): score += 25; criteria.append("Ekonomi Dinamis")
        if task.get("has_health_risk"): score += 25; criteria.append("Biaya Kesehatan")
        if task.get("has_household_cost"): score += 25; criteria.append("Domestic Pressure")
        if task.get("time_scale") == "10min/day": score += 25; criteria.append("Time Precision")
        
        rating = "AAA Simulation" if score >= 90 else "Semi-Realistic"
        return {
            "simulation_score": score,
            "rating": rating,
            "verified_criteria": criteria,
            "feedback": "Sistem sudah sangat mendekati realitas pasar malam Indonesia."
        }
