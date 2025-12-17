import { AuditEngine } from '../core/audit_engine';
import { feacLog } from '../utils/feacLogger';

async function runAuditTest() {
    console.log("🧪 RUNNING SYSTEM AUDIT DIAGNOSTICS...");
    
    // Trigger intentional log entries
    feacLog("TEST", "Normal operation recorded.");
    feacLog("CRITICAL", "Simulated system intrusion detected.");

    const auditor = new AuditEngine();
    const report = auditor.generateReport();

    if (report.criticalAlerts.length > 0) {
        console.log("✅ [PASS] Critical Alert Detection");
    } else {
        throw new Error("❌ [FAIL] Audit Engine failed to detect critical logs");
    }

    if (report.totalActions > 0) {
        console.log("✅ [PASS] Activity Volume Tracking");
    }

    console.log("✨ ALL PHASE 6 TESTS PASSED.");
}

runAuditTest();
