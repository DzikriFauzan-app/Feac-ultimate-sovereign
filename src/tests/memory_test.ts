import { VectorDB } from '../memory/vector_db';
import { PromptComposer } from '../core/prompt_composer';

async function testMemory() {
    console.log("🧪 RUNNING MEMORY & COGNITION TEST...");
    const db = new VectorDB();
    
    const node = {
        id: "MEM-1",
        tag: "PROJECT_GOAL",
        content: "Build a game engine better than Godot",
        importance: 10,
        timestamp: Date.now()
    };
    
    await db.save(node);
    const results = db.search("game engine");
    
    if (results.length > 0 && results[0].tag === "PROJECT_GOAL") {
        console.log("✅ [PASS] Memory Retrieval");
    } else {
        throw new Error("❌ [FAIL] Memory Retrieval");
    }

    const prompt = PromptComposer.compose("Generate physics module", results);
    if (prompt.includes("PROJECT_GOAL")) {
        console.log("✅ [PASS] Prompt Composition with Context");
    } else {
        throw new Error("❌ [FAIL] Prompt Composition");
    }

    console.log("✨ ALL PHASE 4 TESTS PASSED.");
}

testMemory();
