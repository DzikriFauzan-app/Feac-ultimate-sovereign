import fs from 'fs';
import path from 'path';

const LOG_DIR = path.join(process.cwd(), 'data/logs');
const LOG_FILE = path.join(LOG_DIR, 'feac_system.log');

// Pastikan folder log ada
if (!fs.existsSync(LOG_DIR)) {
    fs.mkdirSync(LOG_DIR, { recursive: true });
}

export const feacLog = (module: string, message: string) => {
    const timestamp = new Date().toISOString();
    const logEntry = `[${timestamp}] [${module}] ${message}\n`;
    
    // Output ke terminal
    console.log(logEntry.trim());
    
    // Output ke file
    try {
        fs.appendFileSync(LOG_FILE, logEntry);
    } catch (err) {
        console.error(`FAILED TO WRITE LOG: ${err}`);
    }
};
