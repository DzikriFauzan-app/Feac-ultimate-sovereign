import fs from 'fs';
import path from 'path';
import { feacLog } from '../utils/feacLogger';

export interface MemoryNode {
    id: string;
    tag: string;
    content: string;
    importance: number;
    timestamp: number;
}

export class VectorDB {
    private storagePath = path.join(process.cwd(), 'data/vault/memory.json');

    constructor() {
        if (!fs.existsSync(path.dirname(this.storagePath))) {
            fs.mkdirSync(path.dirname(this.storagePath), { recursive: true });
        }
    }

    async save(node: MemoryNode): Promise<void> {
        feacLog("MEMORY", `Storing new memory node: ${node.tag}`);
        const data = this.loadAll();
        data.push(node);
        fs.writeFileSync(this.storagePath, JSON.stringify(data, null, 2));
    }

    loadAll(): MemoryNode[] {
        if (!fs.existsSync(this.storagePath)) return [];
        return JSON.parse(fs.readFileSync(this.storagePath, 'utf-8'));
    }

    search(query: string): MemoryNode[] {
        const all = this.loadAll();
        // Simple Weighted Search (Industry Grade Minimal)
        return all.filter(n => n.content.toLowerCase().includes(query.toLowerCase()))
                  .sort((a, b) => b.importance - a.importance);
    }
}
