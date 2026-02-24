"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const ProjectCreator_1 = __importDefault(require("./ProjectCreator"));
const ResourceMonitor_1 = __importDefault(require("./ResourceMonitor"));
const lucide_react_1 = require("lucide-react");
const ProjectTab = () => {
    return (<div className="p-4 bg-black min-h-screen pb-24 font-mono">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h2 className="text-xl font-black italic text-blue-500 tracking-tighter uppercase">Project Multiverse</h2>
          <p className="text-[8px] text-gray-500 uppercase">NeoEngine_Agent_Ready</p>
        </div>
        <lucide_react_1.BrainCircuit className="text-emerald-500 animate-pulse" size={20}/>
      </div>

      {/* Monitor Vital Redmi 12 */}
      <ResourceMonitor_1.default />

      {/* Project Creator UI */}
      <ProjectCreator_1.default />

      <div className="mt-6">
         <p className="text-[9px] text-gray-600 font-bold uppercase tracking-widest mb-3">Recent_Encodings</p>
         <div className="p-4 bg-[#0a0a0a] border border-gray-900 rounded-xl text-[10px] text-gray-500 italic">
            Waiting for project initialization...
         </div>
      </div>
    </div>);
};
exports.default = ProjectTab;
