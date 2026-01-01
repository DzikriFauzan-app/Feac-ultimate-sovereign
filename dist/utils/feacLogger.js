"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.feacLog = void 0;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const LOG_DIR = path_1.default.join(process.cwd(), 'data/logs');
const LOG_FILE = path_1.default.join(LOG_DIR, 'feac_system.log');
// Pastikan folder log ada
if (!fs_1.default.existsSync(LOG_DIR)) {
    fs_1.default.mkdirSync(LOG_DIR, { recursive: true });
}
const feacLog = (module, message) => {
    const timestamp = new Date().toISOString();
    const logEntry = `[${timestamp}] [${module}] ${message}\n`;
    // Output ke terminal
    console.log(logEntry.trim());
    // Output ke file
    try {
        fs_1.default.appendFileSync(LOG_FILE, logEntry);
    }
    catch (err) {
        console.error(`FAILED TO WRITE LOG: ${err}`);
    }
};
exports.feacLog = feacLog;
