import pandas as pd
from medsafety.rules import check_allergy_conflict, check_interactions, check_dose_ranges

def test_allergy_conflict():
    lex = pd.read_csv("data/drug_lexicon.csv")
    result = check_allergy_conflict("Penicillin", [("Amoxicillin", None)], lex)
    assert result, "Should flag allergy conflict for Amoxicillin/Penicillin"

def test_interactions():
    lex = pd.read_csv("data/drug_lexicon.csv")
    result = check_interactions([("Warfarin", None), ("Ciprofloxacin", None)], lex)
    assert any("Warfarin" in str(x) and "Ciprofloxacin" in str(x) for x in result)

def test_dose_ranges():
    lex = pd.read_csv("data/drug_lexicon.csv")
    result = check_dose_ranges([("Metoprolol", "500mg")], 60, 75, 1.0, lex)
    assert any("exceeds_max" in str(x) for x in result)

