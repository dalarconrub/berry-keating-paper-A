# Gap ratio statistics of Riemann zeros: measurement, mechanism, and the Berry-Keating correction

**Author:** David Alarcon, Universidad Pablo de Olavide, Sevilla, Spain

**Zenodo DOI:** [10.5281/zenodo.19268721](https://doi.org/10.5281/zenodo.19268721)

## Abstract

We report the first precision measurement of the rate at which the gap ratio
statistic <r> of Riemann zeta zeros converges to the GUE prediction. Using
high-precision zeros up to height T ~ 3x10^10 (log T = 24), we find
<r>(T) = 0.59891(13) + 1.245(40)/log^2(T), with chi^2/dof = 0.50.
The asymptotic value R_inf = 0.59891 lies 6.1 sigma below the GUE limit.
We identify the physical mechanism: Riemann zeros have a narrower spacing
distribution than GUE (std(s) < std_GUE) and stronger anti-correlation
(Corr(s_n,s_{n+1}) < Corr_GUE), both converging as 1/log^2(T).
Decomposing: c_std = +1.60 (+128%) and c_corr = -0.36 (-29%), reproducing
99.5% of the measured coefficient.

## Repository structure

```
main.tex              Main manuscript (13 pages)
references.bib        Bibliography (15 references)
cover_letter.tex      Cover letter
figures/
  fig1_r_vs_logT          <r>(T) with Model A fit (21 points)
  fig2_c_decomposition    c = c_std + c_corr decomposition
  fig3_delta_p_s          Narrowing of p(s)
  ed_fig1_sigma2_delta3   Number variance and spectral rigidity
  ed_fig2_rh_bound        RH consistency bound
  ed_fig4_std_corr        std(s) and Corr convergence
data/
  dataset_v6_21pts.dat    Dataset (21 points: logT, r, sigma)
  dataset_v7_25pts.dat    Extended dataset (25 points)
src/
  01_dataset_measurement.py       Section 2: load dataset, display table
  02_model_comparison.py          Section 3: fit 5 models, AIC, fig1
  03_A1_zero_symmetry.py          Section 4: F-test b=0, symmetry
  04_mechanism_decomposition.py   Section 5: c = c_std + c_corr, fig2
  05_sigma2_delta3.py             Section 6: Sigma^2/Delta_3 framework
  06_rh_consistency.py            Section 7: epsilon bound, ed_fig2
  07_painleve_v.py                Section 8: sigma_GUE, delta_sigma, PV chain
  measure_new_platt.py            Utility: measure <r> from Platt zeros
  measure_odlyzko_sparse.py       Utility: measure <r> from Odlyzko zeros
```

## Compile

```bash
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

## License

CC BY 4.0
