# Arabic NER Corpus

## Asset Profile
- **Asset Type**: Dataset
- **Contributor**: Jules-Alpha-Architect (jules-agent)
- **Status**: Production-Ready
- **Monetization Strategy**: API for Arabic entity extraction, training data for legal and financial document analysis.
- **Moat**: High-quality, gold-standard Named Entity Recognition (NER) labels for Arabic text, crucial for information extraction in complex domains.

## Description
A comprehensive Named Entity Recognition dataset for the Arabic language, focusing on diverse entity types including persons, organizations, locations, and dates. This corpus is essential for building robust Arabic NLP systems.

## Usage
This dataset is mirrored from Hugging Face: `iahlt/arabic_ner_mafat_folds`.
```python
from datasets import load_dataset
dataset = load_dataset("iahlt/arabic_ner_mafat_folds")
```
