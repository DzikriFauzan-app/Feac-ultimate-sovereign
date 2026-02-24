"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
const BRIDGE_URL = 'https://redesigned-yodel-7v6wjx4r9x653ww6g-3001.app.github.dev';
const OWNER_KEY = 'aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1';
async function runTest() {
    console.log("🧪 [TEST] Memulai pengujian koneksi ke Codespace...");
    console.log("🔗 URL: " + BRIDGE_URL);
    try {
        console.log("\n1️⃣ Mengetes Health Check...");
        const health = await axios_1.default.get(`${BRIDGE_URL}/health`);
        console.log("✅ Response:", health.data);
        console.log("\n2️⃣ Mengetes Owner Key Bypass...");
        const auth = await axios_1.default.post(`${BRIDGE_URL}/api/validate-key`, {
            apiKey: OWNER_KEY
        });
        if (auth.data.success && auth.data.message === 'AUTHORIZED') {
            console.log("👑 [SUCCESS] Owner Access Terverifikasi!");
        }
        else {
            console.log("❌ [FAILED] Owner Access Gagal:", auth.data);
        }
    }
    catch (err) {
        console.error("\n❌ [ERROR] Gagal menyambung ke Codespace.");
        console.error("Pesan:", err.message || "Unknown Error");
        console.log("\n💡 TIPS: Pastikan di Codespace Port 3001 sudah diset ke PUBLIC.");
    }
}
runTest();
