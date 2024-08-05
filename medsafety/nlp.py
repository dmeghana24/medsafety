import re
from .utils import normalize_text

def extract_drug_mentions(note, drug_lexicon):
    """Find drug mentions in note using fuzzy/partial match and drug list."""
    mentions = []
    norm_note = normalize_text(note)
    for drug in drug_lexicon['generic']:
        pattern = r'\b' + re.escape(drug.lower()) + r'\b'
        if re.search(pattern, norm_note):
            mentions.append(drug)
    # Also try brand names
    for brand in drug_lexicon['brand']:
        pattern = r'\b' + re.escape(brand.lower()) + r'\b'
        if re.search(pattern, norm_note):
            generic = drug_lexicon[drug_lexicon['brand'] == brand]['generic'].values[0]
            if generic not in mentions:
                mentions.append(generic)
    return mentions

def extract_allergy_mentions(note, allergy_terms):
    """Return all allergy terms mentioned in note."""
    found = []
    norm_note = normalize_text(note)
    for term in allergy_terms:
        if term in norm_note:
            found.append(term)
    return found

