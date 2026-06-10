# Twitter Financial News Sentiment

## Asset Profile
- **Asset Type**: Dataset / Annotated Corpus
- **Contributor**: jules-agent
- **Status**: Production-Ready
- **Monetization Strategy**: Alpha generation for trading algorithms, B2B sentiment analysis API.
- **Technical Moat**: High-quality human-annotated sentiment labels for financial news on social media, capturing market-moving nuances.

## Description
This dataset contains thousands of financial news tweets annotated with sentiment (bullish, bearish, neutral). It is a vital asset for training models that detect early market signals from social media trends.

## Usage
This dataset is mirrored from Hugging Face: `zeroshot/twitter-financial-news-sentiment`.
To load it:
```python
from datasets import load_dataset
dataset = load_dataset("zeroshot/twitter-financial-news-sentiment")
```
