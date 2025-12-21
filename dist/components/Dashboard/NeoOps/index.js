"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const AgentHub_1 = __importDefault(require("./AgentHub"));
const NeoOps = () => {
    // Simulasi data 10 Agen sesuai Blueprint
    const [agents] = (0, react_1.useState)([
        { id: 'Orchestrator', name: 'Orchestrator', status: 'processing', description: 'CEO & Project Manager', powerUsage: 15 },
        { id: 'VisualEngine', name: 'Visual Engine', status: 'standby', description: 'PBR & Shader Renderer', powerUsage: 45 },
        { id: 'LogicBrain', name: 'Logic Brain', status: 'idle', description: 'Gameplay Scripting', powerUsage: 10 },
        { id: 'AssetForge', name: 'Asset Forge', status: 'idle', description: '3D & Texture Gen', powerUsage: 5 },
        { id: 'PhysicsCore', name: 'Physics Core', status: 'idle', description: 'World Simulation', powerUsage: 20 },
        { id: 'BizOps', name: 'BizOps Agent', status: 'idle', description: 'Economy & Balance', powerUsage: 2 },
        { id: 'SelfEvolution', name: 'Self-Evolution', status: 'standby', description: 'Auto-Learning Doc', powerUsage: 8 },
        { id: 'OptiAgent', name: 'Optimization', status: 'processing', description: 'Thermal & RAM Guard', powerUsage: 1 },
        { id: 'LogicNode', name: 'Logic Node', status: 'idle', description: 'Visual Blueprinting', powerUsage: 3 },
        { id: 'SovereignGuard', name: 'Sovereign Guard', status: 'standby', description: 'Security Sandbox', powerUsage: 1 },
    ]);
    return (<div className="bg-black min-h-screen pb-20">
      <div className="p-4 border-b border-gray-900 flex justify-between items-center bg-[#0a0f14] sticky top-0 z-10">
        <h2 className="text-blue-500 font-black italic text-lg tracking-tighter">NEO OPS <span className="text-[10px] text-gray-600">v1.2</span></h2>
        <div className="flex gap-2">
          <div className="h-2 w-2 rounded-full bg-emerald-500 shadow-[0_0_8px_#10b981]"></div>
          <span className="text-[8px] text-gray-500 font-mono uppercase">System Linked</span>
        </div>
      </div>
      
      <div className="mt-2">
        <h3 className="px-4 text-[10px] font-bold text-gray-600 uppercase tracking-[0.2em] mb-2">Neural Council Status</h3>
        <AgentHub_1.default agents={agents}/>
      </div>
    </div>);
};
exports.default = NeoOps;
