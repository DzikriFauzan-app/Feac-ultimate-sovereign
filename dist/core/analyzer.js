"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.SelfAnalyzer = void 0;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const feacLogger_1 = require("../utils/feacLogger");
class SelfAnalyzer {
    static analyzeProject() {
        (0, feacLogger_1.feacLog)("ANALYZER", "Scanning Sovereign Codebase...");
        const files = this.walkDir(path_1.default.join(process.cwd(), 'src'));
        const report = {
            fileCount: files.length,
            totalLoc: 0,
            healthScore: 100
        };
        files.forEach(file => {
            const content = fs_1.default.readFileSync(file, 'utf-8');
            report.totalLoc += content.split('\n').length;
            if (content.includes('TODO') || content.includes('FIXME'))
                report.healthScore -= 5;
        });
        return report;
    }
    static walkDir(dir) {
        let results = [];
        const list = fs_1.default.readdirSync(dir);
        list.forEach(file => {
            file = path_1.default.resolve(dir, file);
            const stat = fs_1.default.statSync(file);
            if (stat && stat.isDirectory())
                results = results.concat(this.walkDir(file));
            else if (file.endsWith('.ts'))
                results.push(file);
        });
        return results;
    }
}
exports.SelfAnalyzer = SelfAnalyzer;
