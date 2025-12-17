import express from 'express';
import cors from 'cors';
import { AriesKernelConnector } from './bridge/ariesKernelConnector';

const app = express();
app.use(cors());
app.use(express.json());

// Endpoint Utama untuk UI FEAC
app.post('/api/command', async (req, res) => {
  const { input, session_id } = req.body;
  const result = await AriesKernelConnector.execute(input, session_id || "ultimate-session");
  res.json(result);
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`[FEAC-ULTIMATE] Sovereign System Bridge Active on Port ${PORT}`);
});
