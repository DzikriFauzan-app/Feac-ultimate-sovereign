import express from 'express';
import cors from 'cors';
import { Consciousness, SystemState } from './core/consciousness';
import { AuditEngine } from './core/audit_engine';

const app = express();
const brain = new Consciousness();
const auditor = new AuditEngine();

app.use(cors());
app.use(express.json());

app.get('/system/pulse', (req, res) => {
    const report = auditor.generateReport();
    res.json({
        identity: "FEAC_ULTIMATE_SOVEREIGN",
        status: brain.getState(),
        health_report: report,
        uptime: process.uptime()
    });
});

const PORT = 3001;
app.listen(PORT, () => {
    brain.updateState(SystemState.IDLE);
    console.log(`[FEAC_SOVEREIGN] MONITORING ACTIVE ON PORT ${PORT}`);
});
