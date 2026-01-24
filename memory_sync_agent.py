import os
import json
import datetime

ARIES_MEMORY_PATH = "/data/data/com.termux/files/home/Aries-api-key/brain_data/memory_logs.json"

def sync_chat_to_aries(chat_data):
    """
    Menyimpan sesi chat FEAC ke dalam memori permanen Aries
    untuk menambah IQ sistem secara berkelanjutan.
    """
    if not os.path.exists(os.path.dirname(ARIES_MEMORY_PATH)):
        os.makedirs(os.path.dirname(ARIES_MEMORY_PATH), exist_ok=True)
    
    current_memory = []
    if os.path.exists(ARIES_MEMORY_PATH):
        with open(ARIES_MEMORY_PATH, 'r') as f:
            try:
                current_memory = json.load(f)
            except: current_memory = []

    # Inject data baru dengan timestamp
    log_entry = {
        "timestamp": str(datetime.datetime.now()),
        "status": "OWNER_AUTHORIZED",
        "data": chat_data
    }
    
    current_memory.append(log_entry)
    
    with open(ARIES_MEMORY_PATH, 'w') as f:
        json.dump(current_memory, f, indent=4)
    
    print("💎 [MEMORY_SYNC]: Intelligence harvested and stored in Aries Brain.")

if __name__ == "__main__":
    # Test Sync manual
    sync_chat_to_aries({"session_id": "99", "context": "Optimization of 46 Agents"})
