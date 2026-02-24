#!/bin/bash
echo "🏛️ NEO-ENGINE SOVEREIGN INSTALLER"
echo "--------------------------------"
echo "📦 Installing Dependencies..."
pip install fastapi uvicorn requests
echo "🔑 Setting up FEAC Repository Link..."
git remote v
echo "🚀 Launching Council of 41 Agents..."
python3 engine_server.py &
echo "✅ SYSTEM ONLINE. Selamat berjualan, Master."
