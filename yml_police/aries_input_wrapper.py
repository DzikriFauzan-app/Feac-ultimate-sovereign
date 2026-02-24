import json
import sys

policy = json.load(sys.stdin)

print("=== AI POLICY MODE ===")
print("MODE:", policy["ai_mode"])
print()

print("=== POLICE REPORT ===")
print(policy["police_report"])
print()

if policy["ai_mode"] == "RESTRICTED":
    print("AI INSTRUCTION:")
    print("- DILARANG membahas build")
    print("- FOKUS perbaikan konfigurasi")
    print("- JANGAN beri command eksekusi")
else:
    print("AI INSTRUCTION:")
    print("- MODE NORMAL")
