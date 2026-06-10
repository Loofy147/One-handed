import os
import pytest
import json

def test_agents_dir_exists():
    assert os.path.isdir("agents"), "Agents directory is missing"
    assert os.path.isfile("agents/template.json"), "Agents template.json is missing"
    assert os.path.isfile("agents/README.md"), "Agents README.md is missing"

def test_arabic_ai_foundation_exists():
    path = "arabic-ai/dataset-foundation"
    assert os.path.isdir(path), "Arabic AI dataset foundation directory is missing"
    assert os.path.isfile(f"{path}/README.md"), "Arabic AI dataset foundation README.md is missing"

def test_agent_template_valid_json():
    with open("agents/template.json", "r") as f:
        data = json.load(f)
        assert "agent_name" in data
        assert "agentdit_id" in data

def test_docs_mention_website():
    for fpath in ["VISION.md", "CONTRIBUTING.md"]:
        with open(fpath, "r") as f:
            content = f.read()
            assert "agentdit.com" in content
