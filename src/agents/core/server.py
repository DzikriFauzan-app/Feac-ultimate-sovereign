import asyncio
import json
from aiohttp import web
from aiohttp_cors import setup, ResourceOptions
import sys
import os

sys.path.append("/sdcard/Buku saya/Fauzan engine/NeoEngine/agents")
from HistoryAgent import history_agent
from CodeAgent import code_agent
from BuildAgent import build_agent
from ExportAgent import export_agent
from KnowledgeAgent import knowledge_agent
from AgencyFactory import factory
from OptiAgent import opti_agent

# [ENDPOINT DASHBOARD STATS]
async def get_dashboard_stats(request):
    try:
        agents = os.listdir("/sdcard/Buku saya/Fauzan engine/NeoEngine/agents")
        projects = os.listdir("/sdcard/Buku saya/Fauzan engine/NeoEngine/storage/world_data")
        exports = os.listdir("/sdcard/Buku saya/Fauzan engine/NeoEngine/exports")
        
        stats = {
            "agent_count": len([f for f in agents if f.endswith('.py')]),
            "project_count": len([f for f in projects if f.endswith('.json')]),
            "export_count": len([f for f in exports if f.endswith('.zip')]),
            "system_health": opti_agent.get_stats()
        }
        return web.json_response(stats)
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

async def handle_agent_chat(request):
    try:
        data = await request.json()
        target_agent = data.get('agent', '').lower()
        message = data.get('message', '').lower()
        
        if "export" in target_agent:
            res = export_agent.bundle_project("Global")
            reply = f"📦 ExportAgent: Global Bundle created in {res.get('file', 'error')}"
        elif "codeagent" in target_agent:
            res = code_agent.generate_code("System", "neo", "core", message)
            reply = f"💻 CodeAgent: Generated {res['file']}"
        else:
            reply = f"Agent {target_agent} stand by. Memori Master tersinkronisasi."

        return web.json_response({"status": "replied", "reply": reply})
    except: return web.json_response({"status": "error"}, status=400)

app = web.Application()
setup(app, defaults={"*": ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*")})

app.router.add_get('/api/dashboard/stats', get_dashboard_stats)
app.router.add_post('/api/agent/chat', handle_agent_chat)

if __name__ == '__main__':
    web.run_app(app, port=8080)
