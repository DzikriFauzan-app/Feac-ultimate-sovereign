[app]
title = Feac Sovereign
package.name = feac_sovereign
package.domain = org.feac.ultimate
source.dir = dist/agents
source.include_exts = py,png,jpg,json,db,yaml,sh,txt,glsl,vert,frag
version = 1.0.0
requirements = python3,kivy==2.2.1,pillow,requests,fastapi,uvicorn,python-socketio,websocket-client,colorama,psutil,sqlite3
orientation = portrait
permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.archs = armeabi-v7a, arm64-v8a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,ACCESS_NETWORK_STATE
