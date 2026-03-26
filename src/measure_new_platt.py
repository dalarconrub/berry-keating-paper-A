"""Measure <r> on newly downloaded Platt files (logT 22.2-22.8)."""
import sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, 'src')

import numpy as np
import platt_zeros
import math

def measure_r(T_start, N=500000):
    zeros = np.array([float(z) for _, z in platt_zeros.zeros_starting_at_t(T_start, number_of_zeros=N)])
    logT = math.log(zeros[0])

    gaps = np.diff(zeros)
    T_mid = (zeros[:-1] + zeros[1:]) / 2
    rho = np.log(T_mid / (2*np.pi)) / (2*np.pi)
    s = gaps * rho
    mask = (s > 0.02) & (s < 6)
    s = s[mask] / s[mask].mean()

    s1, s2 = s[:-1], s[1:]
    r = np.minimum(s1, s2) / np.maximum(s1, s2)

    r_mean = float(r.mean())
    sigma_emp = float(r.std() / np.sqrt(len(r)))
    sigma = max(sigma_emp, 0.00020)
    std_s = float(s.std())
    corr = float(np.corrcoef(s[:-1], s[1:])[0, 1])

    r_pred = 0.59891 + 1.245 / logT**2
    resid = (r_mean - r_pred) / sigma

    return {
        "logT": logT, "r_mean": r_mean, "sigma_emp": sigma_emp,
        "sigma": sigma, "std_s": std_s, "corr": corr,
        "r_pred": r_pred, "resid": resid,
    }

new_t0s = [13492946000, 16649246000, 20544746000, 25347446000]

header = f"{'t0':>15} {'logT':>8} {'<r>':>10} {'sig_emp':>10} {'sigma':>8} {'pred':>10} {'resid':>8} {'std(s)':>8} {'Corr':>8}"
print(header)
print("=" * len(header))

for t0 in new_t0s:
    res = measure_r(t0, N=500000)
    print(f"{t0:>15} {res['logT']:>8.3f} {res['r_mean']:>10.5f} {res['sigma_emp']:>10.5f} {res['sigma']:>8.5f} {res['r_pred']:>10.5f} {res['resid']:>+8.2f}s {res['std_s']:>8.4f} {res['corr']:>8.4f}")
