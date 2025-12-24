import React, { useState } from 'react';
import { API_URL } from './config';
import Dashboard from './components/Dashboard';
import { Zap, Terminal, Database, CreditCard, Brain, Box, Activity } from 'lucide-react';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');

  return (
    <div className="min-h-screen bg-black text-white font-mono">
      {/* Header & Status */}
      <div className="p-4 border-b border-zinc-800 flex justify-between items-center">
        <h1 className="text-xl italic font-bold tracking-tighter">FEAC SOVEREIGN</h1>
        <div className="text-[10px] text-green-500 animate-pulse">OWNER ACCESS</div>
      </div>

      {/* Navigation Menu */}
      <div className="flex overflow-x-auto gap-2 p-2 bg-zinc-900/50 no-scrollbar">
        {['dashboard', 'repo', 'neogrid', 'bridge', 'termux', 'billing', 'artifact', 'brain', 'emergent'].map((tab) => (
          <button 
            key={tab}
            onClick={() => setActiveTab(tab)}
            className={`px-3 py-1 text-xs border ${activeTab === tab ? 'bg-white text-black border-white' : 'border-zinc-700 text-zinc-500'}`}
          >
            {tab.toUpperCase()}
          </button>
        ))}
      </div>

      {/* Content Area */}
      <div className="p-4">
        {activeTab === 'dashboard' && <Dashboard />}
        {activeTab === 'emergent' && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="border border-zinc-800 p-4">
              <h3 className="text-blue-500 mb-2">PROMPT</h3>
              <textarea className="w-full bg-transparent border-none focus:ring-0 text-sm" rows={10} placeholder="Input command..."></textarea>
            </div>
            <div className="border border-zinc-800 p-4 bg-zinc-900/20">
              <h3 className="text-green-500 mb-2">OUTPUT</h3>
              <div className="text-xs text-zinc-400">Waiting for execution...</div>
            </div>
          </div>
        )}
        {/* Tab lainnya akan merender konten minimalis agar build sukses */}
        {!['dashboard', 'emergent'].includes(activeTab) && (
          <div className="p-20 text-center text-zinc-700 border border-dashed border-zinc-800">
            {activeTab.toUpperCase()} MODULE ACTIVE
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
