# Stat4ML

**Statistics and Mathematics for Machine Learning, Deep Learning, Deep NLP,
Reinforcement Learning, and LLM Training.**

This repository is the merged home of Omid Safarzadeh's "trio" of
courses -- previously split across two repos, now combined into one book
so the whole sequence can be read, exercised, and audited together. See
`ABOUT.md` for the full mission and background, `ROADMAP.md` for what's
planned next, `AUDIT.md` for a list of typos/bugs found in the original
material, and `CONTRIBUTING.md` if you want to help write a chapter.

> **Note on this reorganization:** this repo used to keep the original
> Stat4ML slide/homework/prerequisite PDFs sitting loose at the repository
> root, plus a separate `book/` folder for the merged text and exercises.
> Both have since been cleaned up: the `book/` wrapper is gone (its three
> parts now live directly at the repo root), and every original slide deck
> and homework PDF has been moved into its matching chapter's
> `source_slides/` or `homework/` folder (see the table in `CONTRIBUTING.md`
> for the exact mapping). `PreReq0_Calculus.pdf` stays at the root, since
> no single chapter is "the calculus chapter." `distributions.ipynb` has
> been retired in favor of a plain-Python equivalent,
> `part1_statistics_foundations/ch03_distribution_functions/distributions_demo.py`,
> so the repo doesn't require a Jupyter runtime to reproduce it.

## The book

```
part1_statistics_foundations/         Part I:   Statistics Foundation for ML
part2_intro_statistical_learning/     Part II:  Introduction to Statistical Learning
part3_advanced_statistical_learning/  Part III: Advanced Statistical Learning for DL
```

Each chapter is its own folder (O'Reilly-style): a LaTeX/PDF chapter
text, a `source_slides/` copy of the original lecture slide PDF (when one
exists), a `homework/` copy of the original homework PDF (when one
exists), and **at least three homework exercises** in **Python, R, and
Rust**, each covering a different piece of the chapter's material --
every exercise, in every language, also gets a **Rustlings-style
broken-code counterpart**: fully working code with a few deliberate bugs
planted against the chapter's formulas/theorems, which you fix one at a
time until the tests pass. See `CONTRIBUTING.md` for the exact file
layout.

Four chapters are fully authored end to end (text + all three languages'
exercises + buggy exercises, all verified to compile/run) as a reference
for the rest:
- `part1_statistics_foundations/ch00_matrix_algebra_review/`
- `part1_statistics_foundations/ch01_probability_theory_foundations/`
- `part1_statistics_foundations/ch02_moments/`
- `part2_intro_statistical_learning/ch01_learning_algorithms_overview/`

Every other chapter is scaffolded (folder structure, chapter README,
topic list, exercise stubs) so contributors have a consistent shape to
fill in -- see `ROADMAP.md` for the priority order.

## Part I: Statistics Foundation for ML

Probability theory and mathematical statistics: sample spaces, random
variables, moments, the standard discrete/continuous distributions,
convergence concepts, and estimation (MLE and Bayesian).

**Registration (cohort 2):** https://forms.gle/ZqLJLmv1K5nGVx3m7

**Course text:** Casella, G., & Berger, R. (2002). *Statistical
Inference* (2nd ed.). Cengage Learning.

### Prerequisites
- **Calculus:** derivatives (chain rule), integrals (techniques of
  integration, substitution, integration by parts). See
  `PreReq0_Calculus.pdf` (repository root -- no dedicated calculus
  chapter exists yet).
- **Matrix algebra:** matrix operations and multiplication, determinants,
  inverses, transposes, partitioned matrices, eigenvalues/eigenvectors,
  matrix decompositions (LU, Cholesky, QR, SVD), matrix differentiation.
  See `part1_statistics_foundations/ch00_matrix_algebra_review/source_slides/PreReq1_Matrix_Calculus.pdf`,
  now expanded into Chapter 0 below.

### Chapters
0. Matrix Algebra Review *(fully authored -- see `part1_statistics_foundations/ch00_matrix_algebra_review/`)*
1. Probability Theory Foundations *(fully authored -- see `part1_statistics_foundations/ch01_probability_theory_foundations/`)*
2. Moments *(fully authored -- see `part1_statistics_foundations/ch02_moments/`)*
3. Distribution Functions
4. Conditional and Multivariate Distributions
5. Convergence Concepts
6. Maximum Likelihood Estimation
7. Bayesian and Posterior Distribution Estimation

## Part II: Introduction to Statistical Learning

Core statistical/machine learning: regression, regularization, resampling,
unsupervised learning, EM, clustering, and the on-ramp into neural
networks and Transformers.

**Registration (cohort 1):** https://forms.gle/gRqq7uCp9FVcqgej9

**Course texts:**
- James, G., Witten, D., Hastie, T., & Tibshirani, R. *An Introduction to
  Statistical Learning*.
- Murphy, K. *Machine Learning: A Probabilistic Perspective*.

### Chapters
1. Learning Algorithms Overview *(fully authored -- see `part2_intro_statistical_learning/ch01_learning_algorithms_overview/`)*
2. Regression, Cross-Validation
3. Logistic, Ridge, Lasso Regression
4. Recommendation Systems *(content gap -- see `AUDIT.md`)*
5. Unsupervised Learning, PCA
6. EM Algorithm
7. Clustering
8. NN, Activation and Loss Functions
9. Convolutional Neural Networks *(content gap)*
10. RNN, LSTM *(content gap)*
11. Language Models and Tokenization *(content gap)*
12. Transformers
13. Large Language Models *(content gap)*

## Part III: Advanced Statistical Learning for DL

Originally announced as "to be announced" -- scaffolded here from the
topic list already sketched for it (automatic differentiation, AutoML,
GANs, multi-armed bandits, neural architecture search, famous vision
models, advanced language models, NLP downstream tasks, speech
processing, multi-modal models, Gaussian processes, automatic feature
extraction). See `part3_advanced_statistical_learning/README.md` for
the full chapter list and `ROADMAP.md` for authoring priority.

## Where this is going

The goal is for this repo to become a complete, spoon-fed source of
statistics for ML, deep learning, reinforcement learning, and LLM
training -- not just these three courses. `ROADMAP.md` lays out two new
proposed parts (Reinforcement Learning; Large Language Model Training)
plus a shorter capstone part on probabilistic deep learning, in addition
to closing the content gaps already listed above.

## Instructor

**Omid Safarzadeh**
LinkedIn: https://www.linkedin.com/in/omidsafarzadeh/
Instagram: @deepdatascientists

## License

This repository is licensed under the GNU General Public License v2
(GPLv2) -- see `LICENSE`. (Before this merge, Part I's original `Stat4ML`
repo was MIT-licensed; the combined repository has since been relicensed
GPLv2 throughout -- see `ABOUT.md` for the full note.)
