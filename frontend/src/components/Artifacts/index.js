"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const Artifacts = () => {
    const [designPrompt, setDesignPrompt] = (0, react_1.useState)('');
    const [proposals] = (0, react_1.useState)([
        {
            id: 'PATCH-01',
            name: 'neural_bridge_fix.ts',
            content: '// Automated Patch for Neural Bridge\nexport const fix = () => { console.log("System Fixed"); };',
            desc: 'Optimasi alokasi memori pada Termux internal bridge.'
        }
    ]);
    const downloadArtifact = (fileName, content) => {
        const element = document.createElement("a");
        const file = new Blob([content], { type: 'text/plain' });
        element.href = URL.createObjectURL(file);
        element.download = fileName;
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    };
    return (<div className="p-5 pb-24 space-y-6">
      <div className="bg-[#1a0f0f] border border-red-900/30 p-6 rounded-3xl">
        <h2 className="text-xl font-black text-white italic uppercase flex items-center">
          <lucide_react_1.ShieldAlert className="mr-2 text-red-500 w-5 h-5 animate-pulse"/> Internal Evolution
        </h2>
      </div>
      <div className="bg-[#111821] border border-gray-800 p-5 rounded-3xl space-y-4">
        <textarea value={designPrompt} onChange={(e) => setDesignPrompt(e.target.value)} className="w-full bg-black/60 border border-gray-800 p-4 rounded-2xl text-xs text-white outline-none" placeholder="Dikte instruksi perbaikan..."/>
      </div>
      <div className="space-y-4">
        {proposals.map((p) => (<div key={p.id} className="bg-black/40 border border-gray-800 p-5 rounded-3xl flex flex-col space-y-4">
            <div className="flex justify-between items-start">
              <div className="flex-1">
                <p className="text-[10px] text-blue-500 font-black mb-1 font-mono uppercase">{p.id} | {p.name}</p>
                <p className="text-sm font-bold text-white italic">{p.desc}</p>
              </div>
              <button onClick={() => downloadArtifact(p.name, p.content)} className="p-3 bg-blue-600/10 text-blue-400 rounded-2xl"><lucide_react_1.Download className="w-5 h-5"/></button>
            </div>
          </div>))}
      </div>
    </div>);
};
exports.default = Artifacts;
