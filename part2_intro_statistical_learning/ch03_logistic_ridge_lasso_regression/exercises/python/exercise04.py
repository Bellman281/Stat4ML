"""
Chapter 3 exercise -- Ridge, soft-threshold, convexity (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch03_text.tex Section 2 (the ridge
estimator, the lasso soft-threshold, and the sigmoid derivative behind the
logistic Hessian).

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: proof
import math


def ridge_estimator_1d(x, y, lam):
    """Centred 1-D ridge slope: Sxy / (Sxx + lam)."""
    raise NotImplementedError("TODO: ridge_estimator_1d")


def soft_threshold(z, lam):
    """sign(z) * max(|z| - lam, 0)."""
    raise NotImplementedError("TODO: soft_threshold")


def sigmoid_prime(z):
    """Derivative of the sigmoid: s*(1-s) -- the nonnegative factor that makes
    the logistic Hessian positive semidefinite."""
    raise NotImplementedError("TODO: sigmoid_prime")


def main():
    x = [1, 2, 3]; y = [2, 4, 6]
    print("ridge (lam=2)     :", ridge_estimator_1d(x, y, 2.0))
    print("soft_threshold    :", soft_threshold(-2.0, 1.0))
    print("sigmoid_prime(0)  :", sigmoid_prime(0.0))


if __name__ == "__main__":
    main()
