"""Reference solution for exercise04.py (Chapter 2, Exercise 4)."""
import math


def mgf_normal(t, mu, sigma2):
    return math.exp(mu * t + sigma2 * t * t / 2.0)


def first_derivative_at_zero(mu, sigma2, h):
    return (mgf_normal(h, mu, sigma2) - mgf_normal(-h, mu, sigma2)) / (2 * h)


def second_derivative_at_zero(mu, sigma2, h):
    m0 = mgf_normal(0.0, mu, sigma2)
    return (mgf_normal(h, mu, sigma2) - 2 * m0 + mgf_normal(-h, mu, sigma2)) / (h * h)


def variance_from_derivatives(mu, sigma2, h):
    d1 = first_derivative_at_zero(mu, sigma2, h)
    d2 = second_derivative_at_zero(mu, sigma2, h)
    return d2 - d1 * d1


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
