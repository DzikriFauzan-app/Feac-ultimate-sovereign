#!/usr/bin/env python3
import sys
import difflib

def detect_format(text):
    if "=" in text.splitlines()[1]:
        return "SPEC"
    return "YAML"

def parse_spec(lines):
    cfg = {}
    for ln in lines:
        if "=" in ln and not ln.strip().startswith("#"):
            k, v = ln.split("=", 1)
            cfg[k.strip()] = v.strip()
    return cfg

def suggest(cfg):
    suggestions = {}

    py = cfg.get("python", "")
    if py.startswith("3.11") or py.startswith("3.12"):
        suggestions["python"] = "3.10.12"

    api = int(cfg.get("android.api", "0") or 0)
    if api and api < 30:
        suggestions["android.api"] = "33"

    arch = cfg.get("android.arch", "")
    if arch and arch != "arm64-v8a":
        suggestions["android.arch"] = "arm64-v8a"

    if "requirements" in cfg and "numpy>=2" in cfg["requirements"]:
        suggestions["requirements"] = cfg["requirements"].replace("numpy>=2", "numpy<2")

    return suggestions

def main():
    if len(sys.argv) != 2:
        print("USAGE: yml-police-suggest <buildozer.spec | *.yml>")
        sys.exit(1)

    path = sys.argv[1]
    raw = open(path).read()
    lines = raw.splitlines()
    fmt = detect_format(raw)

    print(f"[FORMAT DETECTED] {fmt}")

    if fmt == "SPEC":
        cfg = parse_spec(lines)
    else:
        print("YAML parsing disabled in this mode.")
        sys.exit(0)

    fixes = suggest(cfg)
    if not fixes:
        print("STATUS: 🟢 NO CRITICAL FIX NEEDED")
        return

    print("STATUS: 🔴 SUGGESTED DIFF (READ-ONLY)")
    for k, v in fixes.items():
        old = cfg.get(k, "")
        print(f"- {k}: {old}  →  {v}")

if __name__ == "__main__":
    main()
