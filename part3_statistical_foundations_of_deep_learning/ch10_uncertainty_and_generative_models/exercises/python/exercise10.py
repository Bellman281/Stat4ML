"""
Chapter 10 exercise -- conformal and calibration primitives (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch10_text.tex Sections 1-2.
  - nonconformity : the absolute residual |y - pred|.
  - quantile_rank : the conformal rank k = ceil((n+1)(1-alpha)).
  - coverage      : fraction of points with |y - pred| <= q.

Run with:  python3 exercise10.py
Reference solution: solutions/exercise10_solution.py
"""
# level: core
import math


def nonconformity(y, pred):
    """Nonconformity score: |y - pred|."""
    raise NotImplementedError("TODO: nonconformity")


def quantile_rank(n, alpha):
    """Conformal rank: ceil((n + 1) * (1 - alpha))."""
    raise NotImplementedError("TODO: quantile_rank")


def coverage(ys, preds, q):
    """Fraction of points whose nonconformity is within q."""
    raise NotImplementedError("TODO: coverage")


def main():
    print("nonconformity :", nonconformity(3.0, 2.5))
    print("quantile_rank :", quantile_rank(99, 0.1))
    print("coverage      :", coverage([1.0, 2.0, 3.0], [1.0, 2.0, 5.0], 1.0))


if __name__ == "__main__":
    main()
