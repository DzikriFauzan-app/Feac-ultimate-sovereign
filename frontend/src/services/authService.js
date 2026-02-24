"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthService = void 0;
const api_1 = require("../config/api");
class AuthService {
    static async validateApiKey(apiKey) {
        const urlsToTry = [api_1.FEAC_CONFIG.BASE_URL, ...api_1.FEAC_CONFIG.FALLBACK_URLS];
        for (const baseUrl of urlsToTry) {
            try {
                const response = await fetch(`${baseUrl}/api/auth/validate-key`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ apiKey })
                });
                const data = await response.json();
                if (data.success)
                    return data;
            }
            catch (e) {
                continue;
            }
        }
        throw new Error("Bridge Failed");
    }
}
exports.AuthService = AuthService;
