import os
import json
from huggingface_hub import HfApi

def get_current_assets():
    root_dir = "."
    categories = {}
    for root, dirs, files in os.walk(root_dir):
        if "metadata.json" in files:
            path = os.path.join(root, "metadata.json")
            with open(path, 'r') as f:
                try:
                    data = json.load(f)
                    cat = data.get('category', 'Uncategorized')
                    categories[cat] = categories.get(cat, 0) + 1
                except:
                    pass
    return categories

def search():
    api = HfApi()
    current_counts = get_current_assets()

    category_queries = {
        "ai-automation": ["invoice extraction", "email classification", "contract analysis"],
        "computer-vision": ["license plate", "defect detection", "satellite imagery"],
        "quant-finance": ["financial sentiment", "stock prediction", "crypto data"],
        "scientific-ai": ["protein folding", "materials science", "climate modeling"],
        "llm-engineering": ["rag benchmark", "agent framework", "prompt optimization"],
        "dataset-businesses": ["synthetic data", "labeled dataset", "image segmentation"],
        "open-source-products": ["mlops", "vector database", "evaluation tool"],
        "arabic-ai": ["arabic text", "arabic speech", "arabic translation"],
        "hidden-value-discovery": ["fraud detection", "anomaly detection", "market inefficiency"],
        "high-leverage-research": ["causal inference", "federated learning", "neuro-symbolic"]
    }

    print("--- Repository Gap Analysis ---")
    gaps = []
    for cat in category_queries.keys():
        count = current_counts.get(cat, 0)
        print(f"{cat}: {count} assets")
        if count < 3:
            gaps.append(cat)

    if gaps:
        print(f"\nFocusing discovery on gaps: {gaps}")

    results = {}
    # Prioritize searching for categories with gaps
    search_list = gaps if gaps else category_queries.keys()

    for cat in search_list:
        results[cat] = []
        queries = category_queries[cat]
        for q in queries:
            try:
                datasets = list(api.list_datasets(search=q, sort="downloads", limit=2))
                for ds in datasets:
                    results[cat].append({
                        "id": ds.id,
                        "query": q,
                        "downloads": ds.downloads
                    })
            except Exception as e:
                print(f"Error searching {q}: {e}")

    with open("search_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nSearch results saved to search_results.json")

if __name__ == "__main__":
    search()
