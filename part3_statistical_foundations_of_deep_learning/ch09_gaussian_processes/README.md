# Chapter 09: Gaussian Processes and the Infinite-Width Limit

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

A Gaussian process is a distribution over **functions**: any finite set of values
is jointly Gaussian, with covariance set by a **kernel**. Regression is just
**Gaussian conditioning** (Chapter 4) -- the posterior is again a GP, giving a
predicted curve and a calibrated uncertainty that is small at the data and large
away from it. The chapter closes with Neal's theorem: a neural network of
**infinite width** with random weights **is** a Gaussian process, by the central
limit theorem (Chapter 5).

## Contents

- `ch09_text.tex` / `ch09_text.pdf` -- the chapter text
- `figures/ch09_panel.png` -- GP prior samples, the GP posterior pinching at the data,
  and a random net's output becoming Gaussian as the width grows
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Gaussian processes; the RBF kernel; samples as smooth functions
- GP regression as conditioning a multivariate normal; calibrated predictive variance
- Neal's theorem: a wide random network is a GP (CLT); the NNGP kernel

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise09` | core | `rbf_kernel`, `kernel_vector`, `linear_kernel` |
| `exercise10` | proof | `gp_post_mean`, `gp_post_var` (variance = 0 at a noise-free data point) |
| `exercise11` | research | `relu`, `nn_features`, `nngp_kernel` |

Run one: `python3 exercise10_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
