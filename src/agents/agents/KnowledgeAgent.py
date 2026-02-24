import os
import glob

class KnowledgeAgent:
    def __init__(self, *args, **kwargs):
        self.root_path = "/sdcard/Buku saya/"
        self.supported_ext = [".txt", ".md", ".json"]

    def search_knowledge(self, query):
        """Mencari referensi teks dalam naskah dan buku Master"""
        results = []
        # Mencari di semua subfolder
        files = []
        for ext in self.supported_ext:
            files.extend(glob.glob(f"{self.root_path}/**/*{ext}", recursive=True))

        for file_path in files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        # Ambil potongan teks di sekitar kata kunci
                        index = content.lower().find(query.lower())
                        start = max(0, index - 100)
                        end = min(len(content), index + 200)
                        results.append({
                            "source": os.path.basename(file_path),
                            "snippet": content[start:end].replace("\n", " ")
                        })
            except:
                continue
        
        return results[:5] # Batasi 5 hasil terbaik agar RAM hemat

knowledge_agent = KnowledgeAgent()
