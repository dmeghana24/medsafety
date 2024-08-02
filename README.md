# 💊 Medication Safety Software Pipeline

_A graduate-level, modular pipeline for automated detection of medication safety risks in EHR data—combining clinical NLP, rules-based logic, and analytics._

## 🔬 Motivation

Medication errors are a major patient safety concern (Bates et al., JAMA 1998; Schiff et al., JAMA 2015). This pipeline aims to automate medication safety surveillance using clinical notes and structured medication data.

## 📦 Features

- **NLP**: Extraction of drug names, doses, and frequencies from free-text clinical notes using dictionary/rule-based and ML hybrid approaches
- **Drug Interaction Checks**: Real-time cross-referencing with DrugBank, FDA, and custom rules
- **Allergy Checks**: Allergy/medication reconciliation with robust spelling and synonym handling
- **Dosing Checks**: Contextual dose range validation (age, renal function, weight)
- **De-Identification**: Sample data and scripts respect PHI; real-world pipeline accepts only de-identified input
- **Dashboards**: Analytical notebooks for error type distribution, flag rate, error causes, and reporting
- **Continuous Integration**: CI/CD with GitHub Actions and full test coverage

## 🛠️ Getting Started

```bash
git clone https://github.com/YOURNAME/medsafety.git
cd medsafety
pip install -r requirements.txt
```
