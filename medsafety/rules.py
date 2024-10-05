import numpy as np

def check_allergy_conflict(patient_allergies, med_list, drug_lexicon):
    """
    Check if prescribed meds conflict with allergy list.
    Flags direct or allergy-family conflicts (case/plural insensitive).
    """
    flags = []
    # Lowercase, strip whitespace, and remove trailing "s" for plurals
    allergy_set = set([a.strip().lower().rstrip('s') for a in str(patient_allergies).split(';') if a.strip()])
    for med, _ in med_list:
        med_row = drug_lexicon[drug_lexicon['generic'].str.lower() == med.lower()]
        if not med_row.empty:
            allergy_family = med_row['allergy_family'].values[0]
            # Direct match (singular/plural insensitive)
            if med.lower().rstrip('s') in allergy_set:
                flags.append((med, "allergy_conflict"))
            # Family match (singular/plural insensitive)
            elif isinstance(allergy_family, str) and allergy_family.strip().lower().rstrip('s') in allergy_set:
                flags.append((med, "allergy_family_conflict"))
    return flags

def check_interactions(med_list, drug_lexicon):
    """
    Check for documented drug-drug interactions among prescribed meds.
    """
    flagged = []
    meds = [m[0] for m in med_list]
    for i, med1 in enumerate(meds):
        row1 = drug_lexicon[drug_lexicon['generic'].str.lower() == med1.lower()]
        if row1.empty: continue
        interactions = str(row1['interactions'].values[0]).split(';')
        for med2 in meds[i+1:]:
            if any(med2 in s for s in interactions):
                flagged.append((med1, med2, "interaction"))
    return flagged

def check_dose_ranges(med_list, patient_age, patient_weight, patient_creatinine, drug_lexicon):
    """
    Check if med doses exceed max or should be adjusted for renal function.
    """
    flagged = []
    for med, dose_str in med_list:
        if not dose_str:
            continue
        try:
            # Extract numeric dose (e.g., "500mg" -> 500)
            import re
            dose = float(re.sub(r'[^\d.]', '', dose_str))
        except Exception:
            dose = np.nan
        row = drug_lexicon[drug_lexicon['generic'].str.lower() == med.lower()]
        if row.empty:
            continue
        max_dose = row['max_daily_dose_mg'].values[0]
        renal_adjust = row['renal_adjust'].values[0]
        if dose and dose > float(max_dose):
            flagged.append((med, dose, "exceeds_max"))
        if renal_adjust == 'Yes' and patient_creatinine > 1.5:
            flagged.append((med, dose, "renal_adjustment"))
    return flagged

