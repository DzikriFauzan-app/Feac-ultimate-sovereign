import axios from 'axios';

class AriesAuthAgent {
    private targetUrl = "http://127.0.0.1:3001/api/auth/handshake";
    private testKey = "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1";

    async simulateInput() {
        console.log("📱 [AUTH-AGENT] Memulai simulasi input API Key...");
        try {
            const response = await axios.post(this.targetUrl, {
                apiKey: this.testKey,
                timestamp: new Date().toISOString()
            });

            if (response.data.success) {
                console.log("\n🎊 [RESULT] KONEKSI LOKAL BERHASIL!");
                console.log("📊 Status: " + response.data.status);
                console.log("👑 Role: " + response.data.role);
            }
        } catch (error: any) {
            console.error("\n💀 [RESULT] KONEKSI GAGAL!");
            console.error("Alasan:", error.response?.data?.status || error.message);
        }
    }
}

new AriesAuthAgent().simulateInput();
