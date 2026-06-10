from huggingface_hub import HfApi
import json

def search():
    api = HfApi()

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

    results = {}
    for cat, queries in category_queries.items():
        results[cat] = []
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
    print("Search results saved to search_results.json")

if __name__ == "__main__":
    search()
