# Chapter 07: Bandits and Policy-Gradient Reinforcement Learning

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

Two statistical problems under RL's action side. The **multi-armed bandit** is
explore-vs-exploit in pure form: the right amount of exploration falls out of a
concentration bound (**UCB**, an optimistic Hoeffding width from Chapter 1) or a
posterior (**Thompson sampling**), giving logarithmic regret. The **policy
gradient** optimises a policy you can only sample from -- and it is just the
Chapter 2 **score function** applied to a policy: `grad J = E[R * grad log pi]`.
A **baseline** is a control variate that cuts the estimator's variance without
biasing it (mean-zero score).

## Contents

- `ch07_text.tex` / `ch07_text.pdf` -- the chapter text
- `figures/ch07_panel.png` -- bandit regret (epsilon-greedy linear vs UCB/Thompson
  sub-linear), REINFORCE with vs without a baseline, and the variance-minimising baseline
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Bandits, regret; UCB from a Hoeffding confidence bound; Thompson sampling
- The policy-gradient theorem (REINFORCE) via the log-derivative trick = the score
- Baselines as control variates (unbiased by the mean-zero score); advantage / actor-critic
- Off-policy policy gradients via importance sampling (Chapter 4)

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise07` | core | `ucb_index`, `argmax_index`, `cumulative_regret` |
| `exercise08` | proof | `logit_score`, `pg_grad` (the score; mean-zero identity) |
| `exercise09` | research | `advantage`, `grad_estimate`, `expected_grad` (baseline invariance) |

Run one: `python3 exercise08_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
