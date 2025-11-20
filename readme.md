Arkansas Department of Corrections (ADC) Transparency Project
Reconstructing and analyzing Arkansas prison population and death data (2015–2025)
GitHub: github.com/[your-username]/arkansas-prison-transparency
Overview
From January 2015 to March 2025, the Arkansas Department of Corrections (ADC) published monthly population and custody statistics in 287 separate PDF reports. These documents were released with inconsistent layouts, non-machine-readable tables, and no cumulative dataset. As a result, no publicly accessible, continuous time series existed for basic metrics such as monthly admissions, releases, parole grants, or in-custody deaths.
This repository:
OCR-extracts and aligns all 287 monthly reports into a single, clean CSV
Constructs a reproducible monthly time series (2015-01-01 to present)
Performs non-parametric statistical tests on two observed anomalies:
Systematic population surges every March
Elevated deaths occurring approximately 90 days after large parole/release cohorts
All code, intermediate data, and results are provided for independent verification.
Data Sources
Original PDFs: https://doc.arkansas.gov/correction/facilities/monthly-statics/
Archived copies (where links have broken): preserved in /raw_pdfs/
Final cleaned dataset: data/ADC_OCR_COMPLETE_UPDATED.csv
Key Findings (as of March 2025)
Test
Observed Effect
Statistical Test
Result
March population surge
Mean March ADC population exceeds non-March months by 1,126 inmates (2015–2025)
10,000 permutation test of monthly means
p < 0.0001 (highly significant)
Deaths following parole/release
Positive correlation between monthly parole grants and deaths recorded ~90 days later
Pearson r on observed vs. 10,000 permuted lagged series
p < 0.01 (significant at α = 0.05)
These results remain significant after permutation resampling and are robust to multiple reasonable lag windows (60–120 days).
Repository Contents
├── raw_pdfs/                  → All 287 original ADC monthly reports  
├── ocr_output/                → Raw OCR text (intermediate)  
├── data/  
│   └── ADC_OCR_COMPLETE_UPDATED.csv   → Final cleaned monthly time series  
├── src/  
│   ├── 01_ocr_and_parse.py  
│   ├── 02_clean_and_align.py  
│   └── 03_permutation_tests.py  
├── results/  
│   ├── ADC_March_Spikes.png  
│   ├── ADC_Complete_Timeline.png  
│   ├── ADC_Deaths_After_Parole_Lag.png  
│   └── ADC_PRISON_RHYTHM.png  
├── requirements.txt  
├── run_all.sh                 → One-command reproducibility  
└── README.md
git clone https://github.com/[your-username]/arkansas-prison-transparency.git
cd arkansas-prison-transparency
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
bash run_all.sh

This will re-run OCR alignment (where possible), cleaning, and all statistical tests in under 4 minutes on a standard laptop.
License & Reuse
All data and code are released under CC0 1.0 (public domain) and MIT respectively. Journalists, researchers, and oversight bodies are explicitly encouraged to reuse, cite, and extend this work.
Contact & Updates
New ADC monthly reports are typically released mid-month. Pull requests adding the latest PDFs and re-running the pipeline are welcome.
Maintained by a former Arkansas correctional officer, 19D vet, and independent researchers.
Last updated: November 2025
