import json
import os
from datetime import datetime

class MemoryAgent:
    def __init__(self, *args, **kwargs):
        self.base_path = "/sdcard/Buku saya/Fauzan engine/NeoEngine/storage/memory"
        os.makedirs(self.base_path, exist_ok=True)

    def encode_memory(self, category, tag, content):
        file_path = f"{self.base_path}/{category}.json"
        memories = []
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try: memories = json.load(f)
                except: memories = []
        
        memories.append({
            "timestamp": datetime.now().isoformat(),
            "tag": tag,
            "data": content
        })
        with open(file_path, "w") as f:
            json.dump(memories, f, indent=4)

    def retrieve_memory(self, query):
        """Mencari memori berdasarkan keyword (misal: 'Dragon City')"""
        results = []
        for file in os.listdir(self.base_path):
            if file.endswith(".json"):
                with open(f"{self.base_path}/{file}", "r") as f:
                    data = json.load(f)
                    for entry in data:
                        if query.lower() in str(entry).lower():
                            results.append(entry)
        return results

memory_agent = MemoryAgent()
