import re
from cleaner import normalize_arabic

class ArabicAnalyzer:
    def __init__(self):
        # Basic seed words for sentiment (educational placeholder)
        self.positive_seeds = ["جيد", "ممتاز", "رائع", "جميل", "حب"]
        self.negative_seeds = ["سيء", "قبيح", "فشل", "كره", "حزن"]

    def analyze_sentiment(self, text):
        text = normalize_arabic(text)
        pos_count = sum(1 for word in self.positive_seeds if word in text)
        neg_count = sum(1 for word in self.negative_seeds if word in text)

        if pos_count > neg_count:
            return "positive"
        elif neg_count > pos_count:
            return "negative"
        return "neutral"

    def extract_keywords(self, text, top_n=5):
        text = normalize_arabic(text)
        words = re.findall(r'\b\w+\b', text)
        # Simple frequency distribution (excluding very short words)
        freq = {}
        for w in words:
            if len(w) > 2:
                freq[w] = freq.get(w, 0) + 1

        sorted_keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [k for k, v in sorted_keywords[:top_n]]

if __name__ == "__main__":
    analyzer = ArabicAnalyzer()
    text = "هذا الكتاب رائع جدا وجميل للغاية"
    print(f"Text: {text}")
    print(f"Sentiment: {analyzer.analyze_sentiment(text)}")
    print(f"Keywords: {analyzer.extract_keywords(text)}")
