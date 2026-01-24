export const renderChat = () => {
    const history = JSON.parse(localStorage.getItem('aries_chat') || '[]');
    setTimeout(() => {
        const input = document.getElementById('chat-input');
        const container = document.getElementById('chat-messages');
        if(input) input.focus();
        if(container) container.scrollTop = container.scrollHeight;
    }, 100);

    const messages = history.map(m => `
        <div class="flex ${m.role === 'user' ? 'justify-end' : 'justify-start'} animate-in fade-in duration-300">
            <div class="${m.role === 'user' ? 'bg-purple-600 text-white rounded-tr-none' : 'bg-zinc-900 text-zinc-300 rounded-tl-none border border-zinc-800'} px-4 py-3 rounded-2xl text-[13px] max-w-[85%] shadow-lg">
                ${m.text}
            </div>
        </div>
    `).join('');

    return `
<div class="flex flex-col h-full bg-[#050508]">
    <div id="chat-messages" class="flex-1 overflow-y-auto p-4 space-y-5 pb-24">
        ${messages || '<div class="h-full flex items-center justify-center text-[9px] text-zinc-800 uppercase tracking-widest">System Ready</div>'}
    </div>
    <div class="fixed bottom-0 left-0 w-full p-4 bg-gradient-to-t from-black via-black to-transparent">
        <form onsubmit="event.preventDefault(); window.sendAriesMessage();" class="max-w-xl mx-auto flex items-center gap-2 bg-[#121215] border border-zinc-800 rounded-2xl px-4 py-1 shadow-2xl focus-within:border-purple-600 transition-all">
            <input type="text" id="chat-input" placeholder="Message Aries..." autocomplete="off" class="flex-1 bg-transparent border-none outline-none text-[16px] text-white py-3">
            <button type="submit" class="w-10 h-10 bg-purple-600 rounded-xl flex items-center justify-center text-lg active:scale-90 transition-all">🚀</button>
        </form>
    </div>
</div>`;
};
