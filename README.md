# Stat4ML

### The statistics behind machine learning — proven on paper, then debugged in code.

A free, self-paced course in the mathematics that modern machine learning actually
runs on — from probability and estimation up toward deep learning. Every idea is
worked out in full (definitions, theorems, **real proofs**), then handed to you as
code you run and fix yourself. Think *rustlings, for the math of ML*.

<p align="center">
  <img src="assets/drill.gif" width="620" alt="The drill loop: run the broken exercise, read the first failing check, fix it, watch it pass.">
</p>

Every exercise ships three ways — a from-scratch TODO, a **deliberately broken copy
whose bug breaks a specific theorem from the chapter**, and a reference solution — in
**Python and R**. You run it, read the first failing check, fix that one thing, and
watch it go green. You meet every idea twice: once building it, once debugging it.

## See the ideas move

The chapters don't just state results — they show them happening.

<table>
<tr>
<td align="center">
  <img src="assets/clt.gif" width="400" alt="central limit theorem converging"><br/>
  <sub><b>Central limit theorem</b> — sample means of skewed data become normal.</sub>
</td>
<td align="center">
  <img src="assets/bayes.gif" width="400" alt="bayesian posterior updating"><br/>
  <sub><b>Bayesian updating</b> — the posterior tightens onto the truth as data arrive.</sub>
</td>
</tr>
</table>

## What's in a chapter

- **The chapter, written out properly.** Not slide bullets — prose with real
  definitions, theorems, and worked proofs, colour-typeset so you can tell a
  definition from a theorem from an aside at a glance. PDF, with the LaTeX source
  beside it.
- **Worked code, inline.** A short Python gallery next to the maths (the MLE for ten
  distributions, the CLT across three sources, conjugate Bayesian updates), and a
  simulation figure that makes the key theorem something you *watch happen*.
- **Three exercises, in Python and R**, each covering a different piece of the chapter
  — a from-scratch TODO, a broken copy to debug, and a reference solution.
- **The original lecture slides and homework**, exactly as taught, when they exist.

Nothing to install: the Python exercises use only the standard library, the R ones
only base R.

## Drill it yourself

`drill.py` walks the course one exercise at a time, rustlings-style: run it, read the
first failing check, fix the file, watch it pass, move on. It only ever hands you
exercises whose reference solution actually runs, so unfinished chapters are skipped.

```bash
python3 drill.py           # run the next unfinished exercise
python3 drill.py watch     # rerun automatically every time you save
python3 drill.py list      # see every exercise and its status
python3 drill.py verify    # check every ready exercise is sound
```

By default you fix the deliberately broken copies (`--track debug`); pass
`--track build` to fill in the TODO versions from scratch. Python runs out of the box;
add R with `--lang both` once `Rscript` is installed.

**Drill at your level.** Every exercise is tagged `core` / `proof` / `research`, so the
course scales with you:

```bash
python3 drill.py --level bachelor   # core: results, intuition, code
python3 drill.py --level master     # + the proofs
python3 drill.py --level phd        # + research-grade extensions
```

## A look inside

<table>
<tr>
<td align="center" width="50%">
  <img src="part1_statistics_foundations/ch06_maximum_likelihood_estimation/figures/mle_sampling.png" width="380" alt=""><br/>
  <sub>Ch.6 — the MLE's sampling distribution meets the Cramér–Rao floor.</sub>
</td>
<td align="center" width="50%">
  <img src="part1_statistics_foundations/ch03_distribution_functions/figures/pit_panel.png" width="380" alt=""><br/>
  <sub>Ch.3 — turning a uniform into any distribution, and back.</sub>
</td>
</tr>
<tr>
<td align="center" width="50%">
  <img src="part1_statistics_foundations/ch04_conditional_and_multivariate_distributions/figures/bvn_panel.png" width="380" alt=""><br/>
  <sub>Ch.4 — conditioning a bivariate normal.</sub>
</td>
<td align="center" width="50%">
  <img src="part1_statistics_foundations/ch07_bayesian_estimation/figures/posterior_update.png" width="380" alt=""><br/>
  <sub>Ch.7 — the posterior sharpening onto the true value.</sub>
</td>
</tr>
</table>

## Start here

**Part I (Statistics Foundations) is complete — eight chapters, end to end.** Read it
in order from Chapter 0, or jump to a flagship chapter to see the format:

| Chapter | Why start here |
|---|---|
| [Maximum Likelihood Estimation](part1_statistics_foundations/ch06_maximum_likelihood_estimation/) | proofs + an MLE cookbook for ten distributions + the efficiency simulation |
| [Convergence Concepts](part1_statistics_foundations/ch05_convergence_concepts/) | the law of large numbers and the CLT, proven and simulated |
| [Bayesian Estimation](part1_statistics_foundations/ch07_bayesian_estimation/) | conjugacy, credible intervals, and the bridge back to maximum likelihood |

If you're new to the material, start at
[Chapter 0](part1_statistics_foundations/ch00_matrix_algebra_review/) and read Part I
in order. You'll need calculus (chain rule, integration by parts —
see [`PreReq0_Calculus.pdf`](PreReq0_Calculus.pdf)); Chapter 0 covers the matrix
algebra from scratch.

## Course map

How the parts build on each other, and where each one lands in practice:

```mermaid
flowchart LR
    A["Part I<br/>Statistics Foundations<br/>probability - moments - MLE - Bayesian"]
    B["Part II<br/>Introduction to Statistical Learning<br/>regression - PCA - EM - clustering"]
    C["Part III (planned)<br/>Statistical Foundations of Deep Learning & RL<br/>learning theory - variational inference - bandits & policy gradients"]

    A --> B --> C

    classDef part fill:#4C6EF5,color:#fff,stroke:#333,stroke-width:1px
    classDef planned fill:#adb5bd,color:#fff,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5
    class A,B part
    class C planned
```

Part III reads every deep-learning and reinforcement-learning method through the
statistics underneath it — the method is the example, the statistics is the subject.
It is planned scope; chapter folders are created as each chapter is actually written.

Each chapter is marked **complete** (written chapter + six exercises, three each in
Python and R, with a broken copy of each), **slides only** (lecture slides are there to
learn from; the written chapter isn't done), or **not started**.

## Part I: Statistics Foundations for ML — complete

Probability theory and mathematical statistics: random variables, moments, the standard
distributions and their transforms, convergence (the law of large numbers and the CLT),
and estimation (maximum likelihood and Bayesian).

**Course text:** Casella, G., & Berger, R. (2002). *Statistical Inference* (2nd ed.).

| # | Chapter | Status |
|---|---|---|
| 0 | Matrix Algebra Review | **complete** |
| 1 | Probability Theory Foundations | **complete** |
| 2 | Moments | **complete** |
| 3 | Distribution Functions | **complete** |
| 4 | Conditional and Multivariate Distributions | **complete** |
| 5 | Convergence Concepts | **complete** |
| 6 | Maximum Likelihood Estimation | **complete** |
| 7 | Bayesian and Posterior Distribution Estimation | **complete** |

## Part II: Introduction to Statistical Learning

Regression, regularization, resampling, unsupervised learning, EM, clustering, and one
hands-on neural-network chapter as the on-ramp into Part III.

**Course texts:** James, Witten, Hastie & Tibshirani, *An Introduction to Statistical
Learning*; Murphy, *Machine Learning: A Probabilistic Perspective*.

| # | Chapter | Status |
|---|---|---|
| 1 | Learning Algorithms Overview | **complete** |
| 2 | Regression, Cross-Validation | **complete** |
| 3 | Logistic, Ridge, Lasso Regression | **complete** |
| 4 | Recommendation Systems | not started |
| 5 | Unsupervised Learning, PCA | **complete** |
| 6 | EM Algorithm | **complete** |
| 7 | Clustering | **complete** |
| 8 | NN, Activation and Loss Functions | **complete** |

The deep-learning architecture topics that used to sit here (CNNs, RNN/LSTM, Transformers,
LLMs) move to Part III, recast as statistics rather than architecture tours.

## Part III: Statistical Foundations of Deep Learning & Reinforcement Learning — planned

Not a tour of architectures. Each chapter is a statistical subfield, taught with proofs,
using deep-learning and reinforcement-learning methods as the running examples. This is
the course's "zero to advanced DL" payoff, told in a statistician's language.

**Course texts:** Shalev-Shwartz & Ben-David, *Understanding Machine Learning*; Sutton &
Barto, *Reinforcement Learning: An Introduction*; Murphy, *Probabilistic Machine Learning*.

| # | Chapter | Covers | Status |
|---|---|---|---|
| 1 | Statistical Learning Theory | bias–variance, concentration inequalities, VC / Rademacher / PAC, margins; double descent | planned |
| 2 | Estimation & Losses | losses as MLE (MSE = Gaussian, cross-entropy = multinomial), regularization as priors/MAP, the score function | planned |
| 3 | Stochastic Approximation & Optimisation | SGD as Robbins–Monro, convergence, implicit regularisation | planned |
| 4 | Monte Carlo & Variational Inference | MC estimation, importance sampling, MCMC; the ELBO and the VAE | planned |
| 5 | Information Theory for Learning | entropy, KL, cross-entropy, mutual information, proper scoring rules, perplexity | planned |
| 6 | Markov Decision Processes & Dynamic Programming | MDPs, the Bellman operator as a contraction, value/policy iteration, MC & TD evaluation | planned |
| 7 | Bandits & Policy-Gradient RL | regret, UCB from concentration, Thompson sampling; REINFORCE as the likelihood-ratio estimator, baselines as control variates, off-policy importance sampling | planned |
| 8 | Probabilistic Sequence & Language Models | the chain rule of probability, n-gram → neural LM, perplexity = cross-entropy; word2vec as implicit PMI factorisation; attention as kernel smoothing | planned |
| 9 | Gaussian Processes & the Infinite-Width Limit | GP regression, the kernel view, the infinitely-wide-network = GP result | planned |
| 10 | Uncertainty & Modern Generative Models *(advanced)* | conformal prediction, calibration; score matching and diffusion | planned |

**Note on the old `part3_advanced_statistical_learning/` folder:** its original scope
(AutoML, GANs, NAS, famous vision models, speech, multimodal, …) was an architecture/
applications tour. It is superseded by the statistics-first spine above; those folders
will be reorganised into the chapters above as each one is actually written.

## Instructor

**Omid Safarzadeh**
LinkedIn: https://www.linkedin.com/in/omidsafarzadeh/ · Instagram: @deepdatascientists

## License

GNU General Public License v2 (GPLv2) — see [`LICENSE`](LICENSE).
