# Chapter 03: Logistic, Ridge, and Lasso Regression

_Part II -- Introduction to Statistical Learning_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch03_text.tex` / `ch03_text.pdf` -- the chapter: logistic regression (the
  sigmoid, cross-entropy, the decision boundary); ridge and lasso as penalised
  least squares; proofs that the logistic loss is convex, the ridge closed
  form, and the lasso soft-threshold; and the geometry of sparsity. Includes a
  worked Python snippet and `figures/logreg_panel.png`.
- `source_slides/` -- the original lecture slides, exactly as taught
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise03` -- **core**: the sigmoid, cross-entropy, classification
- `exercise04` -- **proof**: the ridge estimator, the lasso soft-threshold, convexity
- `exercise05` -- **research**: the L1/L2 penalties and the elastic net

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/Chapter_3__Regularization.pdf`.
