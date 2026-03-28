"""
04 — Mechanism: narrowing of spacing distribution (Paper A, Section 5)

Decomposes c = c_std + c_corr = +1.60 + (-0.36) = 1.24 (99.5% of c_emp).
Generates Figure 2 (decomposition bar chart).

Run from repo root: python src/04_mechanism_decomposition.py
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Convergence rates (measured from 18 data points)
std_inf = 0.4212;  a_std = -2.13
corr_inf = -0.3279; a_corr = -3.08

# Sensitivities (CUE Monte Carlo, N=2000)
dr_dstd = -0.749
dr_dcorr = +0.116

c_std = dr_dstd * a_std
c_corr = dr_dcorr * a_corr
c_total = c_std + c_corr
c_emp = 1.245

print("=== Decomposition of c ===")
print(f"std(s;T)  = {std_inf} + ({a_std})/log^2(T)")
print(f"Corr(T)   = {corr_inf} + ({a_corr})/log^2(T)")
print(f"dr/d(std) = {dr_dstd}")
print(f"dr/d(Corr)= {dr_dcorr}")
print(f"\nc_std  = ({dr_dstd}) x ({a_std}) = {c_std:+.3f} ({100*c_std/c_emp:+.0f}%)")
print(f"c_corr = ({dr_dcorr}) x ({a_corr}) = {c_corr:+.3f} ({100*c_corr/c_emp:+.0f}%)")
print(f"c_total = {c_total:.3f} ({100*c_total/c_emp:.1f}% of c_emp = {c_emp})")

# --- Figure 2 ---
fig, ax = plt.subplots(figsize=(6, 4))
bars = ax.bar(["$c_{std}$\n(narrowing)", "$c_{corr}$\n(anti-corr)", "$c_{total}$"],
              [c_std, c_corr, c_total],
              color=["#2196F3", "#FF9800", "#4CAF50"], width=0.5)
ax.axhline(c_emp, color="red", ls="--", label=f"$c_{{emp}} = {c_emp}$")
ax.set_ylabel("Contribution to $c$", fontsize=12)
ax.legend(fontsize=11)
ax.set_title("Two-channel decomposition of $c$")
for bar, val in zip(bars, [c_std, c_corr, c_total]):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.03,
            f"{val:+.3f}", ha="center", fontsize=10)
plt.tight_layout()
plt.savefig("figures/fig2_c_decomposition.pdf", dpi=300, bbox_inches="tight")
plt.savefig("figures/fig2_c_decomposition.png", dpi=150, bbox_inches="tight")
print("Saved figures/fig2_c_decomposition.{pdf,png}")
