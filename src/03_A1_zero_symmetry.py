"""
03 — A1 = 0 by symmetry (Paper A, Section 4)

Demonstrates that the first-order correction A1[r] = 0 via:
1. Empirical: b = 0.019 +/- 0.043 (F-test p=0.66)
2. Symmetry: r symmetric x delta1p antisymmetric = 0

Run from repo root: python src/03_A1_zero_symmetry.py
"""
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import f as f_dist

data = np.loadtxt("data/dataset_v6_21pts.dat", skiprows=1)
logT, r_mean, sigma = data[:, 0], data[:, 1], data[:, 2]

def model_A(x, Rinf, c):       return Rinf + c / x**2
def model_AC(x, Rinf, b, c):   return Rinf + b / x + c / x**2

popt_A, pcov_A = curve_fit(model_A, logT, r_mean, sigma=sigma, absolute_sigma=True)
popt_AC, pcov_AC = curve_fit(model_AC, logT, r_mean, sigma=sigma, absolute_sigma=True)

chi2_A = np.sum(((r_mean - model_A(logT, *popt_A)) / sigma)**2)
chi2_AC = np.sum(((r_mean - model_AC(logT, *popt_AC)) / sigma)**2)

b_val = popt_AC[1]
b_err = np.sqrt(pcov_AC[1, 1])
F_stat = (chi2_A - chi2_AC) / (chi2_AC / (len(logT) - 3))
p_value = 1 - f_dist.cdf(F_stat, 1, len(logT) - 3)
delta_aic = (chi2_A + 4) - (chi2_AC + 6)

print("=== Empirical test: is b/logT term needed? ===")
print(f"b = {b_val:.4f} +/- {b_err:.4f} ({abs(b_val/b_err):.2f} sigma from zero)")
print(f"F-test: F = {F_stat:.3f}, p = {p_value:.4f}")
print(f"Delta AIC (A vs AC) = {delta_aic:.2f} (positive = A preferred)")
print(f"\n=== Symmetry argument ===")
print("r(s1, s2) = r(s2, s1)         [symmetric]")
print("delta1_p(s1, s2) = -delta1_p(s2, s1)  [antisymmetric]")
print("=> A1[r] = integral(symmetric x antisymmetric) = 0  exactly")
