"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AriesGateway = void 0;
const axios_1 = __importDefault(require("axios"));
class AriesGateway {
    static ARIES_ENDPOINT = "http://127.0.0.1:3333/v1/brain";
    static async requestCognition(prompt, context) {
        try {
            const response = await axios_1.default.post(this.ARIES_ENDPOINT, {
                intent: "COGNITIVE_REQUEST",
                payload: { prompt, context },
                timestamp: Date.now()
            }, {
                headers: { "x-aries-key": "aries-sovereign-ultimate" }
            });
            return response.data;
        }
        catch (error) {
            console.error("[ARIES_GATEWAY] Connection lost to Kernel.");
            return null;
        }
    }
}
exports.AriesGateway = AriesGateway;
