"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AriesKernelConnector = void 0;
const axios_1 = __importDefault(require("axios"));
class AriesKernelConnector {
    static KERNEL_URL = "http://127.0.0.1:3333/v1/command";
    static async execute(input, session) {
        try {
            const response = await axios_1.default.post(this.KERNEL_URL, {
                session_id: session,
                user_id: "sovereign_operator",
                input: input
            }, {
                headers: { "x-aries-key": "aries-sovereign-ultimate" }
            });
            return response.data;
        }
        catch (error) {
            return { status: "OFFLINE", message: "Kernel Aries tidak terdeteksi." };
        }
    }
}
exports.AriesKernelConnector = AriesKernelConnector;
