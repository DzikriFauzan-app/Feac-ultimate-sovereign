"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
async function stressTest() {
    console.log("🗣️ [SIMULASI] MEMULAI 20 CHAT SERIUS...");
    for (let i = 1; i <= 20; i++) {
        const res = await axios_1.default.post('http://127.0.0.1:3001/api/chat', {
            message: `Diskusi Teori Kedaulatan Digital Tahap ${i}: Analisa integrasi 40 agen NeoEngine.`
        });
        console.log(`💬 Chat ${i}: ${res.status === 200 ? 'SUCCESS' : 'FAIL'}`);
    }
}
stressTest();
