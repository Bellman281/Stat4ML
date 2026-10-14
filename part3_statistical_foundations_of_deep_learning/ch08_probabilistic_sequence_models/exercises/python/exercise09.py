"""
Chapter 8 exercise -- chain rule and perplexity = cross-entropy (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch08_text.tex Sections 1 (and Chapter 5).
`conditionals` are the per-token probabilities p(x_t | x_<t).
  - chain_rule_prob   : the joint probability, the PRODUCT of the conditionals.
  - avg_cross_entropy : -mean(log p_t), the per-token cross-entropy (nats).
  - perplexity        : exp(avg_cross_entropy).

The test checks the identity perplexity = chain_rule_prob^(-1/n).

Run with:  python3 exercise09.py
Reference solution: solutions/exercise09_solution.py
"""
# level: proof
import math


def chain_rule_prob(conditionals):
    """Joint probability: product of the conditionals."""
    raise NotImplementedError("TODO: chain_rule_prob")


def avg_cross_entropy(conditionals):
    """Per-token cross-entropy: -(1/n) sum log p_t."""
    raise NotImplementedError("TODO: avg_cross_entropy")


def perplexity(avg_ce):
    """Perplexity: exp(avg_cross_entropy)."""
    raise NotImplementedError("TODO: perplexity")


def main():
    c = [0.5, 0.5, 0.25]
    print("chain_rule_prob :", chain_rule_prob(c))
    ace = avg_cross_entropy(c)
    print("avg_cross_entropy:", ace)
    print("perplexity       :", perplexity(ace))
    print("joint^(-1/n)     :", chain_rule_prob(c) ** (-1 / len(c)))


if __name__ == "__main__":
    main()
