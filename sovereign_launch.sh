#!/bin/bash
echo "🚀 Memulai Sovereign Force-Sync..."
pkill -9 python
pm2 restart 0

echo "⏳ Menunggu 39 Agen & Port 8080 Siaga..."
while true; do
  # Cek RAM
  MEM=$(pm2 jlist | jq '.[0].monit.memory / 1024 / 1024' | cut -d. -f1)
  # Cek apakah port 8080 sudah terbuka
  PORT_READY=$(netstat -tunlp | grep :8080)

  if [ "$MEM" -gt 50 ] && [ ! -z "$PORT_READY" ]; then
    echo "✅ RAM: $MEM MB | Port 8080: OPEN"
    echo "🔥 Menjalankan Heavy Task..."
    sleep 2 # Jeda pengamanan terakhir
    python3 test_heavy_task.py
    break
  fi
  echo "Current RAM: $MEM MB | Waiting for Port 8080..."
  sleep 3
done
