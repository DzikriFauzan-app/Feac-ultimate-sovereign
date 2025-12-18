#!/usr/bin/env bash
# FEAC ULTIMATE SOVEREIGN - AUTO PUSH UTILITY
# Standar Industri: Anti-fail, Auto-clean, Secure Token

set -e
echo "🚀 [SOVEREIGN-SHELL] Initiating Automated Deployment..."

if [ -z "$1" ]; then
    echo "❌ Error: Please provide a commit message."
    exit 1
fi

read -s -p "Enter GitHub Token: " AUTH_TOKEN
echo ""

git add .
git commit -m "$1"

echo "📡 Syncing with Global Sovereign Repository..."
git push https://DzikriFauzan-app:${AUTH_TOKEN}@github.com/DzikriFauzan-app/Feac-ultimate-sovereign.git main --force

echo "✅ Deployment Complete. System Synced."
