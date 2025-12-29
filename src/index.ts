import express from 'express';
import cors from 'cors';
import axios from 'axios';

const app = express();
const PORT = 3001;
// Aries URL tetap 127.0.0.1 JIKA Aries-core jalan di mesin yang sama (Termux)
const ARIES_URL = 'http://127.0.0.1:3000/api/auth/validate-key';

app.use(cors({ origin: '*', methods: ['GET', 'POST'] }));
app.use(express.json());

app.post('/api/validate-key', async (req, res) => {
    const { apiKey } = req.body;
    
    // Bypass Owner Key (Selalu Berhasil)
    if (apiKey === 'aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1') {
        console.log("👑 [BRIDGE] Owner Access Detected!");
        return res.json({ success: true, role: 'owner', message: 'AUTHORIZED' });
    }

    try {
        const response = await axios.post(ARIES_URL, { apiKey });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ success: false, message: 'ARIES_UNREACHABLE_FROM_BRIDGE' });
    }
});

app.listen(PORT, () => console.log(`🏛️ BRIDGE SYNCED TO CLOUD ON PORT ${PORT}`));
