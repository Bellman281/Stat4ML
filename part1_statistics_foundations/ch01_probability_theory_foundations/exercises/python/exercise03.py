"""
Chapter 1 exercise 3 -- Independence and the probability integral transform
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch01_text.tex Section 4
(Independence, and the P(B n A^c) = P(B) - P(A n B) identity) and
Section 8 (the probability integral transform, Y = F_X(X) ~ Uniform(0,1)).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
import math
import random


def independence_check(p_a, p_b, p_a_and_b, tol=1e-9):
    """True iff P(A n B) = P(A) P(B) within `tol` (ch01_text.tex
    Section 4's definition of independence)."""
    # TODO
    raise NotImplementedError("TODO: independence_check")


def intersection_with_complement(p_a, p_b_and_a):
    """P(A n B^c) = P(A) - P(A n B). This is Theorem (Elementary
    consequences), item 4 of ch01_text.tex Section 3, applied with the
    roles of A and B swapped."""
    # TODO
    raise NotImplementedError("TODO: intersection_with_complement")


def exponential_cdf(y):
    """F_X(y) = 1 - e^{-y} for y >= 0, else 0 -- the CDF of the
    Exponential(1) distribution from ch01_text.tex Section 8 (obtained
    by integrating the density e^{-y} derived earlier in the chapter)."""
    # TODO
    raise NotImplementedError("TODO: exponential_cdf")


def probability_integral_transform_mean(n, seed=0):
    """Sample n values x_i ~ Exponential(1) (via -log(u) for u ~
    Uniform(0,1)), then apply exponential_cdf to get y_i = F_X(x_i).
    By the probability integral transform (ch01_text.tex Section 8,
    last theorem), Y = F_X(X) ~ Uniform(0,1), so return the sample mean
    of the y_i (should be near 0.5, the mean of Uniform(0,1))."""
    # TODO
    raise NotImplementedError("TODO: probability_integral_transform_mean")


def main():
    print(f"independent (0.5, 0.4, 0.2): {independence_check(0.5, 0.4, 0.2)}  (expect True)")
    print(f"independent (0.5, 0.4, 0.3): {independence_check(0.5, 0.4, 0.3)}  (expect False)")

    print(f"P(A n B^c), A=0.5,B=0.4,AnB=0.3: {intersection_with_complement(0.5, 0.3)}  (expect 0.2)")

    print(f"exponential_cdf(0) = {exponential_cdf(0)}  (expect 0)")
    print(f"exponential_cdf(1) = {exponential_cdf(1):.4f}  (expect ~0.6321)")

    mean = probability_integral_transform_mean(200_000, seed=7)
    print(f"probability_integral_transform_mean = {mean:.4f}  (Uniform(0,1) mean is 0.5)")


if __name__ == "__main__":
    main()
