# Chapter 05: Unsupervised Learning and PCA

_Part II -- Introduction to Statistical Learning_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch05_text.tex` / `ch05_text.pdf` -- the chapter: projecting onto directions
  of greatest variance; the proof that variance-maximisation and
  reconstruction-error-minimisation give the same (eigenvector) components;
  and the SVD, variance-explained, and caveats. Includes a worked Python
  power-iteration snippet and `figures/pca_panel.png`.
- `source_slides/` -- the original lecture slides, exactly as taught
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise05` -- **core**: variance, covariance, and variance-explained ratios
- `exercise06` -- **proof**: projected variance and the top eigenvalue
- `exercise07` -- **research**: cumulative variance, reconstruction error, singular values

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/Chapter_5__Unsupervised_Learning.pdf`.
