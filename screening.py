import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. LOAD DATA
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("Error: 'data.csv' file not found in this directory.")
    exit()

# FIX: Automatically strip hidden spaces from column headers
df.columns = df.columns.str.strip()

print("\nOriginal Dataset")
print(df)

# 2. NORMALIZE DATA
df["EnergyNorm"] = (
    df["EnergyDensity"] 
    / df["EnergyDensity"].max()
)

df["StabilityNorm"] = (
    df["StabilityScore"] 
    / 5
)

df["CostNorm"] = (
    df["CostScore"] 
    / 5
)

# 3. MULTI-CRITERIA SCORE
df["FinalScore"] = (
    0.50 * df["EnergyNorm"]
    + 0.30 * df["StabilityNorm"]
    + 0.20 * df["CostNorm"]
)

# 4. SORT RESULTS
df = df.sort_values(
    by="FinalScore",
    ascending=False
)

print("\nRanked Results")
print(df)

# 5. SAFE DIRECTORY CREATION
# This ensures both the CSV and the PNG plots can save without crashing
os.makedirs("results", exist_ok=True)

# 6. SAVE RANKING
df.to_csv(
    "results/ranked_results.csv",
    index=False,
)

# =====================
# FIGURE 1
# ENERGY DENSITY
# =====================

plt.figure(figsize=(10, 6))

plt.bar(
    df["Material"],
    df["EnergyDensity"]
)

plt.title(
    "Energy Density of Candidate Salt Hydrates"
)

plt.ylabel(
    "Energy Density (GJ/m³)"
)

plt.xlabel(
    "Material"
)

plt.tight_layout()

plt.savefig(
    "results/energy_density.png",
    dpi=300
)

plt.close()

# =====================
# FIGURE 2
# FINAL SCORE
# =====================

plt.figure(figsize=(10, 6))

plt.bar(
    df["Material"],
    df["FinalScore"]
)

plt.title(
    "Multi-Criteria Screening Score"
)

plt.ylabel(
    "Final Score"
)

storage_volume = 2

df["StoredEnergy_GJ"] = (
    df["EnergyDensity"]
    * storage_volume
)

print(
    df[
        ["Material",
         "StoredEnergy_GJ"]
    ]
)

plt.xlabel(
    "Material"
)

plt.tight_layout()

plt.savefig(
    "results/final_score.png",
    dpi=300
)

plt.close()

print("\nAnalysis Complete. Files and charts generated in the 'results' folder.")
