from core.world_registry import WorldRegistry

class FEACWorldAdapter:
    @staticmethod
    def define_region(data):
        # Mendaftarkan ke registry internal
        WorldRegistry.register_region(data['name'], data['type'])
        
        # Mengembalikan struktur yang sudah diperbaiki untuk WorldGraph
        return {
            "node_type": "REGION",
            "name": data['name'],
            "attributes": data
        }

print("✅ FEAC_ADAPTER: Logic definition updated.")
