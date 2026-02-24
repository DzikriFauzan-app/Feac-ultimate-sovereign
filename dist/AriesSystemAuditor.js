"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const child_process_1 = require("child_process");
const fs_1 = __importDefault(require("fs"));
class AriesSystemAuditor {
    constructor() {
        this.name = "Aries Codespaces & Code Error Auditor";
    }
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
            const authStatus = (0, child_process_1.execSync)('gh auth status').toString();
            console.log("✅ GitHub Auth Status:", authStatus);
        }
        catch (e) {
            console.warn("⚠️ [SARAN CODESPACE] Autentikasi bermasalah. Coba ketik: gh auth login");
        }
    }
    scanCodeErrors() {
        console.log("\n🔍 [2] SCANNING SELURUH REPO UNTUK ERROR...");
        try {
            // Menjalankan compiler check tanpa menghasilkan file (noEmit)
            console.log("⏳ Menjalankan TypeScript Check (ini mungkin butuh waktu)...");
            const tsCheck = (0, child_process_1.execSync)('npx tsc --noEmit', { encoding: 'utf8' });
            console.log("✅ Tidak ditemukan error pada struktur TypeScript.");
        }
        catch (error) {
            console.error("❌ ERROR KODE DITEMUKAN:");
            console.log(error.stdout || error.message);
        }
    }
    checkGitLocks() {
        console.log("\n🔍 [3] MEMERIKSA PENYEBAB GAGAL COMMIT...");
        const lockPath = '.git/index.lock';
        if (fs_1.default.existsSync(lockPath)) {
            console.warn("⚠️ ALERT: Ditemukan file 'index.lock'. Ini yang bikin Codespaces gak bisa commit.");
            console.log("💡 SOLUSI: Hapus dengan perintah: rm .git/index.lock");
        }
        else {
            console.log("✅ Git index tidak terkunci.");
        }
    }
}
new AriesSystemAuditor().run();
