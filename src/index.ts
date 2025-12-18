import express from 'express';
import cors from 'cors';
import path from 'path';
import { exec } from 'child_process';
import { Consciousness, SystemState } from './core/consciousness';
import { AuditEngine } from './core/audit_engine';
import { feacLog } from './utils/feacLogger';

const app = express();
const brain = new Consciousness();
const auditor = new AuditEngine();

app.use(cors());
app.use(express.json());
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'ui/views'));

// 1. Dashboard Route
app.get('/', (req, res) => {
    res.render('dashboard');
});

// 2. Pulse API (Data untuk UI)
app.get('/system/pulse', (req, res) => {
    const report = auditor.generateReport();
    res.json({
        identity: "FEAC_ULTIMATE_SOVEREIGN",
        status: brain.getState(),
        health_report: report,
        uptime: process.uptime()
    });
});

// 3. Action Console API (Menerima perintah dari UI)
app.post('/system/execute', (req: any, res: any) => {
    const { task } = req.body;
    feacLog("COMMAND", `Received UI Instruction: ${task}`);

    let command = "";
    switch(task) {
        case 'push': command = "bash scripts/sovereign_push.sh 'Manual UI Sync'"; break;
        case 'audit': command = "npx ts-node src/tests/audit_test.ts"; break;
        case 'rebuild': command = "npm install && npx tsc"; break;
        default: command = "echo 'Unknown Task'";
    }

    exec(command, (error, stdout, stderr) => {
        if (error) {
            feacLog("CRITICAL", `Task ${task} Failed: ${error.message}`);
            return res.status(500).json({ status: "ERROR", message: error.message });
        }
        feacLog("COMMAND", `Task ${task} Executed Successfully`);
        res.json({ status: "SUCCESS", output: stdout });
    });
});

const PORT = 3001;
app.listen(PORT, () => {
    brain.updateState(SystemState.IDLE);
    console.log(`\x1b[33m%s\x1b[0m`, `[FEAC_SOVEREIGN] COMMAND CENTER ONLINE: http://localhost:${PORT}`);
});
