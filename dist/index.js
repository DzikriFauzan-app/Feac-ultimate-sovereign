"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const cors_1 = __importDefault(require("cors"));
const path_1 = __importDefault(require("path"));
const child_process_1 = require("child_process");
const consciousness_1 = require("./core/consciousness");
const audit_engine_1 = require("./core/audit_engine");
const feacLogger_1 = require("./utils/feacLogger");
const app = (0, express_1.default)();
const brain = new consciousness_1.Consciousness();
const auditor = new audit_engine_1.AuditEngine();
app.use((0, cors_1.default)());
app.use(express_1.default.json());
app.set('view engine', 'ejs');
app.set('views', path_1.default.join(__dirname, 'ui/views'));
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
app.post('/system/execute', (req, res) => {
    const { task } = req.body;
    (0, feacLogger_1.feacLog)("COMMAND", `Received UI Instruction: ${task}`);
    let command = "";
    switch (task) {
        case 'push':
            command = "bash scripts/sovereign_push.sh 'Manual UI Sync'";
            break;
        case 'audit':
            command = "npx ts-node src/tests/audit_test.ts";
            break;
        case 'rebuild':
            command = "npm install && npx tsc";
            break;
        default: command = "echo 'Unknown Task'";
    }
    (0, child_process_1.exec)(command, (error, stdout, stderr) => {
        if (error) {
            (0, feacLogger_1.feacLog)("CRITICAL", `Task ${task} Failed: ${error.message}`);
            return res.status(500).json({ status: "ERROR", message: error.message });
        }
        (0, feacLogger_1.feacLog)("COMMAND", `Task ${task} Executed Successfully`);
        res.json({ status: "SUCCESS", output: stdout });
    });
});
const PORT = 3001;
app.listen(PORT, () => {
    brain.updateState(consciousness_1.SystemState.IDLE);
    console.log(`\x1b[33m%s\x1b[0m`, `[FEAC_SOVEREIGN] COMMAND CENTER ONLINE: http://localhost:${PORT}`);
});
