"""
Chapter 6 exercise -- The evidence lower bound (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch06_text.tex Section 2. The hidden label
z has two values; `joint` is [p(x,z=1), p(x,z=2)], `q` a distribution over z,
and `p` the posterior p(z|x). The identity to feel:
log p(x) = ELBO(q) + KL(q || p).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: proof
import math


def log_evidence(joint):
    """log p(x) = log( sum_z p(x,z) )."""
    raise NotImplementedError("TODO: log_evidence")


def elbo(q, joint):
    """sum_z q_z * ( log(joint_z) - log(q_z) )."""
    raise NotImplementedError("TODO: elbo")


def kl(q, p):
    """KL(q || p) = sum_z q_z * log(q_z / p_z)."""
    raise NotImplementedError("TODO: kl")


def main():
    joint = [0.2, 0.3]; q = [0.5, 0.5]; post = [0.4, 0.6]
    print("log_evidence :", log_evidence(joint))
    print("elbo         :", elbo(q, joint))
    print("kl           :", kl(q, post))
    print("elbo + kl    :", elbo(q, joint) + kl(q, post))


if __name__ == "__main__":
    main()
