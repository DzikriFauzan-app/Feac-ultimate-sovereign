export interface Artifact {
    uid: string;
    name: string;
    type: 'CODE' | 'ASSET' | 'DOC';
    version: string;
    content: string;
    checksum: string;
    createdAt: number;
}

export class ArtifactValidator {
    static validate(artifact: Artifact): boolean {
        return !!(artifact.uid && artifact.content && artifact.checksum);
    }
}
