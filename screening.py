"""
Multi-Criteria Evaluation of Salt Hydrates for
Thermochemical Energy Storage Applications

This script:
1. Loads candidate material data
2. Normalizes evaluation criteria
3. Calculates a weighted performance score
4. Ranks materials
5. Exports results
6. Generates comparison figures
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


# Configuration

DATA_FILE = "data.csv"
OUTPUT_DIR = "results"

WEIGHTS = {
    "Energy": 0.50,
    "Stability": 0.30,
    "Cost": 0.20
}


# Load Dataset

try:
    df = pd.read_csv(DATA_FILE)

except FileNotFoundError:
    print(f"Error: '{DATA_FILE}' not found.")
    raise SystemExit


# Remove leading/trailing spaces from column names

df.columns = df.columns.str.strip()


# Validate Required Columns

required_columns = [
    "Material",
    "EnergyDensity",
    "StabilityScore",
    "CostScore"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print(
        f"Missing required columns: {missing_columns}"
    )
    raise SystemExit


# Normalize Criteria

df["EnergyNorm"] = (
    df["EnergyDensity"]
    / df["EnergyDensity"].max()
)

df["StabilityNorm"] = (
    df["StabilityScore"]
    / 5.0
)

df["CostNorm"] = (
    df["CostScore"]
    / 5.0
)


# Calculate Final Weighted Score

df["FinalScore"] = (
    WEIGHTS["Energy"] * df["EnergyNorm"]
    + WEIGHTS["Stability"] * df["StabilityNorm"]
    + WEIGHTS["Cost"] * df["CostNorm"]
)


# Rank Materials

df = df.sort_values(
    by="FinalScore",
    ascending=False
).reset_index(drop=True)


# Create Output Directory

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# Export Ranked Results

output_csv = os.path.join(
    OUTPUT_DIR,
    "ranked_materials.csv"
)

df.to_csv(
    output_csv,
    index=False
)

print("\nMaterial Ranking")
print(
    df[
        [
            "Material",
            "EnergyDensity",
            "FinalScore"
        ]
    ]
)


# Figure Style

plt.style.use("ggplot")


# Figure 1: Energy Density Comparison

fig, ax = plt.subplots(
    figsize=(8, 5)
)

bars = ax.bar(
    df["Material"],
    df["EnergyDensity"]
)

ax.set_title(
    "Energy Density of Candidate Salt Hydrates",
    fontsize=13
)

ax.set_xlabel("Material")
ax.set_ylabel("Energy Density (GJ/m³)")

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

fig.tight_layout()

fig.savefig(
    os.path.join(
        OUTPUT_DIR,
        "Figure1_EnergyDensity.png"
    ),
    dpi=600,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# Figure 2: Final Score Comparison
# ============================================================

fig, ax = plt.subplots(
    figsize=(8, 5)
)

bars = ax.bar(
    df["Material"],
    df["FinalScore"]
)

ax.set_title(
    "Overall Performance Ranking",
    fontsize=13
)

ax.set_xlabel("Material")
ax.set_ylabel("Weighted Score")

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.3f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

fig.tight_layout()

fig.savefig(
    os.path.join(
        OUTPUT_DIR,
        "Figure2_FinalScore.png"
    ),
    dpi=600,
    bbox_inches="tight"
)

plt.close()


# ============================================================
# Summary
# ============================================================

print("\nScoring Weights")
print(WEIGHTS)

print("\nResults saved successfully.")
print(f"CSV file : {output_csv}")
print(f"Output folder : {OUTPUT_DIR}")