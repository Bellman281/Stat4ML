"""
Chapter 3 exercise -- Distribution functions (Core)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch03_text.tex Section 1 (the cdf and
density of the exponential, and inverse-transform sampling).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
# level: core
import math


def exponential_cdf(x, rate):
    """F(x) = 1 - exp(-rate * x) for x >= 0."""
    raise NotImplementedError("TODO: exponential_cdf")


def exponential_pdf(x, rate):
    """f(x) = rate * exp(-rate * x) for x >= 0."""
    raise NotImplementedError("TODO: exponential_pdf")


def inverse_transform_exponential(u, rate):
    """F^{-1}(u) = -log(1 - u) / rate -- turns a uniform u into an
    Exponential(rate) draw."""
    raise NotImplementedError("TODO: inverse_transform_exponential")


def empirical_cdf(data, x):
    """Fraction of the data <= x."""
    raise NotImplementedError("TODO: empirical_cdf")


def main():
    print("F(ln2, rate=1) :", exponential_cdf(math.log(2), 1.0))
    print("f(0, rate=1)   :", exponential_pdf(0.0, 1.0))
    print("Finv(0.5)      :", inverse_transform_exponential(0.5, 1.0))
    print("ecdf at 2.5    :", empirical_cdf([1, 2, 3, 4], 2.5))


if __name__ == "__main__":
    main()
