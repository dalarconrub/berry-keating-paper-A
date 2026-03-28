# Paper A: Gap ratio statistics of Riemann zeros

**Title:** Gap ratio statistics of Riemann zeros: measurement, mechanism, and the Berry-Keating correction

**Author:** David Alarcon, Universidad Pablo de Olavide, Sevilla, Spain

**Zenodo DOI:** [10.5281/zenodo.19268721](https://doi.org/10.5281/zenodo.19268721)

## Contents

- First precision measurement of ⟨r⟩(T) convergence rate (21 points, logT 9.7–24.1)
- Model comparison (5 models, AIC)
- A₁[r] = 0 by symmetry (3 routes)
- Mechanism: c = c_std + c_corr = 1.60 + (−0.36) = 1.24 (99.5%)
- Σ²/Δ₃ validation (Bogomolny-Keating saturation)
- RH consistency (f < 1% for σ₀ > 0.525)

## Related papers

- **Paper A** (this paper): Gap ratio statistics of Riemann zeros — Comm. Math. Phys.
- **Paper B**: Ab initio derivation of the Berry-Keating correction coefficient — J. Number Theory — [GitHub](https://github.com/dalarconrub/berry-keating-paper-B)
- **Paper C**: Berry-Keating spectral convergence rates and the Riemann Hypothesis — Annals of Mathematics — [GitHub](https://github.com/dalarconrub/berry-keating-paper-C)
- **Paper D**: Empirical proof that Berry-Keating convergence implies the Riemann Hypothesis — Nature — [GitHub](https://github.com/dalarconrub/berry-keating-paper-D)
- **Paper E**: Spectral gap functions bounded below by band-limited functions — J. Fourier Anal. Appl. — [GitHub](https://github.com/dalarconrub/berry-keating-paper-E)
- **Data & code**: [GitHub](https://github.com/dalarconrub/berry-keating-riemann)

## Build

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```
