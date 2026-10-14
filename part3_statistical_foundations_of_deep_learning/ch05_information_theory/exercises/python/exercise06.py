"""
Chapter 5 exercise -- the decomposition and Gibbs' inequality (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch05_text.tex Section 1.
  - identity_residual : cross_entropy(p,q) - entropy(p) - kl(p,q), which the
                        decomposition H(p,q) = H(p) + KL(p||q) forces to be 0.
  - kl_is_nonneg      : True iff KL(p||q) >= 0 (Gibbs' inequality).
  - log_bound_gap     : (t - 1) - log(t), the inequality log t <= t-1 that
                        powers the Gibbs proof; it is >= 0 for all t > 0.

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: proof
import math


def _entropy(p):
    return -sum(pi * math.log(pi) for pi in p)


def _cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q))


def _kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))


def identity_residual(p, q):
    """cross_entropy(p,q) - entropy(p) - kl(p,q)  (must be ~0)."""
    raise NotImplementedError("TODO: identity_residual")


def kl_is_nonneg(p, q):
    """True iff KL(p||q) >= 0 (allow tiny negative numerical slack)."""
    raise NotImplementedError("TODO: kl_is_nonneg")


def log_bound_gap(t):
    """(t - 1) - log(t): the slack in log t <= t - 1, always >= 0."""
    raise NotImplementedError("TODO: log_bound_gap")


def main():
    p = [0.2, 0.3, 0.5]; q = [0.3, 0.4, 0.3]
    print("identity_residual:", identity_residual(p, q))
    print("kl_is_nonneg     :", kl_is_nonneg(p, q))
    print("log_bound_gap(2) :", log_bound_gap(2.0))
    print("log_bound_gap(1) :", log_bound_gap(1.0))


if __name__ == "__main__":
    main()
