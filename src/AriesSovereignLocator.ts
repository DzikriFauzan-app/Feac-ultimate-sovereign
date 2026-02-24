import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

const PATHS = {
    ARIES: '/data/data/com.termux/files/home/Dzikrifauzan-app/Aries-api-key',
    NEO: '/sdcard/Buku saya/Fauzan engine'
};

class AriesSovereignLocator {
    async locateAndStart() {
        console.log("🕵️ [LOCATOR] MENCARI TITIK KEDAULATAN DI LUAR REPO...");

        // 1. Audit Aries (3000)
        this.processService('ARIES_BRAIN', PATHS.ARIES, 'index.js');

        // 2. Audit Neo Engine (8080)
        this.processService('NEO_ENGINE', PATHS.NEO, 'main.js');

        console.log("\n🚀 [FINAL] Jalankan 'pm2 status' untuk verifikasi.");
    }

    processService(name: string, dir: string, defaultFile: string) {
        if (fs.existsSync(dir)) {
            console.log(`✅ Folder ${name} Ditemukan.`);
            // Mencari file .js utama
            const files = fs.readdirSync(dir);
            const entryPoint = files.find(f => f === defaultFile || f === 'server.js' || f === 'app.js');

            if (entryPoint) {
                const fullPath = path.join(dir, entryPoint);
                console.log(`📡 Mendaftarkan ${name} dari: ${fullPath}`);
                try {
                    execSync(`pm2 start "${fullPath}" --name "${name.toLowerCase()}"`);
                } catch (e) {
                    execSync(`pm2 restart ${name.toLowerCase()}`);
                }
            } else {
                console.error(`❌ ${name}: File utama tidak ditemukan di ${dir}`);
            }
        } else {
            console.error(`❌ Folder ${name} TIDAK DITEMUKAN di ${dir}`);
            console.log("💡 Saran: Pastikan izin storage Termux aktif (termux-setup-storage).");
        }
    }
}

new AriesSovereignLocator().locateAndStart();
