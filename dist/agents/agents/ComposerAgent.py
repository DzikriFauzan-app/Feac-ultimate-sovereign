import random

class ComposerAgent:
    def __init__(self):
        self.name = "ComposerAgent"

    async def execute(self, task):
        mood = task.get("mood", "mystery") # 'berdebar', 'mencekam', 'bahagia'
        print(f"🎼 [ComposerAgent] Composing original score for mood: {mood.upper()}...")
        
        music_genres = {
            "mystery": ["Gamelan_Synthwave", "Dark_Ambient"],
            "tension": ["Percussion_Heavy", "Drone_Waltz"],
            "joy": ["Upbeat_Dangdut", "Koplo_Pop"]
        }
        chosen_genre = random.choice(music_genres.get(mood, ["Ambient"]))

        return {"status": "MUSIC_COMPOSED", "track_name": f"{mood.capitalize()}_Theme_{chosen_genre}.mp3"}
