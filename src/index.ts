import express, { Request, Response, NextFunction } from 'express';
import axios, { AxiosError } from 'axios';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
// Kita gunakan PORT 3001 sesuai struktur asli FEAC kamu
const PORT = 3001; 
const ARIES_API_URL = 'http://10.159.189.152:3000';
const MAX_RETRIES = 3;
const RETRY_DELAY = 1000;

app.use(express.json());

async function retryWithBackoff<T>(fn: () => Promise<T>, config: any): Promise<T> {
  let lastError: Error | null = null;
  for (let attempt = 1; attempt <= config.maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      if (attempt < config.maxRetries) {
        const delayTime = config.delayMs * Math.pow(2, attempt - 1);
        console.warn(`Attempt ${attempt} failed. Retrying in ${delayTime}ms...`);
        await new Promise(resolve => setTimeout(resolve, delayTime));
      }
    }
  }
  throw new Error(`Failed after ${config.maxRetries} attempts.`);
}

app.post('/api/validate-key', async (req: Request, res: Response) => {
  try {
    const { apiKey } = req.body;
    if (!apiKey) return res.status(400).json({ isValid: false, message: 'API key is required' });

    const result = await retryWithBackoff(async () => {
      const response = await axios.post(`${ARIES_API_URL}/api/auth/validate-key`, { apiKey }, { timeout: 5000 });
      return {
        isValid: response.data.success === true,
        message: 'API key validation successful',
        level: response.data.level
      };
    }, { maxRetries: MAX_RETRIES, delayMs: RETRY_DELAY });

    res.status(200).json(result);
  } catch (error) {
    res.status(500).json({ isValid: false, message: 'Bridge to Aries Failed' });
  }
});

app.get('/health', (req, res) => res.json({ status: 'FEAC ONLINE' }));

app.listen(PORT, () => {
  console.log(`🏛️ FEAC COMMAND SERVER RUNNING ON PORT ${PORT}`);
  console.log(`🔗 CONNECTED TO ARIES AT ${ARIES_API_URL}`);
});
