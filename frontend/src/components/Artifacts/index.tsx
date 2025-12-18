import React, { useState } from 'react';
import { Cpu, Terminal, Check, X, PencilLine, ShieldAlert } from 'lucide-react';

const Artifacts = () => {
  const [designPrompt, setDesignPrompt] = useState('');
  const logs = ['[SYSTEM] Artifacts Secure Access Verified', '[AUTO] Checking core integrity...', '[WARN] 2 minor optimizations found'];

  return (
    <div className="p-5 pb-24 space-y-6 animate-in slide-in-from-top-4">
      <div className="bg-[#1a0f0f] border border-red-900/30 p-6 rounded-3xl relative overflow-hidden">
        <h2 className="text-xl font-black text-white italic uppercase flex items-center">
          <ShieldAlert className="mr-2 text-red-500 w-5 h-5 animate-pulse" /> Internal Evolution
        </h2>
        <p className="text-[10px] text-red-400 font-mono mt-1 uppercase tracking-widest font-bold">Owner Access Only</p>
      </div>

      {/* PROMPT DESAIN SPESIFIK */}
      <div className="bg-[#111821] border border-gray-800 p-5 rounded-3xl space-y-4">
        <div className="flex items-center space-x-2 text-blue-400">
           <PencilLine className="w-4 h-4" />
           <span className="text-[10px] font-black uppercase tracking-widest">System Repair Design Prompt</span>
        </div>
        <textarea 
          value={designPrompt}
          onChange={(e) => setDesignPrompt(e.target.value)}
          className="w-full bg-black/60 border border-gray-800 p-4 rounded-2xl text-xs text-white outline-none focus:border-red-900/50 min-h-[120px]" 
          placeholder="Describe specific design changes or internal fixes (e.g. 'Redesign the neural bus structure to use async buffer v2')..."
        />
        <div className="flex space-x-2">
           <button className="flex-1 bg-red-600 text-white py-3 rounded-xl text-[10px] font-black uppercase active:scale-95 transition-all">Request Proposal</button>
        </div>
      </div>

      {/* APPROVAL QUEUE */}
      <div className="space-y-4">
        <p className="text-[10px] font-black text-gray-700 uppercase tracking-widest px-2">Pending Engine Projections</p>
        <div className="bg-black/40 border border-gray-800 p-5 rounded-3xl flex flex-col space-y-4">
            <div className="flex justify-between items-start">
              <p className="text-sm font-bold text-white tracking-tight leading-tight italic">Improve memory allocation for Termux bridge internal port.</p>
              <span className="text-[8px] bg-blue-900/20 text-blue-400 px-2 py-1 rounded-md font-black">AUTO-GEN</span>
            </div>
            <div className="flex space-x-2 pt-2">
              <button className="flex-1 bg-emerald-600 text-white py-2.5 rounded-xl text-[10px] font-black uppercase flex items-center justify-center"><Check className="w-3 h-3 mr-2" /> Approve</button>
              <button className="flex-1 bg-gray-800 text-gray-500 py-2.5 rounded-xl text-[10px] font-black uppercase flex items-center justify-center"><X className="w-3 h-3 mr-2" /> Reject</button>
            </div>
        </div>
      </div>

      {/* LOGS */}
      <div className="bg-black/80 rounded-2xl p-4 border border-gray-900">
        <div className="flex items-center space-x-2 mb-2 opacity-50 font-mono">
           <Terminal className="w-3 h-3 text-gray-400" />
           <span className="text-[9px] uppercase font-bold tracking-widest">System Activity Log</span>
        </div>
        <div className="space-y-1">
           {logs.map((l, i) => <p key={i} className="text-[10px] font-mono text-gray-600 italic tracking-tighter">&gt; {l}</p>)}
        </div>
      </div>
    </div>
  );
};
export default Artifacts;
