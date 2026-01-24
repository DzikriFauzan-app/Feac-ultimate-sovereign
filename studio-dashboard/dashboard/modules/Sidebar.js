export const renderSidebar = () => {
    const currentKey = localStorage.getItem('aries_api_key') || "";
    return `
    <div class="flex flex-col h-full">
        <div class="mb-10">
            <h2 class="text-[11px] font-black tracking-[0.5em] text-white uppercase">Aries Core</h2>
            <p class="text-[8px] text-purple-600 font-bold uppercase tracking-widest mt-1">Sovereign Access</p>
        </div>

        <div class="bg-zinc-900/40 border border-purple-500/20 rounded-2xl p-5 mb-8">
            <label class="text-[8px] text-zinc-500 uppercase font-bold tracking-widest mb-3 block">Neo Engine Key</label>
            <input id="side-key" type="password" value="${currentKey}" placeholder="ENTER KEY..." 
                class="w-full bg-black border border-zinc-800 rounded-xl p-3 text-[10px] text-white focus:border-purple-500 outline-none mb-4">
            <button onclick="window.saveKeyFromSide()" 
                class="w-full py-3 bg-purple-600 rounded-xl text-[9px] font-black uppercase tracking-[0.2em] text-white active:bg-purple-700 shadow-lg shadow-purple-500/20">
                Authorize System
            </button>
        </div>

        <nav class="flex-1 space-y-2">
            ${['Dashboard', 'Aries Brain', 'Repo Scan', 'Shell', 'Settings'].map(item => `
                <div class="flex items-center gap-4 px-4 py-4 rounded-xl hover:bg-white/5 cursor-pointer group">
                    <div class="w-1 h-1 rounded-full bg-zinc-800 group-hover:bg-purple-500"></div>
                    <span class="text-[10px] font-bold text-zinc-500 group-hover:text-white uppercase tracking-widest">${item}</span>
                </div>
            `).join('')}
        </nav>
    </div>`;
};
