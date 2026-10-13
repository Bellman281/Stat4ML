"""
Chapter 6 exercise -- Score, Fisher Information, Cramer-Rao (Proof tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch06_text.tex Section 2 (score, Fisher
information, the Cramer-Rao bound, efficiency of the Bernoulli MLE).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: proof
import math
import random


def score_bernoulli(p, data):
    """Score U(p) = sum_i [ x_i/p - (1-x_i)/(1-p) ]."""
    raise NotImplementedError("TODO: score_bernoulli")


def fisher_information_bernoulli(p, n):
    """Fisher information in n iid Bernoulli(p) observations: n / (p(1-p))."""
    raise NotImplementedError("TODO: fisher_information_bernoulli")


def cramer_rao_lower_bound(p, n):
    """Cramer-Rao lower bound for an unbiased estimator of p: p(1-p)/n."""
    raise NotImplementedError("TODO: cramer_rao_lower_bound")


def mle_variance_sim(p, n, reps, seed=0):
    """Simulate `reps` datasets of n Bernoulli(p) draws, take the MLE
    (sample mean) of each, and return the population variance of the MLEs.
    It should land near the Cramer-Rao bound (the Bernoulli MLE is
    efficient, ch06_text.tex Section 2)."""
    raise NotImplementedError("TODO: mle_variance_sim")


def main():
    data = [1] * 15 + [0] * 35  # 15/50 ones, MLE = 0.3
    print(f"score at MLE p=0.3 : {score_bernoulli(0.3, data):.6f}  (expect ~0)")
    print(f"Fisher info(0.3,50): {fisher_information_bernoulli(0.3, 50):.4f}")
    print(f"CRLB(0.3,50)       : {cramer_rao_lower_bound(0.3, 50):.6f}")
    print(f"sim var of MLE     : {mle_variance_sim(0.3, 50, 20000, seed=0):.6f}")


if __name__ == "__main__":
    main()
