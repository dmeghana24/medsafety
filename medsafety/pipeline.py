import pandas as pd
from .utils import load_ehr, load_lexicon, parse_med_list
from .nlp import extract_drug_mentions
from .rules import check_allergy_conflict, check_interactions, check_dose_ranges

class MedicationSafetyPipeline:
    """Main pipeline: loads data, applies rules, outputs flag table."""
    def __init__(self, ehr_path, lexicon_path, allergy_terms_path):
        self.ehr = load_ehr(ehr_path)
        self.lexicon = load_lexicon(lexicon_path)
        with open(allergy_terms_path) as f:
            self.allergy_terms = [line.strip().lower() for line in f.readlines()]
    
    def process_patient(self, row):
        med_list = parse_med_list(str(row['med_list']))
        nlp_meds = extract_drug_mentions(str(row['note']), self.lexicon)
        # Merge lists
        full_med_list = list(set([m[0] for m in med_list] + nlp_meds))
        full_med_tuples = [(m, None) for m in full_med_list]
        # Check rules
        allergy_flags = check_allergy_conflict(row['allergies'], full_med_tuples, self.lexicon)
        interaction_flags = check_interactions(full_med_tuples, self.lexicon)
        dose_flags = check_dose_ranges(med_list, row['age'], row['weight_kg'], row['creatinine_mg_dl'], self.lexicon)
        return {
            'patient_id': row['patient_id'],
            'allergy_flags': allergy_flags,
            'interaction_flags': interaction_flags,
            'dose_flags': dose_flags
        }

    def run(self):
        results = [self.process_patient(row) for idx, row in self.ehr.iterrows()]
        return pd.DataFrame(results)

