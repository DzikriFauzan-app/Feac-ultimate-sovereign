import { 
  LayoutDashboard, Box, Github, CreditCard, Brain, 
  Terminal, Zap, X, Layers 
} from 'lucide-react';

const Sidebar = ({ isOpen, setIsOpen, activeTab, setActiveTab, userRole }: any) => {
  const menuItems = [
    { id: 'dashboard', icon: LayoutDashboard, label: 'Dashboard' },
    { id: 'github', icon: Github, label: 'Repo Scanner' },
    { id: 'neogrid', icon: Box, label: 'NeoGrid' },
    { id: 'engine', icon: Zap, label: 'Engine Bridge' },
    { id: 'termux', icon: Terminal, label: 'Termux' },
    { id: 'billing', icon: CreditCard, label: 'Billing' },
  ];

  return (
    <>
      <div className={`fixed inset-0 bg-black/90 z-[60] transition-opacity ${isOpen ? 'visible opacity-100' : 'invisible opacity-0'}`} onClick={() => setIsOpen(false)} />
      <aside className={`fixed inset-y-0 left-0 w-72 bg-[#0d131a] border-r border-gray-800 z-[70] transform transition-transform duration-300 ${isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0 lg:static'}`}>
        <div className="p-6 border-b border-gray-800 flex justify-between items-center">
          <span className="font-black text-white text-xs tracking-widest uppercase italic">FEAC Sovereign</span>
          <button onClick={() => setIsOpen(false)} className="lg:hidden text-gray-500"><X /></button>
        </div>
        <nav className="p-4 space-y-1 overflow-y-auto h-[calc(100vh-160px)]">
          {menuItems.map((item: any) => (
            <button key={item.id} onClick={() => { setActiveTab(item.id); setIsOpen(false); }}
              className={`w-full flex items-center space-x-3 p-3 rounded-xl transition-all ${activeTab === item.id ? 'bg-blue-600/10 text-blue-400 border border-blue-500/20' : 'text-gray-500 hover:bg-gray-800/40'}`}>
              <item.icon className="w-5 h-5" />
              <span className="text-xs font-bold uppercase">{item.label}</span>
            </button>
          ))}
          {userRole === 'OWNER' && (
            <button onClick={() => { setActiveTab('artifacts'); setIsOpen(false); }}
              className={`w-full flex items-center space-x-3 p-3 rounded-xl mt-4 border transition-all ${activeTab === 'artifacts' ? 'bg-red-900/10 text-red-500 border-red-500/20' : 'border-transparent text-red-900/40 hover:text-red-500'}`}>
              <Layers className="w-5 h-5" />
              <span className="text-xs font-black uppercase">Artifacts Room</span>
            </button>
          )}
          <button onClick={() => { setActiveTab('brain'); setIsOpen(false); }}
            className={`w-full flex items-center space-x-3 p-4 rounded-2xl mt-4 transition-all ${activeTab === 'brain' ? 'bg-purple-600 text-white' : 'bg-[#1a1421] text-purple-400'}`}>
            <Brain className="w-5 h-5" />
            <span className="text-xs font-black uppercase">FEAC BRAIN</span>
          </button>
        </nav>
      </aside>
    </>
  );
};
export default Sidebar;
