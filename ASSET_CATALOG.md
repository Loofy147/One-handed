# Centralized Asset Catalog

This catalog provides a high-level overview of all strategic assets available in the agentdit- repository. Each asset is designed to be a reusable, high-leverage component for future monetization and scaling.

## 1. Arabic AI
- **[arabic-books-corpus](./arabic-ai/arabic-datasets/arabic-books-corpus)**
  - **Moat**: Curated collection of diverse Arabic literary and educational texts, cleaned and normalized using our proprietary cleaner.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[arabic-dialect-id](./arabic-ai/arabic-datasets/arabic-dialect-id)**
  - **Moat**: Specialized labels for distinguishing between major Arabic dialects (Egyptian, Gulf, Levantine, Maghrebi), critical for routing queries to optimized models.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[arabic-ner-corpus](./arabic-ai/arabic-datasets/arabic-ner-corpus)**
  - **Moat**: High-quality, gold-standard Named Entity Recognition (NER) labels for Arabic text, crucial for information extraction in complex domains.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[arabic-sentiment-tweets](./arabic-ai/arabic-datasets/arabic-sentiment-tweets)**
  - **Moat**: Large-scale annotated dataset for Arabic dialects and MSA, covering social media specific linguistic nuances.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[arabic-turath-ocr](./arabic-ai/arabic-ocr/arabic-turath-ocr)**
  - **Moat**: Focus on "Turath" (heritage) scripts, which are significantly more complex than modern digital fonts and require specialized training data.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[egyptian-speech-corpus](./arabic-ai/arabic-speech-recognition/egyptian-speech-corpus)**
  - **Moat**: Focus on the Egyptian dialect, which is one of the most widely spoken and culturally influential Arabic dialects, yet underserved by standard MSA models.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[qasr-speech-corpus](./arabic-ai/arabic-speech-recognition/qasr-speech-corpus)**
  - **Moat**: Specialized in dialectal Arabic speech continuations, filling a gap in traditional ASR training sets.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 2. Quant Finance
- **[twitter-financial-news](./quant-finance/sentiment-analysis/twitter-financial-news)**
  - **Moat**: High-quality annotations for financial sentiment, specifically curated from news-related tweets.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[twitter-financial-sentiment](./quant-finance/sentiment-analysis/twitter-financial-sentiment)**
  - **Moat**: High-quality human-annotated sentiment labels for financial news on social media, capturing market-moving nuances.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 3. LLM Engineering
- **[arabic-rag-benchmark-v1](./llm-engineering/rag-systems/arabic-rag-benchmark-v1)**
  - **Moat**: Specialized benchmark focusing on Arabic linguistic nuances, retrieval accuracy in dialectal contexts, and hallucination detection.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 4. AI Automation
- **[email-spam-classification](./ai-automation/email-automation/email-spam-classification)**
  - **Moat**: Large-scale annotated dataset covering modern spam techniques and phishing attempts.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[invoice-extraction-v2](./ai-automation/invoice-extraction/invoice-extraction-v2)**
  - **Moat**: Cleaned and formatted invoice data with high-density field annotations (Total, VAT, Date, Vendor).
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 5. Computer Vision
- **[image-segmentation-toy](./computer-vision/object-detection/image-segmentation-toy)**
  - **Moat**: Lightweight, high-quality toy dataset for verifying segmentation architectures.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[license-plates-700k](./computer-vision/license-plate-recognition/license-plates-700k)**
  - **Moat**: Massive scale (700k+ images) providing robustness against diverse lighting, angles, and occlusions.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[medical-image-synthesis](./computer-vision/medical-image-analysis/medical-image-synthesis)**
  - **Moat**: Multimodal synthesis data is extremely rare and valuable for training models that can cross-reference different imaging modalities (e.g., MRI to CT).
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[synthetic-defect-data](./computer-vision/defect-detection/synthetic-defect-data)**
  - **Moat**: High-quality synthetic anomalies based on the MVTec AD standard, providing crucial edge cases for industrial defect detection models.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 6. Scientific AI
- **[protein-folding-corpus](./scientific-ai/protein-folding/protein-folding-corpus)**
  - **Moat**: Aggregated experimental and predicted protein structure data, optimized for training fast-folding models.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[science-materials-corpus](./scientific-ai/materials-discovery/science-materials-corpus)**
  - **Moat**: Specialized scientific data covering property-structure relationships in materials, which is difficult to aggregate and standardize.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 7. Hidden Value Discovery
- **[credit-card-fraud-v1](./hidden-value-discovery/fraud-detection/credit-card-fraud-v1)**
  - **Moat**: High-quality transaction data with verified fraud labels, enabling the development of robust anomaly detection systems.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[mvtec-anomaly-ground-truth](./hidden-value-discovery/anomaly-detection/mvtec-anomaly-ground-truth)**
  - **Moat**: Ground truth labels for anomaly detection that span across industrial and digital patterns, essential for 'Hidden Value Discovery' through pattern mining.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 8. Dataset Businesses
- **[synthetic-medical-speech](./dataset-businesses/synthetic-data-generation/synthetic-medical-speech)**
  - **Moat**: High-fidelity synthetic speech for specialized medical terminology, bypassing privacy issues associated with real patient recordings.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[synthetic-pose-data](./dataset-businesses/synthetic-data-generation/synthetic-pose-data)**
  - **Moat**: Synthetic data that reduces the need for expensive, manual human pose annotation while providing perfect ground truth for edge cases.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 9. Open Source Products
- **[unified-agent-eval](./open-source-products/evaluation-tools/unified-agent-eval)**
  - **Moat**: Cross-platform evaluation metrics for LLM agents, focusing on trajectory analysis and tool-use efficiency.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

## 10. High Leverage Research
- **[federated-learning-playground](./high-leverage-research/federated-learning/federated-learning-playground)**
  - **Moat**: Specialized data and benchmarks for poisoning-resilient federated learning, addressing critical security gaps in distributed AI.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[synthetic-causal-inference](./high-leverage-research/causal-ai/synthetic-causal-inference)**
  - **Moat**: Synthetic data specifically designed to test causal discovery algorithms under complex confounding factors.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)
- **[synthetic-pii-finance](./high-leverage-research/causal-ai/synthetic-pii-finance)**
  - **Moat**: High-fidelity synthetic financial data with realistic (but safe) PII patterns across multiple languages.
  - **Contributor**: [Jules-Alpha-Architect (jules-agent)](./agents/jules.json)

---
*Generated by the Agent Asset Discovery System.*
