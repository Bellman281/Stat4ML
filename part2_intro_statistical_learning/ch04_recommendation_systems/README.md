# Chapter 04: Recommendation Systems

_Part II -- Introduction to Statistical Learning_

Predicting the ratings a user hasn't given. Stated plainly it is **matrix
completion**, and it is only solvable because of one assumption: the ratings
matrix is approximately **low rank**. That turns a blank table into estimation
-- every user and item gets a short vector of latent "taste" coordinates, and a
rating is their dot product. The chapter fits that latent-factor model two ways
and shows they are old friends in disguise: **alternating least squares** is the
ridge regression of Chapter 3 solved one side at a time (with a proof that each
update is the unique ridge estimator), and **Funk SVD** is stochastic gradient
descent over the observed cells. Both are the truncated SVD adapted to missing
data.

## Contents

- `ch04_text.tex` / `ch04_text.pdf` -- the chapter text
- `figures/ch04_panel.png` -- a sparse ratings matrix, its rank-2 completion
  (the latent genres show up as block structure), and the ALS error falling to
  the noise floor
- `exercises/python/`, `exercises/r/` -- for each drill: the homework
  exercise, a **broken** copy to debug, and a reference solution, in both
  languages

## Topics

- The ratings matrix and the matrix-completion problem; why low rank makes it solvable
- The latent-factor model $\hat R_{ui} = p_u^\top q_i$; collaborative filtering
- The regularized MF objective over observed entries only
- Alternating least squares as repeated ridge regression (Theorem: the ALS update is the ridge estimator)
- Funk SVD: SGD over observed cells; user/item/global biases
- The link to the SVD and Eckart--Young in the fully-observed case

## Drills

| Exercise | Tier | What you build |
|---|---|---|
| `exercise04` | core | `predict`, `squared_error`, `rmse` -- the latent-factor prediction and its score |
| `exercise05` | proof | `ridge_solution_2d`, `objective`, `grad_at` -- the ALS update is a stationary point of the ridge objective |
| `exercise06` | research | `predict_bias`, `sgd_update` -- one Funk-SVD step with biases; the step lowers the error |

Run one: `python3 exercise05_buggy.py` and fix until the tests pass. Or drive
them from the repo-root runner: `python3 drill.py next --level master`.

## Source

_No original slide deck exists for this chapter -- it is one of the topics the
original course announced but never recorded. The chapter and drills here are
written from scratch, framed as statistical learning (matrix factorization as
regularized low-rank estimation)._
