export const renderRepoScanner = () => `
<div class="p-6 bg-[#0a0b10] rounded-2xl border border-gray-900">
    <h2 class="text-sm font-bold mb-6 flex items-center gap-2">📂 REPO SCANNER & SELF-UPGRADE</h2>
    <div class="space-y-4">
        <div class="bg-black/40 p-4 border border-gray-800 rounded-xl">
            <label class="text-[10px] text-gray-500 block mb-2 uppercase">Target Project</label>
            <input type="text" value="~/Feac-ultimate-sovereign" class="w-full bg-transparent border-none text-xs text-green-400 outline-none">
        </div>
        <div class="grid grid-cols-2 gap-4">
            <button class="bg-blue-900/40 border border-blue-500 text-blue-400 py-3 rounded-xl text-[10px] font-bold">START SELF-LEARN</button>
            <button class="bg-green-900/40 border border-green-500 text-green-400 py-3 rounded-xl text-[10px] font-bold">FORCE UPGRADE</button>
        </div>
    </div>
</div>`;
