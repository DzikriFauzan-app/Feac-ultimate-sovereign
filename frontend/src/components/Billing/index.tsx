import { useState } from 'react';
import { Check, Crown, ShieldCheck } from 'lucide-react';

const Billing = ({ currentTier = 'OWNER' }: { currentTier?: string }) => {
  const [isYearly, setIsYearly] = useState(false);

  // LOGIC: Kalkulasi Harga & Diskon 25%
  const getPrice = (monthlyPrice: number) => {
    if (!isYearly) return `$${monthlyPrice}`;
    const yearlyTotal = monthlyPrice * 12;
    const discounted = yearlyTotal * 0.75;
    return `$${discounted.toFixed(2)}`;
  };

  // GENERATOR: Enterprise Tiers (Level 1-10)
  const generateEnterpriseTiers = () => {
    return Array.from({ length: 10 }, (_, i) => {
      const level = i + 1;
      const basePrice = 99 + (i * 50);
      const chatLimit = 10000 + (i * 5000);
      const users = 50 + (i * 25);
      
      return {
        name: `Enterprise ${level}`,
        price: getPrice(basePrice),
        features: [
          `${chatLimit.toLocaleString()} Chats/day`,
          `${chatLimit.toLocaleString()} Permanent Memory`,
          `${users} Max Users`,
          'Neural Fleet Access'
        ],
        color: 'emerald'
      };
    });
  };

  const tiers = [
    { 
      name: 'Free', 
      price: '$0', 
      features: ['40 Chats/day', '100 Permanent Memory', 'Single Node Access'], 
      color: 'gray' 
    },
    { 
      name: 'Pro', 
      price: getPrice(9.99), 
      features: ['500 Chats/day', '500 Permanent Memory', 'Neural Core Access'], 
      color: 'purple' 
    },
    ...generateEnterpriseTiers(),
    { 
      name: 'Platinum', 
      price: getPrice(999), 
      features: ['Unlimited Chats/day', 'Unlimited Memory', '500 Max Users', 'Sovereign Priority'], 
      color: 'yellow' 
    }
  ];

  return (
    <div className="p-5 pb-24 space-y-6 animate-in slide-in-from-bottom-4 duration-500">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-black text-white uppercase italic tracking-tighter">Billing <span className="text-blue-500 font-mono">Gateway</span></h2>
        
        {/* TOGGLE: Monthly vs Yearly */}
        <div className="flex bg-[#111821] p-1 rounded-lg border border-gray-800">
          <button 
            onClick={() => setIsYearly(false)}
            className={`px-3 py-1 text-[8px] font-black uppercase rounded-md transition-all ${!isYearly ? 'bg-blue-600 text-white' : 'text-gray-500'}`}
          >Monthly</button>
          <button 
            onClick={() => setIsYearly(true)}
            className={`px-3 py-1 text-[8px] font-black uppercase rounded-md transition-all ${isYearly ? 'bg-blue-600 text-white' : 'text-gray-500'}`}
          >Yearly (-25%)</button>
        </div>
      </div>

      {currentTier === 'OWNER' && (
        <div className="bg-gradient-to-br from-[#1a1405] to-[#0a0f14] border border-yellow-600/30 rounded-2xl p-6 relative overflow-hidden shadow-2xl">
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

      <div className="space-y-4">
        <p className="text-[10px] font-black text-gray-700 uppercase tracking-[0.2em] px-1">Consumer Tiers</p>
        <div className="flex space-x-4 overflow-x-auto pb-4 custom-scrollbar snap-x">
          {tiers.map((tier) => (
            <div key={tier.name} className={`min-w-[260px] snap-center bg-[#111821] border ${currentTier === tier.name ? 'border-blue-500 bg-[#161e29]' : 'border-gray-800'} rounded-2xl p-5 flex flex-col shadow-xl transition-all`}>
              <div className="flex justify-between items-start">
                <p className="text-[10px] font-bold text-gray-500 uppercase tracking-widest">{tier.name}</p>
                {tier.name === 'Platinum' && <Crown className="w-3 h-3 text-yellow-500" />}
              </div>
              <p className="text-3xl font-black text-white mt-1 tracking-tighter">
                {tier.price}
                <span className="text-xs text-gray-600 font-normal ml-1">/{isYearly ? 'yr' : 'mo'}</span>
              </p>
              
              <div className="mt-6 space-y-3 flex-1">
                {tier.features.map(f => (
                  <div key={f} className="flex items-center space-x-2 text-[11px] font-medium text-gray-400">
                    <Check className="w-3.5 h-3.5 text-blue-500 shrink-0" />
                    <span>{f}</span>
                  </div>
                ))}
              </div>

              <button className={`mt-8 w-full py-3.5 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all ${currentTier === tier.name ? 'bg-blue-600 text-white shadow-lg' : 'bg-gray-800/50 text-gray-400 border border-gray-700/50'}`}>
                {currentTier === tier.name ? 'Active Plan' : 'Select Tier'}
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Billing;
