# Chapter 03: Distribution Functions

_Part I -- Statistics Foundation for ML_

**Status:** complete -- a written chapter, plus three exercises in each of
Python and R, with a broken copy of each to fix.

## Contents

- `ch03_text.tex` / `ch03_text.pdf` -- the chapter: the cdf and density; the
  probability integral transform and inverse-transform sampling; the monotone
  change-of-variables formula; and non-monotone transforms and the Jacobian.
  Includes a worked Python snippet (sampling three distributions from
  uniforms) and `figures/pit_panel.png`.
- `source_slides/` -- the original lecture slides, exactly as taught
- `homework/` -- the original homework PDF from the course
- `exercises/python/`, `exercises/r/` -- three exercises, a **broken** copy
  of each for you to debug, and a reference solution, in each language

## Drilling by level

- `exercise03` -- **core**: the exponential cdf/pdf and inverse-transform sampling
- `exercise04` -- **proof**: density as F', the monotone change-of-variables formula
- `exercise05` -- **research**: non-monotone transforms and the 2-D Jacobian

```bash
python3 drill.py --level bachelor   # core only
python3 drill.py --level master     # core + proof
python3 drill.py --level phd        # all three
```

## Source

Original slide deck preserved at `source_slides/STAT4ML_Slide_3__Distributions.pdf`.
