import net from 'net';

const PORTS = [3000, 3001, 8080];

console.log("🕵️ [RESCUER] MEMERIKSA KETERSEDIAAN PORT...");

PORTS.forEach(port => {
    const tester = net.createServer()
        .once('error', (err: any) => {
            if (err.code === 'EADDRINUSE') {
                console.log(`✅ Port ${port}: TERPAKAI (Aplikasi berjalan)`);
            }
        })
        .once('listening', () => {
            console.log(`❌ Port ${port}: KOSONG (Aplikasi tidak mendengarkan)`);
            tester.close();
        })
        .listen(port, '127.0.0.1');
});
