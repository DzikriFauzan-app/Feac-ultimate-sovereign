import axios from 'axios';
import { execSync } from 'child_process';

const CONFIG = {
    bridgeUrl: 'https://redesigned-yodel-7v6wjx4r9x653ww6g-3001.app.github.dev',
    ownerKey: 'aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1',
    testMessage: "Aries, lakukan audit kedaulatan pada sistem ini."
};

class FeacSovereignEmulator {
    async startSimulation() {
        console.log("🏛️ [EMULATOR] MENGAKTIFKAN FEAC SOVEREIGN VIRTUAL CORE...");
        
        try {
            // 1. DIAGNOSIS KODE (Mencari Akar Masalah Kompilasi)
            this.diagnoseSourceCode();

            // 2. SIMULASI INPUT API KEY (Handshake Test)
            await this.simulateLogin();

            // 3. SIMULASI DASHBOARD CHAT (Real Interaction Test)
            await this.simulateChat();

        } catch (error: any) {
            console.error("\n💀 [FATAL SYSTEM ERROR]:");
            this.analyzeRootCause(error);
        }
    }

    diagnoseSourceCode() {
        console.log("\n🔍 [1] AUDIT KODE SUMBER...");
        try {
            execSync('npx tsc --noEmit');
            console.log("✅ Kode Sumber: BERSIH (Siap Deploy)");
        } catch (e: any) {
            console.warn("❌ Kode Sumber: PECAH");
            if (e.stdout.includes('requestCognition')) {
                console.log("💡 AKAR MASALAH: 'negotiator.ts' memanggil method yang hilang di 'aries_gateway.ts'.");
            }
        }
    }

    async simulateLogin() {
        console.log("\n🔑 [2] SIMULASI INPUT API KEY DI APK...");
        const res = await axios.post(`${CONFIG.bridgeUrl}/api/validate-key`, { apiKey: CONFIG.ownerKey });
        if (res.data.success) {
            console.log("✅ Handshake Berhasil. Role: " + res.data.role);
        }
    }

    async simulateChat() {
        console.log("\n💬 [3] SIMULASI CHAT ARIES (DASHBOARD)...");
        const res = await axios.post(`${CONFIG.bridgeUrl}/api/chat`, {
            apiKey: CONFIG.ownerKey,
            message: CONFIG.testMessage
        });
        console.log("🤖 [RESPONSE ARIES]:", res.data.response || res.data.message);
    }

    analyzeRootCause(err: any) {
        if (err.response?.status === 404) {
            console.log("🚨 SOLUSI: Endpoint tidak ditemukan. Pastikan 'npm run dev' di Codespaces sudah rilis rute /api/validate-key.");
        } else if (err.code === 'ECONNREFUSED') {
            console.log("🚨 SOLUSI: Koneksi ditolak. Cek apakah Port 3001 di Codespace sudah PUBLIC.");
        } else {
            console.log("🚨 DETAIL:", err.message);
        }
    }
}

new FeacSovereignEmulator().startSimulation();
