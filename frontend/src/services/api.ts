const BRIDGE_URL = 'https://redesigned-yodel-7v6wjx4r9x653ww6g-3001.app.github.dev';

export const validateKey = async (apiKey: string) => {
    try {
        console.log("🚀 [FRONTEND] Connecting to Bridge:", BRIDGE_URL);
        const response = await fetch(`${BRIDGE_URL}/api/validate-key`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ apiKey })
        });
        return await response.json();
    } catch (error) {
        console.error("❌ [FRONTEND] Connection Failed:", error);
        return { success: false, message: 'BRIDGE_UNREACHABLE' };
    }
};
