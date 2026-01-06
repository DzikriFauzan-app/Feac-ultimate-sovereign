#!/bin/bash
echo "🚀 Memulai perbaikan frontend Sovereign..."
cd frontend
# Hapus lockfile lama untuk menghindari konflik
rm -rf node_modules package-lock.json
# Install ulang dengan paksa agar peer dependencies ikut terangkut
npm install --force
# Tambahkan vite secara eksplisit untuk menjamin keberadaan type definitions
npm install vite @vitejs/plugin-react --save-dev
echo "✅ Dependensi frontend berhasil diperbarui!"
