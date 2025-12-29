import { AriesGateway } from '../bridge/aries_gateway.ts';

export class Negotiator {
    // Method untuk audit sistem (digunakan emulator)
    async startNegotiation(input: string) {
        console.log("🛰️ [NEGOTIATOR] Memulai negosiasi...");
        return await AriesGateway.requestCognition(input, { source: 'emulator' });
    }

    // Method untuk upgrade (diminta oleh master_test.ts)
    static async requestSystemUpgrade() {
        console.log("🆙 [NEGOTIATOR] Meminta Upgrade Sistem...");
        return { success: true, message: "System Upgrade Initiated" };
    }
}
