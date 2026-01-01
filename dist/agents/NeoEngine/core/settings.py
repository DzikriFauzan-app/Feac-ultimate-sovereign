import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "data", "neoengine.db")
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    PLUGIN_DIR = os.path.join(BASE_DIR, "plugins")
    
    HOST = "0.0.0.0"
    PORT = 8080
    
    # Security
    ALLOWED_COMMANDS = ["ls", "git", "echo", "mkdir", "touch", "godot", "cat", "grep", "clang++", "javac"]
    BLOCKED_COMMANDS = ["rm -rf /", ":(){ :|:& };:"]
    
    # Resource Limits
    MAX_CPU_PERCENT = 80
    MAX_MEMORY_MB = 1024

    @staticmethod
    def setup_dirs():
        os.makedirs(Settings.LOG_DIR, exist_ok=True)
        os.makedirs(Settings.PLUGIN_DIR, exist_ok=True)
