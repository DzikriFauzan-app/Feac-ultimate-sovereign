echo "🚀 Memulai Operasi Penimpaan AAPT2..."

# 1. Temukan AAPT2 asli Termux
TERMUX_AAPT2=$(find $ANDROID_HOME -name aapt2 | head -n 1)

if [ -z "$TERMUX_AAPT2" ]; then
    echo "❌ Error: AAPT2 Termux tidak ditemukan!"
    exit 1
fi

echo "🎯 Sumber: $TERMUX_AAPT2"

# 2. Cari semua binari aapt2 yang salah di cache Gradle dan timpa secara paksa
find /data/data/com.termux/files/home/.gradle/caches -name aapt2 -type f | while read -r bad_bin; do
    echo "🔨 Menimpa: $bad_bin"
    cp "$TERMUX_AAPT2" "$bad_bin"
    chmod +x "$bad_bin"
done

echo "✅ Semua binari AAPT2 di cache telah diperbaiki."
