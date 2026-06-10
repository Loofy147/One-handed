from huggingface_hub import HfApi

def search_hf():
    api = HfApi()

    queries = {
        "agent framework": "Open Source Products",
        "causal inference": "High Leverage Research",
        "invoice extraction": "AI Automation",
        "protein folding": "Scientific AI",
        "arabic sentiment": "Arabic AI"
    }

    for query, label in queries.items():
        try:
            datasets = api.list_datasets(search=query, sort="downloads", limit=3)
            print(f"\n{label}:")
            for ds in datasets:
                print(f"- {ds.id}")
        except Exception as e:
            print(f"HF Error searching {query}: {e}")

if __name__ == "__main__":
    search_hf()
