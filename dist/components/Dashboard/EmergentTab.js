"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const EmergentTab = () => {
    const [proposals, setProposals] = (0, react_1.useState)([]);
    const [isScanning, setIsScanning] = (0, react_1.useState)(false);
    const scanRepo = async () => {
        setIsScanning(true);
        try {
            const res = await fetch('http://10.4.35.107:3000/api/emergent/scan');
            const json = await res.json();
            setProposals(json.data);
        }
        catch (err) {
            console.error("Scan failed:", err);
        }
        finally {
            setIsScanning(false);
        }
    };
    const handleApprove = async (issue) => {
        try {
            await fetch('http://10.4.35.107:3000/api/emergent/approve', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ issue })
            });
            scanRepo();
        }
        catch (err) {
            console.error("Approval failed:", err);
        }
    };
    return (<div className="p-4 space-y-4 font-mono">
      <div className="flex justify-between items-center border-b border-gray-800 pb-2">
        <h3 className="text-blue-500 font-black text-[10px] uppercase tracking-widest">Emergent Engine</h3>
        <button onClick={scanRepo} className="p-2 bg-blue-600/20 text-blue-400 rounded-md">
          <lucide_react_1.RefreshCw size={14} className={isScanning ? 'animate-spin' : ''}/>
        </button>
      </div>

      <div className="space-y-3">
        {proposals.map((p) => (<div key={p.id} className="bg-[#111821] p-4 rounded-xl border border-gray-800">
            <div className="flex justify-between">
              <span className="text-[10px] bg-red-500/10 text-red-500 px-2 py-0.5 rounded">{p.type}</span>
              <span className="text-gray-500 text-[10px]">{p.file}</span>
            </div>
            <p className="text-[11px] text-white mt-2 italic">{p.desc}</p>
            <div className="flex gap-2 mt-4">
              <button onClick={() => handleApprove(p)} className="flex-1 py-2 bg-emerald-600/20 text-emerald-500 rounded-lg text-[9px] font-black uppercase flex items-center justify-center gap-2">
                <lucide_react_1.CheckCircle size={12}/> Approve
              </button>
              <button className="flex-1 py-2 bg-red-600/20 text-red-500 rounded-lg text-[9px] font-black uppercase flex items-center justify-center gap-2">
                <lucide_react_1.XCircle size={12}/> Refuse
              </button>
            </div>
          </div>))}
        {proposals.length === 0 && !isScanning && (<p className="text-[10px] text-gray-600 text-center py-10 uppercase tracking-widest">No Active Proposals</p>)}
      </div>
    </div>);
};
exports.default = EmergentTab;
