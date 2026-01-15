import requests
import json

try:
    # Meminta snapshot terakhir dari WorldGraph melalui API NeoEngine
    response = requests.get('http://localhost:8080/api/dashboard/stats')
    data = response.json()
    
    print("\n📊 COUNCIL WORKLOAD STATUS:")
    print(f"📍 World Nodes: {data.get('world_nodes', 'N/A')}")
    print(f"🔗 World Edges: {data.get('world_edges', 'N/A')}")
    
    if int(data.get('world_nodes', 0)) > 0:
        print("\n✅ ARCHOSAUR CITY MANIFESTED IN WORLD GRAPH")
    else:
        print("\n⏳ GENERATION IN PROGRESS...")
except Exception as e:
    print(f"❌ Connection Error: {e}")
