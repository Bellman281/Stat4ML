"""Chapter 8 -- reference solution (Proof)."""
# level: proof
import math


def chain_rule_prob(conditionals):
    prod = 1.0
    for p in conditionals:
        prod *= p
    return prod


def avg_cross_entropy(conditionals):
    return -sum(math.log(p) for p in conditionals) / len(conditionals)


def perplexity(avg_ce):
    return math.exp(avg_ce)


def main():
    c = [0.5, 0.5, 0.25]
    print("chain_rule_prob :", chain_rule_prob(c))
    ace = avg_cross_entropy(c)
    print("avg_cross_entropy:", ace)
    print("perplexity       :", perplexity(ace))
    print("joint^(-1/n)     :", chain_rule_prob(c) ** (-1 / len(c)))


if __name__ == "__main__":
    main()
