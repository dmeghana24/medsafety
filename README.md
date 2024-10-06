# medsafety: Automated Medication Safety Surveillance Pipeline

## Overview

**medsafety** is a modular, open-source pipeline for automated detection of medication safety risks in electronic health record (EHR) data. It combines advanced clinical natural language processing (NLP), rules-based logic, and analytics to support medication safety surveillance across both structured and unstructured clinical data.

---

## Features & Algorithms

### 1. Clinical NLP Extraction

**Algorithm:**  
- Utilizes a hybrid approach combining rule-based parsing (using regular expressions and clinical drug dictionaries) and machine learning models (e.g., CRF, spaCy NER) to extract medication names, dosages, and frequencies from free-text clinical notes.
- Post-processing steps normalize extracted entities to standard vocabularies (e.g., RxNorm).

**Description:**  
- Extracts structured medication data from unstructured clinical notes, enabling downstream safety checks.

---

### 2. Drug Interaction Checks

**Algorithm:**  
- For each extracted or structured medication, queries DrugBank and FDA databases via RESTful APIs.
- Applies a rules engine that matches medication pairs against a curated interactions list, flagging known high-risk combinations.

**Description:**  
- Detects potential drug-drug interactions in real time, leveraging both external databases and user-defined rules.

---

### 3. Allergy Checks

**Algorithm:**  
- Compares prescribed medications against the patient’s allergy list.
- Uses fuzzy string matching (Levenshtein distance) and synonym mapping to account for spelling variations and alternative drug names.

**Description:**  
- Flags medications that may cause allergic reactions, even if drug names are misspelled or listed as synonyms.

---

### 4. Dosing Checks

**Algorithm:**  
- Validates prescribed dosages against age, weight, and renal function-adjusted reference ranges.
- Rules are encoded in YAML/JSON and can be customized for specific populations.

**Description:**  
- Identifies potentially inappropriate dosing, reducing risk of adverse drug events.

---

### 5. De-Identification

**Algorithm:**  
- Applies regular expressions and lookup tables to remove or mask protected health information (PHI) from input data.
- Ensures that all processing is performed on de-identified datasets.

**Description:**  
- Maintains patient privacy and regulatory compliance.

---

### 6. Analytics and Dashboards

**Algorithm:**  
- Aggregates flagged events and error types using pandas and SQL.
- Generates summary statistics and visualizations via Jupyter notebooks and matplotlib/seaborn.

**Description:**  
- Provides actionable insights into medication safety issues, error distributions, and system performance.

---

### 7. Continuous Integration/Testing

**Algorithm:**  
- Automated test suite (pytest) covers all modules.
- GitHub Actions CI/CD pipeline ensures code reliability and reproducibility.

**Description:**  
- Facilitates robust, production-ready deployment and ongoing development.

---

## Architecture

```
[Input: De-identified EHR Data]
        |
        v
[Clinical NLP Extraction] --> [Drug Interaction Checks] --> [Allergy & Dosing Checks]
        |                                 |                           |
        +-----------------------------+---+---------------------------+
                                      |
                                 [Analytics & Dashboards]
```

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dmeghana24/medsafety.git
   cd medsafety
   ```

2. **Set up the Python environment:**
   - Requires Python 3.8+.
   - Use `virtualenv` or `conda`:
     ```bash
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

3. **Install dependencies:**
   - All required packages are listed in `requirements.txt`.

---

## Usage

1. **Prepare your (de-identified) EHR data** in the expected format (see `examples/`).
2. **Run the pipeline:**
   ```bash
   python run_pipeline.py --input data/sample_ehr.csv --output results/
   ```
3. **View analytics:**
   - Open the Jupyter notebooks in `notebooks/` for dashboards and reports.

---

## Configuration

- **Custom Drug Rules:** Edit `config/drug_rules.yaml` to add or modify interaction rules.
- **Data Sources:** Update API keys or endpoints in `config/data_sources.yaml` for DrugBank or FDA integration.
- **De-identification:** Adjust settings in `config/deid.yaml` to match your institution's requirements.

---

## Testing

- **Run tests:**
  ```bash
  pytest tests/
  ```
- Continuous integration is set up via GitHub Actions. All code is covered by automated tests.

---

## Example

**Input:**  
A sample EHR note:
```
Patient prescribed amoxicillin 500mg BID. History of penicillin allergy.
```

**Output:**  
- Flags potential allergy conflict.
- Extracts medication, dose, frequency.
- Checks for dosing appropriateness.

---

## References

For references see the references directory.



---

## Contributing

Contributions are welcome! Please submit pull requests or open issues for feature requests and bug reports. See `CONTRIBUTING.md` for guidelines.

---

## License

MIT License. See `LICENSE` for details.








