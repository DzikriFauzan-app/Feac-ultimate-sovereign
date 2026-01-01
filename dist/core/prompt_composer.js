"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PromptComposer = void 0;
class PromptComposer {
    static compose(task, context) {
        const contextString = context.map(c => `[CONTEXT: ${c.tag}] ${c.content}`).join('\n');
        return `### SOVEREIGN INSTRUCTION
TASK: ${task}

### RELEVANT MEMORY
${contextString || "No previous context found."}

### EXECUTION RULES
1. Maintain industrial grade stability.
2. Ensure strict security validation.
3. Align with Aries Kernel Policy.`;
    }
}
exports.PromptComposer = PromptComposer;
