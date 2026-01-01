"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const audit_engine_1 = require("../core/audit_engine");
const feacLogger_1 = require("../utils/feacLogger");
async function runAuditTest() {
    console.log("🧪 RUNNING SYSTEM AUDIT DIAGNOSTICS...");
    // Trigger intentional log entries
    (0, feacLogger_1.feacLog)("TEST", "Normal operation recorded.");
    (0, feacLogger_1.feacLog)("CRITICAL", "Simulated system intrusion detected.");
    const auditor = new audit_engine_1.AuditEngine();
    const report = auditor.generateReport();
    if (report.criticalAlerts.length > 0) {
        console.log("✅ [PASS] Critical Alert Detection");
    }
    else {
        throw new Error("❌ [FAIL] Audit Engine failed to detect critical logs");
    }
    if (report.totalActions > 0) {
        console.log("✅ [PASS] Activity Volume Tracking");
    }
    console.log("✨ ALL PHASE 6 TESTS PASSED.");
}
runAuditTest();
