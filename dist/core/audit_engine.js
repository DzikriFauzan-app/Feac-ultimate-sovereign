"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuditEngine = void 0;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const feacLogger_1 = require("../utils/feacLogger");
class AuditEngine {
    constructor() {
        this.logPath = path_1.default.join(process.cwd(), 'data/logs/feac_system.log');
    }
    generateReport() {
        (0, feacLogger_1.feacLog)("AUDIT", "Generating System Health Report...");
        const logs = fs_1.default.readFileSync(this.logPath, 'utf-8').split('\n');
        const criticalAlerts = logs.filter(l => l.includes('[CRITICAL]'))
            .map(l => l.split('] ').pop() || "");
        return {
            timestamp: Date.now(),
            totalActions: logs.length,
            failures: logs.filter(l => l.includes('failed') || l.includes('error')).length,
            criticalAlerts: criticalAlerts.slice(-5) // Ambil 5 terakhir
        };
    }
}
exports.AuditEngine = AuditEngine;
