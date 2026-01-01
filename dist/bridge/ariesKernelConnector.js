"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.KERNEL_CONFIG = void 0;
exports.KERNEL_CONFIG = {
    connectorUrl: process.env.KERNEL_URL || 'http://127.0.0.1:4000',
    timeout: 5000
};
