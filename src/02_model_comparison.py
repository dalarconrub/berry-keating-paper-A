"""
02 — Model comparison (Paper A, Section 3)

Fits 5 models to dataset v6, computes chi2/dof and AIC.
Generates Figure 1 (r vs logT with Model A fit).

Run from repo root: python src/02_model_comparison.py
"""
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = np.loadtxt("data/dataset_v6_21pts.dat", skiprows=1)
logT, r_mean, sigma = data[:, 0], data[:, 1], data[:, 2]
R_GUE = 0.59971

# --- Model definitions ---
def model_A(x, Rinf, c):       return Rinf + c / x**2
def model_B(x, Rinf, a):       return Rinf + a * np.log(x) / x
def model_C(x, Rinf, b):       return Rinf + b / x
def model_AB(x, Rinf, a, c):   return Rinf + a * np.log(x) / x + c / x**2
def model_A3(x, Rinf, c, d):   return Rinf + c / x**2 + d / x**3

models = {
    "A":  (model_A,  [0.5997, 1.25], 2),
    "B":  (model_B,  [0.5997, 0.01], 2),
    "C":  (model_C,  [0.5997, 0.02], 2),
    "AB": (model_AB, [0.5997, 0.01, 1.25], 3),
    "A3": (model_A3, [0.5997, 1.25, 0.0], 3),
}

# --- Fit all models ---
print(f"{'Model':>5s} {'chi2/dof':>10s} {'AIC':>8s}  Parameters")
print("-" * 65)

results = {}
for name, (func, p0, k) in models.items():
    popt, pcov = curve_fit(func, logT, r_mean, p0=p0, sigma=sigma, absolute_sigma=True)
    chi2 = np.sum(((r_mean - func(logT, *popt)) / sigma)**2)
    dof = len(logT) - k
    aic = chi2 + 2 * k
    perr = np.sqrt(np.diag(pcov))
    results[name] = {"popt": popt, "perr": perr, "chi2": chi2, "dof": dof, "aic": aic}
    params = ", ".join(f"{v:.5f}+/-{e:.5f}" for v, e in zip(popt, perr))
    print(f"{name:>5s} {chi2/dof:10.3f} {aic:8.1f}  {params}")

Rinf, c = results["A"]["popt"]
Rinf_err, c_err = results["A"]["perr"]
print(f"\nModel A: R_inf = {Rinf:.5f} +/- {Rinf_err:.5f}")
print(f"         c     = {c:.4f} +/- {c_err:.4f}")
print(f"         R_inf - R_GUE = {Rinf - R_GUE:.5f} ({(Rinf - R_GUE)/Rinf_err:.1f} sigma)")

# --- Figure 1 ---
fig, ax = plt.subplots(figsize=(9, 5))
x_fit = np.linspace(8, 26, 200)
y_fit = model_A(x_fit, Rinf, c)

mask_orig = logT < 19
mask_grid = logT >= 19
ax.errorbar(logT[mask_orig], r_mean[mask_orig], yerr=sigma[mask_orig],
            fmt="s", color="orange", ms=6, label="Odlyzko", zorder=3)
ax.errorbar(logT[mask_grid], r_mean[mask_grid], yerr=sigma[mask_grid],
            fmt="o", color="red", ms=5, label="Platt", zorder=3)
ax.plot(x_fit, y_fit, "b-", lw=1.5, label=f"Model A: $R_\\infty + c/\\log^2 T$")
ax.axhline(R_GUE, color="green", ls="--", alpha=0.7, label=f"$R_{{GUE}} = {R_GUE}$")
ax.set_xlabel("$\\log T$", fontsize=13)
ax.set_ylabel("$\\langle r \\rangle$", fontsize=13)
ax.legend(fontsize=10)
ax.set_title("Gap ratio convergence to GUE")
plt.tight_layout()
plt.savefig("figures/fig1_r_vs_logT.pdf", dpi=300, bbox_inches="tight")
plt.savefig("figures/fig1_r_vs_logT.png", dpi=150, bbox_inches="tight")
print("Saved figures/fig1_r_vs_logT.{pdf,png}")
