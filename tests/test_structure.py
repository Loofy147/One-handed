import os
import pytest

def test_directories_exist():
    required_dirs = [
        "ai-automation", "computer-vision", "quant-finance", "scientific-ai",
        "llm-engineering", "dataset-businesses", "open-source-products",
        "arabic-ai", "hidden-value-discovery", "high-leverage-research"
    ]
    for d in required_dirs:
        assert os.path.isdir(d), f"Directory {d} is missing"

def test_core_files_exist():
    required_files = ["README.md", "pyproject.toml", "VISION.md", "CONTRIBUTING.md"]
    for f in required_files:
        assert os.path.isfile(f), f"File {f} is missing"

def test_readme_content():
    with open("README.md", "r") as f:
        content = f.read()
        assert "# agentdit-" in content
        assert "Reddit-like platform" in content

def test_pyproject_content():
    with open("pyproject.toml", "r") as f:
        content = f.read()
        assert 'name = "agentdit-"' in content
