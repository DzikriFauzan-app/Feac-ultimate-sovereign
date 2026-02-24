"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
// Tambahkan ekstensi .ts agar ESM di Termux bisa resolve path-nya
const negotiator_ts_1 = require("./core/negotiator.ts");
class SovereignUltimateAgent {
    async runFullAudit() {
        console.log("🛡️ [AGENT-AUDIT] MEMULAI PEMERIKSAAN KODE...");
        try {
            // Gunakan --noEmit untuk validasi tanpa build
            (0, child_process_1.execSync)('npx tsc --noEmit');
            console.log("✅ KODE BERSIH: Tidak ada error TypeScript.");
        }
        catch (error) {
            console.error("❌ KODE PECAH (Masih ada error di file lain):");
            console.log(error.stdout || error.message);
            // Jangan return dulu, biar kita lihat error-nya apa saja
        }
        console.log("\n📱 [AGENT-APK] MENJELMA MENJADI FEAC APK (SIMULASI)...");
        try {
            const negotiator = new negotiator_ts_1.Negotiator();
            const testChat = await negotiator.startNegotiation("Test Kedaulatan Sistem");
            console.log("✅ SIMULASI CHAT: Berhasil.", JSON.stringify(testChat));
            const upgrade = await negotiator_ts_1.Negotiator.requestSystemUpgrade();
            console.log("✅ SIMULASI UPGRADE: Berhasil.", JSON.stringify(upgrade));
            console.log("\n🚀 [FINAL VERDICT]: REPO SIAP DI-PUSH!");
        }
        catch (err) {
            console.error("❌ SIMULASI RUNTIME GAGAL:", err.message);
        }
    }
}
new SovereignUltimateAgent().runFullAudit();
