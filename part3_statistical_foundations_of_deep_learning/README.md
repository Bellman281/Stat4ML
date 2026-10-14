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
| 02 | [Estimation & Losses](./ch02_estimation_and_losses/) | losses as MLE, regularization as priors/MAP, the score function | **complete** |
| 03 | [Stochastic Approximation & Optimisation](./ch03_stochastic_approximation/) | SGD as Robbins-Monro, convergence, implicit regularisation | **complete** |
| 04 | [Monte Carlo & Variational Inference](./ch04_monte_carlo_and_variational_inference/) | MC estimation, importance sampling; the ELBO and the VAE | **complete** |
| 05 | [Information Theory for Learning](./ch05_information_theory/) | entropy, KL, cross-entropy, mutual information, perplexity | **complete** |
| 06 | [Markov Decision Processes & Dynamic Programming](./ch06_markov_decision_processes/) | MDPs, the Bellman operator as a contraction, value/policy iteration, MC & TD | **complete** |
| 07 | [Bandits & Policy-Gradient RL](./ch07_bandits_and_policy_gradients/) | regret, UCB, Thompson sampling; REINFORCE as the likelihood-ratio estimator, baselines, off-policy IS | **complete** |
| 08 | [Probabilistic Sequence & Language Models](./ch08_probabilistic_sequence_models/) | chain rule of probability, n-gram -> neural LM, perplexity = cross-entropy; word2vec as PMI factorisation | **complete** |
| 09 | [Gaussian Processes & the Infinite-Width Limit](./ch09_gaussian_processes/) | GP regression, the kernel view, the infinitely-wide-network = GP result | **complete** |
| 10 | [Uncertainty & Modern Generative Models](./ch10_uncertainty_and_generative_models/) | conformal prediction, calibration; score matching and diffusion | **complete** |

**complete** means a written chapter plus six exercises (three each in Python and
R, with a broken copy of each). All ten chapters are complete.

> The original `part3_advanced_statistical_learning/` folder held an
> architecture/applications tour (AutoML, GANs, NAS, vision/speech/multimodal).
> It is superseded by this statistics-first spine; its one surviving slide deck
> (feature extraction) will be folded into the relevant chapter as it is written.
