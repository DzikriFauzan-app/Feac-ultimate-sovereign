import { Artifact } from '../artifacts/schemas/sovereignArtifact';
import { v4 as uuidv4 } from 'uuid';
import * as crypto from 'crypto';

export class CodeGenerator {
    generate(name: string, lang: string, rawCode: string): Artifact {
        const checksum = crypto.createHash('md5').update(rawCode).digest('hex');
        return {
            uid: uuidv4(),
            name: `${name}.${lang === 'typescript' ? 'ts' : 'py'}`,
            type: 'CODE',
            version: '1.0.0',
            content: rawCode,
            checksum: checksum,
            createdAt: Date.now()
        };
    }
}
