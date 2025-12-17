import axios from 'axios';
import { feacLog } from '../utils/feacLogger';

export class NeoAdapter {
    private static readonly NEO_URL = "http://127.0.0.1:5000/render"; 

    static async dispatchRenderTask(taskId: string, payload: any) {
        feacLog("BRIDGE", `Connecting to Neo Engine for Task: ${taskId}`);
        try {
            const response = await axios.post(this.NEO_URL, {
                task_id: taskId,
                payload,
                timestamp: Date.now()
            }, { timeout: 2000 });
            return response.data;
        } catch (error: any) {
            feacLog("BRIDGE", "Neo Engine status: OFFLINE (Expected in standalone test)");
            return { status: "OFFLINE" };
        }
    }
}
