import { execSync } from 'child_process';
import fs from 'fs';

class AriesWorkflowPathologist {
    analyze() {
        console.log("🕵️ [PATHOLOGIST] MEMBEDAH WORKFLOW & ARTEFAK...");

        const workflowPath = '.github/workflows/';
        if (!fs.existsSync(workflowPath)) {
            console.error("❌ ERROR: Folder .github/workflows tidak ditemukan!");
            return;
        }

        const files = fs.readdirSync(workflowPath);
        files.forEach(file => {
            console.log(`\n📄 Memeriksa: ${file}`);
            const content = fs.readFileSync(`${workflowPath}${file}`, 'utf8');

            // 1. Cek Port Exposure
            if (!content.includes('3001')) {
                console.warn("⚠️  [DIAGNOSA]: Workflow tidak menyebutkan Port 3001. Bridge mungkin terisolasi.");
            }

            // 2. Cek Environment Variables
            if (!content.includes('ARIES_API_KEY')) {
                console.warn("⚠️  [DIAGNOSA]: Secrets ARIES_API_KEY tidak di-inject ke Workflow.");
            }

            // 3. Cek Kesalahan CommonJS vs ESM
            if (content.includes('node index.js') && !content.includes('type: module')) {
                console.warn("⚠️  [DIAGNOSA]: Workflow mencoba menjalankan Node tanpa mode ESM.");
            }
        });

        this.checkArtifactSymptom();
    }

    checkArtifactSymptom() {
        console.log("\n📦 [ANALISA ARTEFAK]:");
        console.log("- Jika Bridge Connection Gagal, biasanya karena IP di Workflows bersifat DINAMIS.");
        console.log("- Solusi: Pastikan Workflow menggunakan 'actions/upload-artifact' untuk menyimpan log server.");
        console.log("- Saran: Cek apakah ada 'CORS Error' di log artefak.");
    }
}

new AriesWorkflowPathologist().analyze();
