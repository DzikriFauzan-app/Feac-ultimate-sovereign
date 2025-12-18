import { ShieldAlert, Terminal, ChevronRight, Crown } from 'lucide-react';

const Dashboard = ({ userRole = 'OWNER' }: { userRole?: string }) => {
  return (
    <div className="p-5 pb-20 space-y-6 animate-in fade-in duration-500">
      {/* STATUS HEADER */}
      <div className="flex justify-between items-end border-b border-gray-800/50 pb-4">
        <div>
          <h2 className="text-2xl font-black text-white tracking-tighter uppercase italic">Dashboard <span className="text-blue-500">v5.3</span></h2>
          <p className="text-[10px] text-gray-500 font-mono tracking-widest uppercase">Protocol: Active</p>
        </div>
        <div className="text-right">
          <p className="text-[9px] font-black text-blue-400 uppercase tracking-widest">Access Level</p>
          <p className="text-sm font-bold text-white flex items-center justify-end">
            {userRole === 'OWNER' && <Crown className="w-3 h-3 mr-1 text-yellow-500" />}
            {userRole}
          </p>
        </div>
      </div>

      {/* SUPERKEY PANEL (Sesuai Gambar 1000183132) */}
      <div className="bg-[#062d24] border border-[#10b981]/30 rounded-2xl p-6 relative overflow-hidden group shadow-2xl shadow-emerald-900/20">
        <div className="relative z-10 space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-[#10b981]/20 rounded-lg border border-[#10b981]/30">
              <ShieldAlert className="text-[#10b981] w-6 h-6" />
            </div>
            <div>
              <h3 className="text-sm font-black text-white uppercase tracking-tight leading-none">SuperKey Required</h3>
              <p className="text-[9px] text-emerald-400/70 mt-1 uppercase tracking-widest">Restricted Mode Active</p>
            </div>
          </div>
          <div className="flex space-x-2">
            <input 
              type="password" 
              placeholder="Enter SuperKey..." 
              className="bg-black/40 border border-emerald-900/50 p-3 rounded-xl flex-1 text-emerald-500 text-xs focus:outline-none focus:border-[#10b981] placeholder:text-emerald-900/50" 
            />
            <button className="bg-[#10b981] text-black px-4 rounded-xl active:scale-95 transition-transform">
              <ChevronRight className="w-5 h-5" />
            </button>
          </div>
        </div>
      </div>

      {/* STATS GRID */}
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-[#111821] border border-gray-800 rounded-2xl p-4">
          <p className="text-[8px] text-gray-500 uppercase font-black tracking-widest mb-1">Revenue</p>
          <p className="text-xl font-black text-emerald-400">$1.2M</p>
        </div>
        <div className="bg-[#111821] border border-gray-800 rounded-2xl p-4">
          <p className="text-[8px] text-gray-500 uppercase font-black tracking-widest mb-1">Nodes</p>
          <p className="text-xl font-black text-blue-400 tracking-tighter">4 <span className="text-[10px] text-blue-900 italic">ACTIVE</span></p>
        </div>
      </div>

      {/* TERMUX BRIDGE */}
      <div className="bg-[#111821] border border-gray-800 rounded-2xl p-5 shadow-xl">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <Terminal className="text-emerald-500 w-4 h-4"/> 
            <span className="text-[10px] font-black uppercase tracking-widest text-gray-400 font-mono">Termux Bridge</span>
          </div>
          <span className="text-[8px] text-emerald-500 font-bold animate-pulse">ONLINE</span>
        </div>
        <div className="bg-black/60 p-4 h-32 rounded-xl border border-gray-900 font-mono text-[10px] overflow-y-auto text-emerald-500/70 space-y-1 custom-scrollbar">
          <p>&gt; [08:42:11] FEAC Core Initialized</p>
          <p className="text-emerald-900">&gt; Connected: ws://localhost:3000</p>
          <p className="text-blue-900">&gt; Protocol: Aries-v2 Active</p>
          <p className="animate-pulse text-emerald-400/50 mt-2">&gt; Awaiting SuperKey Command...</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
