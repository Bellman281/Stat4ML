# Roadmap: Statistics for ML, Deep Learning, RL, and LLM Training

This repo's stated ambition is to become a single, spoon-feed-friendly
source for the statistics underlying modern ML, deep learning,
reinforcement learning, and LLM training -- not just a slide archive. This
document is split into two horizons: (A) closing gaps in the three parts
that already exist (`part1_*`, `part2_*`, `part3_*`), and (B) new
parts to add so the "trio" of courses grows into that fuller curriculum.
Every proposed chapter follows the same O'Reilly-style folder contract
already used in this repo: `chNN_text.tex`/`.pdf`, `exercises/{python,r,rust}`,
and a Rustlings-style buggy exercise per chapter (see `CONTRIBUTING.md`).

## Recently completed

**Part I, Chapter 0 -- Matrix Algebra Review** is now fully authored (see
`part1_statistics_foundations/ch00_matrix_algebra_review/`), expanding
the `PreReq1_Matrix_Calculus.pdf` prerequisite deck (previously just
linked from the README, not its own chapter) into a full chapter with
three exercises across Python/R/Rust: core matrix operations, LU
decomposition, and eigenvalues/eigenvectors. It is now a fourth PILOT
chapter alongside Part I Ch. 1-2 and Part II Ch. 1.

## A. Close existing gaps (highest priority)

These are chapters the two original READMEs already promised but that
have no slide deck (see `AUDIT.md`, Section 3). Filling these in is
lower-risk and higher-value than adding all-new parts, because the
scaffolding, numbering, and topic scope are already agreed:

1. **Part II, Ch. 3 -- Lasso regression** (currently only Ridge is fully
   derived). Add: the L1 penalty, why it induces sparsity (geometric +
   subgradient argument), coordinate descent as the standard solver, and
   a worked comparison against Ridge on the same toy dataset used in
   `ch03_text.tex`.
2. **Part II, Ch. 4 -- Recommendation Systems** (no slide exists at all).
   Collaborative filtering, matrix factorization, Funk SVD, alternating
   least squares -- as already listed in the README.
3. **Part II, Ch. 9 -- CNNs**, **Ch. 10 -- RNN/LSTM/GRU**, **Ch. 11 --
   Language Models and Tokenization**, **Ch. 13 -- LLMs (BERT/GPT-3)**.
   These four are the biggest missing stretch of Part II -- right now the
   course jumps from activation/loss functions (Ch. 8) to Transformers
   (Ch. 12) with nothing in between. Recommend authoring in this order:
   CNN -> RNN/LSTM -> tokenization -> (then Transformers, already done)
   -> LLMs, since each builds representationally on the last.
4. **Part III -- the entire "Advanced Statistical Learning for DL"
   part.** The original README literally says "to be announced"; only
   Chapter 12 (Automatic Feature Extraction) has a slide deck. Suggested
   authoring priority, based on what Part II leaves as prerequisites:
   Automatic Differentiation (1) -> GANs (3) -> Multi-Armed Bandits (4)
   -> Neural Architecture Search (5) -> Famous Vision Models (6) ->
   Advanced Language Models (7) -> the rest.

## B. New parts to add

The existing "trio" (Statistics Foundation -> Intro to Statistical
Learning -> Advanced Statistical Learning) does not yet have a dedicated
treatment of reinforcement learning as its own subject (today it is one
paradigm mentioned in Part II Ch. 1, plus multi-armed bandits in Part
III), and has no dedicated LLM-*training* pipeline (Part III's "Advanced
Language Models" chapter is about model families, not how they are
actually trained end to end). Both are core to the "source of statistics
for ML, DL, RL, and LLM training" ambition, so they are proposed as new
parts rather than squeezed into existing ones.

### Part IV -- Reinforcement Learning

1. Markov Decision Processes: states, actions, rewards, the Bellman
   equations, value iteration, policy iteration.
2. Model-Free Prediction and Control: Monte Carlo methods, temporal
   difference learning (TD(0), TD(λ)), SARSA, Q-learning.
3. Function Approximation in RL: why tabular methods break down,
   linear function approximation, the deadly triad.
4. Deep Q-Networks: experience replay, target networks, DQN and its
   main variants (Double DQN, Dueling DQN).
5. Policy Gradient Methods: REINFORCE, the policy gradient theorem,
   variance reduction with baselines.
6. Actor-Critic and Modern Policy Optimization: A2C/A3C, TRPO, PPO --
   the algorithm family behind most modern RL and RLHF.
7. Multi-Armed Bandits (cross-reference: this can absorb/supersede Part
   III Ch. 4 once written, to avoid duplicating content).
8. Exploration vs. Exploitation at Scale: UCB variants, Thompson
   sampling, intrinsic motivation.
9. Model-Based RL and Planning: world models, MuZero-style planning.
10. Multi-Agent RL and Self-Play (ties back to the AlphaGo/AlphaZero and
    hide-and-seek examples already referenced in Part II Ch. 1).

### Part V -- Large Language Model Training

1. The Pretraining Objective: causal vs. masked language modeling,
   next-token prediction as density estimation (ties directly back to
   Part I -- this is MLE on an enormous scale).
2. Tokenization at Scale: BPE, WordPiece, SentencePiece, vocabulary size
   tradeoffs (extends Part II Ch. 11 once written).
3. Scaling Laws: the Chinchilla/Kaplan-style compute-optimal tradeoffs
   between model size, data size, and compute budget.
4. Distributed Training: data parallelism, tensor/pipeline parallelism,
   ZeRO-style optimizer state sharding -- the systems side of training a
   model too large for one GPU.
5. Supervised Fine-Tuning (SFT) and Instruction Tuning.
6. Reward Modeling: learning a reward model from human preference data
   (the statistics here -- Bradley-Terry models -- connect directly back
   to Part I's MLE chapter).
7. RLHF and Direct Preference Optimization (DPO): both as concrete
   applications of Part IV's policy-gradient/actor-critic material.
8. Evaluation of LLMs: perplexity, benchmark suites, the statistics of
   why single-number leaderboards mislead (confidence intervals on eval
   scores, contamination).
9. Efficient Inference: quantization, KV-caching, speculative decoding.
10. Retrieval-Augmented Generation and Agents: grounding generation in
    external knowledge/tools -- a natural capstone chapter.

### Part VI -- Probabilistic Deep Learning (proposed, lower priority)

A shorter, more theoretical part that ties Part I's probability
foundations directly to modern generative modeling -- useful once Parts
I-V exist, as a "graduate capstone":
1. Variational Inference and the ELBO.
2. Variational Autoencoders.
3. Normalizing Flows.
4. Diffusion Models (the forward/reverse SDE view, connecting back to
   Part I's convergence-concepts chapter).
5. Uncertainty Quantification in Deep Networks (calibration, conformal
   prediction).

## Suggested near-term sequencing

Given limited authoring time, the highest-leverage order is:
1. Finish Part II's five missing chapters (Section A.2-A.3 above) --
   this makes the existing, already-promised course complete.
2. Author Part III in full -- likewise, already promised, "to be
   announced" is the only thing blocking it.
3. Start Part IV (Reinforcement Learning) -- it is self-contained and
   only needs Part I as a prerequisite.
4. Start Part V (LLM Training) once Part II's language-model chapters
   (11, 12, 13) and Part IV's policy-gradient chapters exist, since Part
   V leans on both.
5. Part VI last -- it is the most advanced and benefits from every other
   part being in place first.
