"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const code_generator_1 = require("../compiler/code_generator");
const sovereignArtifact_1 = require("../artifacts/schemas/sovereignArtifact");
const storage_manager_1 = require("../artifacts/storage_manager");
const fs_1 = __importDefault(require("fs"));
async function runTest() {
    console.log("🧪 RUNNING FORGE SYSTEM TEST...");
    const generator = new code_generator_1.CodeGenerator();
    const storage = new storage_manager_1.StorageManager();
    // Test 1: Generation
    const code = "console.log('Sovereign Active');";
    const artifact = generator.generate("test_pulse", "typescript", code);
    if (sovereignArtifact_1.ArtifactValidator.validate(artifact)) {
        console.log("✅ [PASS] Artifact Validation");
    }
    else {
        throw new Error("❌ [FAIL] Artifact Validation");
    }
    // Test 2: Persistence
    const path = storage.save(artifact);
    if (fs_1.default.existsSync(path)) {
        console.log("✅ [PASS] Persistence Storage");
    }
    else {
        throw new Error("❌ [FAIL] Persistence Storage");
    }
    console.log("✨ ALL PHASE 2 CORE TESTS PASSED.");
}
runTest().catch(err => {
    console.error(err.message);
    process.exit(1);
});
