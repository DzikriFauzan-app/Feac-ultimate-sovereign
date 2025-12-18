import { Check, Crown, ShieldCheck } from 'lucide-react';

const Billing = ({ currentTier = 'OWNER' }: { currentTier?: string }) => {
  const tiers = [
    { name: 'Free', price: '$0', features: ['Basic Chat', '1 Node'], color: 'gray' },
    { name: 'Standard', price: '$19', features: ['Advanced AI', '4 Nodes', 'Aries Lite'], color: 'blue' },
    { name: 'Pro', price: '$49', features: ['Full Neural Access', '10 Nodes', 'Godot Bridge'], color: 'purple' },
    { name: 'Ultimate', price: '$99', features: ['Zero Latency', 'Unlimited Nodes', 'Fleet Monitor'], color: 'emerald' },
  ];

  return (
    <div className="p-5 pb-24 space-y-6 animate-in slide-in-from-bottom-4 duration-500">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-black text-white uppercase italic tracking-tighter">Billing <span className="text-blue-500 font-mono">Gateway</span></h2>
        <span className="text-[8px] font-mono bg-blue-500/10 text-blue-400 px-3 py-1 rounded-full border border-blue-500/20">SESSION: 0x826</span>
      </div>

      {/* OWNER STATUS PANEL */}
      {currentTier === 'OWNER' && (
        <div className="bg-gradient-to-br from-[#1a1405] to-[#0a0f14] border border-yellow-600/30 rounded-2xl p-6 relative overflow-hidden shadow-2xl shadow-yellow-900/10">
          <div className="relative z-10">
            <div className="flex items-center space-x-2 text-yellow-500 mb-2">
              <Crown className="w-4 h-4" />
              <span className="text-[10px] font-black uppercase tracking-[0.3em]">Sovereign Level</span>
            </div>
            <h3 className="text-2xl font-black text-white tracking-tighter">OWNER PRIVILEGE</h3>
            <p className="text-[9px] text-yellow-600/70 mt-1 uppercase font-mono italic leading-relaxed">
              Global bypass active. No billing limits. All neural cores unlocked.
            </p>
          </div>
          <ShieldCheck className="absolute -right-6 -bottom-6 w-32 h-32 text-yellow-500 opacity-5 rotate-12" />
        </div>
      )}

      {/* TIERS LIST */}
      <div className="space-y-4">
        <p className="text-[10px] font-black text-gray-700 uppercase tracking-[0.2em] px-1">Consumer Tiers</p>
        <div className="flex space-x-4 overflow-x-auto pb-4 custom-scrollbar snap-x">
          {tiers.map((tier) => (
            <div key={tier.name} className={`min-w-[240px] snap-center bg-[#111821] border ${currentTier === tier.name ? 'border-blue-500 bg-[#161e29]' : 'border-gray-800'} rounded-2xl p-5 flex flex-col shadow-xl`}>
              <div className="flex justify-between items-start">
                <p className="text-[10px] font-bold text-gray-500 uppercase tracking-widest">{tier.name}</p>
                {currentTier === tier.name && <div className="w-2 h-2 bg-blue-500 rounded-full animate-ping"></div>}
              </div>
              <p className="text-3xl font-black text-white mt-1 tracking-tighter">{tier.price}<span className="text-xs text-gray-600 font-normal">/mo</span></p>
              
              <div className="mt-6 space-y-3 flex-1">
                {tier.features.map(f => (
                  <div key={f} className="flex items-center space-x-2 text-[11px] font-medium text-gray-400">
                    <Check className="w-3.5 h-3.5 text-blue-500 shrink-0" />
                    <span>{f}</span>
                  </div>
                ))}
              </div>
              
              <button className={`mt-8 w-full py-3.5 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all active:scale-95 ${currentTier === tier.name ? 'bg-blue-600 text-white shadow-lg shadow-blue-900/40' : 'bg-gray-800/50 text-gray-500'}`}>
                {currentTier === tier.name ? 'Current Active' : 'Upgrade Plan'}
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Billing;
