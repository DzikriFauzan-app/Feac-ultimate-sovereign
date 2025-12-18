import fs from 'fs';
import path from 'path';
import { feacLog } from '../utils/feacLogger';

export class SelfAnalyzer {
    static analyzeProject() {
        feacLog("ANALYZER", "Scanning Sovereign Codebase...");
        const files = this.walkDir(path.join(process.cwd(), 'src'));
        const report = {
            fileCount: files.length,
            totalLoc: 0,
            healthScore: 100
        };

        files.forEach(file => {
            const content = fs.readFileSync(file, 'utf-8');
            report.totalLoc += content.split('\n').length;
            if (content.includes('TODO') || content.includes('FIXME')) report.healthScore -= 5;
        });

        return report;
    }

    private static walkDir(dir: string): string[] {
        let results: string[] = [];
        const list = fs.readdirSync(dir);
        list.forEach(file => {
            file = path.resolve(dir, file);
            const stat = fs.statSync(file);
            if (stat && stat.isDirectory()) results = results.concat(this.walkDir(file));
            else if (file.endsWith('.ts')) results.push(file);
        });
        return results;
    }
}
