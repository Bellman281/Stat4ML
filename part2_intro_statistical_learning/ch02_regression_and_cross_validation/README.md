# Chapter 02: Regression and Cross-Validation

_Part II -- Introduction to Statistical Learning_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch02_text.tex` / `ch02_text.pdf` -- the chapter: the linear model and
  least squares (normal equations, R^2); the normal-equations and
  Gauss-Markov proofs and the bias-variance decomposition; and
  cross-validation (k-fold, and the no-refit LOOCV leverage shortcut).
  Includes a worked Python regression snippet and `figures/overfit_panel.png`
  (the training-vs-validation error curve).
- `source_slides/` -- the original lecture slides, exactly as taught
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise02` -- **core**: simple linear regression and R^2
- `exercise03` -- **proof**: the bias-variance decomposition
- `exercise04` -- **research**: k-fold sizes and the LOOCV leverage shortcut

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/Chapter_2__Cross_Validation.pdf`.
