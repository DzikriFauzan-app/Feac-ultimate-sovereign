import { useState, useEffect } from 'react';
import { ShieldCheck, Box, Users, Zap, DownloadCloud } from 'lucide-react';

const MasterDashboard = () => {
  const [stats, setStats] = useState({ agent_count: 0, project_count: 0, export_count: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await fetch('http://10.159.189.152:8080/api/dashboard/stats');
        const data = await res.json();
        setStats(data);
      } catch (err) { console.error("Sync Error"); }
    };
    fetchStats();
    const interval = setInterval(fetchStats, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-5 space-y-4">
      {/* Sovereign Header */}
      <div className="flex items-center gap-3 bg-blue-600/10 border border-blue-500/20 p-4 rounded-3xl">
        <ShieldCheck className="text-blue-500" size={32} />
        <div>
          <h1 className="text-white font-black tracking-tighter text-lg uppercase">Sovereign_Control</h1>
          <p className="text-[8px] text-blue-400 font-bold uppercase tracking-[0.2em]">NeoEngine Core V2.5 Active</p>
        </div>
      </div>

      {/* Grid Stats */}
      <div className="grid grid-cols-3 gap-3">
        <div className="bg-[#0a0a0a] border border-gray-900 p-3 rounded-2xl text-center">
          <Users size={16} className="text-emerald-500 mx-auto mb-1" />
          <p className="text-[7px] text-gray-500 font-bold uppercase">Agents</p>
          <p className="text-sm text-white font-black">{stats.agent_count}</p>
        </div>
        <div className="bg-[#0a0a0a] border border-gray-900 p-3 rounded-2xl text-center">
          <Box size={16} className="text-blue-500 mx-auto mb-1" />
          <p className="text-[7px] text-gray-500 font-bold uppercase">Projects</p>
          <p className="text-sm text-white font-black">{stats.project_count}</p>
        </div>
        <div className="bg-[#0a0a0a] border border-gray-900 p-3 rounded-2xl text-center">
          <DownloadCloud size={16} className="text-amber-500 mx-auto mb-1" />
          <p className="text-[7px] text-gray-500 font-bold uppercase">Exports</p>
          <p className="text-sm text-white font-black">{stats.export_count}</p>
        </div>
      </div>

      {/* Quick Action Button */}
      <button className="w-full bg-white text-black font-black py-4 rounded-2xl text-[10px] uppercase tracking-widest flex items-center justify-center gap-2 active:scale-95 transition-all shadow-[0_0_20px_rgba(255,255,255,0.1)]">
        <Zap size={14} fill="black" /> Emergency_Global_Export
      </button>
    </div>
  );
};

export default MasterDashboard;
