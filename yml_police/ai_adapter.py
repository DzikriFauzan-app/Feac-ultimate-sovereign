import subprocess
import sys

def run_police(file):
    p = subprocess.run(
        ["python", "yml_police/yml_police.py", file],
        capture_output=True,
        text=True
    )
    return p.stdout, p.returncode

def main():
    if len(sys.argv) != 2:
        print("USAGE: ai-adapter <file>")
        sys.exit(1)

    out, code = run_police(sys.argv[1])

    print("=== YML POLICE REPORT ===")
    print(out.strip())

    if code != 0:
        print("\n=== AI DIRECTIVE ===")
        print("STATUS: BLOCKED")
        print("RULE: AI TIDAK BOLEH MEMBERI SARAN BUILD")
        print("TASK: Sarankan PERBAIKAN KONFIGURASI SAJA")
    else:
        print("\n=== AI DIRECTIVE ===")
        print("STATUS: ALLOWED")
        print("TASK: AI boleh melanjutkan diskusi build")

if __name__ == "__main__":
    main()
