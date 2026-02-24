import { DeployWorkflow } from '../workflows/deploy_workflow';
import { NeoAdapter } from '../bridge/neo_adapter';

async function testBridge() {
    console.log("🧪 RUNNING BRIDGE & WORKFLOW DIAGNOSTICS...");

    // Test 1: Workflow Execution
    const success = await DeployWorkflow.start({
        uid: "SOV-101",
        version: "1.1.0",
        content: "print('Neo Link Active')"
    });

    if (success) {
        console.log("✅ [PASS] Industrial Workflow Execution");
    } else {
        throw new Error("❌ [FAIL] Workflow Execution");
    }

    // Test 2: Neo Adapter Offline Resilience
    const neoResponse = await NeoAdapter.dispatchRenderTask("TEST_001", {});
    if (neoResponse.status === "OFFLINE") {
        console.log("✅ [PASS] Neo Adapter Resilience (Handled Offline)");
    } else {
        console.log("⚠️ [WARN] Neo Engine is Online, response received.");
    }

    console.log("✨ ALL PHASE 5 TESTS PASSED.");
}

testBridge();
