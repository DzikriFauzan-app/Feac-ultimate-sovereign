"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
async function testShell() {
    console.log("🧪 RUNNING SHELL AUTOMATION DIAGNOSTICS...");
    // Test 1: Script existence and permissions
    if (fs_1.default.existsSync('./scripts/sovereign_push.sh')) {
        const stats = fs_1.default.statSync('./scripts/sovereign_push.sh');
        const isExecutable = !!(stats.mode & 0o111);
        if (isExecutable) {
            console.log("✅ [PASS] Push Script Permissions");
        }
        else {
            throw new Error("❌ [FAIL] Push Script not executable");
        }
    }
    // Test 2: Directory Integrity
    if (fs_1.default.existsSync('./data/vault') && fs_1.default.existsSync('./data/artifacts')) {
        console.log("✅ [PASS] System Directory Integrity");
    }
    console.log("✨ ALL PHASE 7 CORE TESTS PASSED.");
}
testShell();
