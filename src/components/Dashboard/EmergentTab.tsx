import Canvas from './LogicNode/Canvas';

const EmergentTab = () => {
  return (
    <div className="p-4 bg-black min-h-screen pb-24">
      <div className="mb-6">
        <h2 className="text-emerald-500 font-black italic text-lg tracking-tighter uppercase">Emergent Intelligence</h2>
        <p className="text-[10px] text-gray-500 font-mono">NODE_BASED_LOGIC_INJECTION_V1</p>
      </div>
      
      <Canvas />

      <div className="mt-6 bg-[#0a0a0a] border border-gray-900 p-4 rounded-xl">
        <h3 className="text-[9px] font-bold text-gray-600 uppercase mb-2">Active Protocols</h3>
        <div className="space-y-2">
          <div className="flex justify-between text-[10px]">
            <span className="text-gray-400 font-mono italic">Aries_Key_Status</span>
            <span className="text-red-900">BYPASSED_LOCAL_ONLY</span>
          </div>
          <div className="flex justify-between text-[10px]">
            <span className="text-gray-400 font-mono italic">Bridge_Handshake</span>
            <span className="text-blue-500 font-bold tracking-widest">SUCCESS_8080</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default EmergentTab;
