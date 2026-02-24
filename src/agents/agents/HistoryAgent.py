class HistoryAgent:
    def __init__(self):
        self.name = "HistoryAgent"
        self.milestones = []

    async def execute(self, task):
        action = task.get("action")
        if action == "record_milestone":
            event = task.get("event")
            self.milestones.append(event)
            return {"status": "JOURNALED", "total_events": len(self.milestones)}
        
        if action == "get_summary":
            return {"history": self.milestones}
