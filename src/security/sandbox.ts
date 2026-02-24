import { feacLog } from '../utils/feacLogger';

export class SecuritySandbox {
    private static readonly BANNED_KEYWORDS = ['rm -rf', ':(){ :|:& };:', 'mv /', 'dd if='];

    static validateSafeCode(code: string): boolean {
        feacLog("SECURITY", "Initiating Static Code Analysis...");
        for (const keyword of this.BANNED_KEYWORDS) {
            if (code.includes(keyword)) {
                feacLog("CRITICAL", `MALICIOUS CODE DETECTED: Contains ${keyword}`);
                return false;
            }
        }
        feacLog("SECURITY", "Code Scan: CLEAN.");
        return true;
    }
}
