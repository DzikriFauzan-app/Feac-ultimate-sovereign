import { execSync } from 'child_process';
import fs from 'fs';

class AriesFinalInsight {
    async extract() {
        console.log("🏛️ [FINAL AGENT] MENYEREAP SARAN SISTEM CODESPACES...");

        const insights = {
            github_cli_advice: "",
            terminal_errors: "",
            env_suggestions: "",
            port_configs: ""
        };

        try {
            // 1. Ambil saran dari GitHub CLI
            insights.github_cli_advice = execSync('gh auth status').toString();
            
            // 2. Scan error TypeScript terakhir sebagai daftar "Dosa" yang harus ditebus
            try {
                execSync('npx tsc --noEmit');
                insights.terminal_errors = "CLEAN";
            } catch (e: any) {
                insights.terminal_errors = e.stdout || e.message;
            }

            // 3. Catat Port yang terekspos
            try {
                insights.port_configs = execSync('gh codespace ports').toString();
            } catch (e) {
                insights.port_configs = "No gh ports found";
            }

            // Simpan ke file lokal untuk kita baca
            fs.writeFileSync('CODESPACE_ADVICE.md', `# CODESPACE ADVICE LOG\n\n${JSON.stringify(insights, null, 2)}`);
            console.log("✅ [SUCCESS] Saran telah disimpan di CODESPACE_ADVICE.md");
            console.log("\n--- ISI SARAN TERAKHIR ---");
            console.log(insights.terminal_errors);
        } catch (err) {
            console.error("Gagal menyerap data.");
        }
    }
}

new AriesFinalInsight().extract();
