"""
05 — Number variance and spectral rigidity (Paper A, Section 6)

Theoretical predictions for Sigma^2(L,T) and Delta_3(L,T).
Shows GUE for L < L_cross and Bogomolny-Keating saturation for L > L_cross.

Note: Computing Sigma^2 from actual zeros requires access to Platt files
in the main repo (berry-keating-riemann/data/platt/).
This script shows the theoretical framework and L_cross values.

Run from repo root: python src/05_sigma2_delta3.py
"""
import numpy as np

def sigma2_GUE(L):
    """GUE number variance (Dyson-Mehta)."""
    return (2/np.pi**2) * (np.log(2*np.pi*L) + np.euler_gamma + 1 - np.pi**2/8)

def delta3_GUE(L):
    """GUE spectral rigidity (Dyson-Mehta)."""
    return (1/np.pi**2) * (np.log(2*np.pi*L) + np.euler_gamma - 5/4)

# L_cross = logT / (2*pi)
log_T_vals = [19.0, 21.0, 22.1, 24.1]
L_cross = [lt / (2*np.pi) for lt in log_T_vals]

print("=== Bogomolny-Keating saturation ===")
print(f"L_cross = logT / (2*pi)\n")
print(f"{'logT':>6s} {'L_cross':>8s} {'Sigma2_GUE(L_cross)':>20s} {'Delta3_GUE(L_cross)':>20s}")
print("-" * 58)
for lt, lc in zip(log_T_vals, L_cross):
    s2 = sigma2_GUE(lc)
    d3 = delta3_GUE(lc)
    print(f"{lt:6.1f} {lc:8.2f} {s2:20.4f} {d3:20.4f}")

print("\nFor L < L_cross: Sigma^2, Delta_3 follow GUE (logarithmic)")
print("For L > L_cross: saturation due to prime number contribution")
print("\nTo generate ED Figure 1, run sigma2_delta3_bogomolny.ipynb")
print("in the main repo with access to Platt zero files.")
