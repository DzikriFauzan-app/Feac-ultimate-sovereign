#!/bin/bash

# 1. Ambil IP Address menggunakan ip route (lebih aman untuk Termux)
IP_ADDRESS=$(ip route get 1.1.1.1 | grep -oP 'src \K\S+')

if [ -z "$IP_ADDRESS" ]; then
    # Cara alternatif jika cara pertama gagal
    IP_ADDRESS=$(getprop gsm.network.type > /dev/null && ip addr show wlan0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}')
fi

if [ -z "$IP_ADDRESS" ]; then
    echo "❌ Gagal mendapatkan IP. Masukkan IP secara manual?"
    read -p "Masukkan IP Termux kamu: " IP_ADDRESS
fi

echo "🌐 IP Termux Terdeteksi: $IP_ADDRESS"

# 2. Pastikan file config ada (Sesuaikan path jika perlu)
CONFIG_FILE="frontend/src/config.ts"
mkdir -p frontend/src

# Jika file tidak ada, kita buat baru
if [ ! -f "$CONFIG_FILE" ]; then
    echo "export const API_URL = 'http://$IP_ADDRESS:3000';" > $CONFIG_FILE
    echo "✅ File konfigurasi baru dibuat: $CONFIG_FILE"
else
    # Jika ada, kita timpa isinya
    echo "export const API_URL = 'http://$IP_ADDRESS:3000';" > $CONFIG_FILE
    echo "✅ Config updated: $CONFIG_FILE"
fi

# 3. Push ke GitHub
git add .
git commit -m "chore: sync bridge endpoint to $IP_ADDRESS"
git push origin main

echo "🚀 Push selesai. Cek GitHub Actions untuk status build APK."
