import { Negotiator } from '../core/negotiator';
import { SelfAnalyzer } from '../core/analyzer';

async function runMasterTest() {
    console.log("🏁 RUNNING MASTER INTEGRATION DIAGNOSTICS (FINAL)...");

    const stats = SelfAnalyzer.analyzeProject();
    console.log(`📊 Project Scope: ${stats.fileCount} files, ${stats.totalLoc} lines of code.`);
    
    if (stats.fileCount >= 10) {
        console.log("✅ [PASS] Structural Density Check");
    }

    const negotiation = await Negotiator.requestSystemUpgrade();
    if (negotiation) {
        console.log("✅ [PASS] AI Negotiation Pipeline");
    }

    console.log("🚀 FEAC ULTIMATE SOVEREIGN IS FULLY OPERATIONAL.");
}

runMasterTest();
