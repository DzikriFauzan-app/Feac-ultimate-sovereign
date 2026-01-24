export const renderMainGrid = () => `
<div class="p-6 h-full overflow-y-auto bg-black">
    <div class="mb-8 p-6 bg-zinc-900/50 border border-purple-900/30 rounded-3xl">
        <label class="text-[10px] font-bold text-purple-500 tracking-[0.3em] uppercase mb-4 block">Neo Engine Access</label>
        <div class="flex gap-3">
            <input type="password" id="api-key-input" placeholder="ENTER SYSTEM API KEY..." 
                class="flex-1 bg-black border border-zinc-800 rounded-xl px-4 py-3 text-xs text-green-500 outline-none focus:border-purple-500">
            <button onclick="alert('API KEY SYNCED')" class="bg-purple-600 px-6 py-3 rounded-xl text-[10px] font-bold hover:bg-purple-400 transition">ACTIVATE</button>
        </div>
    </div>

    <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
        ${['DASHBOARD', 'CHAT', 'REPO SCANNER', 'NEOGRID', 'ENGINE BRIDGE', 'TERMUX SHELL', 'BILLING BYPASS', 'SELF UPGRADE', 'EMERGENT'].map(m => `
            <div onclick="window.switchMenu('${m.toLowerCase().replace(' ', '')}')" 
                class="bg-zinc-900/30 border border-zinc-800 p-6 rounded-2xl hover:border-purple-500 transition cursor-pointer group text-center">
                <div class="text-2xl mb-3 opacity-50 group-hover:opacity-100 transition">📦</div>
                <h3 class="text-[9px] font-bold tracking-widest text-zinc-500 group-hover:text-purple-400 uppercase">${m}</h3>
            </div>
        `).join('')}
    </div>
</div>`;
