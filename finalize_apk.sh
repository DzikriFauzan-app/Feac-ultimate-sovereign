echo "🚚 Memindahkan Aset Sovereign ke Android Wrapper..."
# 1. Sinkronisasi aset www ke public folder Capacitor
rm -rf android/app/src/main/assets/public
mkdir -p android/app/src/main/assets/public
cp -r dist_sovereign/www/* android/app/src/main/assets/public/

# 2. Sinkronisasi konfigurasi
npx cap sync android

echo "✅ Aset sinkron! FEAC siap di-build menjadi APK."
echo "💡 Jalankan: cd android && ./gradlew assembleDebug"
