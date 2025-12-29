#!/bin/bash
echo "🛡️ RE-INITIALIZING SOVEREIGN CORE..."
pm2 delete all
npx tsc src/bridge.ts src/index.ts --outDir dist --module CommonJS --target ESNext --esModuleInterop --skipLibCheck
mv dist/bridge.js dist/bridge.cjs
mv dist/index.js dist/index.cjs
pm2 start dist/index.cjs --name aries-brain
pm2 start dist/bridge.cjs --name aries-bridge
echo "✅ SYSTEM IS ONLINE AND SYNCED"
pm2 list
