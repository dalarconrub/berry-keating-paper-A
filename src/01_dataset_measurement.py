"""
01 — Dataset and measurement (Paper A, Section 2)

Loads dataset v6 (21 points), displays the unfolding formula,
and prints the complete data table.
"""
import numpy as np

# --- Load dataset v6 ---
data = np.loadtxt("data/dataset_v6_21pts.dat", skiprows=1)
logT = data[:, 0]
r_mean = data[:, 1]
sigma = data[:, 2]

print(f"Dataset v6: {len(logT)} points")
print(f"logT range: {logT.min():.3f} to {logT.max():.3f}")
print(f"<r> range:  {r_mean.min():.5f} to {r_mean.max():.5f}")

# --- Unfolding formula ---
print("\nUnfolding: s_n = (gamma_{n+1} - gamma_n) * log(gamma_n / 2pi) / (2pi)")
print("Sigma floor: max(sigma_emp, 0.00020)")

# --- Data table ---
print(f"\n{'logT':>8s} {'<r>':>8s} {'sigma':>8s}")
print("-" * 28)
for i in range(len(logT)):
    print(f"{logT[i]:8.3f} {r_mean[i]:8.5f} {sigma[i]:8.5f}")
