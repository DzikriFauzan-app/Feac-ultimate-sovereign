import { FEAC_CONFIG } from '../config/api';

export class AuthService {
    static async validateApiKey(apiKey: string) {
        const urlsToTry = [FEAC_CONFIG.BASE_URL, ...FEAC_CONFIG.FALLBACK_URLS];
        for (const baseUrl of urlsToTry) {
            try {
                const response = await fetch(`${baseUrl}/api/auth/validate-key`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ apiKey })
                });
                const data = await response.json();
                if (data.success) return data;
            } catch (e) { continue; }
        }
        throw new Error("Bridge Failed");
    }
}
