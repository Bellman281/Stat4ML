# Chapter 04: Monte Carlo and Variational Inference

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

Most quantities a model needs -- an expected loss, a posterior mean, a marginal
likelihood -- are intractable integrals. Two ways to attack one: **Monte Carlo**
estimates it by sampling (unbiased, error `~ 1/sqrt(n)` regardless of dimension;
importance sampling reweights draws from a proposal), and **variational
inference** turns it into an optimisation, maximising the **ELBO** -- the same
bound that drove EM in Part II, and the objective the VAE trains.

## Contents

- `ch04_text.tex` / `ch04_text.pdf` -- the chapter text
- `figures/ch04_panel.png` -- MC error `~ 1/sqrt(n)`, importance sampling tracking a
  rare event where naive MC fails, and the ELBO rising to meet `log p(x)` at the posterior
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Monte Carlo estimation: unbiased, dimension-free `1/sqrt(n)` standard error
- Importance sampling and rare events; the effective sample size
- Variational inference: `log p(x) = ELBO(q) + KL(q || p(z|x))`
- EM as the tractable-posterior case; the VAE (encoder/decoder, ELBO = reconstruction - KL)

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise04` | core | `mc_estimate`, `mc_variance`, `mc_standard_error` |
| `exercise05` | proof | `importance_weight`, `is_estimate`, `eff_sample_size` (q=p reduces to plain MC) |
| `exercise06` | research | `gaussian_kl`, `mc_expectation`, `elbo` (the VAE objective) |

Run one: `python3 exercise05_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
