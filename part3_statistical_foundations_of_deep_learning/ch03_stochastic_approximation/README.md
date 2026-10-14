# Chapter 03: Stochastic Approximation and Optimisation

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

SGD is not a deep-learning invention -- it is **Robbins-Monro's 1951 stochastic
approximation**, the statistical method for solving an equation you can only
observe through noise. A minibatch is an unbiased noisy estimate of the risk
gradient, so SGD is exactly Robbins-Monro applied to `grad R = 0`. That lineage
hands over the convergence theory: the steps must satisfy `sum a_t = infinity`
(enough travel) and `sum a_t^2 < infinity` (the noise averages away). A constant
step leaves a **noise ball**; the noise itself acts as an **implicit
regulariser**.

## Contents

- `ch03_text.tex` / `ch03_text.pdf` -- the chapter text
- `figures/ch03_panel.png` -- diminishing vs constant step, the two Robbins-Monro
  conditions (`sum a_t` diverges, `sum a_t^2` -> pi^2/6), and the error-decay rates
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Stochastic approximation; SGD as Robbins-Monro on `grad R = 0`
- The two step-size conditions and why they pull in opposite directions
- The constant-step noise ball; stationary variance `a*sigma^2/(2H)`
- Implicit regularisation (flat / minimum-norm minima); the stability limit `a < 2/H`

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise03` | core | `sgd_step`, `inverse_time_lr`, `quad_grad` |
| `exercise04` | proof | `harmonic_partial`, `basel_partial`, `rm_valid` (the two RM conditions) |
| `exercise05` | research | `ou_stationary_var`, `critical_lr`, `polyak_var` |

Run one: `python3 exercise04_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
