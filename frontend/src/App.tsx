import React, { useState, useRef } from 'react';
import { Menu, Send, Plus, Paperclip } from 'lucide-react';
import Sidebar from './components/Sidebar';
import Dashboard from './components/Dashboard';
import Billing from './components/Billing';
import Artifacts from './components/Artifacts';
import EngineBridge from './components/EngineBridge';
import TermuxInternal from './components/Termux';
import RepositoryManager from './components/Repository';
import NeoGrid from './components/NeoGrid';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [chatMsg, setChatMsg] = useState('');
  const [userRole, setUserRole] = useState('OWNER');
  const [chatHistory, setChatHistory] = useState([
    { role: 'aries', text: 'Sovereign identity verified. Input instructions or upload files for multi-engine processing.' }
  ]);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleSendMessage = () => {
    if (!chatMsg.trim()) return;
    const newHistory = [...chatHistory, { role: 'user', text: chatMsg }];
    setChatHistory(newHistory);
    setChatMsg('');
    setTimeout(() => {
      setChatHistory(prev => [...prev, { role: 'aries', text: `Processing instruction: "${chatMsg}"... Sovereign command accepted.` }]);
    }, 1000);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (files && files.length > 0) {
      const fileNames = Array.from(files).map(f => f.name).join(', ');
      setChatHistory(prev => [...prev, { role: 'user', text: `Uploading files: ${fileNames}` }]);
      setTimeout(() => {
        setChatHistory(prev => [...prev, { role: 'aries', text: `Documents received. Indexing content for analysis...` }]);
      }, 1500);
    }
  };

  return (
    <div className="flex h-screen w-full bg-[#0a0f14] text-gray-300 overflow-hidden font-sans select-none">
      <Sidebar 
        isOpen={isSidebarOpen} 
        setIsOpen={setIsSidebarOpen} 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
        userRole={userRole} 
      />
      
      <div className="flex-1 flex flex-col min-w-0 h-screen overflow-hidden">
        <header className="h-14 border-b border-gray-800/50 flex items-center px-4 justify-between bg-[#0d131a] shrink-0 z-40">
          <button onClick={() => setIsSidebarOpen(true)} className="p-2 text-gray-400 lg:hidden"><Menu className="w-6 h-6" /></button>
          <div className="text-center">
            <h1 className="text-[10px] font-black tracking-[0.3em] uppercase text-blue-500">FEAC Sovereign OS</h1>
            <p className="text-[8px] font-mono text-gray-700 uppercase">{userRole} ACCESS</p>
          </div>
          <div className="w-10" />
        </header>

        <main className="flex-1 overflow-y-auto bg-[#0a0f14] relative">
          {activeTab === 'dashboard' && <Dashboard />}
          {activeTab === 'github' && <RepositoryManager />}
          {activeTab === 'neogrid' && <NeoGrid />}
          {activeTab === 'engine' && <EngineBridge />}
          {activeTab === 'artifacts' && userRole === 'OWNER' && <Artifacts />}
          {activeTab === 'termux' && <TermuxInternal />}
          {activeTab === 'billing' && <Billing />}
          {activeTab === 'brain' && (
            <div className="h-full flex flex-col p-4 bg-gradient-to-b from-[#0a0f14] to-[#110a1a]">
              <div className="flex-1 overflow-y-auto p-2 space-y-4 custom-scrollbar">
                 {chatHistory.map((msg, i) => (
                   <div key={i} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in slide-in-from-bottom-2`}>
                      <div className={`p-4 rounded-3xl max-w-[85%] border ${msg.role === 'user' ? 'bg-blue-600/10 border-blue-500/20 text-blue-100' : 'bg-purple-900/10 border-purple-500/10'}`}>
                        <p className="text-[9px] font-black text-purple-400 uppercase tracking-widest mb-1">
                          {msg.role === 'user' ? 'Sovereign' : 'Aries Brain v2'}
                        </p>
                        <p className="text-sm leading-relaxed">{msg.text}</p>
                      </div>
                   </div>
                 ))}
              </div>
              
              <div className="mb-2 mt-4 flex items-center space-x-2 bg-[#1a1421] p-3 rounded-[2.5rem] border border-purple-900/20 shadow-2xl">
                <input type="file" ref={fileInputRef} className="hidden" multiple accept="*" onChange={handleFileChange} />
                <button onClick={() => fileInputRef.current?.click()} className="p-4 bg-purple-950/40 text-purple-400 rounded-full hover:bg-purple-900/40 transition-all active:scale-90 flex shrink-0">
                  <Paperclip className="w-6 h-6"/>
                </button>
                <input 
                  value={chatMsg} 
                  onChange={(e) => setChatMsg(e.target.value)} 
                  onKeyDown={handleKeyDown}
                  className="flex-1 bg-transparent py-3 px-3 text-sm outline-none text-white placeholder:text-gray-600" 
                  placeholder="Direct prompt to Aries..." 
                />
                <button onClick={handleSendMessage} className="p-4 bg-purple-600 text-white rounded-full shadow-lg active:scale-95 flex shrink-0">
                  <Send className="w-6 h-6"/>
                </button>
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
export default App;
