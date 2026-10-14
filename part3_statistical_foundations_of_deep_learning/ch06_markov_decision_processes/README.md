# Chapter 06: Markov Decision Processes and Dynamic Programming

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

Reinforcement learning begins with a fixed point. An MDP turns "act well over
time" into the **value function**, characterised by the **Bellman equation**. It
can be solved because the **Bellman operator is a gamma-contraction**: by Banach
it has a unique fixed point `V*` that value iteration converges to geometrically.
When the model is unknown, the value is estimated from experience -- **Monte
Carlo** toward the return, **TD(0)** bootstrapping toward `r + gamma V(s')`, the
latter being the Chapter 3 stochastic approximation of the Bellman equation.

## Contents

- `ch06_text.tex` / `ch06_text.pdf` -- the chapter text
- `figures/ch06_panel.png` -- a solved slippery gridworld (`V*` + greedy policy), the
  sup-norm error staying under the `gamma^k` bound, and TD(0) vs Monte Carlo evaluation
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- MDPs, policies, the value function; Bellman expectation & optimality equations
- The Bellman operator as a sup-norm gamma-contraction; value iteration convergence (Banach)
- Policy iteration (finite strict-improvement steps)
- Monte Carlo and TD(0) evaluation; TD as stochastic approximation of the Bellman equation

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise06` | core | `discounted_return`, `q_backup`, `greedy_action` |
| `exercise07` | proof | `sup_norm`, `geometric_bound`, `num_iters_for_tol` (the contraction bound) |
| `exercise08` | research | `mc_update`, `td_error`, `td_update` |

Run one: `python3 exercise07_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
