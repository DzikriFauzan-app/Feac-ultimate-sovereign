import axios from 'axios';

const BRIDGE_URL = 'https://redesigned-yodel-7v6wjx4r9x653ww6g-3001.app.github.dev';
const OWNER_KEY = 'aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1';

async function simulateRealApp() {
    console.log("🚀 [REAL-TEST] Menyimulasikan APK FEAC...");

    try {
        // STEP 1: LOGIN
        console.log("\n🔑 [STEP 1] Mengirim Owner Key...");
        const login = await axios.post(`${BRIDGE_URL}/api/validate-key`, { apiKey: OWNER_KEY });
        
        if (login.data.success) {
            console.log("✅ Login Sukses: AUTHORIZED");

            // STEP 2: CHAT (Kirim pesan ke mesin Aries via Bridge)
            console.log("\n💬 [STEP 2] Mengirim pesan ke Aries-core...");
            const chat = await axios.post(`${BRIDGE_URL}/api/chat`, {
                apiKey: OWNER_KEY,
                message: "Aries, jelaskan kenapa sistem kedaulatan data itu penting?"
            });

            console.log("\n🤖 [ARIES RESPONSE]:");
            console.log(chat.data.response || chat.data.message);
        }
    } catch (err: any) {
        console.error("\n❌ [ERROR] Gagal di tengah jalan!");
        console.error("Status:", err.response?.status || "No Status");
        console.log("Detail:", err.response?.data || err.message);
    }
}

simulateRealApp();
