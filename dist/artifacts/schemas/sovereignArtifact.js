"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ArtifactValidator = void 0;
class ArtifactValidator {
    static validate(artifact) {
        return !!(artifact.uid && artifact.content && artifact.checksum);
    }
}
exports.ArtifactValidator = ArtifactValidator;
