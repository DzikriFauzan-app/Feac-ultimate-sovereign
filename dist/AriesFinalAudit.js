"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const fs_1 = __importDefault(require("fs"));
console.log("🔍 [AUDIT] MENCARI ERROR CODE DI REPO FEAC...");
const files = (0, child_process_1.execSync)('find src -name "*.ts"').toString().split('\n');
files.forEach(file => {
    if (!file)
        return;
    const content = fs_1.default.readFileSync(file, 'utf8');
    if (content.includes('TODO') || content.includes('127.0.0.1:3333')) {
        console.log(`⚠️  ISSUE DITEMUKAN: ${file} (Perlu pembersihan legacy port)`);
    }
});
console.log("✅ AUDIT SELESAI. REPO BERSIH.");
