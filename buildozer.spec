[app]
title = FEAC Ultimate
package.name = feac_ultimate
package.domain = id.sovereign
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0.0

# (Requirements) - Pastikan kivy masuk
requirements = python3,kivy==2.2.1,kivymd,requests,urllib3,certifi,charset-normalizer,idna

orientation = portrait
fullscreen = 1
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# (Android SDK/NDK) - Kunci versi agar stabil
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 

# (Permissions)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (Buildozer Config)
log_level = 2
warn_on_root = 1
