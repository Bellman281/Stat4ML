"""
Chapter 1 exercise 2 -- Random variables: PMF, CDF, and change of variables
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch01_text.tex Sections 5-6
(random variables, CDFs, densities, and the change-of-variables /
inverse-transform-sampling example with Y = -log(X)).

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""
import math
import random


def pmf_three_coins(x):
    """P(X = x) for X = number of heads in 3 fair coin tosses, x in
    {0,1,2,3}. See ch01_text.tex Section 5, the three-fair-coins example:
    P(X=x) = C(3,x) * (1/2)^3."""
    # TODO
    raise NotImplementedError("TODO: pmf_three_coins")


def cdf_three_coins(x):
    """F_X(x) = P(X <= x), built from pmf_three_coins. Match the table in
    ch01_text.tex Section 6.1 exactly (0 for x<0, 1/8 for 0<=x<1, ...,
    1 for x>=3)."""
    # TODO
    raise NotImplementedError("TODO: cdf_three_coins")


def inverse_transform_sample(u):
    """Given u ~ Uniform(0,1), return y = -log(u), which is
    Exponential(1)-distributed (ch01_text.tex Section 8, the
    inverse-transform-sampling example)."""
    # TODO
    raise NotImplementedError("TODO: inverse_transform_sample")


def exponential_pdf(y):
    """f_Y(y) = e^{-y} for y >= 0, else 0 -- the density obtained via the
    change-of-variables theorem in ch01_text.tex Section 8. Provided for
    you -- not part of this exercise."""
    return math.exp(-y) if y >= 0 else 0.0


def main():
    total = sum(pmf_three_coins(x) for x in range(4))
    print(f"sum of pmf over x=0..3: {total}  (should be 1.0)")

    print(f"F_X(2.5) = {cdf_three_coins(2.5)}  (should be 7/8 = 0.875)")
    print(f"F_X(-1) = {cdf_three_coins(-1)}, F_X(3.5) = {cdf_three_coins(3.5)}")

    rng = random.Random(7)
    n = 200_000
    samples = [inverse_transform_sample(max(rng.random(), 1e-12)) for _ in range(n)]
    mean = sum(samples) / n
    print(f"mean of {n} inverse-transform samples: {mean:.4f}  (Exponential(1) mean is 1.0)")


if __name__ == "__main__":
    main()
