# Chapter 06: Maximum Likelihood Estimation

_Part I -- Statistics Foundation for ML_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch06_text.tex` / `ch06_text.pdf` -- the chapter: the likelihood and the
  MLE; the Bernoulli / Normal / Poisson estimators; the score, Fisher
  information, the Cramer-Rao bound, and asymptotic normality; and a closing
  section on what the estimator does when the model is wrong (the
  Kullback-Leibler view and the sandwich variance).
- `mle_cookbook.py` / `mle_cookbook.R` -- a runnable reference gallery:
  the maximum-likelihood estimator for ten common distributions (Bernoulli,
  Binomial, Geometric, Poisson, Exponential, Normal, Uniform, Laplace,
  Pareto, Gamma) plus one numeric (Newton) example
- `source_slides/` -- the original lecture slides, exactly as taught
- `homework/` -- the original homework PDF from the course
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

The three exercises are tagged by difficulty, so the runner can serve just
your level:

- `exercise06` -- **core**: computing the MLE for the standard models
- `exercise07` -- **proof**: score, Fisher information, Cramer-Rao, efficiency
- `exercise08` -- **research**: M-estimation, Fisher scoring, the sandwich variance

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/STAT4ML_Slide_6__MLE.pdf`.
