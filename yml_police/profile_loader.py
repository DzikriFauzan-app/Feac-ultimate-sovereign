import os
from profiles import PROFILES

def detect_profile():
    # Override manual
    if os.getenv("YML_PROFILE"):
        return os.getenv("YML_PROFILE")

    # Heuristik lingkungan
    if os.path.exists("/data/data/com.termux"):
        return "buildozer-termux"

    if os.getenv("GITHUB_ACTIONS") == "true":
        return "github-actions"

    return "docker-build"

def load_profile():
    name = detect_profile()
    return name, PROFILES.get(name, {})
