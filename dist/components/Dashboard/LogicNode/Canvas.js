"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const SovereignSound_1 = require("../../../utils/SovereignSound");
const STORAGE_KEY = 'SOVEREIGN_NODE_LAYOUT';
const Canvas = () => {
    const [nodes, setNodes] = (0, react_1.useState)([
        { id: 1, type: 'Trigger', x: 20, y: 100, label: 'ON_START', color: 'border-blue-500' },
        { id: 2, type: 'Condition', x: 180, y: 150, label: 'IF_RAM_>_80%', color: 'border-amber-500' },
        { id: 3, type: 'Action', x: 340, y: 250, label: 'SEND_SHELL_ALERT', color: 'border-emerald-500' }
    ]);
    const [draggingNode, setDraggingNode] = (0, react_1.useState)(null);
    const canvasRef = (0, react_1.useRef)(null);
    // LOAD: Ambil data saat komponen pertama kali dimuat
    (0, react_1.useEffect)(() => {
        const savedLayout = localStorage.getItem(STORAGE_KEY);
        if (savedLayout) {
            setNodes(JSON.parse(savedLayout));
        }
    }, []);
    // SAVE: Simpan ke LocalStorage setiap kali nodes berubah
    (0, react_1.useEffect)(() => {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(nodes));
    }, [nodes]);
    const handleGrab = (id) => {
        SovereignSound_1.sfx.playGrab();
        setDraggingNode(id);
    };
    const handleTouchMove = (e) => {
        if (draggingNode === null || !canvasRef.current)
            return;
        const touch = e.touches[0];
        const rect = canvasRef.current.getBoundingClientRect();
        const x = touch.clientX - rect.left - 64;
        const y = touch.clientY - rect.top - 20;
        setNodes(prev => prev.map(node => node.id === draggingNode ? { ...node, x, y } : node));
    };
    const resetLayout = () => {
        if (confirm("Reset Arsitektur Node?")) {
            localStorage.removeItem(STORAGE_KEY);
            window.location.reload();
        }
    };
    const runLogic = async () => {
        SovereignSound_1.sfx.playInitialize();
        try {
            const response = await fetch('http://10.159.189.152:8080/api/logic/run', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    nodes: nodes.map(n => ({
                        type: n.id === 2 ? 'if_ram_high' : 'print_log',
                        data: n.label
                    }))
                })
            });
            const result = await response.json();
            alert("Sovereign Intelligence: \n" + result.details.join('\n'));
        }
        catch (e) {
            alert("⚠️ Engine Offline. Pastikan neo.sh berjalan.");
        }
    };
    return (<div ref={canvasRef} onTouchMove={handleTouchMove} onTouchEnd={() => setDraggingNode(null)} className="relative w-full h-[550px] bg-[#050505] bg-[radial-gradient(#1a1a1a_1px,transparent_1px)] [background-size:25px_25px] overflow-hidden rounded-2xl border border-gray-900 touch-none">
      <div className="absolute top-4 left-4 z-20 flex gap-2">
        <button onClick={runLogic} className="flex items-center gap-2 bg-blue-600 text-[10px] font-bold px-4 py-2 rounded-full shadow-lg active:scale-95 transition-all">
          <lucide_react_1.Activity size={12}/> RUN
        </button>
        <button onClick={resetLayout} className="flex items-center gap-2 bg-zinc-900 text-[10px] font-bold px-4 py-2 rounded-full border border-zinc-800 active:scale-95">
          <lucide_react_1.RefreshCw size={12}/> RESET
        </button>
      </div>

      <div className="absolute top-4 right-4 z-20">
        <div className="flex items-center gap-1 text-[8px] text-emerald-500 font-mono bg-emerald-500/10 px-2 py-1 rounded-md border border-emerald-500/20">
          <lucide_react_1.Save size={8}/> AUTO_SAVE_ACTIVE
        </div>
      </div>

      {nodes.map((node) => (<div key={node.id} onTouchStart={() => handleGrab(node.id)} className={`absolute bg-[#0a0a0a]/90 backdrop-blur-md border-2 ${node.color} ${draggingNode === node.id ? 'scale-110 z-30 shadow-[0_0_30px_rgba(59,130,246,0.2)]' : 'z-10 shadow-xl'} p-3 rounded-xl w-36 transition-all duration-75`} style={{ left: node.x, top: node.y, touchAction: 'none' }}>
          <div className="text-[7px] text-gray-500 font-mono mb-1 tracking-[0.2em]">{node.type.toUpperCase()}</div>
          <div className="text-[11px] text-white font-black">{node.label}</div>
        </div>))}
      
      <svg className="absolute inset-0 pointer-events-none w-full h-full opacity-20">
        <path d={`M ${nodes[0].x + 140} ${nodes[0].y + 40} L ${nodes[1].x} ${nodes[1].y + 40}`} stroke="white" strokeWidth="0.5" fill="none"/>
        <path d={`M ${nodes[1].x + 140} ${nodes[1].y + 40} L ${nodes[2].x} ${nodes[2].y + 40}`} stroke="white" strokeWidth="0.5" fill="none"/>
      </svg>
    </div>);
};
exports.default = Canvas;
