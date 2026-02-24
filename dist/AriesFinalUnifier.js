"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const fs_1 = __importDefault(require("fs"));
class AriesFinalUnifier {
    run() {
        console.log("🏛️ [UNIFIER] EXECUTING SOVEREIGN ALIGNMENT...");
        // 1. Aries Brain (Jantung Utama - Port 3000)
        const ariesPath = '/data/data/com.termux/files/home/Aries-api-key/dist/index.js';
        this.safeStart('aries-brain', ariesPath, 'node');
        // 2. Neo Engine Server (Kekuatan 40 Agen - Port 8080)
        const neoServerPath = '/sdcard/Buku saya/Fauzan engine/NeoEngine/engine_server.py';
        this.safeStart('neo-engine', neoServerPath, 'python3');
        console.log("\n🚀 [STATUS] Verifikasi dengan: npx ts-node --esm src/AriesPortRescuer.ts");
    }
    safeStart(name, path, interpreter) {
        try {
            (0, child_process_1.execSync)(`pm2 delete ${name} || true`);
            if (fs_1.default.existsSync(path)) {
                (0, child_process_1.execSync)(`pm2 start "${path}" --name "${name}" --interpreter ${interpreter}`);
                console.log(`✅ ${name} AKTIF: ${path}`);
            }
            else {
                console.error(`❌ PATH TIDAK DITEMUKAN: ${path}`);
            }
        }
        catch (e) {
            console.error(`⚠️ Gagal inisialisasi ${name}`);
        }
    }
}
new AriesFinalUnifier().run();
