import { Box, Code2, RefreshCw, Plus } from 'lucide-react';

const EngineBridge = () => {
  const [projects] = useState([
    { name: 'Sovereign-Shooter', engine: 'Godot', status: 'LINKED' }
  ]);

  return (
    <div className="p-5 pb-24 space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-black text-white uppercase italic tracking-tighter">Engine <span className="text-blue-500">Bridge</span></h2>
        <button onClick={() => {}} className="p-2.5 bg-blue-600 rounded-xl text-white shadow-lg active:scale-90 transition-transform">
          <Plus className="w-5 h-5" />
        </button>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {projects.map(proj => (
          <div key={proj.name} className="bg-[#111821] border border-gray-800 p-5 rounded-2xl space-y-4">
            <div className="flex justify-between items-center">
              <div className="flex items-center space-x-3">
                <Box className="text-blue-400 w-5 h-5" />
                <div>
                  <h3 className="text-sm font-black text-white uppercase">{proj.name}</h3>
                  <p className="text-[9px] text-gray-500 font-mono tracking-widest">{proj.engine} Engine</p>
                </div>
              </div>
              <span className="text-[8px] bg-emerald-900/20 text-emerald-500 px-2 py-1 rounded-md border border-emerald-500/20 font-bold tracking-tighter uppercase">{proj.status}</span>
            </div>
            
            <div className="grid grid-cols-2 gap-3">
              <button className="bg-gray-800/50 text-gray-400 py-3 rounded-xl text-[10px] font-black uppercase flex items-center justify-center border border-gray-800">
                <RefreshCw className="w-3 h-3 mr-2" /> Scan Assets
              </button>
              <button className="bg-blue-600 text-white py-3 rounded-xl text-[10px] font-black uppercase flex items-center justify-center shadow-lg">
                <Code2 className="w-3 h-3 mr-2" /> Gen Code
              </button>
            </div>
            <div className="bg-black/50 p-3 rounded-xl">
               <input type="text" placeholder="Generate logic prompt..." className="w-full bg-transparent text-[11px] text-blue-400 outline-none placeholder:text-gray-700" />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default EngineBridge;
