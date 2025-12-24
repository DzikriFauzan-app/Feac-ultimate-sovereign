
import React, { useState } from 'react';

const SovereignDashboard = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [installPath, setInstallPath] = useState('/data/data/com.termux/files/home/Feac-ultimate-sovereign/android');
  
  // Sidebar Menu Data
  const menuItems = [
    { id: 'dashboard', label: 'DASHBOARD', icon: '📊' },
    { id: 'emergent', label: 'EMERGENT THREATS', icon: '⚠️' },
    { id: 'chat', label: 'ARIES BRAIN', icon: '🧠' },
    { id: 'settings', label: 'SETTINGS', icon: '⚙️' }
  ];

  return (
    <div className="flex min-h-screen bg-[#020202] text-white font-sans overflow-hidden">
      {/* SIDEBAR: Desain Mahal & Pro */}
      <aside className="w-64 bg-[#080808] border-r border-white/5 flex flex-col shadow-2xl">
        <div className="p-6 border-b border-white/5">
          <h2 className="text-xl font-black tracking-tighter bg-gradient-to-r from-blue-500 to-emerald-400 bg-clip-text text-transparent">FEAC SOVEREIGN</h2>
          <p className="text-[10px] text-gray-600 font-mono tracking-widest mt-1">ACCESS: AUTHORIZED</p>
        </div>
        
        <nav className="flex-1 p-4 space-y-2 mt-4">
          {menuItems.map((item) => (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center gap-4 px-4 py-3 rounded-xl transition-all ${
                activeTab === item.id 
                ? 'bg-blue-600/10 border border-blue-500/30 text-blue-400 shadow-[0_0_15px_rgba(59,130,246,0.1)]' 
                : 'text-gray-500 hover:bg-white/5 hover:text-gray-300'
              }`}
            >
              <span className="text-lg">{item.icon}</span>
              <span className="text-xs font-bold tracking-widest">{item.label}</span>
            </button>
          ))}
        </nav>

        <div className="p-6 border-t border-white/5 text-center">
            <div className="text-[9px] text-gray-600 font-mono">PROTOCOL_STANDBY_V5.4</div>
        </div>
      </aside>

      {/* MAIN CONTENT AREA */}
      <main className="flex-1 p-8 overflow-y-auto">
        
        {/* TAB: DASHBOARD (Overview) */}
        {activeTab === 'dashboard' && (
          <div className="space-y-6 animate-in fade-in duration-500">
            <h3 className="text-2xl font-bold">System Overview</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-[#0f0f0f] p-6 rounded-2xl border border-white/5 shadow-xl">
                <p className="text-gray-500 text-[10px] uppercase font-bold tracking-widest">Revenue</p>
                <p className="text-3xl font-black text-emerald-400 mt-2">$1.2M</p>
              </div>
              <div className="bg-[#0f0f0f] p-6 rounded-2xl border border-white/5 shadow-xl">
                <p className="text-gray-500 text-[10px] uppercase font-bold tracking-widest">Active Nodes</p>
                <p className="text-3xl font-black text-blue-500 mt-2">4</p>
              </div>
              <div className="bg-[#0f0f0f] p-6 rounded-2xl border border-white/5 shadow-xl">
                <p className="text-gray-500 text-[10px] uppercase font-bold tracking-widest">Uptime</p>
                <p className="text-3xl font-black text-purple-500 mt-2">99.9%</p>
              </div>
            </div>
          </div>
        )}

        {/* TAB: EMERGENT THREATS */}
        {activeTab === 'emergent' && (
          <div className="space-y-6 animate-in slide-in-from-bottom-4 duration-500">
             <div className="flex items-center gap-3">
                <div className="w-3 h-3 bg-red-600 rounded-full animate-ping"></div>
                <h3 className="text-2xl font-bold text-red-500">Emergent Threats Center</h3>
             </div>
             <div className="bg-red-950/10 border border-red-900/30 p-8 rounded-3xl">
                <div className="space-y-4 font-mono">
                    <div className="flex justify-between p-4 bg-black/40 border border-red-500/20 rounded-xl">
                        <span className="text-red-400">AAPT2_INTERNAL_SYNTAX_ERROR</span>
                        <span className="text-red-600 font-black underline">PATCHING_NEEDED</span>
                    </div>
                    <div className="flex justify-between p-4 bg-black/40 border border-white/5 rounded-xl">
                        <span className="text-gray-400">UNAUTHORIZED_ACCESS_ATTEMPT</span>
                        <span className="text-yellow-500">BLOCKED</span>
                    </div>
                </div>
             </div>
          </div>
        )}

        {/* TAB: ARIES BRAIN (GPT STYLE) */}
        {activeTab === 'chat' && (
          <div className="flex flex-col h-full animate-in zoom-in-95 duration-500">
            <div className="bg-[#0f0f0f] border border-white/5 rounded-3xl flex-1 flex flex-col overflow-hidden shadow-2xl">
              <div className="p-4 bg-white/5 border-b border-white/5 font-bold text-xs tracking-[0.3em] text-blue-400">ARIES_COMM_CORE</div>
              <div className="flex-1 p-6 space-y-4 overflow-y-auto">
                <div className="bg-blue-600/10 border border-blue-500/20 p-4 rounded-2xl rounded-tl-none max-w-[80%] text-sm">
                  Identity Verified. Saya telah merombak desain Dashboard sesuai standar "Luxury Tech". Instruksi build AAPT2 siap diproses.
                </div>
              </div>
              <div className="p-6 bg-black/60 border-t border-white/5 backdrop-blur-xl">
                <div className="relative">
                  <input className="w-full bg-white/5 border border-white/10 rounded-2xl py-4 px-6 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all shadow-inner" placeholder="Ask anything to Aries Brain..." />
                  <button className="absolute right-3 top-2 bottom-2 bg-blue-600 px-4 rounded-xl font-bold text-xs">SEND</button>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* TAB: SETTINGS (Edit Path) */}
        {activeTab === 'settings' && (
          <div className="space-y-6 animate-in fade-in duration-500">
            <h3 className="text-2xl font-bold text-gray-400">System Preferences</h3>
            <div className="bg-[#0f0f0f] border border-white/5 p-8 rounded-3xl max-w-2xl">
              <label className="text-xs text-gray-600 uppercase font-black tracking-widest">Build Installation Path</label>
              <div className="mt-4 flex gap-3">
                <input 
                  value={installPath}
                  onChange={(e) => setInstallPath(e.target.value)}
                  className="flex-1 bg-black border border-white/10 rounded-xl px-4 py-3 text-xs font-mono text-emerald-500 focus:border-blue-500 outline-none transition-all" 
                />
                <button className="bg-white text-black px-6 rounded-xl font-bold text-xs hover:bg-emerald-400 transition-colors">SAVE</button>
              </div>
              <p className="mt-4 text-[10px] text-gray-700 italic">Pastikan path mengarah ke folder android yang memiliki file gradlew.</p>
            </div>
          </div>
        )}

      </main>
    </div>
  );
};

export default SovereignDashboard;
