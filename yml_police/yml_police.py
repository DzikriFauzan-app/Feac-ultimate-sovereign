#!/usr/bin/env python3
import sys
import yaml
from rules import run_hard_rules
from heuristics import run_heuristics

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def parse_yaml(text):
    try:
        return yaml.safe_load(text), None
    except Exception as e:
        return None, str(e)

def main():
    if len(sys.argv) != 2:
        print("USAGE: yml-police <file.yml | buildozer.spec>")
        sys.exit(1)

    path = sys.argv[1]
    raw = load_file(path)

    data, err = parse_yaml(raw)
    if err:
        print("STATUS: 🔴 RED")
        print("REASON: YAML SYNTAX INVALID")
        print("DETAIL:", err)
        sys.exit(2)

    hard_errors = run_hard_rules(data)
    risk_score, warnings = run_heuristics(data)

    if hard_errors:
        print("STATUS: 🔴 RED")
        print("REASON: DETERMINISTIC FAILURE")
        for e in hard_errors:
            print("-", e)
        sys.exit(3)

    if risk_score >= 70:
        print("STATUS: 🔴 RED")
        print(f"RISK SCORE: {risk_score}")
        for w in warnings:
            print("-", w)
        sys.exit(4)

    if risk_score >= 40:
        print("STATUS: 🟡 YELLOW")
        print(f"RISK SCORE: {risk_score}")
        for w in warnings:
            print("-", w)
        sys.exit(0)

    print("STATUS: 🟢 GREEN")
    print("SAFE TO BUILD")

if __name__ == "__main__":
    main()
