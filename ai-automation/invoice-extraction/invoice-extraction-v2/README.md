# Invoice Extraction Dataset v2

## Asset Profile
- **Asset Type**: Dataset
- **Contributor**: Jules-Alpha-Architect (jules-agent)
- **Status**: Production-Ready
- **Monetization Strategy**: OCR/Extraction API for accounting firms, Automated accounts payable services.
- **Moat**: Cleaned and formatted invoice data with high-density field annotations (Total, VAT, Date, Vendor).

## Assessment
Core to "AI Automation". This dataset allows for the training of high-accuracy document intelligence models, significantly reducing manual data entry in business workflows.

## Usability
- **Primary Use Case**: Training LayoutLM or similar vision-language models for document understanding.
- **Data Format**: Images with JSON-formatted extraction labels.
- **Accessibility**: Available on Hugging Face as `manuelaschrittwieser/invoice-extraction-dataset-v2`.

## Usage
```python
from datasets import load_dataset
dataset = load_dataset("manuelaschrittwieser/invoice-extraction-dataset-v2")
```
