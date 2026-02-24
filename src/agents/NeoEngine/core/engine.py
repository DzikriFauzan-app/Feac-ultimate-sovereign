import asyncio
from .settings import Settings
from .database import Database
from .message_bus import MessageBus
from .scheduler import Scheduler
from .agent_manager import AgentManager

class NeoEngine:
    def __init__(self):
        Settings.setup_dirs()
        self.db = Database()
        self.bus = MessageBus()
        self.scheduler = Scheduler(self.bus, self.db)
        self.agent_manager = AgentManager(self.bus, self.db)

    async def start(self):
        print("[ENGINE] Initializing agents and scheduler...")
        self.agent_manager.load_agents()
        # Run scheduler in background
        asyncio.create_task(self.scheduler.start())
        print("[ENGINE] NeoEngine initialized.")
    
    async def execute_command(self, agent, command, params):
        return await self.scheduler.schedule_task(agent, command, params)
