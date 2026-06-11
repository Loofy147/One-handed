import re

def normalize_arabic(text):
    """
    Advanced normalization for Arabic text.
    - Removes diacritics (harakat).
    - Normalizes alef, hamza, and teh marbuta.
    - Removes Kashida (Tatweel).
    - Normalizes digits (Western and Eastern).
    - Cleans non-Arabic characters if requested (optional).
    """
    if not text:
        return ""

    # 1. Remove diacritics
    text = re.sub(r'[\u064B-\u0652]', '', text)

    # 2. Remove Kashida (Tatweel)
    text = re.sub(r'\u0640', '', text)

    # 3. Normalize Alef
    text = re.sub(r'[\u0622\u0623\u0625]', '\u0627', text)

    # 4. Normalize Teh Marbuta
    text = re.sub(r'\u0629', '\u0647', text)

    # 5. Normalize Hamza on Waw and Ya
    text = re.sub(r'\u0624', '\u0648', text)
    text = re.sub(r'\u0626', '\u064A', text)

    # 6. Normalize Eastern Arabic Digits to Western
    eastern_to_western = {
        '\u0660': '0', '\u0661': '1', '\u0662': '2', '\u0663': '3', '\u0664': '4',
        '\u0665': '5', '\u0666': '6', '\u0667': '7', '\u0668': '8', '\u0669': '9'
    }
    for e, w in eastern_to_western.items():
        text = text.replace(e, w)

    return text.strip()

def clean_noise(text):
    """Removes special characters and extra whitespace."""
    text = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

if __name__ == "__main__":
    sample = "الْعَرَبِيَّةُ لُغَةٌ جَمِيلَةٌ... ١٢٣٤٥"
    print(f"Original: {sample}")
    norm = normalize_arabic(sample)
    print(f"Normalized: {norm}")
    print(f"Cleaned: {clean_noise(norm)}")
