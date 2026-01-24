import http from 'http';

const ports = [
    { name: 'ARIES (Intelligence)', port: 3333 },
    { name: 'NEOENGINE (Execution)', port: 8080 },
    { name: 'FEAC (UI/Dashboard)', port: 3000 }
];

console.log("🔍 [LOCAL_TEST] Memulai Validasi Infrastruktur FEAC (ESM Mode)...\n");

const checkPort = (service) => {
    return new Promise((resolve) => {
        const req = http.get(`http://localhost:${service.port}`, (res) => {
            console.log(`✅ ${service.name} di Port ${service.port}: ONLINE (Status: ${res.statusCode})`);
            resolve(true);
        });

        req.on('error', () => {
            console.log(`❌ ${service.name} di Port ${service.port}: OFFLINE`);
            resolve(false);
        });

        req.setTimeout(2000, () => {
            req.destroy();
            console.log(`❌ ${service.name} di Port ${service.port}: TIMEOUT`);
            resolve(false);
        });
    });
};

async function runTest() {
    let allOk = true;
    for (const service of ports) {
        const ok = await checkPort(service);
        if (!ok) allOk = false;
    }
    
    console.log("\n-------------------------------------------");
    if (allOk) {
        console.log("🚀 STATUS: SIAP UNTUK TESTING WEB (LOCAL)");
        console.log("Semua jalur (3333, 8080, 3000) terhubung.");
    } else {
        console.log("⚠️ STATUS: PERIKSA SERVICE PM2 ANDA");
        console.log("Gunakan 'pm2 status' untuk memastikan semua port aktif.");
    }
    console.log("-------------------------------------------\n");
}

runTest();
