"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NeoEngineService = void 0;
/**
 * FEAC Service untuk berkomunikasi dengan NeoEngine (Port 8080)
 */
const NEO_ENGINE_URL = 'http://localhost:8080';
exports.NeoEngineService = {
    async sendCommand(taskType) {
        console.log(`📡 [FEAC -> NEO] Mengirim perintah ke 8080: ${taskType}`);
        try {
            const response = await fetch(`${NEO_ENGINE_URL}/execute`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ task: taskType })
            });
            return await response.json();
        }
        catch (error) {
            console.error("❌ NeoEngine Offline atau Port 8080 Tertutup");
        }
    }
};
