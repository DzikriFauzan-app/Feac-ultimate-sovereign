import { useState } from 'react';
import { Box,  Plus } from 'lucide-react';

const EngineBridge = () => {
  const [projects] = useState([{ name: 'Sovereign-Shooter', engine: 'Godot', status: 'LINKED' }]);
  return (
    <div className="p-5 pb-24 space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-black text-white uppercase italic">Engine <span className="text-blue-500">Bridge</span></h2>
        <button className="p-2.5 bg-blue-600 rounded-xl text-white"><Plus className="w-5 h-5" /></button>
      </div>
      <div className="grid grid-cols-1 gap-4">
        {projects.map((proj: any) => (
          <div key={proj.name} className="bg-[#111821] border border-gray-800 p-5 rounded-2xl space-y-4">
             <div className="flex items-center space-x-3">
                <Box className="text-blue-400 w-5 h-5" />
                <h3 className="text-sm font-black text-white uppercase">{proj.name}</h3>
             </div>
          </div>
        ))}
      </div>
    </div>
  );
};
export default EngineBridge;
