"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const fs_1 = __importDefault(require("fs"));
class AriesGitAuditor {
    constructor() {
        this.name = "Aries GitHub Recovery Agent";
    }
    runAudit() {
        console.log(`🛡️ Starting ${this.name}...`);
        try {
            // 1. Periksa Status Disk & Git
            console.log("\n📊 [AUDIT] Checking Git Status & Locks...");
            const status = (0, child_process_1.execSync)('git status').toString();
            console.log(status);
            // 2. Deteksi Kenapa Gak Bisa Commit (Check index.lock)
            if (fs_1.default.existsSync('.git/index.lock')) {
                console.warn("⚠️ [ALERT] Found git index.lock! This prevents commits. Deleting...");
                fs_1.default.unlinkSync('.git/index.lock');
            }
            // 3. Periksa Konfigurasi Remote
            console.log("\n🔗 [AUDIT] Checking Remote URLs...");
            const remotes = (0, child_process_1.execSync)('git remote -v').toString();
            console.log(remotes);
            // 4. Periksa Masalah Autentikasi
            console.log("\n🔑 [AUDIT] Checking GitHub Auth Status...");
            try {
                const authStatus = (0, child_process_1.execSync)('gh auth status').toString();
                console.log(authStatus);
            }
            catch (e) {
                console.error("❌ [ERROR] GitHub CLI (gh) not authenticated or not installed.");
            }
            // 5. Diagnosa Codespaces Suggestion
            console.log("\n💡 [DIAGNOSIS] Codespaces Push Failure...");
            console.log("- Recommendation: If commit fails, try: git add . && git commit -m 'Force Sync'");
            console.log("- Recommendation: If push fails, check if you are in a 'Detached HEAD' state.");
        }
        catch (error) {
            console.error("❌ [CRITICAL] Audit Interrupted:", error.message);
        }
    }
    generateEvacuationPlan() {
        console.log("\n🚀 [EVACUATION PLAN] Since you want a new link:");
        console.log("1. Create a NEW Repository on GitHub.");
        console.log("2. Run: git remote set-url origin <NEW_REPO_URL>");
        console.log("3. Run: git push -u origin main");
    }
}
const auditor = new AriesGitAuditor();
auditor.runAudit();
auditor.generateEvacuationPlan();
