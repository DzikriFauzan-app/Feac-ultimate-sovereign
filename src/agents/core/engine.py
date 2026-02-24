import asyncio
import logging
import os
from core.agent_manager import AgentManager
from core.database import Database

class NeoEngine:
    def __init__(self):
        self.project_root = "/sdcard/Buku saya/Fauzan engine/NeoEngine"
        self.db = Database()
        self.agent_manager = AgentManager(self.project_root, self.db)
        self.is_running = False

    async def start(self):
        self.is_running = True
        self.agent_manager.load_agents()
        # Log manual untuk verifikasi agen baru
        loaded = list(self.agent_manager.agents.keys())
        print(f"--- COUNCIL STATUS: {len(loaded)} AGENTS ACTIVE ---")
        print(f"Agents: {', '.join(loaded)}")
        while self.is_running:
            await asyncio.sleep(1)

    async def dispatch_task(self, payload: dict):
        # Jika payload berisi list 'tasks', jalankan semua
        if "tasks" in payload:
            results = []
            for task in payload["tasks"]:
                res = await self._execute_single(task)
                results.append(res)
            return {"status": "batch_complete", "results": results}
        return await self._execute_single(payload)

    async def _execute_single(self, task):
        target = task.get("agent")
        agent = self.agent_manager.get_agent(target)
        if not agent: return {"error": f"{target} not found"}
        
        method = getattr(agent, "execute", getattr(agent, "process_task", getattr(agent, "run", getattr(agent, "handle", None))))
        if asyncio.iscoroutinefunction(method): return await method(task)
        return method(task)

