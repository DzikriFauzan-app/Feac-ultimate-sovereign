"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const axios_1 = __importDefault(require("axios"));
const ENDPOINTS = {
    ARIES: 'http://127.0.0.1:3000',
    FEAC_BRIDGE: 'http://127.0.0.1:3001/api/auth/handshake', // Targetkan rute spesifik
    NEO_ENGINE: 'http://10.159.189.152:8080' // Gunakan IP yang terdeteksi di log
};
class AriesConnectivityAgent {
    async checkAll() {
        console.log("🛡️ [CONNECTIVITY-AGENT] SCANNING INFRASTRUKTUR...");
        console.log("---------------------------------------------------");
        await this.testService("🧠 ARIES BRAIN", ENDPOINTS.ARIES);
        await this.testService("🌉 FEAC BRIDGE", ENDPOINTS.FEAC_BRIDGE);
        await this.testService("⚙️ NEO ENGINE", ENDPOINTS.NEO_ENGINE);
        console.log("---------------------------------------------------");
    }
    async testService(name, url) {
        try {
            const start = Date.now();
            const res = await axios_1.default.get(url, { timeout: 2000 });
            console.log(`✅ ${name} - CONNECTED (${Date.now() - start}ms)`);
        }
        catch (error) {
            if (error.response) {
                console.log(`⚠️  ${name} - ACTIVE (Status: ${error.response.status})`);
            }
            else {
                console.error(`❌ ${name} - UNREACHABLE (${url})`);
            }
        }
    }
}
new AriesConnectivityAgent().checkAll();
