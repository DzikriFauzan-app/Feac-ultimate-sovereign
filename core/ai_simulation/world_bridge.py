from core.render_kernel.kernel import RenderKernel
from typing import List, Dict

class WorldBridge:
    """
    Jembatan FEAC: Menghubungkan data Agent ke Graph Kernel NeoEngine.
    """
    def __init__(self):
        self.kernel = RenderKernel()
        self.active_agents = []

    def sync_agents_to_graph(self, agents_data: List[Dict]):
        """
        Mengonversi data dari 47+ Agent menjadi node yang bisa dirender secara logis.
        """
        passes = ["agent_logic_pass"]
        for agent in agents_data:
            # Setiap agent menjadi 'pass' atau 'node' dalam logika render
            passes.append(f"process_{agent['name']}")
            
        # Eksekusi via Kernel ABI (Opsi 1)
        return self.kernel.execute(
            pipeline_name="feac_world_simulation",
            passes=passes
        )

# Instance global untuk digunakan oleh semua Agent
feac_bridge = WorldBridge()
