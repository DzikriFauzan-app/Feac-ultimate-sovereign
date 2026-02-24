import requests

URL = "http://10.4.35.107:8080/api/task"

def record_achievements():
    milestones = [
        "Membangun Gerobak Kayu Pertama dengan Modal 20jt",
        "Mencapai Skor Simulasi 100 (AAA Rating)",
        "Berhasil melayani 77 NPC dengan Rasio Daging 1:1",
        "Mendapatkan 490 Review Bintang 5 dari 500 Pelanggan"
    ]
    
    for m in milestones:
        requests.post(URL, json={
            "agent": "HistoryAgent",
            "action": "record_milestone",
            "event": m
        })
    
    res = requests.post(URL, json={"agent": "HistoryAgent", "action": "get_summary"})
    print(f"📖 BUKU SEJARAH JURAGAN:\n{res.json()}")

if __name__ == "__main__":
    record_achievements()
