"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SecuritySandbox = void 0;
const feacLogger_1 = require("../utils/feacLogger");
class SecuritySandbox {
    static BANNED_KEYWORDS = ['rm -rf', ':(){ :|:& };:', 'mv /', 'dd if='];
    static validateSafeCode(code) {
        (0, feacLogger_1.feacLog)("SECURITY", "Initiating Static Code Analysis...");
        for (const keyword of this.BANNED_KEYWORDS) {
            if (code.includes(keyword)) {
                (0, feacLogger_1.feacLog)("CRITICAL", `MALICIOUS CODE DETECTED: Contains ${keyword}`);
                return false;
            }
        }
        (0, feacLogger_1.feacLog)("SECURITY", "Code Scan: CLEAN.");
        return true;
    }
}
exports.SecuritySandbox = SecuritySandbox;
