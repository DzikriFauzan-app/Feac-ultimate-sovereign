import importlib
import os
import inspect
from agents.BaseAgent import BaseAgent

class AgentManager:
    def __init__(self, bus, db):
        self.bus = bus
        self.db = db
        self.agents = {}

    def load_agents(self):
        agent_dir = os.path.join(os.getcwd(), "agents")
        for filename in os.listdir(agent_dir):
            if filename.endswith("Agent.py") and filename != "BaseAgent.py":
                module_name = f"agents.{filename[:-3]}"
                try:
                    module = importlib.import_module(module_name)
                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj) and issubclass(obj, BaseAgent) and obj is not BaseAgent:
                            agent = obj(self.bus, self.db)
                            self.agents[agent.name] = agent
                            agent.start()
                            print(f"[AgentManager] Loaded agent: {agent.name}")
                except Exception as e:
                    print(f"Failed to load {filename}: {e}")
