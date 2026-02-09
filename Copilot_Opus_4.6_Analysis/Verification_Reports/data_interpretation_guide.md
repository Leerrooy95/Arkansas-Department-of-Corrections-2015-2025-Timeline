# Data Interpretation Guide

**Prepared by**: GitHub Copilot (Opus 4.6)
**Date**: February 9, 2026

---

## Understanding the CSV Data

### What the numbers represent

The monthly CSV files (`ADC_FINAL_CLEAN.csv`, `ADC_FULL_TIMELINE.csv`, `ADC_OCR_COMPLETE.csv`) contain **keyword frequency counts** extracted from 287 official ADC PDF reports via OCR:

| Column | Meaning | Example |
|--------|---------|---------|
| `death` | Number of times death-related keywords appeared in that month's PDF | `4` = the word "death" appeared 4 times |
| `parole` | Number of times parole-related keywords appeared | `60` = 60 mentions of parole |
| `population` | Number of times population-related keywords appeared | `45` = 45 mentions of population |

These are **not** raw counts of individual deaths, parole grants, or population headcounts.

### Why this still matters

Keyword frequency in official government reports is itself a meaningful signal:
- **March reports** consistently contain far more population-related keyword mentions than other months, suggesting ADC uses March reports for annual population summaries or reviews
- **Temporal correlation** between parole and death keywords (with a 90-day lag) indicates that months with heavy parole reporting are followed by months with elevated death reporting
- **Trend analysis** on keyword frequencies can reveal shifts in institutional reporting emphasis over time

### Actual population figures (for context)

For reference, the actual Arkansas prison population during this period:

| Year | Approximate Population | Source |
|------|----------------------|--------|
| 2015 | ~17,000 | ADC Annual Reports |
| 2020 | ~16,000 (COVID reduction) | ADC Annual Reports |
| 2024 | 17,000+ | Multiple sources |
| Dec 2025 | 18,997 (including jail backup) | Arkansas Advocate |

### The `adc_monthly_events.csv` file

This file uses a different extraction method and includes an `other` column. Its values differ from the three primary CSV files, suggesting a separate OCR pass with different keyword categories.

### The `adc_timeline_data.csv` file

This year-level summary shows:
- **Document Count**: How many of the 287 source PDFs reference that year
- **Key Events**: Notable documents identified per year (annual reports, population projections, recidivism studies)
- **Sample Statistics**: Representative numerical values extracted from the text

The year range (1992–2026) extends beyond the 2015–2025 monthly data because many ADC documents contain historical references and forward projections.

---

## Recommendations for Researchers

1. **For keyword frequency analysis**: Use the monthly CSV files as-is. The permutation tests are appropriate for this data type.
2. **For actual population/death counts**: Cross-reference with the [ADC Secretary's Reports](https://doc.arkansas.gov/office-of-the-secretary/secretarys-reports/) and the Director's Board Reports available at media.ark.org.
3. **For expenditure data**: See the companion repository [Arkansas-DOC-Expenditures-2015-2025](https://github.com/Leerrooy95/Arkansas-DOC-Expenditures-2015-2025).

---

*Prepared February 9, 2026*
