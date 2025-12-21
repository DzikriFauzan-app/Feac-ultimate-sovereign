import { useState } from 'react';
import { ShieldCheck, ArrowRight, Activity, Database } from 'lucide-react';

const Dashboard = () => {
  const [key, setKey] = useState('');
  const [status, setStatus] = useState('RESTRICTED MODE ACTIVE');
  const [accessLevel, setAccessLevel] = useState('UNAUTHORIZED');
  const [isGodMode, setIsGodMode] = useState(false);

  const handleSovereignEntry = async () => {
    try {
      const response = await fetch('http://10.4.35.107:3000/api/validate-key', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ key })
      });

      const result = await response.json();

      if (result.success) {
        setStatus('IDENTITY VERIFIED');
        setAccessLevel(result.data.access_level);
        setIsGodMode(result.data.access_level === 'GOD_MODE');
      } else {
        alert("ACCESS DENIED");
      }
    } catch (error) {
      alert("BRIDGE CONNECTION FAILED");
    }
  };

  return (
    <div className="p-6 space-y-6 bg-[#0a0f14] min-h-screen text-white">
      <div className="flex justify-between items-start">
        <div>
          <h1 className="text-3xl font-black italic tracking-tighter">DASHBOARD <span className="text-blue-500 underline">V5.3</span></h1>
          <p className="text-[10px] font-mono text-gray-500 uppercase tracking-widest">Protocol: {isGodMode ? 'GOD_MODE_ACTIVE' : 'STANDBY'}</p>
        </div>
        <div className="text-right">
          <p className="text-[10px] font-bold text-gray-400 uppercase">Access Level</p>
          <p className={`text-sm font-black uppercase tracking-tighter ${isGodMode ? 'text-yellow-500' : 'text-red-500'}`}>
            {isGodMode ? '👑 GOD MODE' : accessLevel}
          </p>
        </div>
      </div>

      <div className={`p-6 rounded-2xl border transition-all duration-700 ${isGodMode ? 'bg-emerald-950/20 border-emerald-500/50' : 'bg-[#111821] border-gray-800'}`}>
        {!isGodMode && (
          <div className="relative flex items-center">
            <input 
              type="password"
              value={key}
              onChange={(e) => setKey(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSovereignEntry()}
              placeholder="ENTER ENCRYPTED KEY..."
              className="w-full bg-black/40 border border-gray-800 rounded-xl py-4 px-5 text-sm font-mono tracking-[0.5em] focus:border-blue-500 outline-none transition-all"
            />
            <button 
              onClick={handleSovereignEntry}
              className="absolute right-2 p-3 bg-blue-600 rounded-lg hover:bg-blue-500 active:scale-90 transition-all"
            >
              <ArrowRight size={18} />
            </button>
          </div>
        )}
        {isGodMode && (
          <div className="flex items-center space-x-3">
             <ShieldCheck className="text-emerald-500" size={20} />
             <div>
               <h2 className="text-xs font-black uppercase tracking-widest text-emerald-400">SOVEREIGN ACCESS GRANTED</h2>
               <p className="text-[9px] text-gray-500 uppercase font-mono">{status}</p>
             </div>
          </div>
        )}
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div className="bg-[#111821] p-5 rounded-2xl border border-gray-800">
          <p className="text-[10px] font-bold text-gray-500 uppercase tracking-widest flex items-center gap-2"><Activity size={12}/> Revenue</p>
          <p className="text-2xl font-black text-emerald-500 mt-2">$1.2M</p>
        </div>
        <div className="bg-[#111821] p-5 rounded-2xl border border-gray-800">
          <p className="text-[10px] font-bold text-gray-500 uppercase tracking-widest flex items-center gap-2"><Database size={12}/> Nodes</p>
          <p className="text-2xl font-black text-blue-500 mt-2">4 <span className="text-[10px] font-normal text-blue-400 italic">ACTIVE</span></p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
