import pandas as pd
import matplotlib.pyplot as plt

def error_type_distribution(flag_df):
    """Plot number of each flag type across all patients."""
    errors = []
    for col in ['allergy_flags', 'interaction_flags', 'dose_flags']:
        errors.extend([flag[1] if isinstance(flag, tuple) else 'flag' for sublist in flag_df[col] for flag in (sublist if isinstance(sublist, list) else [sublist]) if sublist])
    pd.Series(errors).value_counts().plot(kind='bar', title='Medication Safety Flags')
    plt.xlabel("Flag Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

