# Chapter 05: Convergence Concepts

_Part I -- Statistics Foundation for ML_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch05_text.tex` / `ch05_text.pdf` -- the chapter: the law of large numbers
  and the central limit theorem; Markov's and Chebyshev's inequalities and
  the proofs built on them; the four modes of convergence, Slutsky's theorem,
  the continuous mapping theorem, and the delta method. Includes a worked
  Python snippet (the CLT across three very different source distributions)
  and the `figures/clt_panel.png` figure showing the CLT emerge as n grows.
- `source_slides/` -- the original lecture slides, exactly as taught
- `homework/` -- the original homework PDF from the course
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise05` -- **core**: sample-mean variance, Chebyshev's bound, the standardized CLT mean
- `exercise06` -- **proof**: Markov, Chebyshev, and the weak-law bound
- `exercise07` -- **research**: the CLT's MGF limit and the delta method

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/STAT4ML_Slide_5__Convergence_in_Probability.pdf`.
