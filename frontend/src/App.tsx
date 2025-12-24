import React, { useState, useEffect } from 'react';
import { API_URL } from './config';
import { Menu, X, Cpu, Zap, Terminal, Database, CreditCard, Brain, Box, Activity, Send, RefreshCw } from 'lucide-react';
import { LiveUpdates } from '@capacitor/live-updates';
import Dashboard from './components/Dashboard';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [ariesStatus, setAriesStatus] = useState('CONNECTING');
  const [otaStatus, setOtaStatus] = useState('V5.3 - STABLE');

  // Logika Check OTA Update
  const checkUpdate = async () => {
    try {
      setOtaStatus('CHECKING OTA...');
      const result = await LiveUpdates.sync();
      if (result.next) {
        setOtaStatus('UPDATING...');
        await LiveUpdates.reload();
      } else {
        setOtaStatus('LATEST VERSION');
      }
    } catch (e) {
      setOtaStatus('STABLE');
    }
  };

  useEffect(() => {
    checkUpdate();
    const interval = setInterval(() => {
      fetch(`${API_URL}/status`)
        .then(res => res.ok ? setAriesStatus('APPROVED') : setAriesStatus('CONNECTED'))
        .catch(() => setAriesStatus('LOCAL_MODE'));
    }, 5000);
    return () => clearInterval(interval);
  }, []);

  const menuItems = [
    { id: 'dashboard', label: 'DASHBOARD', icon: <Activity size={18}/> },
    { id: 'brain', label: 'FEAC BRAIN', icon: <Brain size={18}/> },
    { id: 'neogrid', label: 'NEO GRID', icon: <Database size={18}/> },
    { id: 'emergent', label: 'EMERGENT', icon: <Send size={18}/> },
    { id: 'artifact', label: 'ARTIFACT', icon: <Cpu size={18}/> },
    { id: 'billing', label: 'BILLING', icon: <CreditCard size={18}/> },
  ];

  return (
    <div className="min-h-screen bg-black text-zinc-300 font-mono flex flex-col">
      <header className="p-4 border-b border-zinc-800 flex justify-between items-center bg-black sticky top-0 z-50">
        <button onClick={() => setIsMenuOpen(true)} className="p-1"><Menu size={24} /></button>
        <div className="flex flex-col items-center">
          <h1 className="text-[10px] font-bold tracking-[0.3em] text-white">FEAC SOVEREIGN</h1>
          <span className="text-[8px] text-zinc-600">{otaStatus}</span>
        </div>
        <div className="text-[9px] text-green-500 font-bold border border-green-900 px-2 py-0.5 rounded">{ariesStatus}</div>
      </header>

      {isMenuOpen && (
        <div className="fixed inset-0 bg-black/98 z-[100] p-6 animate-in slide-in-from-left">
          <div className="flex justify-between items-center mb-10 text-zinc-600">
            <button onClick={checkUpdate} className="flex items-center gap-2"><RefreshCw size={14}/> <span className="text-[8px]">SYNC OTA</span></button>
            <button onClick={() => setIsMenuOpen(false)} className="text-white"><X size={28}/></button>
          </div>
          <div className="grid grid-cols-1 gap-3">
            {menuItems.map((item) => (
              <button 
                key={item.id}
                onClick={() => { setActiveTab(item.id); setIsMenuOpen(false); }}
                className={`flex items-center gap-4 p-4 border ${activeTab === item.id ? 'border-blue-500 text-white bg-blue-900/10' : 'border-zinc-900 text-zinc-700'}`}
              >
                {item.icon}
                <span className="text-xs font-bold tracking-widest">{item.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      <main className="flex-1 p-4 overflow-hidden">
        {activeTab === 'dashboard' && <Dashboard />}
        {activeTab === 'brain' && (
           <div className="flex flex-col h-full bg-zinc-950/50 rounded-t-3xl border-t border-zinc-800 p-4">
              <div className="flex-1 overflow-y-auto mb-4 space-y-4">
                 <div className="bg-blue-900/10 p-3 rounded-lg border-l-2 border-blue-500 text-[11px]">
                    System initialized. Standing by for command...
                 </div>
              </div>
              <div className="flex gap-2 bg-zinc-900 p-2 rounded-xl">
                 <input className="flex-1 bg-transparent outline-none text-xs px-2" placeholder="Send prompt..." />
                 <button className="text-blue-500"><Send size={18}/></button>
              </div>
           </div>
        )}
        {/* Placeholder tab lainnya agar build aman */}
        {!['dashboard', 'brain'].includes(activeTab) && (
          <div className="flex flex-col items-center justify-center h-full opacity-30 border border-dashed border-zinc-800">
            <span className="text-[10px] tracking-widest">{activeTab.toUpperCase()} MODULE LOADED</span>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
