"""
Chapter 7 exercise -- Conjugacy, prediction, Bernstein-von Mises (Research tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch07_text.tex Sections 1 and 3 (the
Gamma-Poisson update, the posterior-predictive success probability, and the
Bernstein-von Mises posterior spread).

Run with:  python3 exercise09.py
Reference solution: solutions/exercise09_solution.py
"""
# level: research
import math


def gamma_poisson_posterior(a, b, total, n):
    """Gamma(a,b) prior + Poisson data: posterior (a + total, b + n)
    in (shape, rate)."""
    raise NotImplementedError("TODO: gamma_poisson_posterior")


def posterior_predictive_next_success(alpha, beta):
    """For a Beta(alpha, beta) posterior on p, P(next trial is a success)
    equals the posterior mean alpha / (alpha + beta)."""
    raise NotImplementedError("TODO: posterior_predictive_next_success")


def bvm_posterior_sd(fisher_info_n):
    """Bernstein-von Mises: large-n posterior sd is 1 / sqrt(I_n)."""
    raise NotImplementedError("TODO: bvm_posterior_sd")


def main():
    print("gamma-poisson post :", gamma_poisson_posterior(2, 1, 30, 10))
    print("predictive success :", posterior_predictive_next_success(9, 3))
    print("BvM posterior sd   :", bvm_posterior_sd(100))


if __name__ == "__main__":
    main()
