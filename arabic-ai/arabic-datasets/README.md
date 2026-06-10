# Arabic Datasets

This module contains tools and resources for creating and processing high-quality Arabic datasets.

## Utilities

### Cleaner
Located at `src/cleaner.py`, this utility provides foundational text normalization for Arabic, including:
- Removal of diacritics (harakat).
- Normalization of Alef variants.
- Normalization of Teh Marbuta and Hamza.

## Usage
```python
from src.cleaner import normalize_arabic
clean_text = normalize_arabic("الْعَرَبِيَّةُ")
```
