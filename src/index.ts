import express from 'express';
import cors from 'cors';
const app = express();
app.use(cors());
app.use(express.json());

app.post('/api/chat', (req, res) => {
    console.log("🧠 ARIES BRAIN PROCESSING:", req.body.message);
    res.json({ response: "Sovereign Intelligence Confirmed: " + req.body.message });
});

app.listen(3000, () => console.log("🧠 ARIES BRAIN 3000 ONLINE"));
