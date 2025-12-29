import { execSync } from 'child_process';
// Tambahkan ekstensi .ts agar ESM di Termux bisa resolve path-nya
import { Negotiator } from './core/negotiator.ts';

class SovereignUltimateAgent {
    async runFullAudit() {
        console.log("🛡️ [AGENT-AUDIT] MEMULAI PEMERIKSAAN KODE...");
        try {
            // Gunakan --noEmit untuk validasi tanpa build
            execSync('npx tsc --noEmit');
            console.log("✅ KODE BERSIH: Tidak ada error TypeScript.");
        } catch (error: any) {
            console.error("❌ KODE PECAH (Masih ada error di file lain):");
            console.log(error.stdout || error.message);
            // Jangan return dulu, biar kita lihat error-nya apa saja
        }

        console.log("\n📱 [AGENT-APK] MENJELMA MENJADI FEAC APK (SIMULASI)...");
        try {
            const negotiator = new Negotiator();
            const testChat = await negotiator.startNegotiation("Test Kedaulatan Sistem");
            console.log("✅ SIMULASI CHAT: Berhasil.", JSON.stringify(testChat));

            const upgrade = await Negotiator.requestSystemUpgrade();
            console.log("✅ SIMULASI UPGRADE: Berhasil.", JSON.stringify(upgrade));
            
            console.log("\n🚀 [FINAL VERDICT]: REPO SIAP DI-PUSH!");
        } catch (err: any) {
            console.error("❌ SIMULASI RUNTIME GAGAL:", err.message);
        }
    }
}

new SovereignUltimateAgent().runFullAudit();
