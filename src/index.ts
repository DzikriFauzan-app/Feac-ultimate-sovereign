import express from 'express';
import cors from 'cors';
import { Consciousness, SystemState } from './core/consciousness';
import { Governor } from './core/governor';

const app = express();
const brain = new Consciousness();
const guard = new Governor();

app.use(cors());
app.use(express.json());

app.get('/system/pulse', (req, res) => {
    res.json({
        identity: "FEAC_ULTIMATE_SOVEREIGN",
        status: brain.getState(),
        protocol: guard.getSecurityProtocol()
    });
});

const PORT = 3001;
app.listen(PORT, () => {
    brain.updateState(SystemState.IDLE);
    console.log(`[FEAC_SOVEREIGN] PULSE ACTIVE ON PORT ${PORT}`);
});
