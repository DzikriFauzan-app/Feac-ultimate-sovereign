import express from 'express';
import axios from 'axios';
const app = express();
app.use(express.json());

// Proxy ke Aries (3000)
app.post('/api/chat', async (req, res) => {
    try {
        const response = await axios.post('http://127.0.0.1:3000/api/chat', req.body);
        res.json(response.data);
    } catch (e) {
        res.status(500).json({ error: "Aries Brain Unreachable" });
    }
});

app.listen(3001, () => console.log("🌉 SOVEREIGN BRIDGE 3001 ALIGNED"));
