import os
import importlib
import inspect
import asyncio

class AgentManager:
    def get_agent(self, name):
        return self.agents.get(name)
    def __init__(self, bus, db):
        self.bus = bus
        self.db = db
        self.agents = {}
        self.agents_path = "/sdcard/Buku saya/Fauzan engine/NeoEngine/agents"

    def load_agents(self):
        print("\n--- [NEURAL COUNCIL: SMART AUTO-LOAD] ---")
        base_pkg = "agents"
        
        for file in os.listdir(self.agents_path):
            if file.endswith(".py") and not file.startswith("__") and file != "agent_manager.py" and file != "BaseAgent.py":
                module_name = file[:-3]
                try:
                    module = importlib.import_module(f"{base_pkg}.{module_name}")
                    # Cari semua class di dalam module ini
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        # Pastikan class berasal dari file ini, bukan import-an
                        if obj.__module__ == f"{base_pkg}.{module_name}":
                            try:
                                # Inisialisasi dengan Fallback Protocol
                                try:
                                    instance = obj(self.bus, self.db)
                                except TypeError:
                                    instance = obj()
                                
                                self.agents[name] = instance
                                print(f"[AgentManager] ✅ {name} ONLINE (from {file})")
                            except Exception as e:
                                print(f"[AgentManager] ❌ Failed to init {name}: {e}")
                except Exception as e:
                    print(f"[AgentManager] ⚠️ Error loading module {module_name}: {e}")
        
        print(f"--- TOTAL POWER: {len(self.agents)} CLASSES ACTIVE ---\n")

    async def handle_task(self, task):
        name = task.get("agent")
        agent = self.agents.get(name)
        if not agent: return {"error": f"Agent {name} not found"}
        
        for m in ["process_task", "execute", "run"]:
            method = getattr(agent, m, None)
            if method:
                if asyncio.iscoroutinefunction(method): return await method(task)
                return method(task)
        return {"error": "No execution method"}
