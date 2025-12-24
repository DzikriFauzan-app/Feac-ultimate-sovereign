import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
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

export default config;
