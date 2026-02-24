import axios from 'axios';
async function stressTest() {
    console.log("🗣️ [SIMULASI] MEMULAI 20 CHAT SERIUS...");
    for(let i=1; i<=20; i++) {
        const res = await axios.post('http://127.0.0.1:3001/api/chat', {
            message: `Diskusi Teori Kedaulatan Digital Tahap ${i}: Analisa integrasi 40 agen NeoEngine.`
        });
        console.log(`💬 Chat ${i}: ${res.status === 200 ? 'SUCCESS' : 'FAIL'}`);
    }
}
stressTest();
