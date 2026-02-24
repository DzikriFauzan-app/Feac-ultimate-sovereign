import os

class Settings:
    # Base dir is project root (one level up from core)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DB_PATH = os.path.join(BASE_DIR, "neoengine.db")

    # Directories
    SRC_DIR = BASE_DIR
    MODULES_DIR = os.path.join(BASE_DIR, "modules")
    LOGS_DIR = os.path.join(BASE_DIR, "logs")
    CACHE_DIR = os.path.join(BASE_DIR, "cache")
    UI_DIR = os.path.join(BASE_DIR, "ui")

    # Server config
    HOST = "0.0.0.0"
    PORT = 8080

    # Worker config
    MAX_WORKERS = 4
    TASK_TIMEOUT_SECONDS = 300

    # Security
    ALLOWED_COMMANDS = ["ls", "git", "echo", "mkdir", "touch", "cat", "grep", "python3"]
    BLOCKED_PATTERNS = ["rm -rf", ":(){ :|:& };:"]

    @staticmethod
    def setup_dirs():
        os.makedirs(Settings.LOGS_DIR, exist_ok=True)
        os.makedirs(Settings.MODULES_DIR, exist_ok=True)
        os.makedirs(Settings.CACHE_DIR, exist_ok=True)
        os.makedirs(Settings.UI_DIR, exist_ok=True)
