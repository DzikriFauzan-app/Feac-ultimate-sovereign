import asyncio
import json
from core.engine import NeoEngine

async def main():
    print("👑 NEO-ENGINE SOVEREIGN: EMPIRE EDITION (34 AGENTS)...")
    e = NeoEngine()
    if not hasattr(e.agent_manager, 'get_agent'):
        e.agent_manager.get_agent = lambda name: e.agent_manager.agents.get(name)

    asyncio.create_task(e.start())
    await asyncio.sleep(2) 

    tasks = [
        {"agent": "NarrativeAgent", "action": "generate_story"},
        {"agent": "ComposerAgent", "action": "compose_track"},
        {"agent": "AudioAgent", "action": "mix_ambience"},
        {"agent": "UnrealAgent", "action": "render_heavy"},
        {"agent": "CrowdSimulationAgent", "action": "simulate_crowd"},
        {"agent": "GrandAestheteAgent", "action": "polish_visuals"},
        {"agent": "WhaleRetentionAgent", "action": "optimize_revenue"}, # STRATEGI DUIT
        {"agent": "MapGeneratorAgent", "action": "layout"},
        {"agent": "UIAgent", "action": "generate_hud"},
        {"agent": "GenesisAgent", "action": "hybrid_sync"},
        {"agent": "SentientTesterAgent", "action": "final_validation"},
        {"agent": "MarketingAgent", "action": "prepare_viral_kit"}
    ]

    print("\n🚀 EXECUTING EMPIRE PRODUCTION CHAIN...")
    for task in tasks:
        res = await e.dispatch_task(task)
        if task['agent'] == "WhaleRetentionAgent":
            print(f"\n💵 REVENUE STRATEGY: {json.dumps(res.get('strategy'), indent=2)}")
            print(f"📈 FORECAST: {res.get('forecast')}")
        else:
            print(f"✅ {task['agent']}: {res.get('status') or 'SUCCESS'}")
        await asyncio.sleep(0.5)

if __name__ == "__main__":
    asyncio.run(main())
