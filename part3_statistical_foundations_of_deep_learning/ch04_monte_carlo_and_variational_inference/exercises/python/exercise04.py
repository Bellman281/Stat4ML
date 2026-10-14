"""
Chapter 4 exercise -- Monte Carlo estimation (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch04_text.tex Section 1. The MC estimate of
E[f] is the sample average; its standard error is sigma/sqrt(n) with sigma the
(population) standard deviation of the f-values.
  - mc_estimate       : the sample mean of the f-values.
  - mc_variance       : the population variance (1/n) sum (f - mean)^2.
  - mc_standard_error : sqrt(mc_variance / n).

Run with:  python3 exercise04.py
Reference solution: solutions/exercise04_solution.py
"""
# level: core
import math


def mc_estimate(fvals):
    """Monte Carlo estimate of E[f]: the sample mean."""
    raise NotImplementedError("TODO: mc_estimate")


def mc_variance(fvals):
    """Population variance of the f-values: (1/n) sum (f - mean)^2."""
    raise NotImplementedError("TODO: mc_variance")


def mc_standard_error(fvals):
    """Standard error of the MC estimate: sqrt(mc_variance / n)."""
    raise NotImplementedError("TODO: mc_standard_error")


def main():
    f = [2, 4, 4, 4, 5, 5, 7, 9]   # mean 5, population variance 4
    print("mc_estimate       :", mc_estimate(f))
    print("mc_variance       :", mc_variance(f))
    print("mc_standard_error :", mc_standard_error(f))


if __name__ == "__main__":
    main()
