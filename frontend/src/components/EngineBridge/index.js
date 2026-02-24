"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const react_1 = require("react");
const lucide_react_1 = require("lucide-react");
const EngineBridge = () => {
    const [projects] = (0, react_1.useState)([{ name: 'Sovereign-Shooter', engine: 'Godot', status: 'LINKED' }]);
    return (<div className="p-5 pb-24 space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-xl font-black text-white uppercase italic">Engine <span className="text-blue-500">Bridge</span></h2>
        <button className="p-2.5 bg-blue-600 rounded-xl text-white"><lucide_react_1.Plus className="w-5 h-5"/></button>
      </div>
      <div className="grid grid-cols-1 gap-4">
        {projects.map((proj) => (<div key={proj.name} className="bg-[#111821] border border-gray-800 p-5 rounded-2xl space-y-4">
             <div className="flex items-center space-x-3">
                <lucide_react_1.Box className="text-blue-400 w-5 h-5"/>
                <h3 className="text-sm font-black text-white uppercase">{proj.name}</h3>
             </div>
          </div>))}
      </div>
    </div>);
};
exports.default = EngineBridge;
