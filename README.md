# Arkansas Department of Corrections — Population & Death Timeline, 2015–2025

A data-driven reconstruction of monthly prison population, parole, and in-custody death statistics from 287 official PDF reports published by the Arkansas Division of Correction (ADC).

**Full source archive**: [Zenodo — DOI: 10.5281/zenodo.17663528](https://doi.org/10.5281/zenodo.17663528)

---

## Table of Contents
- [Overview](#overview)
- [Key Findings](#key-findings)
- [Recent Developments](#recent-developments)
- [Repository Contents](#repository-contents)
- [Data Sources](#data-sources)
- [Data Verification](#data-verification)
- [Methodology](#methodology)
- [Connected Repositories](#connected-repositories)
- [Limitations & Disclaimer](#limitations--disclaimer)
- [License & Contact](#license--contact)

---

## Overview

From January 2015 to March 2025, the Arkansas Department of Corrections published monthly population and custody statistics in 287 separate PDF reports. These documents were released with inconsistent layouts, non-machine-readable tables, and no cumulative dataset. As a result, no publicly accessible, continuous time series existed for basic metrics such as monthly admissions, releases, parole grants, or in-custody deaths.

This repository:
- OCR-extracts and aligns all 287 monthly reports into a single, clean CSV
- Constructs a reproducible monthly time series (January 2015 – December 2025, with data through August 2025)
- Performs non-parametric statistical tests on two observed anomalies:
  - Systematic population surges every March
  - Elevated deaths occurring approximately 90 days after large parole/release cohorts

All code, intermediate data, and results are provided for independent verification.

---

## Key Findings

| Test | Observed Effect | Statistical Test | Result |
|------|----------------|------------------|--------|
| March population surge | Mean March ADC population exceeds non-March months by +1,126 inmates (2015–2025) | 10,000-iteration permutation test of monthly means | p < 0.0001 (highly significant) |
| Deaths following parole/release | Positive correlation between monthly parole grants and deaths recorded ~90 days later | Pearson r on observed vs. 10,000 permuted lagged series | p < 0.01 (significant at α = 0.05) |

These results remain significant after permutation resampling and are robust to multiple reasonable lag windows (60–120 days).

---

## Recent Developments

Since this repository was created in November 2025, independent reporting has corroborated and expanded upon the patterns documented here:

| Development | Source | Date |
|-------------|--------|------|
| Arkansas prison deaths nearly doubled from 51 (2022) to 110 (through October 2025) | [White River Now / Arkansas Democrat-Gazette](https://www.whiterivernow.com/2025/12/28/arkansas-prison-deaths-nearly-double-since-2022-reports-show/) | Dec 28, 2025 |
| Prison system costs detailed — county jail overflow reimbursement hit $27.7M in FY24–25 | [Arkansas Advocate](https://arkansasadvocate.com/2025/12/17/overcrowded-arkansas-prison-system-costs-inmates-taxpayers/) | Dec 17, 2025 |
| Protect Arkansas Act (2023) projected to add ~3,000 inmates over next decade | [Arkansas Advocate](https://arkansasadvocate.com/2025/12/19/overcrowded-protect-arkansas-act-to-drive-continued-prison-population-growth-for-at-least-a-decade/) | Dec 19, 2025 |
| ADC reported 82–84 deaths through August 2025 at legislative committee hearing | [CitizenPortal / ADC testimony](https://citizenportal.ai/articles/6424201/Arkansas/DOC-reports-dozens-of-inmate-deaths-this-year-officials-point-to-drug-overdoses-and-chronic-illness) | 2025 |

### Annual Death Totals (Independent Reporting)

| Year | Deaths | Source |
|------|--------|--------|
| 2022 | 51 | White River Now |
| 2023 | 81 | White River Now |
| 2024 | 100 | White River Now |
| 2025 | 110 (through October) | White River Now / Arkansas Democrat-Gazette |

---

## Repository Contents

```
Arkansas-Department-of-Corrections-2015-2025-Timeline/
├── README.md                          # This file
├── ADC_FINAL_CLEAN.csv                # Cleaned monthly death/parole/population (132 months)
├── ADC_FULL_TIMELINE.csv              # Full monthly time series (2015–2025)
├── ADC_OCR_COMPLETE.csv               # Complete OCR-extracted data from all 287 PDFs
├── adc_monthly_events.csv             # Monthly event counts (death, other, parole, population)
├── adc_timeline_data.csv              # Year-level document counts and key events (1992–2026)
├── run_updated_permutation_tests.py   # Statistical analysis: permutation tests (Python)
├── ADC_Complete_Timeline.png          # Visualization: full timeline
├── ADC_Deaths_After_Parole.png        # Visualization: deaths vs. parole lag
├── ADC_March_Spikes.png               # Visualization: March population spikes
├── ADC_AddOns.zip                     # Supplementary PDFs (43 files: budget schedules, facility reports)
└── Copilot_Opus_4.6_Analysis/         # Independent verification workstation
    ├── README.md
    └── Verification_Reports/
        ├── core_data_verification.md  # ✅ Data quality and claims verification
        └── data_interpretation_guide.md # 📊 Guide to interpreting the CSV data
```

### Files in the Zenodo Archive (Too Large for GitHub)

The full dataset referenced by the analysis script (`ADC_OCR_COMPLETE_UPDATED.csv`) and the 287 source PDFs (~2.8 GB) are preserved in the [Zenodo archive](https://doi.org/10.5281/zenodo.17663528). These files exceeded GitHub's size limits and are hosted externally for reproducibility.

---

## Data Sources

| Source | URL |
|--------|-----|
| ADC monthly statistics (official) | https://doc.arkansas.gov/correction/facilities/monthly-statistics/ |
| ADC Secretary's Reports | https://doc.arkansas.gov/office-of-the-secretary/secretarys-reports/ |
| Full PDF archive (287 files, Zenodo) | https://doi.org/10.5281/zenodo.17663528 |
| Prison Policy Initiative — Arkansas | https://www.prisonpolicy.org/profiles/AR.html |

**Note**: The ADC website has periodically restructured its URLs. If the monthly statistics link above has changed, the Zenodo archive preserves all 287 original PDFs for reproducibility.

---

## Data Verification

Core statistical claims have been independently verified. See [`Copilot_Opus_4.6_Analysis/Verification_Reports/core_data_verification.md`](Copilot_Opus_4.6_Analysis/Verification_Reports/core_data_verification.md) for the full report.

| Claim | Status |
|-------|--------|
| 287 monthly PDF reports extracted via OCR | ✅ Verified |
| Monthly time series spans January 2015 – December 2025 | ✅ Verified (132 rows, data through August 2025) |
| March population surge: +1,126 inmates avg | ✅ Methodology verified (permutation test) |
| Deaths-parole lag correlation (90-day) | ✅ Methodology verified (Pearson r with permutation) |
| Death trends consistent with independent reporting | ✅ Corroborated by White River Now (Dec 2025) |

### Contextual Data Points

| Fact | Value | Source |
|------|-------|--------|
| Arkansas incarceration rate | 912 per 100,000 (3rd in U.S.) | [Prison Policy Initiative](https://www.prisonpolicy.org/profiles/AR.html) |
| State prison population | 17,000+ (18,997 including jail backup, Dec 2025) | ADC / Arkansas Advocate |
| County jail backup (state inmates) | ~1,663/month avg | ADC Director's Board Report |
| Prison deaths (2025, through October) | 110 | White River Now |

---

## Methodology

1. **Source documents**: 287 official monthly PDF reports published by the Arkansas Division of Correction (January 2015 – March 2025), obtained from [doc.arkansas.gov](https://doc.arkansas.gov/)
2. **Extraction**: OCR-based text extraction producing structured monthly data rows across death, parole, and population metrics
3. **Statistical analysis**: Non-parametric permutation testing (10,000 iterations) for:
   - March vs. non-March population means
   - Pearson correlation with 90-day lag between parole grants and subsequent deaths
4. **Verification**: Key findings cross-checked against official annual reports, legislative testimony, and independent news coverage (December 2025)
5. **Transparency**: Full archive of all 287 source PDFs preserved on [Zenodo](https://doi.org/10.5281/zenodo.17663528) for reproducibility

---

## Connected Repositories

| Repository | Focus |
|-----------|-------|
| [Arkansas-DOC-Expenditures-2015-2025](https://github.com/Leerrooy95/Arkansas-DOC-Expenditures-2015-2025) | Ten-year expenditure analysis ($3.92B ADC spending), financial trends, revenue offsets |
| [The_Regulated_Friction_Project](https://github.com/Leerrooy95/The_Regulated_Friction_Project) | Data-driven analysis of temporal correlations between friction events, policy shifts, and capital flows |

---

## Limitations & Disclaimer

- All data consists of **public records** published by the Arkansas Department of Corrections. No external estimates or modeling were used for the core dataset.
- The CSV datasets were produced via OCR extraction from scanned PDFs. While key figures have been verified, individual row-level accuracy may vary due to OCR artifacts in the source documents.
- Several months in 2024–2025 show zero values across all metrics, likely reflecting reports not yet available at time of extraction rather than actual zero activity.
- The statistical tests identify correlations and patterns. They do not make claims about causation, policy intent, or institutional motivation.
- The Zenodo DOI (10.5281/zenodo.17663528) may not be publicly accessible yet. If the link does not resolve, the source PDFs are available from [doc.arkansas.gov](https://doc.arkansas.gov/office-of-the-secretary/secretarys-reports/).

---

## License & Contact

**Data**: CC0 1.0 — Public Domain. Use and share freely.
**Code**: MIT License.

Journalists, researchers, advocacy groups, and oversight bodies are explicitly encouraged to reuse, cite, and extend this work.

**Prepared by**: Austin Smith
U.S. Army 19D Veteran | Former Arkansas Correctional Officer
November 2025

**GitHub**: [@Leerrooy95](https://github.com/Leerrooy95)
