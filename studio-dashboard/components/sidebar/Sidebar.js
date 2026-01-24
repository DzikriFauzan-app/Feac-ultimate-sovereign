export const renderSidebar = () => `
<div id="sidebar" class="fixed left-0 top-0 h-full w-64 bg-[#0a0b10] border-r border-gray-900 z-50 transition-transform -translate-x-full">
    <div class="p-6">
        <h2 class="text-white font-bold text-xs tracking-widest mb-10">FEAC SOVEREIGN</h2>
        <nav class="space-y-6 text-gray-400 text-xs">
            <div class="flex items-center gap-3 hover:text-white cursor-pointer"><span class="w-4">📊</span> DASHBOARD</div>
            <div class="flex items-center gap-3 hover:text-white cursor-pointer"><span class="w-4">📂</span> REPO SCANNER</div>
            <div class="flex items-center gap-3 hover:text-white cursor-pointer"><span class="w-4">🤖</span> NEOGRID</div>
            <div class="flex items-center gap-3 text-blue-500 cursor-pointer"><span class="w-4">⚡</span> ENGINE BRIDGE</div>
            <div class="flex items-center gap-3 hover:text-white cursor-pointer"><span class="w-4">🐚</span> TERMUX</div>
            <div class="flex items-center gap-3 hover:text-white cursor-pointer"><span class="w-4">💳</span> BILLING</div>
        </nav>
        <div class="mt-20 p-4 bg-[#1a1b23] rounded-xl border border-purple-900/30">
            <div class="flex items-center gap-2 text-purple-400 text-[10px] mb-1">
                <span>🧠</span> FEAC BRAIN
            </div>
            <p class="text-[8px] text-gray-500 italic">Core: Active</p>
        </div>
    </div>
</div>`;
