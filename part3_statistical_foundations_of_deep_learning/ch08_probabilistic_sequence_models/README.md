# Chapter 08: Probabilistic Sequence and Language Models

_Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning_

A language model is a probability distribution over sequences, and it all
follows from the **chain rule of probability**: the joint factorises into
next-token conditionals, so an autoregressive model only needs `p(x_t | x_<t)`.
Training it is maximum likelihood -- cross-entropy -- and its score, **perplexity**,
is the exponentiated cross-entropy of Chapter 5. Two modern pieces read
statistically: **word embeddings** implicitly factorise a **PMI matrix** (PCA for
co-occurrence), and **attention** is **Nadaraya-Watson kernel smoothing**.

## Contents

- `ch08_text.tex` / `ch08_text.pdf` -- the chapter text
- `figures/ch08_panel.png` -- n-gram perplexity dropping with context, attention as a
  kernel smoother (weights peaking at the query), and word2vec = PMI embeddings clustering
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both languages

## Topics

- The chain rule and the autoregressive model; n-gram (Markov) vs neural
- LM training = MLE = cross-entropy; perplexity = exp(cross-entropy)
- word2vec as implicit factorisation of the shifted-PMI matrix
- Attention as the Nadaraya-Watson kernel estimator

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise08` | core | `seq_logprob`, `perplexity_from_logprob`, `ngram_prob` |
| `exercise09` | proof | `chain_rule_prob`, `avg_cross_entropy`, `perplexity` (= joint^(-1/n)) |
| `exercise10` | research | `softmax_weights`, `attention`, `pmi` |

Run one: `python3 exercise10_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level phd`.
