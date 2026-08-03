"""
Chapter 2 exercise -- Moments
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch02_text.tex (expected value,
variance, covariance, correlation, moment generating functions) and
Python's standard library `random`/`math` modules.

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""
import math
import random


def expected_value(values, probs):
    """E[X] for a discrete random variable with support `values` and
    matching probabilities `probs` (same length, probs sums to 1)."""
    # TODO
    raise NotImplementedError("TODO: expected_value")


def variance(values, probs):
    """Var(X) = E[X^2] - (E[X])^2. Reuse expected_value; do not use a
    two-pass "E[(X-mu)^2]" loop -- the point of this exercise is the
    E[X^2] - mu^2 identity from ch02_text.tex Section 1.2."""
    # TODO
    raise NotImplementedError("TODO: variance")


def covariance(xy_values, joint_probs):
    """Cov(X,Y) = E[XY] - E[X]E[Y].
    `xy_values` is a list of (x, y) pairs; `joint_probs` is the matching
    list of P(X=x, Y=y), summing to 1. Derive the marginals of X and Y
    from the joint distribution -- do not assume X, Y independent."""
    # TODO
    raise NotImplementedError("TODO: covariance")


def correlation(cov_xy, var_x, var_y):
    """rho = Cov(X,Y) / (sigma_x * sigma_y)."""
    # TODO
    raise NotImplementedError("TODO: correlation")


def normal_mgf_theoretical(t, mu, sigma2):
    """Closed-form MGF of N(mu, sigma2): exp(mu*t + sigma2*t^2/2)."""
    # TODO
    raise NotImplementedError("TODO: normal_mgf_theoretical")


def _standard_normal_pair(rng):
    """Box-Muller transform: turn 2 uniform(0,1) draws into 2 independent
    standard-normal draws. Provided for you -- not part of the exercise."""
    u1, u2 = rng.random(), rng.random()
    u1 = max(u1, 1e-12)  # avoid log(0)
    r = math.sqrt(-2.0 * math.log(u1))
    theta = 2.0 * math.pi * u2
    return r * math.cos(theta), r * math.sin(theta)


def normal_mgf_monte_carlo(t, mu, sigma2, n, seed=0):
    """Estimate E[e^{tX}] for X ~ N(mu, sigma2) by sampling `n` draws of X
    (via _standard_normal_pair, scaled/shifted to N(mu, sigma2)) and
    averaging e^{t*x}."""
    # TODO: seed an rng, draw n samples of X = mu + sqrt(sigma2)*Z where Z
    # is standard normal (use _standard_normal_pair, which returns 2 at a
    # time), and return the average of exp(t * x) over all n samples.
    raise NotImplementedError("TODO: normal_mgf_monte_carlo")


def main():
    xs = [0, 1, 2, 3]
    ps = [1 / 8, 3 / 8, 3 / 8, 1 / 8]  # Binomial(3, 0.5)
    mu = expected_value(xs, ps)
    var = variance(xs, ps)
    print(f"E[X] = {mu}, Var(X) = {var}  (Binomial(3, 0.5): expect mean 1.5, var 0.75)")

    xy = [(0, 0), (0, 1), (1, 0), (1, 1)]
    joint = [0.4, 0.1, 0.1, 0.4]  # positively associated
    cov = covariance(xy, joint)
    ex = expected_value([0, 1], [0.5, 0.5])
    var_x = variance([0, 1], [0.5, 0.5])
    print(f"Cov(X,Y) = {cov}, corr = {correlation(cov, var_x, var_x)}")

    mu_n, sigma2_n, t = 2.0, 4.0, 0.4
    theo = normal_mgf_theoretical(t, mu_n, sigma2_n)
    mc = normal_mgf_monte_carlo(t, mu_n, sigma2_n, 200_000, seed=7)
    print(f"Normal MGF at t={t}: theoretical={theo:.5f}, Monte Carlo={mc:.5f}")


if __name__ == "__main__":
    main()
