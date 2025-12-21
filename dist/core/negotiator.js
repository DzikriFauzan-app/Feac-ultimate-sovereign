"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SovereignNegotiator = void 0;
const analyzer_1 = require("./analyzer");
const aries_gateway_1 = require("../bridge/aries_gateway");
const feacLogger_1 = require("../utils/feacLogger");
class SovereignNegotiator {
    static async requestSystemUpgrade() {
        const stats = analyzer_1.SelfAnalyzer.analyzeProject();
        if (stats.healthScore < 90) {
            (0, feacLogger_1.feacLog)("NEGOTIATOR", "System health degraded. Negotiating with Aries Kernel...");
            const proposal = `URGENT_UPGRADE: Current Health ${stats.healthScore}%. Optimization required.`;
            return await aries_gateway_1.AriesGateway.requestCognition(proposal, stats);
        }
        (0, feacLogger_1.feacLog)("NEGOTIATOR", "System health optimal. No negotiation needed.");
        return { status: "STABLE" };
    }
}
exports.SovereignNegotiator = SovereignNegotiator;
