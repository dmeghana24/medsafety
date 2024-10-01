# Pipeline Architecture

- Input: De-identified CSVs of EHR and drug lexicon
- Preprocessing: Normalization, tokenization, basic NLP
- Rules engine: Allergy, interaction, and dose checking
- Analytics: Error type aggregation, dashboard
- Reporting: CSV output, plots
- Modular design supports extension to more advanced NLP (e.g., spaCy, MedEx)

