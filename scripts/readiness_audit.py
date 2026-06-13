import os
import json

def run_audit():
    root_dir = "."
    audit_results = {}

    # Load requirements
    req_path = "technical_requirements_schema.json"
    if not os.path.exists(req_path):
        print("Error: technical_requirements_schema.json missing.")
        return

    with open(req_path, 'r') as f:
        config = json.load(f)
        criteria = config["readiness_criteria"]
        alpha_threshold = config["alpha_threshold"]

    for root, dirs, files in os.walk(root_dir):
        if "metadata.json" in files:
            asset_path = root
            status = {"missing_docs": [], "missing_benchmarks": [], "low_alpha": False}

            # Check Documentation
            for doc in criteria["documentation"]:
                if doc not in files:
                    status["missing_docs"].append(doc)

            # Check Specifications content for benchmarks
            if "specifications.md" in files:
                with open(os.path.join(root, "specifications.md"), 'r') as f:
                    content = f.read().lower()
                    for bench in criteria["benchmarks"]:
                        if bench not in content:
                            status["missing_benchmarks"].append(bench)
            else:
                status["missing_benchmarks"] = list(criteria["benchmarks"])

            # Check Alpha Score
            with open(os.path.join(root, "metadata.json"), 'r') as f:
                data = json.load(f)
                augs = data.get('augmentation', [])
                if augs:
                    score = augs[-1].get('strategic_value', 0)
                    if score < alpha_threshold:
                        status["low_alpha"] = True
                else:
                    status["low_alpha"] = True

            # Readiness Score (0-100)
            score = 100
            score -= len(status["missing_docs"]) * 20
            score -= len(status["missing_benchmarks"]) * 15
            if status["low_alpha"]: score -= 20

            audit_results[root] = {
                "score": max(0, score),
                "issues": status
            }

    with open("readiness_report.json", 'w') as f:
        json.dump(audit_results, f, indent=2)

    # Print summary of failing assets
    print(f"Readiness audit complete. Audited {len(audit_results)} assets.")
    print("--- Audit Summary (Failing < 80) ---")
    for asset, data in audit_results.items():
        if data["score"] < 80:
            print(f"Asset: {asset} | Score: {data['score']}")
            if data['issues']['missing_docs']: print(f"  Missing Docs: {data['issues']['missing_docs']}")
            if data['issues']['missing_benchmarks']: print(f"  Missing Benchmarks: {data['issues']['missing_benchmarks']}")
            if data['issues']['low_alpha']: print(f"  Low Alpha Score")

if __name__ == "__main__":
    run_audit()
