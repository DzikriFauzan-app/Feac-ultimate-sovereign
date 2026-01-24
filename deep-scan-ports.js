import http from 'http';

const targetPorts = [3000, 3001, 3333, 4173, 5173, 8080];

console.log("🕵️ [DEEP_SCAN] Mencari Aries & FEAC di berbagai port...\n");

const scan = (port) => {
    return new Promise((resolve) => {
        const req = http.get(`http://localhost:${port}`, { timeout: 1000 }, (res) => {
            console.log(`📡 Port ${port}: FOUND (Status: ${res.statusCode})`);
            resolve(port);
        });
        req.on('error', () => resolve(null));
        req.on('timeout', () => { req.destroy(); resolve(null); });
    });
};

async function runScan() {
    for (const port of targetPorts) {
        await scan(port);
    }
    console.log("\nScan Selesai. Gunakan port yang 'FOUND' untuk konfigurasi FEAC.");
}

runScan();
