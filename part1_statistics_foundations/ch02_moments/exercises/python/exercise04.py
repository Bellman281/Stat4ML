"""
Chapter 2 exercise 4 -- MGF derivatives give moments
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch02_text.tex Section 3 (moment
generating functions, and the theorem E[X^n] = M_X^(n)(0)) and the Normal
MGF formula in Section 3.1. Approximate derivatives with the standard
central finite-difference formulas:
  M'(0)  ~= (M(h) - M(-h)) / (2h)
  M''(0) ~= (M(h) - 2 M(0) + M(-h)) / h^2

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
import math


def mgf_normal(t, mu, sigma2):
    """M_X(t) = exp(mu*t + sigma2*t^2/2) for X ~ N(mu, sigma2). Provided
    for you -- not part of this exercise."""
    return math.exp(mu * t + sigma2 * t * t / 2.0)


def first_derivative_at_zero(mu, sigma2, h):
    """Central-difference approximation to M_X'(0), which by
    ch02_text.tex Section 3's theorem should be approximately E[X] = mu."""
    # TODO
    raise NotImplementedError("TODO: first_derivative_at_zero")


def second_derivative_at_zero(mu, sigma2, h):
    """Central-difference approximation to M_X''(0), which should be
    approximately E[X^2] = sigma2 + mu^2."""
    # TODO
    raise NotImplementedError("TODO: second_derivative_at_zero")


def variance_from_derivatives(mu, sigma2, h):
    """Var(X) = E[X^2] - (E[X])^2, using the two functions above."""
    # TODO
    raise NotImplementedError("TODO: variance_from_derivatives")


def main():
    mu, sigma2, h = 2.0, 4.0, 1e-4

    d1 = first_derivative_at_zero(mu, sigma2, h)
    print(f"M_X'(0) ~= {d1:.6f}  (theoretical E[X] = mu = {mu})")

    d2 = second_derivative_at_zero(mu, sigma2, h)
    print(f"M_X''(0) ~= {d2:.6f}  (theoretical E[X^2] = sigma2+mu^2 = {sigma2 + mu * mu})")

    var = variance_from_derivatives(mu, sigma2, h)
    print(f"Var(X) via derivatives ~= {var:.6f}  (theoretical Var(X) = sigma2 = {sigma2})")


if __name__ == "__main__":
    main()
