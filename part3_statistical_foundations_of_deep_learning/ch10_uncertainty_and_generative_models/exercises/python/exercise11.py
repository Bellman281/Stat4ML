"""
Chapter 10 exercise -- the conformal coverage quantile (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch10_text.tex Section 1. From calibration
scores, take the rank-k value (k = ceil((n+1)(1-alpha))) as the threshold q; then
the empirical coverage on fresh scores should meet the 1-alpha guarantee.
  - conformal_q       : the k-th smallest calibration score (k capped at n -> +inf).
  - empirical_coverage: fraction of test scores <= q.
  - guarantee_holds   : True iff empirical_coverage >= 1 - alpha (small slack).

Run with:  python3 exercise11.py
Reference solution: solutions/exercise11_solution.py
"""
# level: proof
import math


def conformal_q(cal_scores, alpha):
    """The conformal threshold: the k-th smallest score, k = ceil((n+1)(1-alpha));
    if k > n return +inf (the set is all of R)."""
    raise NotImplementedError("TODO: conformal_q")


def empirical_coverage(test_scores, q):
    """Fraction of test scores that are <= q."""
    raise NotImplementedError("TODO: empirical_coverage")


def guarantee_holds(cov, alpha):
    """True iff cov >= 1 - alpha (allow tiny numerical slack)."""
    raise NotImplementedError("TODO: guarantee_holds")


def main():
    cal = [0.2, 0.4, 0.6, 0.8, 1.0]
    q = conformal_q(cal, 0.2)
    print("conformal_q       :", q)
    cov = empirical_coverage([0.5, 0.9, 1.5, 0.1, 0.7], q)
    print("empirical_coverage:", cov)
    print("guarantee_holds   :", guarantee_holds(cov, 0.2))


if __name__ == "__main__":
    main()
