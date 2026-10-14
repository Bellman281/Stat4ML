"""
Chapter 5 exercise -- entropy, cross-entropy, KL (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch05_text.tex Section 1. p and q are
probability distributions given as lists that sum to 1 (all entries > 0). Work
in nats (natural log).
  - entropy       : H(p)   = -sum p_i log p_i.
  - cross_entropy : H(p,q) = -sum p_i log q_i.
  - kl            : KL(p||q) = sum p_i log(p_i / q_i).

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: core
import math


def entropy(p):
    """Shannon entropy of p (nats)."""
    raise NotImplementedError("TODO: entropy")


def cross_entropy(p, q):
    """Cross-entropy H(p, q) (nats)."""
    raise NotImplementedError("TODO: cross_entropy")


def kl(p, q):
    """KL divergence KL(p || q) (nats)."""
    raise NotImplementedError("TODO: kl")


def main():
    p = [0.5, 0.5]; q = [0.25, 0.75]
    print("entropy      :", entropy(p))
    print("cross_entropy:", cross_entropy(p, q))
    print("kl           :", kl(p, q))


if __name__ == "__main__":
    main()
