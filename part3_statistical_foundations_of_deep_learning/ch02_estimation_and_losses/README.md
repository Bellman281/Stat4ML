# Chapter 02: Estimation and Losses

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

Every loss a network minimises is a likelihood in disguise, and every
regulariser is a prior. Squared error is the **negative log-likelihood of
Gaussian noise**; cross-entropy is the NLL of a categorical label; adding a
penalty is **maximising the posterior** (MAP), with the L2 penalty a Gaussian
prior and the L1 penalty a Laplace prior whose sharp peak at zero gives sparse
weights. Threading both is the **score function**, the gradient of the
log-likelihood, whose expectation is zero at the truth -- the object estimation,
and later policy gradients, are built on.

## Contents

- `ch02_text.tex` / `ch02_text.pdf` -- the chapter text
- `figures/ch02_panel.png` -- least squares = maximum likelihood (same minimiser),
  Gaussian vs Laplace priors, and the L1-diamond / L2-circle geometry of sparsity
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Losses as negative log-likelihoods: MSE = Gaussian MLE, cross-entropy = categorical MLE
- Regularisation as a prior: MAP = loss + penalty; ridge = Gaussian prior (lam = sigma^2/tau^2); lasso = Laplace prior
- The score function: mean-zero at the truth, Fisher information as its variance, the log-derivative trick

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise02` | core | `mse`, `bernoulli_nll`, `gaussian_nll` |
| `exercise03` | proof | `gaussian_log_prior`, `ridge_lambda`, `ridge_estimate_1d` (MAP minimises the penalised objective) |
| `exercise04` | research | `gaussian_score`, `bernoulli_score`, `mle_mean` (total score zero at the MLE) |

Run one: `python3 exercise03_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
