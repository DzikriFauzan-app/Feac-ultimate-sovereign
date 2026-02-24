"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = __importStar(require("react"));
const lucide_react_1 = require("lucide-react");
const Dashboard = () => {
    const [key, setKey] = (0, react_1.useState)('');
    const [status, setStatus] = (0, react_1.useState)('RESTRICTED MODE ACTIVE');
    const [accessLevel, setAccessLevel] = (0, react_1.useState)('UNAUTHORIZED');
    const [isGodMode, setIsGodMode] = (0, react_1.useState)(false);
    const handleSovereignEntry = async () => {
        try {
            const response = await fetch('http://10.159.189.152:3000/api/validate-key', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ key })
            });
            const result = await response.json();
            if (result.success) {
                setStatus('IDENTITY VERIFIED');
                setAccessLevel(result.data.access_level);
                setIsGodMode(result.data.access_level === 'GOD_MODE');
                console.log("⚡ GOD MODE ACTIVATED");
            }
            else {
                alert("ACCESS DENIED: INVALID SUPERKEY");
            }
        }
        catch (error) {
            console.error("Bridge Error:", error);
            alert("BRIDGE CONNECTION FAILED - CHECK TERMUX");
        }
    };
    return (<div className="p-6 space-y-6 bg-[#0a0f14] min-h-screen text-white">
      {/* HEADER STATUS */}
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

      {/* SUPERKEY INPUT PANEL */}
      <div className={`p-6 rounded-2xl border transition-all duration-700 ${isGodMode ? 'bg-emerald-950/20 border-emerald-500/50' : 'bg-[#111821] border-gray-800'}`}>
        <div className="flex items-center space-x-3 mb-4">
          <lucide_react_1.ShieldCheck className={isGodMode ? 'text-emerald-500' : 'text-gray-600'} size={20}/>
          <div>
            <h2 className="text-xs font-black uppercase tracking-widest">{isGodMode ? 'SOVEREIGN ACCESS GRANTED' : 'SUPERKEY REQUIRED'}</h2>
            <p className="text-[9px] text-gray-500 uppercase font-mono">{status}</p>
          </div>
        </div>

        {!isGodMode && (<div className="relative flex items-center">
            <input type="password" value={key} onChange={(e) => setKey(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && handleSovereignEntry()} placeholder="ENTER ENCRYPTED KEY..." className="w-full bg-black/40 border border-gray-800 rounded-xl py-4 px-5 text-sm font-mono tracking-[0.5em] focus:border-blue-500 outline-none transition-all"/>
            <button onClick={handleSovereignEntry} className="absolute right-2 p-3 bg-blue-600 rounded-lg hover:bg-blue-500 active:scale-90 transition-all">
              <lucide_react_1.ArrowRight size={18}/>
            </button>
          </div>)}
      </div>

      {/* STATS GRID */}
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-[#111821] p-5 rounded-2xl border border-gray-800">
          <p className="text-[10px] font-bold text-gray-500 uppercase tracking-widest flex items-center gap-2"><lucide_react_1.Activity size={12}/> Revenue</p>
          <p className="text-2xl font-black text-emerald-500 mt-2">$1.2M</p>
        </div>
        <div className="bg-[#111821] p-5 rounded-2xl border border-gray-800">
          <p className="text-[10px] font-bold text-gray-500 uppercase tracking-widest flex items-center gap-2"><lucide_react_1.Database size={12}/> Nodes</p>
          <p className="text-2xl font-black text-blue-500 mt-2">4 <span className="text-[10px] font-normal text-blue-400 italic">ACTIVE</span></p>
        </div>
      </div>
    </div>);
};
exports.default = Dashboard;
