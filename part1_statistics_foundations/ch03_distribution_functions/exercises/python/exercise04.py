"""
Chapter 3 exercise -- Change of variables (Proof tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch03_text.tex Section 2 (density as the
derivative of the cdf, and the monotone change-of-variables formula).

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: proof
import math


def numerical_pdf(cdf, x, h=1e-5):
    """Density as the derivative of the cdf, by a centered difference:
    (cdf(x+h) - cdf(x-h)) / (2h)."""
    raise NotImplementedError("TODO: numerical_pdf")


def change_of_variables(fx, hprime):
    """One-dimensional change of variables value: f_X(h(y)) * |h'(y)|."""
    raise NotImplementedError("TODO: change_of_variables")


def square_uniform_pdf(y):
    """Density of Y = X^2 when X ~ Uniform(0,1): 1 / (2*sqrt(y)) for 0<y<1."""
    raise NotImplementedError("TODO: square_uniform_pdf")


def main():
    cdf = lambda x: 1 - math.exp(-x)        # Exponential(1) cdf
    print("numerical pdf at 1 :", numerical_pdf(cdf, 1.0))   # ~ e^{-1}
    print("change_of_vars     :", change_of_variables(2.0, -3.0))
    print("square_uniform(.25):", square_uniform_pdf(0.25))


if __name__ == "__main__":
    main()
