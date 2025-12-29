import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';

class AriesSystemAuditor {
    name: string = "Aries Codespaces & Code Error Auditor";

    run() {
        console.log("🛡️ [AGENT] MEMULAI AUDIT TOTAL SISTEM...");

        // 1. CEK GITHUB & CODESPACES SUGGESTIONS
        this.checkCodespacesIssues();

        // 2. SCAN SELURUH REPO UNTUK ERROR CODE (TypeScript/Lint)
        this.scanCodeErrors();

        // 3. CEK GIT LOCKS (Penyebab Gagal Commit)
        this.checkGitLocks();
    }

    checkCodespacesIssues() {
        console.log("\n🔍 [1] MEMERIKSA MASALAH CODESPACES...");
        try {
            // Cek status autentikasi dan saran dari GitHub CLI
            const authStatus = execSync('gh auth status').toString();
            console.log("✅ GitHub Auth Status:", authStatus);
        } catch (e) {
            console.warn("⚠️ [SARAN CODESPACE] Autentikasi bermasalah. Coba ketik: gh auth login");
        }
    }

    scanCodeErrors() {
        console.log("\n🔍 [2] SCANNING SELURUH REPO UNTUK ERROR...");
        try {
            // Menjalankan compiler check tanpa menghasilkan file (noEmit)
            console.log("⏳ Menjalankan TypeScript Check (ini mungkin butuh waktu)...");
            const tsCheck = execSync('npx tsc --noEmit', { encoding: 'utf8' });
            console.log("✅ Tidak ditemukan error pada struktur TypeScript.");
        } catch (error: any) {
            console.error("❌ ERROR KODE DITEMUKAN:");
            console.log(error.stdout || error.message);
        }
    }

    checkGitLocks() {
        console.log("\n🔍 [3] MEMERIKSA PENYEBAB GAGAL COMMIT...");
        const lockPath = '.git/index.lock';
        if (fs.existsSync(lockPath)) {
            console.warn("⚠️ ALERT: Ditemukan file 'index.lock'. Ini yang bikin Codespaces gak bisa commit.");
            console.log("💡 SOLUSI: Hapus dengan perintah: rm .git/index.lock");
        } else {
            console.log("✅ Git index tidak terkunci.");
        }
    }
}

new AriesSystemAuditor().run();
