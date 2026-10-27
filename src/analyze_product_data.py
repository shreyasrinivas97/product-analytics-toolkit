"""Analyze the synthetic product feedback and A/B test datasets.
Run from project root: python src/analyze_product_data.py
"""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
feedback = pd.read_csv(ROOT / "data" / "user_feedback.csv")
experiment = pd.read_csv(ROOT / "data" / "ab_experiment.csv")
features = pd.read_csv(ROOT / "data" / "feature_prioritization.csv")

print("\nFEEDBACK BY THEME")
theme_summary = (feedback.groupby("theme")
                 .agg(feedback_count=("feedback_id", "count"),
                      avg_satisfaction=("satisfaction_score_1_to_5", "mean"),
                      negative_count=("sentiment", lambda s: (s == "Negative").sum()))
                 .reset_index())
theme_summary["negative_rate_pct"] = 100 * theme_summary["negative_count"] / theme_summary["feedback_count"]
print(theme_summary.sort_values("feedback_count", ascending=False).round(2).to_string(index=False))

print("\nA/B EXPERIMENT SUMMARY")
ab = experiment.groupby("variant").agg(
    users=("user_id", "count"),
    conversions=("converted", "sum"),
    avg_session_seconds=("session_duration_seconds", "mean")
)
ab["conversion_rate"] = ab["conversions"] / ab["users"]
print(ab.round(4).to_string())

control = experiment.loc[experiment.variant == "Control", "converted"]
treatment = experiment.loc[experiment.variant == "Treatment", "converted"]
p1, p2 = control.mean(), treatment.mean()
pooled = (control.sum() + treatment.sum()) / (len(control) + len(treatment))
se = np.sqrt(pooled * (1-pooled) * (1/len(control) + 1/len(treatment)))
z = (p2-p1)/se if se else np.nan
print(f"\nAbsolute conversion lift: {(p2-p1)*100:.2f} percentage points")
print(f"Relative conversion lift: {((p2-p1)/p1)*100:.2f}%")
print(f"Approximate two-sided z statistic: {z:.3f}")
print("Interpretation caution: synthetic sample; do not treat this as real product evidence.")

print("\nFEATURE PRIORITIZATION")
print(features[["feature", "priority_score", "evidence"]].sort_values("priority_score", ascending=False).round(2).to_string(index=False))
