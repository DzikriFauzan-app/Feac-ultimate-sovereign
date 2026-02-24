import express from 'express';
const app = express();
app.use(express.json());

const VALID_KEY = "aries-owner-33d7d4d4224cdb40b0aef205b64f76414efb2f9bc70ee1f1";

app.post('/api/auth/handshake', (req, res) => {
    const { apiKey } = req.body;
    console.log("🔑 [BRIDGE] Menerima kiriman API Key...");
    
    if (apiKey === VALID_KEY) {
        console.log("✅ [BRIDGE] Akses Diterima. Role: OWNER.");
        return res.json({ success: true, status: "CONNECTED", role: "OWNER" });
    }
    console.log("❌ [BRIDGE] Akses Ditolak. Key Ilegal.");
    res.status(401).json({ success: false, status: "DENIED" });
});

app.listen(3001, '127.0.0.1', () => {
    console.log("🚀 [LOCAL BRIDGE] Aktif di http://127.0.0.1:3001");
});
