#!/usr/bin/env bash
# FEAC AUTO-RECOVERY WATCHDOG

PORT=3001
SERVICE_NAME="FEAC_CORE"

while true; do
    if ! lsof -i :$PORT > /dev/null; then
        echo "[WATCHDOG] $SERVICE_NAME is DOWN. Restarting..."
        nohup npx ts-node src/index.ts > data/logs/runtime.log 2>&1 &
        echo "[WATCHDOG] Restart signal sent."
    fi
    sleep 60
done
