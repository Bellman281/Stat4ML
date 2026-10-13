"""
Chapter 6 exercise -- The E and M steps (Core)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch06_text.tex Section 1 (the Gaussian
density, the responsibility of the E-step, and the weighted mean of the
M-step).

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: core
import math


def gaussian_pdf(x, mu, s2):
    """N(x; mu, s2) = exp(-(x-mu)^2 / (2 s2)) / sqrt(2*pi*s2)."""
    raise NotImplementedError("TODO: gaussian_pdf")


def responsibility(x, pis, mus, s2s, k):
    """r_k = pi_k N_k(x) / sum_j pi_j N_j(x)."""
    raise NotImplementedError("TODO: responsibility")


def weighted_mean(xs, resps):
    """M-step mean: sum(r_i x_i) / sum(r_i)."""
    raise NotImplementedError("TODO: weighted_mean")


def main():
    print("gaussian_pdf(0,0,1) :", gaussian_pdf(0.0, 0.0, 1.0))
    print("responsibility      :", responsibility(0.0, [0.5, 0.5], [-1, 1], [1, 1], 0))
    print("weighted_mean       :", weighted_mean([1, 2, 3], [1, 1, 0]))


if __name__ == "__main__":
    main()
