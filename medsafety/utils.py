import pandas as pd

def load_ehr(path):
    """Load EHR CSV file as DataFrame."""
    return pd.read_csv(path)

def load_lexicon(path):
    """Load drug lexicon as DataFrame."""
    return pd.read_csv(path)

def normalize_text(text):
    """Basic lowercase and whitespace stripping."""
    if pd.isna(text):
        return ''
    return str(text).strip().lower()

def tokenize(text, stopwords):
    tokens = [w for w in str(text).split() if w.lower() not in stopwords]
    return tokens

def parse_med_list(med_list):
    """Parse medication strings into (name, dose, freq) tuples."""
    meds = []
    for item in med_list.split(';'):
        parts = item.strip().split()
        if len(parts) >= 2:
            meds.append((parts[0], parts[1]))
        elif len(parts) == 1:
            meds.append((parts[0], None))
    return meds

