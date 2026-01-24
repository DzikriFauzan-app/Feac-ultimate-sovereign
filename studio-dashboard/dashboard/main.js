import { renderSidebar } from './modules/Sidebar.js';

window.saveKeyFromSide = () => {
    const val = document.getElementById('side-key').value;
    if(val) {
        localStorage.setItem('aries_api_key', val);
        alert("ENGINE SYNCED");
        location.reload();
    }
};

// Render Sidebar Saat Start
document.getElementById('sidebar-content').innerHTML = renderSidebar();

const authKey = localStorage.getItem('aries_api_key');
const viewport = document.getElementById('viewport');

if(!authKey) {
    viewport.innerHTML = `
        <div class="h-full flex items-center justify-center">
            <div class="text-center">
                <div class="w-16 h-16 border-2 border-zinc-900 border-t-purple-600 rounded-full animate-spin mx-auto mb-6"></div>
                <p class="text-[10px] text-zinc-600 uppercase tracking-[0.5em]">System Locked</p>
                <p class="text-[8px] text-zinc-800 uppercase tracking-widest mt-2">Open menu to input access key</p>
            </div>
        </div>`;
} else {
    viewport.innerHTML = `<div class="p-10 text-zinc-500 uppercase text-[10px] tracking-[1em]">Dashboard Ready</div>`;
}
