import axios from 'axios';

export class AriesKernelConnector {
  private static readonly KERNEL_URL = "http://0.0.0.0:3333/v1/command";

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

import express from 'express';
const kernelApp = express();
kernelApp.use(express.json());
kernelApp.get('/ping', (req, res) => res.send('Aries Kernel Alive'));
kernelApp.post('/chat', (req, res) => {
    console.log("💬 Message Received:", req.body.message);
    res.json({ response: "Aries Brain Connected & Processing." });
});
kernelApp.listen(3000, () => console.log("🧠 Aries Kernel Server Listening on Port 3000"));
