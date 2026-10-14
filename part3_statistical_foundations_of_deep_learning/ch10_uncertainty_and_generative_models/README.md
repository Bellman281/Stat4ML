# Chapter 10: Uncertainty and Modern Generative Models

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

Knowing when not to trust a model, and generating from it. **Conformal
prediction** turns any model into one with a finite-sample, distribution-free
coverage guarantee (resting only on exchangeability). **Calibration** asks
whether a classifier's probabilities mean what they say, and measures the gap.
**Score matching** -- learning `grad log p` -- is the engine inside **diffusion
models**, which generate by following the score from noise back to the data. The
score, one of statistics' oldest objects, at the heart of its newest models.

## Contents

- `ch10_text.tex` / `ch10_text.pdf` -- the chapter text
- `figures/ch10_panel.png` -- a 90% conformal band (measured coverage 90.4%), a
  calibration reliability diagram, and the score field grad-log-p pointing to the modes
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Conformal prediction; marginal coverage from exchangeability (proved)
- Calibration; reliability diagrams and the expected calibration error
- Score matching (denoising); diffusion as following the score from noise to data

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise10` | core | `nonconformity`, `quantile_rank`, `coverage` |
| `exercise11` | proof | `conformal_q`, `empirical_coverage`, `guarantee_holds` |
| `exercise12` | research | `gaussian_score`, `denoising_target`, `langevin_step` |

Run one: `python3 exercise11_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
