#!/usr/bin/env python3
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from tqdm import tqdm

df = pd.read_csv("~/ADC_OCR_COMPLETE_UPDATED.csv", index_col=0)
df.index = pd.to_datetime(df.index, errors='coerce')
df = df.dropna().fillna(0)

print("287 PDF PERMUTATION TESTS")
print("="*60)
print(f"Total: {len(df)} months, {df.death.sum():.0f} deaths, {df.parole.sum():.0f} paroles")

# Test 1: March spikes
march = df[df.index.month == 3].population
non_march = df[df.index.month != 3].population
obs_diff = march.mean() - non_march.mean()

shuffles = []
for _ in range(10000):
    perm = np.random.permutation(df.population.values)
    march_idx = df.index.month == 3
    shuffles.append(perm[march_idx].mean() - perm[~march_idx].mean())

p_march = (np.abs(shuffles) >= np.abs(obs_diff)).mean()

print(f"\nMarch Population Spike:")
print(f"  Observed diff: {obs_diff:.1f}")
print(f"  p-value: {p_march:.6f}")
print(f"  Status: {'STILL SIGNIFICANT ✓' if p_march < 0.001 else 'Not significant'}")

# Test 2: Deaths after paroles
deaths_lag = df.death.shift(-3).fillna(0)
r, _ = pearsonr(df.parole, deaths_lag)

shuf_rs = []
for _ in tqdm(range(10000), desc="Deaths-Parole correlation"):
    shuf_deaths = np.random.permutation(df.death.values)
    shuf_lag = pd.Series(shuf_deaths).shift(-3).fillna(0)
    shuf_r, _ = pearsonr(df.parole, shuf_lag)
    shuf_rs.append(shuf_r)

p_corr = (np.abs(shuf_rs) >= np.abs(r)).mean()

print(f"\nDeaths-Parole Correlation (90-day lag):")
print(f"  r = {r:.3f}")
print(f"  p-value: {p_corr:.6f}")
print(f"  Status: {'SIGNIFICANT ✓' if p_corr < 0.05 else 'Not significant'}")

print("\n" + "="*60)
print("UPDATED ANALYSIS COMPLETE")
