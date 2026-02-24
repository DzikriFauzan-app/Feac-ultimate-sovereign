import os
import importlib
import sys

class AgencyFactory:
    def __init__(self):
        self.agent_dir = "/sdcard/Buku saya/Fauzan engine/NeoEngine/agents"
        os.makedirs(self.agent_dir, exist_ok=True)
        sys.path.append(self.agent_dir)

    def spawn_specialized_agent(self, agent_name, capability_desc):
        """Melahirkan agen baru berdasarkan deskripsi kemampuan yang dibutuhkan"""
        filename = f"{agent_name}.py"
        path = os.path.join(self.agent_dir, filename)
        
        template = f'''
class {agent_name}:
    def __init__(self):
        self.name = "{agent_name}"
        self.capability = "{capability_desc}"

    def execute(self, task_data):
        # Otonomous Execution Logic for {capability_desc}
        print(f"[{{self.name}}] Processing: {{task_data}}")
        return {{"status": "success", "agent": self.name, "result": "Task completed via " + self.capability}}

agent_instance = {agent_name}()
'''
        with open(path, "w") as f:
            f.write(template)
        
        return f"🌟 Agent {agent_name} has been synthesized for: {capability_desc}"

factory = AgencyFactory()
