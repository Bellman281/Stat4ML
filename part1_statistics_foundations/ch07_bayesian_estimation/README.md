# Chapter 07: Bayesian Estimation

_Part I -- Statistics Foundation for ML_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch07_text.tex` / `ch07_text.pdf` -- the chapter: prior, likelihood, and
  posterior; conjugate families (Beta-Binomial, Gamma-Poisson, Normal-Normal)
  with proofs; posterior mean, MAP, credible intervals and the posterior
  predictive; and the Bernstein-von Mises link back to the maximum-likelihood
  estimator. Includes a worked Python conjugacy snippet and
  `figures/posterior_update.png` (the posterior tightening as data arrive).
- `source_slides/` -- the original lecture slides, exactly as taught
- `homework/` -- the original homework PDF from the course
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise07` -- **core**: the Beta-Binomial posterior, its mean, and the MAP estimate
- `exercise08` -- **proof**: Normal-Normal conjugacy (precisions add)
- `exercise09` -- **research**: Gamma-Poisson, posterior prediction, Bernstein-von Mises

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/STAT4ML_Slide_7__Bayesian_Estimation.pdf`.
