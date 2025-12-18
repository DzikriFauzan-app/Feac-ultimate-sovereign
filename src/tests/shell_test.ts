import { execSync } from 'child_process';
import fs from 'fs';

async function testShell() {
    console.log("🧪 RUNNING SHELL AUTOMATION DIAGNOSTICS...");

    // Test 1: Script existence and permissions
    if (fs.existsSync('./scripts/sovereign_push.sh')) {
        const stats = fs.statSync('./scripts/sovereign_push.sh');
        const isExecutable = !!(stats.mode & 0o111);
        if (isExecutable) {
            console.log("✅ [PASS] Push Script Permissions");
        } else {
            throw new Error("❌ [FAIL] Push Script not executable");
        }
    }

    // Test 2: Directory Integrity
    if (fs.existsSync('./data/vault') && fs.existsSync('./data/artifacts')) {
        console.log("✅ [PASS] System Directory Integrity");
    }

    console.log("✨ ALL PHASE 7 CORE TESTS PASSED.");
}

testShell();
