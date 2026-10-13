# Chapter 06: Maximum Likelihood Estimation

_Part I -- Statistics Foundation for ML_

**Status:** complete -- written chapter in three difficulty tiers, plus
three exercises in each of Python and R, with a broken copy of each to fix.

## Difficulty tiers

The chapter and its exercises are layered so one chapter serves three
audiences. Each exercise is tagged with its tier:

- **● Core** (bachelor) -- the likelihood and the Bernoulli / Normal /
  Poisson MLEs, with code. (`exercise06`)
- **●● Proof** (master's) -- score, Fisher information, the Cramer-Rao
  bound, and asymptotic normality of the MLE, with proofs. (`exercise07`)
- **●●● Research** -- regularity conditions and where they fail, the MLE as
  an M-estimator minimising KL divergence, and the sandwich variance under
  misspecification. (`exercise08`)

Drill just your level, with the runner at the repo root:

```bash
python3 drill.py --level bachelor   # Core only
python3 drill.py --level master     # Core + Proof
python3 drill.py --level phd        # all three tiers
```

## Contents

- `ch06_text.tex` / `ch06_text.pdf` -- the chapter text (all three tiers)
- `source_slides/` -- the original lecture slides, exactly as taught
- `homework/` -- the original homework PDF from the course
- `exercises/python/`, `exercises/r/` -- three exercises (one per tier), a
  **broken** copy of each for you to debug, and a reference solution, in
  each of the two languages

## Source

Original slide deck preserved at `source_slides/STAT4ML_Slide_6__MLE.pdf`.
