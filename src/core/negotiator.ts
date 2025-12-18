import { SelfAnalyzer } from './analyzer';
import { AriesGateway } from '../bridge/aries_gateway';
import { feacLog } from '../utils/feacLogger';

export class SovereignNegotiator {
    static async requestSystemUpgrade() {
        const stats = SelfAnalyzer.analyzeProject();
        
        if (stats.healthScore < 90) {
            feacLog("NEGOTIATOR", "System health degraded. Negotiating with Aries Kernel...");
            const proposal = `URGENT_UPGRADE: Current Health ${stats.healthScore}%. Optimization required.`;
            return await AriesGateway.requestCognition(proposal, stats);
        }
        
        feacLog("NEGOTIATOR", "System health optimal. No negotiation needed.");
        return { status: "STABLE" };
    }
}
