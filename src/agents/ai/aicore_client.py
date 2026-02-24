import os
import requests

class AICoreClient:
    def __init__(self):
        # Ambil API key dari environment atau config
        self.api_key = os.getenv("NEO_AI_API_KEY")
        self.api_url = ""  # contoh endpoint

    def generate_texture(self, prompt: str):
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "task": "texture",
            "prompt": prompt,
            "resolution": [1024, 1024]
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            result = response.json()
            texture_url = result.get("texture_url")
            return texture_url
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None  # Handle the error as appropriate for your application
        except Exception as e:
            print(f"AI API error: {e}")
            return None  # Handle the error as appropriate for your application
