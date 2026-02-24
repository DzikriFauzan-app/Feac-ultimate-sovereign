"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const SovereignSound_1 = require("../../utils/SovereignSound");
const ProjectCreator = () => {
    const [loading, setLoading] = (0, react_1.useState)(false);
    const gameTypes = [
        { id: 'INIT_PERFECT_WORLD', name: '3D RPG (Perfect World)', icon: <lucide_react_1.Sword />, color: 'text-red-500' },
        { id: 'INIT_SUDOKU', name: '2D Logic (Sudoku)', icon: <lucide_react_1.LayoutGrid />, color: 'text-blue-500' },
        { id: 'INIT_FARM', name: 'Simulation (Farmville)', icon: <lucide_react_1.Wheat />, color: 'text-emerald-500' },
        { id: 'INIT_TOWER_DEFENSE', name: 'Strategy (Tower Defense)', icon: <lucide_react_1.Box />, color: 'text-amber-500' },
    ];
    const handleCreate = async (type, name) => {
        SovereignSound_1.sfx.playInitialize();
        setLoading(true);
        try {
            const res = await fetch('http://10.159.189.152:8080/api/task/execute', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ project: name, type: type, desc: `Inisialisasi Proyek ${name}` })
            });
            const data = await res.json();
            alert(data.result || "Project Created!");
        }
        catch (err) {
            alert("NeoEngine Offline!");
        }
        setLoading(false);
    };
    return (<div className="p-6 bg-[#050505] rounded-3xl border border-gray-900 mt-4">
      <h3 className="text-white font-black text-sm mb-4 tracking-widest uppercase flex items-center gap-2">
        <lucide_react_1.PlusCircle size={16} className="text-blue-500"/> Spawn_New_Multiverse
      </h3>
      
      <div className="grid grid-cols-2 gap-3">
        {gameTypes.map((game) => (<button key={game.id} onClick={() => handleCreate(game.id, prompt("Nama Proyek?") || "NewGame")} disabled={loading} className="flex flex-col items-center justify-center p-4 bg-[#0a0a0a] border border-gray-800 rounded-2xl hover:border-blue-500 transition-all active:scale-95 group">
            <div className={`${game.color} mb-2 group-hover:scale-110 transition-transform`}>
              {game.icon}
            </div>
            <span className="text-[9px] text-gray-400 font-bold text-center uppercase tracking-tighter">
              {game.name}
            </span>
          </button>))}
      </div>
    </div>);
};
exports.default = ProjectCreator;
