"""
Chapter 5 exercise -- Convergence (Core)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch05_text.tex Section 1 -- the sample
mean's variance sigma^2/n, Chebyshev's bound, and the standardized sample
mean of the central limit theorem.

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: core
import math


def var_of_sample_mean(sigma2, n):
    """Variance of the sample mean of n iid observations: sigma^2 / n."""
    raise NotImplementedError("TODO: var_of_sample_mean")


def chebyshev_bound(sigma2, n, eps):
    """Chebyshev bound on P(|Xbar_n - mu| >= eps): sigma^2 / (n * eps^2)."""
    raise NotImplementedError("TODO: chebyshev_bound")


def running_mean(data):
    """Cumulative means [x1, (x1+x2)/2, ...] -- the law of large numbers in
    action as more data arrive."""
    raise NotImplementedError("TODO: running_mean")


def clt_standardized(xbar, mu, sigma, n):
    """The CLT's standardized sample mean: (xbar - mu) / (sigma / sqrt(n))."""
    raise NotImplementedError("TODO: clt_standardized")


def main():
    print("Var(Xbar) sigma2=4,n=100 :", var_of_sample_mean(4.0, 100))
    print("Chebyshev bound           :", chebyshev_bound(4.0, 100, 0.5))
    print("running mean of [2,4,6]   :", running_mean([2, 4, 6]))
    print("standardized (1.6,1,2,100):", clt_standardized(1.6, 1.0, 2.0, 100))


if __name__ == "__main__":
    main()
