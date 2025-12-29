import { execSync } from 'child_process';
import fs from 'fs';

const TARGETS = [
    '/data/data/com.termux/files/home', // Mencari Dzikrifauzan-app
    '/sdcard/Buku saya/Fauzan engine'    // Membedah isi Neo Engine
];

console.log("🔍 [DEEP-SCANNER] MEMULAI PENCARIAN FILE KRITIKAL...");

TARGETS.forEach(path => {
    console.log(`\n📂 Scanning: ${path}`);
    try {
        if (fs.existsSync(path)) {
            const files = execSync(`ls -R "${path}" | head -n 20`).toString();
            console.log("📄 Isi Folder (Top 20):\n" + files);
        } else {
            console.log("❌ Path tidak ditemukan secara langsung.");
            // Coba cari folder dengan nama mirip
            const search = execSync(`find /data/data/com.termux/files/home -maxdepth 2 -name "*Aries*" || true`).toString();
            console.log("💡 Hasil pencarian alternatif 'Aries':\n" + search);
        }
    } catch (e) {
        console.log("⚠️ Gagal akses path ini.");
    }
});
