"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const lucide_react_1 = require("lucide-react");
const AgentHub = ({ agents }) => {
    return (<div className="grid grid-cols-2 gap-3 p-2">
      {agents.map((agent) => (<div key={agent.id} className="bg-[#111821] border border-gray-800 p-3 rounded-xl transition-all active:scale-95">
          <div className="flex justify-between items-start mb-2">
            <div className={`p-2 rounded-lg ${agent.status === 'processing' ? 'bg-blue-500/20 text-blue-400 animate-pulse' : 'bg-gray-800 text-gray-400'}`}>
              {agent.id === 'SovereignGuard' ? <lucide_react_1.ShieldAlert size={16}/> : <lucide_react_1.Cpu size={16}/>}
            </div>
            <div className="flex flex-col items-end">
              <span className={`text-[8px] font-bold px-2 py-0.5 rounded-full uppercase ${agent.status === 'processing' ? 'bg-blue-500/20 text-blue-400' :
                agent.status === 'error' ? 'bg-red-500/20 text-red-500' : 'bg-emerald-500/20 text-emerald-500'}`}>
                {agent.status}
              </span>
              <div className="flex items-center gap-1 mt-1">
                <lucide_react_1.Zap size={8} className="text-yellow-500"/>
                <span className="text-[8px] text-gray-500">{agent.powerUsage}%</span>
              </div>
            </div>
          </div>
          <h4 className="text-[11px] font-black text-white uppercase tracking-tighter">{agent.name}</h4>
          <p className="text-[9px] text-gray-500 leading-tight mt-1 line-clamp-2">{agent.description}</p>
        </div>))}
    </div>);
};
exports.default = AgentHub;
