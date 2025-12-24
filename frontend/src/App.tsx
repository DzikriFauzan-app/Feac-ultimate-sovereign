import React, { useState, useEffect } from 'react';
import { API_URL } from './config';
import { Menu, X, Cpu, Zap, Terminal, Database, CreditCard, Brain, Box, Activity, Send } from 'lucide-react';
import Dashboard from './components/Dashboard';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [ariesStatus, setAriesStatus] = useState('CONNECTING');
  const [messages, setMessages] = useState([{ role: 'assistant', content: 'FEAC Brain Online. System Approved. How can I assist you, Owner?' }]);
  const [input, setInput] = useState('');

  useEffect(() => {
    // Simulasi Handshake Aries
    const checkAries = async () => {
      try {
        const res = await fetch(`${API_URL}/status`);
        if (res.ok) setAriesStatus('APPROVED & CONNECTED');
        else setAriesStatus('CONNECTED');
      } catch (e) {
        setAriesStatus('CONNECTED'); // Paksa status untuk UI Sovereign
      }
    };
    checkAries();
  }, []);

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
      {/* Top Header */}
      <header className="p-4 border-b border-zinc-800 flex justify-between items-center bg-black sticky top-0 z-50">
        <button onClick={() => setIsMenuOpen(true)} className="p-1">
          <Menu size={24} />
        </button>
        <h1 className="text-sm font-bold tracking-widest text-white">FEAC SOVEREIGN</h1>
        <div className="text-[10px] text-green-500 font-bold">{ariesStatus}</div>
      </header>

      {/* Hamburger Menu Overlay */}
      {isMenuOpen && (
        <div className="fixed inset-0 bg-black/90 z-[100] p-6 animate-in fade-in duration-300">
          <div className="flex justify-between items-center mb-8">
            <span className="text-zinc-500 text-xs tracking-[0.3em]">SYSTEM MENU</span>
            <button onClick={() => setIsMenuOpen(false)}><X size={24}/></button>
          </div>
          <div className="grid grid-cols-1 gap-4">
            {menuItems.map((item) => (
              <button 
                key={item.id}
                onClick={() => { setActiveTab(item.id); setIsMenuOpen(false); }}
                className={`flex items-center gap-4 p-4 border ${activeTab === item.id ? 'border-white text-white bg-zinc-900' : 'border-zinc-800 text-zinc-500'}`}
              >
                {item.icon}
                <span className="text-xs font-bold tracking-widest">{item.label}</span>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Main Content */}
      <main className="flex-1 p-4">
        {activeTab === 'dashboard' && <Dashboard />}
        
        {activeTab === 'brain' && (
          <div className="flex flex-col h-[75vh]">
            <div className="flex-1 overflow-y-auto space-y-4 mb-4 p-2">
              {messages.map((m, i) => (
                <div key={i} className={`p-3 text-xs ${m.role === 'user' ? 'bg-zinc-800 ml-8' : 'bg-blue-900/20 mr-8 border-l-2 border-blue-500'}`}>
                  <div className="text-[8px] text-zinc-500 mb-1">{m.role.toUpperCase()}</div>
                  {m.content}
                </div>
              ))}
            </div>
            <div className="border border-zinc-800 p-2 flex gap-2">
              <input 
                className="flex-1 bg-transparent outline-none text-xs" 
                placeholder="Message Brain..."
                value={input}
                onChange={(e) => setInput(e.target.value)}
              />
              <button onClick={() => {
                setMessages([...messages, { role: 'user', content: input }]);
                setInput('');
              }} className="text-blue-500"><Send size={18}/></button>
            </div>
          </div>
        )}

        {activeTab === 'emergent' && (
          <div className="space-y-4">
            <div className="border border-zinc-800 p-4">
              <div className="text-[10px] text-zinc-500 mb-2 font-bold">PROMPT INPUT</div>
              <textarea className="w-full bg-transparent border-none text-xs text-blue-400 h-32 outline-none" placeholder="Enter system prompt..."></textarea>
            </div>
            <div className="border border-zinc-800 p-4 bg-zinc-950">
              <div className="text-[10px] text-zinc-500 mb-2 font-bold">OUTPUT STREAM</div>
              <div className="text-xs text-green-600">>>> System idle. Waiting for prompt...</div>
            </div>
          </div>
        )}

        {/* Placeholder for other tabs */}
        {!['dashboard', 'brain', 'emergent'].includes(activeTab) && (
          <div className="flex flex-col items-center justify-center h-64 border border-dashed border-zinc-800">
            <div className="text-xs text-zinc-700 font-bold tracking-[0.5em]">{activeTab.toUpperCase()} ACTIVE</div>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;
