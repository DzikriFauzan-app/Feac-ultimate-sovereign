import os
import json
import re

def get_package_name():
    # Coba cari package name dari capacitor.config.json
    try:
        if os.path.exists("frontend/capacitor.config.json"):
            with open("frontend/capacitor.config.json", 'r') as f:
                data = json.load(f)
                return data.get("appId", "io.ionic.starter")
    except:
        pass
    return "io.ionic.starter" # Fallback default

def restore_manifest():
    target_path = "frontend/android/app/src/main/AndroidManifest.xml"
    
    # Pastikan folder ada
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    
    package_name = get_package_name()
    print(f"⚙️ Terdeteksi App ID: {package_name}")

    # Template Manifest Standar Capacitor (Clean & Valid)
    manifest_content = f"""<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{package_name}">

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

        <activity
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|locale|smallestScreenSize|screenLayout|uiMode"
            android:name=".MainActivity"
            android:label="@string/title_activity_main"
            android:theme="@style/AppTheme.NoActionBarLaunch"
            android:launchMode="singleTask"
            android:exported="true">

            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>

        </activity>

        <provider
            android:name="androidx.core.content.FileProvider"
            android:authorities="${{applicationId}}.fileprovider"
            android:exported="false"
            android:grantUriPermissions="true">
            <meta-data
                android:name="android.support.FILE_PROVIDER_PATHS"
                android:resource="@xml/file_paths" />
        </provider>
    </application>
</manifest>
"""

    with open(target_path, "w") as f:
        f.write(manifest_content)
    
    print(f"✅ Manifest berhasil direstorasi total di: {target_path}")
    print("🚀 File ini sekarang bersih dari syntax error.")

if __name__ == "__main__":
    restore_manifest()
