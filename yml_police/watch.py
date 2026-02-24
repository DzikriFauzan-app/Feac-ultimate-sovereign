#!/usr/bin/env python3
import os
import sys
import time
import subprocess

WATCH_FILES = ["buildozer.spec"]

def mtime(path):
    try:
        return os.path.getmtime(path)
    except:
        return 0

def run_checks(path):
    print("\n==============================")
    print(f"[YML POLICE] CHANGE DETECTED: {path}")
    print("------------------------------")

    subprocess.run(
        ["python", "yml_police/yml_police.py", path],
        stdout=sys.stdout,
        stderr=sys.stderr
    )

    subprocess.run(
        ["python", "yml_police/suggest_diff.py", path],
        stdout=sys.stdout,
        stderr=sys.stderr
    )

def main():
    print("[YML POLICE] WATCH MODE ACTIVE")
    print("[YML POLICE] Monitoring:", ", ".join(WATCH_FILES))
    print("[CTRL+C] to stop\n")

    last = {f: mtime(f) for f in WATCH_FILES}

    while True:
        time.sleep(1)
        for f in WATCH_FILES:
            now = mtime(f)
            if now != last[f]:
                last[f] = now
                run_checks(f)

if __name__ == "__main__":
    main()
