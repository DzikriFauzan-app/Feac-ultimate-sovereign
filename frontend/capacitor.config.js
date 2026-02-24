"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const config = {
    appId: 'com.feac.sovereign',
    appName: 'Feac-ultimate-sovereign',
    webDir: 'dist',
    bundledWebRuntime: false,
    plugins: {
        LiveUpdates: {
            appId: 'feac-sovereign-ota',
            channel: 'Production',
            autoUpdateMethod: 'background',
            maxVersions: 3
        }
    }
};
exports.default = config;
