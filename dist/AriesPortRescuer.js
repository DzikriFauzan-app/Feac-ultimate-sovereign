"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const net_1 = __importDefault(require("net"));
const PORTS = [3000, 3001, 8080];
console.log("🕵️ [RESCUER] MEMERIKSA KETERSEDIAAN PORT...");
PORTS.forEach(port => {
    const tester = net_1.default.createServer()
        .once('error', (err) => {
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
