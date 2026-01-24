export const renderApiKey = () => `
<div class="h-full flex items-center justify-center bg-[#050508] p-6">
    <div class="w-full max-w-sm glass p-8 rounded-[2rem] text-center border-purple-900/20 shadow-2xl shadow-purple-900/10">
        <div class="w-16 h-16 bg-purple-600 rounded-2xl mx-auto mb-6 flex items-center justify-center shadow-lg shadow-purple-600/40">
            <span class="text-2xl">🔑</span>
        </div>
        <h2 class="text-xs font-bold tracking-[0.5em] text-white uppercase mb-2">Access Required</h2>
        <p class="text-[9px] text-zinc-500 uppercase tracking-widest mb-8">Enter your Neo Engine Key</p>
        <div class="space-y-4">
            <input type="password" id="api-input" placeholder="••••••••" 
                class="w-full bg-zinc-900/50 border border-zinc-800 rounded-xl px-4 py-4 text-center text-purple-500 outline-none focus:border-purple-500 transition-all">
            <button onclick="window.authorizeAccess()" class="w-full bg-white text-black py-4 rounded-xl text-[10px] font-bold uppercase tracking-widest hover:bg-purple-500 hover:text-white transition-all">Initialize System</button>
        </div>
    </div>
</div>`;
