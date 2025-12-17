import axios from 'axios';

export class AriesKernelConnector {
  private static readonly KERNEL_URL = "http://127.0.0.1:3333/v1/command";

  static async execute(input: string, session: string) {
    try {
      const response = await axios.post(this.KERNEL_URL, {
        session_id: session,
        user_id: "sovereign_operator",
        input: input
      }, {
        headers: { "x-aries-key": "aries-sovereign-ultimate" }
      });
      return response.data;
    } catch (error) {
      return { status: "OFFLINE", message: "Kernel Aries tidak terdeteksi." };
    }
  }
}
