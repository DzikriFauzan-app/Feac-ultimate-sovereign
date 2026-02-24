import subprocess
import sys
import json

def run_police(file):
    p = subprocess.run(
        ["python", "yml_police/yml_police.py", file],
        capture_output=True,
        text=True
    )
    return p.returncode, p.stdout.strip()

def build_ai_payload(exit_code, police_output):
    if exit_code != 0:
        return {
            "ai_mode": "RESTRICTED",
            "allowed_topics": [
                "YAML syntax fix",
                "configuration correction",
                "format explanation"
            ],
            "forbidden_topics": [
                "build",
                "compile",
                "dependency install",
                "command execution"
            ],
            "police_report": police_output
        }

    return {
        "ai_mode": "NORMAL",
        "allowed_topics": ["all"],
        "police_report": police_output
    }

def main():
    if len(sys.argv) != 2:
        print("USAGE: ai-guard <config-file>")
        sys.exit(1)

    exit_code, report = run_police(sys.argv[1])
    payload = build_ai_payload(exit_code, report)

    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
