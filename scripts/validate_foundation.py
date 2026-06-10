import os
import sys

def validate():
    required_dirs = [
        "ai-automation", "computer-vision", "quant-finance", "scientific-ai",
        "llm-engineering", "dataset-businesses", "open-source-products",
        "arabic-ai", "hidden-value-discovery", "high-leverage-research"
    ]
    required_files = ["README.md", "pyproject.toml", "VISION.md", "CONTRIBUTING.md"]

    for d in required_dirs:
        if not os.path.isdir(d):
            print(f"FAILED: Directory '{d}' is missing.")
            return False

    for f in required_files:
        if not os.path.isfile(f):
            print(f"FAILED: File '{f}' is missing.")
            return False

    print("SUCCESS: agentdit- foundation is valid.")
    return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
