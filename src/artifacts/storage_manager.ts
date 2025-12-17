import fs from 'fs';
import path from 'path';
import { Artifact } from './schemas/sovereignArtifact';

export class StorageManager {
    private basePath = path.join(__dirname, '../../data/artifacts');

    save(artifact: Artifact): string {
        const filePath = path.join(this.basePath, artifact.name);
        fs.writeFileSync(filePath, artifact.content);
        return filePath;
    }

    exists(name: string): boolean {
        return fs.existsSync(path.join(this.basePath, name));
    }
}
