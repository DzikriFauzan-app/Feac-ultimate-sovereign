import os

config_path = "capacitor.config.ts"
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        content = f.read()
    
    # Mengarahkan webDir ke folder distribusi sovereign kita
    if "webDir: 'dist'" in content:
        content = content.replace("webDir: 'dist'", "webDir: 'dist_sovereign/www'")
        with open(config_path, 'w') as f:
            f.write(content)
        print("✅ capacitor.config.ts diarahkan ke dist_sovereign/www")
    else:
        print("ℹ️ Jalur sudah benar atau format berbeda.")
