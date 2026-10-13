"""
Chapter 5 exercise -- CLT via the MGF, and the delta method (Research tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch05_text.tex Sections 2 and 3 (the MGF
proof of the CLT and the delta method).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: research
import math


def mgf_standard_normal(t):
    """MGF of N(0,1): exp(t^2 / 2) -- the limit the CLT drives toward."""
    raise NotImplementedError("TODO: mgf_standard_normal")


def clt_mgf_limit(t, n):
    """Approximate MGF of the standardized sum of n terms, (1 + t^2/(2n))^n,
    which converges to exp(t^2/2) as n -> infinity."""
    raise NotImplementedError("TODO: clt_mgf_limit")


def delta_method_variance(gprime, sigma2):
    """Delta-method asymptotic variance of g(theta_hat): g'(theta)^2 * sigma^2."""
    raise NotImplementedError("TODO: delta_method_variance")


def delta_method_sd(gprime, sigma2):
    """Standard-deviation form: |g'(theta)| * sqrt(sigma^2)."""
    raise NotImplementedError("TODO: delta_method_sd")


def main():
    print("MGF N(0,1) at t=0.5 :", mgf_standard_normal(0.5))
    print("CLT MGF limit t=2   :", clt_mgf_limit(2.0, 1_000_000))
    print("delta variance      :", delta_method_variance(2.0, 3.0))
    print("delta sd            :", delta_method_sd(2.0, 3.0))


if __name__ == "__main__":
    main()
