PROFILES = {
    "buildozer-termux": {
        "forbidden_python": ["3.11", "3.12"],
        "min_android_api": 30,
        "allowed_arch": ["arm64-v8a"],
        "notes": [
            "Termux TIDAK stabil untuk python >=3.11",
            "arm64-v8a paling aman di Termux",
        ]
    },

    "github-actions": {
        "forbidden_python": [],
        "min_android_api": 29,
        "allowed_arch": ["arm64-v8a", "armeabi-v7a"],
        "notes": [
            "GitHub Actions lebih toleran",
            "Disk & RAM lebih besar"
        ]
    },

    "docker-build": {
        "forbidden_python": [],
        "min_android_api": 30,
        "allowed_arch": ["arm64-v8a", "x86_64"],
        "notes": [
            "Docker paling fleksibel",
            "Cocok untuk eksperimen berat"
        ]
    }
}
