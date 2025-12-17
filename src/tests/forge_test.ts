import { CodeGenerator } from '../compiler/code_generator';
import { ArtifactValidator } from '../artifacts/schemas/sovereignArtifact';
import { StorageManager } from '../artifacts/storage_manager';
import fs from 'fs';

async function runTest() {
    console.log("🧪 RUNNING FORGE SYSTEM TEST...");
    
    const generator = new CodeGenerator();
    const storage = new StorageManager();
    
    // Test 1: Generation
    const code = "console.log('Sovereign Active');";
    const artifact = generator.generate("test_pulse", "typescript", code);
    
    if (ArtifactValidator.validate(artifact)) {
        console.log("✅ [PASS] Artifact Validation");
    } else {
        throw new Error("❌ [FAIL] Artifact Validation");
    }

    // Test 2: Persistence
    const path = storage.save(artifact);
    if (fs.existsSync(path)) {
        console.log("✅ [PASS] Persistence Storage");
    } else {
        throw new Error("❌ [FAIL] Persistence Storage");
    }

    console.log("✨ ALL PHASE 2 CORE TESTS PASSED.");
}

runTest().catch(err => {
    console.error(err.message);
    process.exit(1);
});
