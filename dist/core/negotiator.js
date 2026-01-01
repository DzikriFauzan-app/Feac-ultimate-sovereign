"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Negotiator = void 0;
const aries_gateway_1 = require("../bridge/aries_gateway");
class Negotiator {
    // Method untuk audit sistem (digunakan emulator)
    async startNegotiation(input) {
        console.log("🛰️ [NEGOTIATOR] Memulai negosiasi...");
        return await aries_gateway_1.AriesGateway.requestCognition(input, { source: 'emulator' });
    }
    // Method untuk upgrade (diminta oleh master_test.ts)
    static async requestSystemUpgrade() {
        console.log("🆙 [NEGOTIATOR] Meminta Upgrade Sistem...");
        return { success: true, message: "System Upgrade Initiated" };
    }
}
exports.Negotiator = Negotiator;
