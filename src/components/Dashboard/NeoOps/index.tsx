import { useState } from 'react';
import AgentHub from './AgentHub';
import ShellView from './ShellView';
import { Agent } from './types';

const NeoOps = () => {
  const [agents] = useState<Agent[]>([
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

  return (
    <div className="bg-black min-h-screen pb-20 scrollbar-hide">
      <div className="p-4 border-b border-gray-900 flex justify-between items-center bg-[#0a0f14] sticky top-0 z-10">
        <h2 className="text-blue-500 font-black italic text-lg tracking-tighter uppercase">Neo Engine Studio</h2>
        <div className="flex gap-2">
          <div className="h-2 w-2 rounded-full bg-emerald-500 shadow-[0_0_8px_#10b981]"></div>
          <span className="text-[8px] text-gray-500 font-mono">LINKED_TO_ARIES</span>
        </div>
      </div>
      
      <div className="mt-4">
        <h3 className="px-4 text-[9px] font-bold text-gray-600 uppercase tracking-[0.2em] mb-3">Neural Council Monitor</h3>
        <AgentHub agents={agents} />
      </div>

      <div className="mt-6">
        <h3 className="px-4 text-[9px] font-bold text-gray-600 uppercase tracking-[0.2em] mb-3">Sovereign Shell</h3>
        <ShellView />
      </div>
    </div>
  );
};

export default NeoOps;
