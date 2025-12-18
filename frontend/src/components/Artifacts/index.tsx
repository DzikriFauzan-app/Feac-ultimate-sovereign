import { Terminal, Check, X, PencilLine, ShieldAlert, Download } from 'lucide-react';

const Artifacts = () => {
  const [designPrompt, setDesignPrompt] = useState('');
  const [proposals] = useState([
    { 
      id: 'PATCH-01', 
      name: 'neural_bridge_fix.ts', 
      content: '// Automated Patch for Neural Bridge\nexport const fix = () => { console.log("System Fixed"); };',
      desc: 'Optimasi alokasi memori pada Termux internal bridge.' 
    }
  ]);

  // WORKFLOW: DOWNLOAD ARTIFACTS
  const downloadArtifact = (fileName: string, content: string) => {
    const element = document.createElement("a");
    const file = new Blob([content], {type: 'text/plain'});
    element.href = URL.createObjectURL(file);
    element.download = fileName;
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
  };

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
          className="w-full bg-black/60 border border-gray-800 p-4 rounded-2xl text-xs text-white outline-none focus:border-red-900/50 min-h-[100px]" 
          placeholder="Dikte instruksi perbaikan spesifik di sini..."
        />
      </div>

      {/* DOWNLOADABLE PROPOSALS */}
      <div className="space-y-4">
        <p className="text-[10px] font-black text-gray-700 uppercase tracking-widest px-2">Proposed Artifacts</p>
        {proposals.map((p) => (
          <div key={p.id} className="bg-black/40 border border-gray-800 p-5 rounded-3xl flex flex-col space-y-4">
            <div className="flex justify-between items-start">
              <div className="flex-1">
                <p className="text-[10px] text-blue-500 font-black mb-1 font-mono uppercase">{p.id} | {p.name}</p>
                <p className="text-sm font-bold text-white tracking-tight leading-tight italic">{p.desc}</p>
              </div>
              <button 
                onClick={() => downloadArtifact(p.name, p.content)}
                className="p-3 bg-blue-600/10 text-blue-400 rounded-2xl border border-blue-500/20 active:scale-90 transition-all shadow-lg shadow-blue-900/10"
              >
                <Download className="w-5 h-5" />
              </button>
            </div>
            
            <div className="flex space-x-2 pt-2 border-t border-gray-900">
              <button className="flex-1 bg-emerald-600 text-white py-2.5 rounded-xl text-[10px] font-black uppercase flex items-center justify-center transition-all active:scale-95"><Check className="w-3 h-3 mr-2" /> Approve</button>
              <button className="flex-1 bg-gray-800 text-gray-500 py-2.5 rounded-xl text-[10px] font-black uppercase flex items-center justify-center transition-all active:scale-95"><X className="w-3 h-3 mr-2" /> Reject</button>
            </div>
          </div>
        ))}
      </div>

      {/* SYSTEM LOGS */}
      <div className="bg-black/80 rounded-2xl p-4 border border-gray-900">
        <div className="flex items-center space-x-2 mb-2 opacity-50 font-mono">
           <Terminal className="w-3 h-3 text-gray-400" />
           <span className="text-[9px] uppercase font-bold tracking-widest">System Activity Log</span>
        </div>
        <div className="h-24 overflow-y-auto space-y-1 custom-scrollbar font-mono text-[9px] text-gray-600">
           <p>&gt; [SYSTEM] Awaiting Sovereign instructions...</p>
           <p>&gt; [ID] Artifact patched for download protocol.</p>
        </div>
      </div>
    </div>
  );
};
export default Artifacts;
