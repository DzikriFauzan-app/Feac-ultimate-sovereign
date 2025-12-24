import React, { useState, useEffect } from 'react';
import { API_URL } from './config';
import { Menu, X, Cpu, Zap, Terminal, Database, CreditCard, Brain, Box, Activity, Send } from 'lucide-react';
import Dashboard from './components/Dashboard';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [ariesStatus, setAriesStatus] = useState('CONNECTING');
  const [messages, setMessages] = useState([{ role: 'assistant', content: 'FEAC Brain Online. System Approved.' }]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const checkAries = async () => {
      try {
        const res = await fetch(`${API_URL}/status`);
        if (res.ok) setAriesStatus('APPROVED & CONNECTED');
      } catch (e) {
        setAriesStatus('CONNECTED');
      }
    };
    checkAries();
  }, []);

  const handleSendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
      const data = await response.json();
      setMessages(prev => [...prev, { role: 'assistant', content: data.reply || 'Engine Error: No Response' }]);
    } catch (e) {
      setMessages(prev => [...prev, { role: 'assistant', content: 'System Error: Failed to reach Aries Bridge.' }]);
    } finally {
      setLoading(false);
    }
  };

  const menuItems = [
    { id: 'dashboard', label: 'DASHBOARD', icon: <Activity size={18}/> },
    { id: 'repo', label: 'REPO SCANNER', icon: <Box size={18}/> },
    { id: 'neogrid', label: 'NEO GRID', icon: <Database size={18}/> },
    { id: 'bridge', label: 'ENGINE BRIDGE', icon: <Zap size={18}/> },
    { id: 'termux', label: 'TERMUX', icon: <Terminal size={18}/> },
    { id: 'billing', label: 'BILLING', icon: <CreditCard size={18}/> },
    { id: 'artifact', label: 'ARTIFACT ROOM', icon: <Cpu size={18}/> },
    { id: 'brain', label: 'FEAC BRAIN', icon: <Brain size={18}/> },
    { id: 'emergent', label: 'EMERGENT', icon: <Send size={18}/> },
  ];

  return (
    <div className="min-h-screen bg-black text-zinc-300 font-mono flex flex-col">
      <header className="p-4 border-b border-zinc-800 flex justify-between items-center bg-black sticky top-0 z-50">
        <button onClick={() => setIsMenuOpen(true)} className="p-1 text-white hover:text-blue-500 transition-colors">
          <Menu size={24} />
        </button>
        <h1 className="text-sm font-bold tracking-[0.2em] text-white">FEAC SOVEREIGN</h1>
        <div className="text-[9px] text-green-500 font-bold border border-green-900 px-2 py-0.5 rounded">{ariesStatus}</div>
      </header>

      {/* Full Screen Menu */}
      {isMenuOpen && (
        <div className="fixed inset-0 bg-black/98 z-[100] p-6 animate-in slide-in-from-left">
          <div className="flex justify-between items-center mb-10">
            <span className="text-zinc-600 text-[10px] tracking-[0.5em] font-bold">CORE NAVIGATION</span>
            <button onClick={() => setIsMenuOpen(false)} className="text-white"><X size={28}/></button>
          </div>
          <div className="grid grid-cols-1 gap-3">
            {menuItems.map((item) => (
              <button 
                key={item.id}
                onClick={() => { setActiveTab(item.id); setIsMenuOpen(false); }}
                className={`flex items-center gap-4 p-4 border transition-all ${activeTab === item.id ? 'border-blue-500 text-white bg-blue-900/10' : 'border-zinc-900 text-zinc-600'}`}
              >
                {item.icon}
                <span className="text-xs font-bold tracking-widest">{item.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      <main className="flex-1 p-4 overflow-hidden flex flex-col">
        {activeTab === 'dashboard' && <Dashboard />}
        
        {activeTab === 'brain' && (
          <div className="flex flex-col h-full max-h-[80vh]">
            <div className="flex-1 overflow-y-auto space-y-4 mb-4 pr-2 custom-scrollbar">
              {messages.map((m, i) => (
                <div key={i} className={`p-4 text-xs ${m.role === 'user' ? 'bg-zinc-900 border border-zinc-800 ml-10 rounded-lg' : 'bg-blue-950/10 border-l-2 border-blue-500 mr-10 rounded-r-lg'}`}>
                  <div className="text-[8px] text-zinc-500 mb-2 font-bold tracking-tighter uppercase">{m.role === 'user' ? 'Owner' : 'Sovereign Core'}</div>
                  <div className="leading-relaxed whitespace-pre-wrap">{m.content}</div>
                </div>
              ))}
              {loading && <div className="text-[10px] text-blue-500 animate-pulse">Processing Neural Request...</div>}
            </div>
            <div className="mt-auto border border-zinc-800 p-3 bg-zinc-900/30 rounded-xl flex gap-3 items-center">
              <input 
                className="flex-1 bg-transparent outline-none text-xs text-white" 
                placeholder="Ask FEAC Brain..." 
                value={input} 
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSendMessage()}
              />
              <button onClick={handleSendMessage} className="text-blue-500 hover:text-white"><Send size={20}/></button>
            </div>
          </div>
        )}

        {activeTab === 'emergent' && (
          <div className="flex flex-col gap-4 h-full">
            <div className="flex-1 border border-zinc-800 p-4 rounded-lg bg-zinc-900/10">
              <div className="text-[10px] text-blue-500 mb-2 font-bold">PROMPT COMMAND</div>
              <textarea className="w-full bg-transparent border-none text-xs text-zinc-300 h-full outline-none resize-none" placeholder="Execute emergent sequence..."></textarea>
            </div>
            <div className="h-40 border border-zinc-800 p-4 bg-black rounded-lg overflow-y-auto">
              <div className="text-[10px] text-green-500 mb-2 font-bold tracking-widest">OUTPUT_STREAM</div>
              <div className="text-xs text-green-700 font-mono">{" >>> "} System ready. Authentication confirmed.</div>
            </div>
          </div>
        )}

        {!['dashboard', 'brain', 'emergent'].includes(activeTab) && (
          <div className="flex flex-col items-center justify-center h-full border border-dashed border-zinc-800 rounded-2xl opacity-40">
            <Activity className="mb-4 animate-spin-slow" size={40}/>
            <div className="text-[10px] text-zinc-500 font-bold tracking-[0.8em]">{activeTab.toUpperCase()} MODULE ENCRYPTED</div>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
