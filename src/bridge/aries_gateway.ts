import axios from 'axios';

export class AriesGateway {
    private static readonly ARIES_ENDPOINT = "http://10.159.189.152:3333/v1/brain";

    static async requestCognition(prompt: string, context: any) {
        try {
            const response = await axios.post(this.ARIES_ENDPOINT, {
                intent: "COGNITIVE_REQUEST",
                payload: { prompt, context },
                timestamp: Date.now()
            }, {
                headers: { "ngrok-skip-browser-warning": "true", "ngrok-skip-browser-warning": "true", "Content-Type": "application/json", "ngrok-skip-browser-warning": "true", "x-aries-key": "aries-sovereign-ultimate" }
            });
            return response.data;
        } catch (error) {
            console.error("[ARIES_GATEWAY] Connection lost to Kernel.");
            return null;
        }
    }
}
