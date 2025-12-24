import React, { useState, useEffect } from 'react';
import { API_URL } from './config';
import { Menu, X, Cpu, Zap, Terminal, Database, CreditCard, Brain, Box, Activity, Send, Plus, RefreshCw } from 'lucide-react';
import Dashboard from './components/Dashboard';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [ariesStatus, setAriesStatus] = useState('CONNECTING');
  
  // State untuk Chat (FEAC Brain)
  const [messages, setMessages] = useState([{ role: 'assistant', content: 'FEAC Brain Online. System Approved.' }]);
  const [chatInput, setChatInput] = useState('');
  
  // State untuk Emergent (Prompt)
  const [promptInput, setPromptInput] = useState('');
  const [outputStream, setOutputStream] = useState('>>> System ready. Waiting for prompt...');

  // Fungsi Kirim Chat (FEAC Brain)
  const handleSendChat = async () => {
    if (!chatInput.trim()) return;
    const newMsgs = [...messages, { role: 'user', content: chatInput }];
    setMessages(newMsgs);
    const currentInput = chatInput;
    setChatInput('');

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: currentInput })
      });
      const data = await res.json();
      setMessages([...newMsgs, { role: 'assistant', content: data.reply || 'No response from Aries.' }]);
    } catch (e) {
      setMessages([...newMsgs, { role: 'assistant', content: 'Error: Aries Bridge Unreachable.' }]);
    }
  };

  // Fungsi Eksekusi Prompt (Emergent)
  const handleExecutePrompt = async () => {
    if (!promptInput.trim()) return;
    setOutputStream(`>>> Executing: ${promptInput}\n...`);
    try {
      const res = await fetch(`${API_URL}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: promptInput })
      });
      const data = await res.json();
      setOutputStream(`>>> Result:\n${data.output}`);
    } catch (e) {
      setOutputStream(`>>> Error: Connection to Neo Engine failed.`);
    }
  };

  return (
    <div className="min-h-screen bg-black text-zinc-300 font-mono flex flex-col">
      <header className="p-4 border-b border-zinc-800 flex justify-between items-center bg-black sticky top-0 z-50">
        <button onClick={() => setIsMenuOpen(true)}><Menu size={24} /></button>
        <h1 className="text-xs font-bold tracking-[0.2em] text-white">FEAC SOVEREIGN</h1>
        <div className="text-[9px] text-green-500 font-bold">{ariesStatus}</div>
      </header>

      {/* Full Overlay Menu */}
      {isMenuOpen && (
        <div className="fixed inset-0 bg-black/98 z-[100] p-6 overflow-y-auto">
          <div className="flex justify-between items-center mb-8">
            <span className="text-zinc-600 text-[10px] tracking-widest">SOVEREIGN CORE</span>
            <button onClick={() => setIsMenuOpen(false)}><X size={28}/></button>
          </div>
          <div className="grid grid-cols-1 gap-3">
            {[
              { id: 'dashboard', label: 'DASHBOARD', icon: <Activity/> },
              { id: 'brain', label: 'FEAC BRAIN', icon: <Brain/> },
              { id: 'neogrid', label: 'NEO GRID', icon: <Database/> },
              { id: 'bridge', label: 'ENGINE BRIDGE', icon: <Zap/> },
              { id: 'emergent', label: 'EMERGENT', icon: <Send/> },
              { id: 'billing', label: 'BILLING', icon: <CreditCard/> },
            ].map((item) => (
              <button key={item.id} onClick={() => { setActiveTab(item.id); setIsMenuOpen(false); }} className={`flex items-center gap-4 p-4 border ${activeTab === item.id ? 'border-blue-500 text-white bg-blue-900/10' : 'border-zinc-900 text-zinc-700'}`}>
                {item.icon} <span className="text-xs font-bold">{item.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      <main className="flex-1 p-4 overflow-hidden">
        {activeTab === 'dashboard' && <Dashboard />}

        {activeTab === 'brain' && (
          <div className="flex flex-col h-full max-h-[80vh]">
            <div className="flex-1 overflow-y-auto space-y-4 mb-4">
              {messages.map((m, i) => (
                <div key={i} className={`p-3 text-xs ${m.role === 'user' ? 'bg-zinc-900 ml-8 border border-zinc-800' : 'bg-blue-950/20 mr-8 border-l-2 border-blue-500'}`}>
                  <div className="text-[8px] text-zinc-600 mb-1">{m.role.toUpperCase()}</div>
                  {m.content}
                </div>
              ))}
            </div>
            <div className="flex gap-2 bg-zinc-900 p-2 rounded-xl">
              <input 
                className="flex-1 bg-transparent outline-none text-xs px-2" 
                placeholder="Type message..." 
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSendChat()}
              />
              <button onClick={handleSendChat} className="text-blue-500"><Send size={20}/></button>
            </div>
          </div>
        )}

        {activeTab === 'emergent' && (
          <div className="flex flex-col gap-4 h-full">
            <div className="flex-1 border border-zinc-800 p-4 rounded bg-zinc-900/10 flex flex-col">
              <span className="text-[10px] text-blue-500 mb-2">PROMPT</span>
              <textarea 
                className="flex-1 bg-transparent outline-none text-xs resize-none" 
                value={promptInput}
                onChange={(e) => setPromptInput(e.target.value)}
                placeholder="Enter command..."
              />
              <button onClick={handleExecutePrompt} className="mt-2 bg-blue-600 text-white py-2 text-[10px] font-bold">EXECUTE</button>
            </div>
            <div className="h-1/3 bg-black border border-zinc-800 p-3 text-[10px] text-green-600 overflow-y-auto font-mono">
              <pre>{outputStream}</pre>
            </div>
          </div>
        )}

        {activeTab === 'bridge' && (
          <div className="flex flex-col items-center justify-center h-64 border border-zinc-800 rounded-lg">
            <button className="bg-white text-black p-4 rounded-full hover:scale-110 transition-transform shadow-[0_0_20px_rgba(255,255,255,0.3)]">
              <Plus size={32} />
            </button>
            <span className="mt-4 text-[10px] text-zinc-500 tracking-widest">ADD NEW ENGINE</span>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
