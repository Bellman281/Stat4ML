# Chapter 04: Conditional and Multivariate Distributions

_Part I -- Statistics Foundation for ML_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch04_text.tex` / `ch04_text.pdf` -- the chapter: joint, marginal, and
  conditional distributions and independence; the laws of total expectation
  and total variance with proofs; and the bivariate / multivariate normal
  conditional formulas (the root of linear regression and the GP posterior).
  Includes a worked Python snippet (marginals and conditionals from a joint
  table) and `figures/bvn_panel.png`.
- `source_slides/` -- the original lecture slides, exactly as taught
- `homework/` -- the original homework PDF from the course
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise04` -- **core**: joint table -> marginal, conditional, covariance
- `exercise05` -- **proof**: the laws of total expectation and total variance
- `exercise06` -- **research**: conditioning the bivariate and multivariate normal

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/STAT4ML_Slide_4__Multivariate_Dist_.pdf`.
