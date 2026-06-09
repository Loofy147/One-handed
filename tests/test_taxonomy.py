import os
import pytest

def test_sub_categories_exist():
    # Sampling a few from each to ensure structure is there
    checks = [
        "ai-automation/customer-support-chatbots",
        "computer-vision/ocr-systems",
        "quant-finance/market-prediction-models",
        "scientific-ai/protein-folding",
        "llm-engineering/rag-systems",
        "dataset-businesses/arabic-datasets",
        "open-source-products/vector-databases",
        "arabic-ai/arabic-ocr",
        "hidden-value-discovery/anomaly-detection",
        "high-leverage-research/federated-learning"
    ]
    for path in checks:
        assert os.path.isdir(path), f"Sub-category {path} is missing"
        assert os.path.isfile(f"{path}/README.md"), f"README for {path} is missing"

def test_readme_taxonomy():
    with open("README.md", "r") as f:
        content = f.read()
        assert "AI Automation" in content
        assert "Arabic AI (High Opportunity)" in content
        assert "Hidden-Value Discovery" in content
