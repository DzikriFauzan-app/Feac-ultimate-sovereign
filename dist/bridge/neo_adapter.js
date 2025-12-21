"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.NeoAdapter = void 0;
const axios_1 = __importDefault(require("axios"));
const feacLogger_1 = require("../utils/feacLogger");
class NeoAdapter {
    static NEO_URL = "http://127.0.0.1:5000/render";
    static async dispatchRenderTask(taskId, payload) {
        (0, feacLogger_1.feacLog)("BRIDGE", `Connecting to Neo Engine for Task: ${taskId}`);
        try {
            const response = await axios_1.default.post(this.NEO_URL, {
                task_id: taskId,
                payload,
                timestamp: Date.now()
            }, { timeout: 2000 });
            return response.data;
        }
        catch (error) {
            (0, feacLogger_1.feacLog)("BRIDGE", "Neo Engine status: OFFLINE (Expected in standalone test)");
            return { status: "OFFLINE" };
        }
    }
}
exports.NeoAdapter = NeoAdapter;
