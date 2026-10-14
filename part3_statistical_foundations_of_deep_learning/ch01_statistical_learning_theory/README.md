# Chapter 01: Statistical Learning Theory

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

Why does fitting the training data say anything about unseen data? The answer is
a concentration argument: empirical risk is an average of i.i.d. terms, so it
concentrates around the true risk, and only a hypothesis class rich enough to
chase the noise breaks the link. This chapter builds the guarantee from
**Hoeffding's inequality** to the **finite-class bound**, names the capacity
measures (**VC dimension**, **Rademacher complexity**) that extend it to
infinite classes, and reads the **bias-variance trade-off** and **double
descent** through the same lens. It is the spine the rest of Part III hangs on.

## Contents

- `ch01_text.tex` / `ch01_text.pdf` -- the chapter text
- `figures/slt_panel.png` -- the bias-variance U, the Hoeffding band tightening
  around the true mean, and the double-descent spike at the interpolation threshold
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Risk, empirical risk, ERM, the generalisation gap
- Hoeffding's inequality; the finite-class generalisation bound (with proof)
- VC dimension, shattering, Sauer-Shelah; Rademacher complexity
- Bias-variance as the statistical shadow of capacity; double descent

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise01` | core | `zero_one_loss`, `empirical_risk`, `generalisation_gap` |
| `exercise02` | proof | `hoeffding_tail`, `confidence_width`, `finite_class_bound` (width inverts the tail) |
| `exercise03` | research | `sauer_bound`, `vc_bound_term`, `shatters` |

Run one: `python3 exercise02_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
