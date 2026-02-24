"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const fs_1 = __importDefault(require("fs"));
const TARGETS = [
    '/data/data/com.termux/files/home', // Mencari Dzikrifauzan-app
    '/sdcard/Buku saya/Fauzan engine' // Membedah isi Neo Engine
];
console.log("🔍 [DEEP-SCANNER] MEMULAI PENCARIAN FILE KRITIKAL...");
TARGETS.forEach(path => {
    console.log(`\n📂 Scanning: ${path}`);
    try {
        if (fs_1.default.existsSync(path)) {
            const files = (0, child_process_1.execSync)(`ls -R "${path}" | head -n 20`).toString();
            console.log("📄 Isi Folder (Top 20):\n" + files);
        }
        else {
            console.log("❌ Path tidak ditemukan secara langsung.");
            // Coba cari folder dengan nama mirip
            const search = (0, child_process_1.execSync)(`find /data/data/com.termux/files/home -maxdepth 2 -name "*Aries*" || true`).toString();
            console.log("💡 Hasil pencarian alternatif 'Aries':\n" + search);
        }
    }
    catch (e) {
        console.log("⚠️ Gagal akses path ini.");
    }
});
