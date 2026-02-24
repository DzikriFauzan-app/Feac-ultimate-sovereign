import fs from 'fs';
import path from 'path';
import { feacLog } from '../utils/feacLogger';

export interface AuditReport {
    timestamp: number;
    totalActions: number;
    failures: number;
    criticalAlerts: string[];
}

export class AuditEngine {
    private logPath = path.join(process.cwd(), 'data/logs/feac_system.log');

    generateReport(): AuditReport {
        feacLog("AUDIT", "Generating System Health Report...");
        const logs = fs.readFileSync(this.logPath, 'utf-8').split('\n');
        
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
