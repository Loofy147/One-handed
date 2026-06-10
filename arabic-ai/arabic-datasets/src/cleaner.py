import re

def normalize_arabic(text):
    """
    Basic normalization for Arabic text.
    - Removes diacritics (harakat).
    - Normalizes alef, hamza, and teh marbuta.
    """
    if not text:
        return ""

    # Remove diacritics
    text = re.sub(r'[\u064B-\u0652]', '', text)

    # Normalize Alef
    text = re.sub(r'[\u0622\u0623\u0625]', '\u0627', text)

    # Normalize Teh Marbuta
    text = re.sub(r'\u0629', '\u0647', text)

    # Normalize Hamza on Waw and Ya
    text = re.sub(r'\u0624', '\u0648', text)
    text = re.sub(r'\u0626', '\u064A', text)

    return text.strip()

if __name__ == "__main__":
    sample = "الْعَرَبِيَّةُ لُغَةٌ جَمِيلَةٌ"
    print(f"Original: {sample}")
    print(f"Normalized: {normalize_arabic(sample)}")
