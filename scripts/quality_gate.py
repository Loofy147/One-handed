import json
import os
import sys

def enforce_gate():
    report_path = "readiness_report.json"
    if not os.path.exists(report_path):
        print("FAIL: readiness_report.json missing. Run readiness_audit.py first.")
        sys.exit(1)

    with open(report_path, 'r') as f:
        report = json.load(f)

    threshold = 80
    failing_assets = []

    for asset, data in report.items():
        if data["score"] < threshold:
            failing_assets.append((asset, data["score"]))

    if failing_assets:
        print(f"--- QUALITY GATE FAILED (Threshold: {threshold}) ---")
        for asset, score in failing_assets:
            print(f"  - {asset}: Score {score}")
        print("\nFix documentation, benchmarks, or compliance in specifications.md to pass.")
        sys.exit(1)

    print(f"--- QUALITY GATE PASSED (All assets >= {threshold}) ---")
    sys.exit(0)

if __name__ == "__main__":
    enforce_gate()
