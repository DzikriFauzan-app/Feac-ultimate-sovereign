import { Activity, Cpu, Zap } from 'lucide-react';

const NeoGrid = () => {
  const agents = [
    { id: 'AG-01', task: 'Optimizing Neural Bus', load: '45%' },
    { id: 'AG-02', task: 'Scanning Artifacts', load: '12%' }
  ];

  return (
    <div className="p-5 pb-24 space-y-6">
      <div className="bg-[#0a1612] border border-emerald-500/20 p-6 rounded-2xl relative overflow-hidden shadow-2xl">
        <h2 className="text-xl font-black text-white italic tracking-tighter uppercase flex items-center">
          <Activity className="mr-2 text-emerald-500 w-5 h-5 animate-pulse" /> NeoGrid Agents
        </h2>
        <p className="text-[10px] text-emerald-500/50 font-mono mt-1 uppercase tracking-widest italic">Autonomous Sovereign Intelligence</p>
      </div>

      <div className="space-y-4">
        {agents.map(agent => (
          <div key={agent.id} className="bg-[#111821] border border-gray-800 p-5 rounded-2xl flex items-center justify-between group hover:border-emerald-500/30 transition-all">
            <div className="flex items-center space-x-4">
              <div className="p-3 bg-emerald-500/10 rounded-xl border border-emerald-500/20">
                <Cpu className="text-emerald-500 w-5 h-5" />
              </div>
              <div>
                <p className="text-[10px] font-black text-emerald-500 uppercase tracking-[0.2em]">{agent.id}</p>
                <p className="text-sm font-bold text-white mt-1 italic tracking-tight">{agent.task}</p>
              </div>
            </div>
            <div className="text-right">
              <p className="text-xs font-black text-gray-500 uppercase">{agent.load}</p>
              <div className="w-16 h-1.5 bg-gray-900 rounded-full mt-2 overflow-hidden">
                <div className="h-full bg-emerald-500" style={{ width: agent.load }}></div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="bg-black/50 border border-gray-800 p-4 rounded-2xl">
        <p className="text-[9px] font-black text-gray-600 uppercase mb-3 tracking-widest">Master Autonomous Command</p>
        <div className="flex space-x-2">
          <input type="text" placeholder="Prompt agent behavior..." className="flex-1 bg-transparent border-b border-gray-800 py-2 text-xs text-blue-400 outline-none focus:border-blue-500" />
          <button className="bg-blue-600 p-2 rounded-lg text-white active:scale-90"><Zap className="w-4 h-4" /></button>
        </div>
      </div>
    </div>
  );
};

export default NeoGrid;
