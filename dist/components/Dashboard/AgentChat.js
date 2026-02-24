"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const SovereignSound_1 = require("../../utils/SovereignSound");
const AgentChat = () => {
    const [target, setTarget] = (0, react_1.useState)('AssetAgent');
    const [msg, setMsg] = (0, react_1.useState)('');
    const [history, setHistory] = (0, react_1.useState)([]);
    const sendChat = async () => {
        if (!msg)
            return;
        SovereignSound_1.sfx.playGrab();
        const userMsg = { role: 'MASTER', text: msg };
        setHistory(prev => [...prev, userMsg]);
        try {
            const res = await fetch('http://10.159.189.152:8080/api/agent/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ agent: target, message: msg })
            });
            const data = await res.json();
            if (data.status === 'spawned') {
                SovereignSound_1.sfx.playInitialize(); // Suara "Kelahiran" Agen
            }
            setHistory(prev => [...prev, {
                    role: target.toUpperCase(),
                    text: data.reply,
                    type: data.status
                }]);
        }
        catch {
            setHistory(prev => [...prev, { role: 'SYSTEM', text: 'CONNECTION_LOST' }]);
        }
        setMsg('');
    };
    return (<div className="bg-[#050505] border border-gray-900 rounded-3xl p-5 mt-4 flex flex-col h-[450px] shadow-2xl">
      <div className="flex justify-between items-center mb-4 pb-2 border-b border-gray-900">
        <div className="flex items-center gap-2">
           <lucide_react_1.UserCog size={14} className="text-blue-500"/>
           <input className="bg-transparent text-[10px] text-white font-black outline-none w-32 uppercase tracking-widest" value={target} onChange={(e) => setTarget(e.target.value)} placeholder="AGENT_NAME"/>
        </div>
        <lucide_react_1.Sparkles size={14} className="text-emerald-500 animate-pulse"/>
      </div>

      <div className="flex-1 overflow-y-auto space-y-3 mb-4 pr-2 scrollbar-hide">
        {history.map((chat, i) => (<div key={i} className={`text-[10px] p-3 rounded-2xl ${chat.role === 'MASTER'
                ? 'bg-blue-600/10 ml-10 border border-blue-500/20'
                : 'bg-zinc-900/50 mr-10 border border-emerald-500/20'} ${chat.type === 'spawned' ? 'border-amber-500/50 bg-amber-500/5' : ''}`}>
            <span className="block text-[7px] font-black opacity-40 mb-1 tracking-tighter">
              {chat.role} {chat.type === 'spawned' && '— SYNTHESIZING...'}
            </span>
            <p className="leading-relaxed text-gray-200">{chat.text}</p>
          </div>))}
      </div>

      <div className="flex gap-2 bg-black p-1 rounded-2xl border border-gray-800">
        <input value={msg} onChange={(e) => setMsg(e.target.value)} onKeyDown={(e) => e.key === 'Enter' && sendChat()} placeholder="COMMAND_AGENT_..." className="flex-1 bg-transparent px-4 py-2 text-[10px] text-white outline-none"/>
        <button onClick={sendChat} className="bg-blue-600 p-2 rounded-xl hover:bg-blue-500 transition-colors">
          <lucide_react_1.Send size={16} className="text-white"/>
        </button>
      </div>
    </div>);
};
exports.default = AgentChat;
