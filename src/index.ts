import express from 'express';
import axios from 'axios';

const app = express();
app.use(express.json());

const ARIES_URL = 'http://127.0.0.1:3000/api/auth/validate-key';

app.post('/api/validate-key', async (req, res) => {
    try {
        const { apiKey } = req.body;
        console.log("🔄 Forwarding Owner Key to Aries...");

        const response = await axios.post(ARIES_URL, { apiKey }, { timeout: 5000 });
        
        console.log("✅ Aries Response:", response.data.status);
        res.status(200).json(response.data);
    } catch (error: any) {
        // Menggunakan : any atau pengecekan pesan untuk menghindari error TS18046
        const errorMessage = error instanceof Error ? error.message : String(error);
        console.error("❌ Bridge Error:", errorMessage);
        
        res.status(503).json({ 
            success: false, 
            status: "BRIDGE_CONNECTION_FAILED",
            message: errorMessage
        });
    }
});

app.get('/health', (req, res) => res.json({ status: "BRIDGE_ACTIVE" }));

app.listen(3001, '0.0.0.0', () => {
    console.log('🏛️ FEAC BRIDGE ONLINE ON PORT 3001');
});
