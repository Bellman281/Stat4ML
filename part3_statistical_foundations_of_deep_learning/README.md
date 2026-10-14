# Part III -- Statistical Foundations of Deep Learning & Reinforcement Learning

Not a tour of architectures. Each chapter is a **statistical subfield**, taught
with proofs, using deep-learning and reinforcement-learning methods as the
running examples. The method is the example; the statistics is the subject. This
is the course's "zero to advanced DL" payoff, told in a statistician's language.

**Course texts:** Shalev-Shwartz & Ben-David, *Understanding Machine Learning*;
Sutton & Barto, *Reinforcement Learning: An Introduction*; Murphy, *Probabilistic
Machine Learning*.

| # | Chapter | Covers | Status |
|---|---------|--------|--------|
| 01 | [Statistical Learning Theory](./ch01_statistical_learning_theory/) | bias-variance, concentration inequalities, VC / Rademacher / PAC, margins; double descent | **complete** |
| 02 | Estimation & Losses | losses as MLE, regularization as priors/MAP, the score function | planned |
| 03 | Stochastic Approximation & Optimisation | SGD as Robbins-Monro, convergence, implicit regularisation | planned |
| 04 | Monte Carlo & Variational Inference | MC estimation, importance sampling, MCMC; the ELBO and the VAE | planned |
| 05 | Information Theory for Learning | entropy, KL, cross-entropy, mutual information, proper scoring rules, perplexity | planned |
| 06 | Markov Decision Processes & Dynamic Programming | MDPs, the Bellman operator as a contraction, value/policy iteration, MC & TD | planned |
| 07 | Bandits & Policy-Gradient RL | regret, UCB, Thompson sampling; REINFORCE as the likelihood-ratio estimator, baselines, off-policy IS | planned |
| 08 | Probabilistic Sequence & Language Models | chain rule of probability, n-gram -> neural LM, perplexity = cross-entropy; word2vec as PMI factorisation | planned |
| 09 | Gaussian Processes & the Infinite-Width Limit | GP regression, the kernel view, the infinitely-wide-network = GP result | planned |
| 10 | Uncertainty & Modern Generative Models | conformal prediction, calibration; score matching and diffusion | planned |

**complete** means a written chapter plus six exercises (three each in Python and
R, with a broken copy of each). **planned** means the chapter folder is created
only when it is actually written -- nothing here is an empty stub.

> The original `part3_advanced_statistical_learning/` folder held an
> architecture/applications tour (AutoML, GANs, NAS, vision/speech/multimodal).
> It is superseded by this statistics-first spine; its one surviving slide deck
> (feature extraction) will be folded into the relevant chapter as it is written.
