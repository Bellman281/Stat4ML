# Chapter 05: Information Theory for Learning

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

The loss that trains almost every classifier and language model -- **cross-entropy**
-- is an information-theoretic quantity. Entropy measures uncertainty;
cross-entropy measures the cost of coding the truth with the wrong model; the two
differ by exactly the **KL divergence**. Since the entropy of the truth is fixed,
minimising cross-entropy minimises KL to the data distribution. **Gibbs'
inequality** (`KL >= 0`) means no model beats the data's own entropy, and
**perplexity** is just cross-entropy exponentiated.

## Contents

- `ch05_text.tex` / `ch05_text.pdf` -- the chapter text
- `figures/ch05_panel.png` -- binary entropy, cross-entropy bottoming at the entropy
  floor (the gap is the KL), and perplexity = exp(cross-entropy)
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- Entropy, cross-entropy, KL; the decomposition `H(p,q) = H(p) + KL(p||q)`
- Gibbs' inequality `KL >= 0` (and KL's asymmetry: forward vs reverse)
- Mutual information `I(X;Y) = H(X) - H(X|Y) = KL(p(x,y) || p(x)p(y))`
- Perplexity as effective vocabulary size

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise05` | core | `entropy`, `cross_entropy`, `kl` |
| `exercise06` | proof | `identity_residual`, `kl_is_nonneg`, `log_bound_gap` (the decomposition + Gibbs) |
| `exercise07` | research | `perplexity`, `joint_entropy`, `mutual_information` |

Run one: `python3 exercise06_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
