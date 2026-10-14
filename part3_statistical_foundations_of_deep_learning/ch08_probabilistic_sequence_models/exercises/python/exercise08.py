"""
Chapter 8 exercise -- sequence probability and perplexity (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch08_text.tex Section 1. `conditionals` is a
list of next-token probabilities p(x_t | x_<t) along a sequence.
  - seq_logprob            : sum of log p(x_t | x_<t).
  - perplexity_from_logprob: exp(-total_logprob / n).
  - ngram_prob             : add-alpha smoothed (count+alpha)/(ctx_count+alpha*V).

Run with:  python3 exercise08.py
Reference solution: solutions/exercise08_solution.py
"""
# level: core
import math


def seq_logprob(conditionals):
    """Total log-probability of the sequence: sum of log of each conditional."""
    raise NotImplementedError("TODO: seq_logprob")


def perplexity_from_logprob(total_logprob, n):
    """Perplexity: exp(-total_logprob / n)."""
    raise NotImplementedError("TODO: perplexity_from_logprob")


def ngram_prob(count, ctx_count, V, alpha):
    """Add-alpha smoothed probability: (count + alpha) / (ctx_count + alpha * V)."""
    raise NotImplementedError("TODO: ngram_prob")


def main():
    c = [0.5, 0.5, 0.25]
    lp = seq_logprob(c)
    print("seq_logprob            :", lp)
    print("perplexity_from_logprob:", perplexity_from_logprob(lp, len(c)))
    print("ngram_prob             :", ngram_prob(2, 10, 5, 1.0))


if __name__ == "__main__":
    main()
