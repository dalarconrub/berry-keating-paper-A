"""
Medir <r> en los datasets sparse de Odlyzko (zeros3, zeros4, zeros5).
Solo ~10k zeros por fichero → sigma grande (~0.0023), pero logT muy alto → leverage.

NOTA: zeros4/5 tienen base_T > 1e20. Float64 no puede representar base_T + offset
sin perder los decimales. Solución: calcular gaps directamente de los offsets
(diff de los valores del fichero = diff de las gammas, porque base_T se cancela).
"""
import numpy as np
import math
from pathlib import Path

DATA_DIR = Path("../src/odlyzko_data")

DATASETS = {
    "zeros3": {"base_T": 267_653_395_647.0, "base_N": 10**12 + 1},
    "zeros4": {"base_T": 144_176_897_509_546_973_000.0, "base_N": 10**21 + 1},
    "zeros5": {"base_T": 1_370_919_909_931_995_300_000.0, "base_N": 10**22 + 1},
}

def read_offsets(name):
    """Read raw offset values from file, skipping header lines."""
    vals = []
    with open(DATA_DIR / f"{name}.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                vals.append(float(line))
            except ValueError:
                continue
    return np.array(vals)

def measure_r(name):
    """Measure <r>, std(s), Corr from Odlyzko sparse dataset."""
    d = DATASETS[name]
    vals = read_offsets(name)

    # Gaps from offsets (avoids float64 precision loss with huge base_T)
    gaps_raw = np.diff(vals)

    # Approximate logT for unfolding
    T_approx = d["base_T"] + vals[0]
    logT = math.log(T_approx)
    rho = logT / (2 * math.pi)  # log(T/2pi)/(2pi) ≈ logT/(2pi) for logT >> 1

    # Unfold to unit mean spacing
    s = gaps_raw * rho
    s = s / s.mean()

    # Filter pathological gaps
    mask = (s > 0.02) & (s < 6)
    s = s[mask]

    # Gap ratios
    s1, s2 = s[:-1], s[1:]
    r = np.minimum(s1, s2) / np.maximum(s1, s2)

    return {
        "name": name,
        "logT": logT,
        "N_zeros": len(vals),
        "N_ratios": len(r),
        "r_mean": r.mean(),
        "sigma_r": r.std() / np.sqrt(len(r)),
        "std_s": s.std(),
        "corr": np.corrcoef(s[:-1], s[1:])[0, 1],
    }

# ── Main ──
print(f"{'Dataset':<10} {'logT':>8} {'N':>7} {'<r>':>10} {'sigma':>10} {'std(s)':>8} {'Corr':>8}")
print("=" * 65)

results = []
for name in ["zeros3", "zeros4", "zeros5"]:
    res = measure_r(name)
    results.append(res)
    print(f"{res['name']:<10} {res['logT']:>8.3f} {res['N_zeros']:>7} {res['r_mean']:>10.5f} {res['sigma_r']:>10.5f} {res['std_s']:>8.4f} {res['corr']:>8.4f}")

print(f"\n{'Dataset':<10} {'logT':>8} {'<r> meas':>10} {'<r> pred':>10} {'resid':>8}")
print("-" * 50)
for res in results:
    logT = res["logT"]
    r_pred = 0.59891 + 1.245 / logT**2
    resid = (res["r_mean"] - r_pred) / res["sigma_r"]
    print(f"{res['name']:<10} {logT:>8.3f} {res['r_mean']:>10.5f} {r_pred:>10.5f} {resid:>+7.2f}s")
