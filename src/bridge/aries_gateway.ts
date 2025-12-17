import axios from 'axios';

export class AriesGateway {
    private static readonly ARIES_ENDPOINT = "http://127.0.0.1:3333/v1/brain";

    static async requestCognition(prompt: string, context: any) {
        try {
            const response = await axios.post(this.ARIES_ENDPOINT, {
                intent: "COGNITIVE_REQUEST",
                payload: { prompt, context },
                timestamp: Date.now()
            }, {
                headers: { "x-aries-key": "aries-sovereign-ultimate" }
            });
            return response.data;
        } catch (error) {
            console.error("[ARIES_GATEWAY] Connection lost to Kernel.");
            return null;
        }
    }
}
