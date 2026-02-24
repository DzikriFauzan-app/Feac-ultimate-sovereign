import { MemoryNode } from '../memory/vector_db';

export class PromptComposer {
    static compose(task: string, context: MemoryNode[]): string {
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
