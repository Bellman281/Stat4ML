# Chapter 06: The EM Algorithm

_Part II -- Introduction to Statistical Learning_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch06_text.tex` / `ch06_text.pdf` -- the chapter: fitting mixture models
  with hidden labels by alternating the E-step (responsibilities) and M-step
  (weighted re-estimation); the evidence lower bound and the proof that each
  iteration cannot decrease the log-likelihood; and EM as coordinate ascent
  (its hard limit is k-means). Includes a worked Python `em_step` snippet and
  `figures/em_panel.png` (a GMM fit and the climbing log-likelihood).
- `source_slides/` -- the original lecture slides, exactly as taught
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise06` -- **core**: the Gaussian density, responsibilities, the weighted mean
- `exercise07` -- **proof**: the ELBO identity, log p(x) = ELBO + KL
- `exercise08` -- **research**: hard assignment (the k-means link) and monotonicity

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/Chapter_7__EM_Algorithm.pdf`.
