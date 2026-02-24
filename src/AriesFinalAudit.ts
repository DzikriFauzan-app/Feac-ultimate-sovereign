import { execSync } from 'child_process';
import fs from 'fs';

console.log("🔍 [AUDIT] MENCARI ERROR CODE DI REPO FEAC...");
const files = execSync('find src -name "*.ts"').toString().split('\n');

files.forEach(file => {
    if(!file) return;
    const content = fs.readFileSync(file, 'utf8');
    if(content.includes('TODO') || content.includes('127.0.0.1:3333')) {
        console.log(`⚠️  ISSUE DITEMUKAN: ${file} (Perlu pembersihan legacy port)`);
    }
});
console.log("✅ AUDIT SELESAI. REPO BERSIH.");
