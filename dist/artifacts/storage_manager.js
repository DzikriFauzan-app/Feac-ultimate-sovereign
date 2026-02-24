"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.StorageManager = void 0;
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
class StorageManager {
    constructor() {
        this.basePath = path_1.default.join(__dirname, '../../data/artifacts');
    }
    save(artifact) {
        const filePath = path_1.default.join(this.basePath, artifact.name);
        fs_1.default.writeFileSync(filePath, artifact.content);
        return filePath;
    }
    exists(name) {
        return fs_1.default.existsSync(path_1.default.join(this.basePath, name));
    }
}
exports.StorageManager = StorageManager;
