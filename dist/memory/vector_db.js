"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.VectorDB = void 0;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const feacLogger_1 = require("../utils/feacLogger");
class VectorDB {
    storagePath = path_1.default.join(process.cwd(), 'data/vault/memory.json');
    constructor() {
        if (!fs_1.default.existsSync(path_1.default.dirname(this.storagePath))) {
            fs_1.default.mkdirSync(path_1.default.dirname(this.storagePath), { recursive: true });
        }
    }
    async save(node) {
        (0, feacLogger_1.feacLog)("MEMORY", `Storing new memory node: ${node.tag}`);
        const data = this.loadAll();
        data.push(node);
        fs_1.default.writeFileSync(this.storagePath, JSON.stringify(data, null, 2));
    }
    loadAll() {
        if (!fs_1.default.existsSync(this.storagePath))
            return [];
        return JSON.parse(fs_1.default.readFileSync(this.storagePath, 'utf-8'));
    }
    search(query) {
        const all = this.loadAll();
        // Simple Weighted Search (Industry Grade Minimal)
        return all.filter(n => n.content.toLowerCase().includes(query.toLowerCase()))
            .sort((a, b) => b.importance - a.importance);
    }
}
exports.VectorDB = VectorDB;
