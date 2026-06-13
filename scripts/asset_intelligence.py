import os
import json

def generate_dashboard():
    root_dir = "."
    categories = {}
    total_assets = 0
    total_samples = 0
    strategic_value_sum = 0

    # Load readiness report
    readiness = {}
    if os.path.exists("readiness_report.json"):
        with open("readiness_report.json", 'r') as f:
            readiness = json.load(f)

    all_categories = [
        "arabic-ai", "quant-finance", "llm-engineering", "ai-automation",
        "computer-vision", "scientific-ai", "hidden-value-discovery",
        "dataset-businesses", "open-source-products", "high-leverage-research"
    ]

    for cat in all_categories:
        categories[cat] = {"count": 0, "strategic_value": 0, "samples": 0, "ready_count": 0}

    for root, dirs, files in os.walk(root_dir):
        if "metadata.json" in files:
            total_assets += 1
            with open(os.path.join(root, "metadata.json"), 'r') as f:
                data = json.load(f)
                cat = data.get('category', 'Uncategorized')
                if cat not in categories:
                    categories[cat] = {"count": 0, "strategic_value": 0, "samples": 0, "ready_count": 0}
                categories[cat]["count"] += 1

                augs = data.get('augmentation', [])
                if augs:
                    v = augs[-1].get('strategic_value', 0.5)
                    categories[cat]["strategic_value"] += v
                    strategic_value_sum += v

            # Check readiness from audit
            if root in readiness:
                if readiness[root]["score"] >= 80:
                    categories[cat]["ready_count"] += 1

            sidecar_path = os.path.join(root, "proprietary_alpha.json")
            if os.path.exists(sidecar_path):
                with open(sidecar_path, 'r') as f:
                    alpha = json.load(f)
                    s = alpha.get('synthetic_samples_count', 0)
                    categories[cat]["samples"] += s
                    total_samples += s

    lines = ["# Asset Intelligence Dashboard", ""]
    lines.append(f"**Total Assets**: {total_assets}")
    lines.append(f"**Total Synthetic Samples**: {total_samples:,}")
    lines.append(f"**Avg Strategic Value**: {strategic_value_sum / total_assets:.2f}" if total_assets > 0 else "0")
    lines.append("")

    lines.append("## Category Breakdown")
    lines.append("| Category | Assets | Ready (80+) | Avg Strat Value | Gap Priority |")
    lines.append("|----------|--------|-------------|-----------------|--------------|")

    for cat in all_categories:
        info = categories[cat]
        avg_v = info["strategic_value"] / info["count"] if info["count"] > 0 else 0

        priority_weight = {
            "arabic-ai": 1.5, "quant-finance": 1.4, "high-leverage-research": 1.3,
            "llm-engineering": 1.2, "ai-automation": 1.1
        }.get(cat, 1.0)

        gap_score = max(0, (5 - info["count"]) * 20 * priority_weight)

        lines.append(f"| {cat} | {info['count']} | {info['ready_count']} | {avg_v:.2f} | {gap_score:.0f} |")

    lines.append("")
    lines.append("## Production Readiness Audit")
    lines.append("Top assets by readiness score:")
    sorted_ready = sorted(readiness.items(), key=lambda x: x[1]['score'], reverse=True)
    for path, data in sorted_ready[:10]:
        lines.append(f"- **{os.path.basename(path)}**: Score {data['score']} ({path})")

    with open("ASSET_DASHBOARD.md", 'w') as f:
        f.write("\n".join(lines))
    print("ASSET_DASHBOARD.md upgraded.")

if __name__ == "__main__":
    generate_dashboard()
