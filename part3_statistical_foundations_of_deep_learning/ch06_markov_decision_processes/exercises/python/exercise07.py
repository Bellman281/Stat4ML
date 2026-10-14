"""
Chapter 6 exercise -- the Bellman contraction bound (Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch06_text.tex Section 2. Because T is a
gamma-contraction, ||V_k - V*|| <= gamma^k ||V_0 - V*||.
  - sup_norm       : max_i |v_i - u_i|.
  - geometric_bound: the error bound gamma^k * init_err.
  - num_iters_for_tol: the smallest k with gamma^k * init_err <= tol.

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: proof
import math


def sup_norm(v, u):
    """Sup-norm distance max_i |v_i - u_i|."""
    raise NotImplementedError("TODO: sup_norm")


def geometric_bound(init_err, gamma, k):
    """The contraction bound gamma^k * init_err."""
    raise NotImplementedError("TODO: geometric_bound")


def num_iters_for_tol(init_err, gamma, tol):
    """Smallest integer k with gamma^k * init_err <= tol."""
    raise NotImplementedError("TODO: num_iters_for_tol")


def main():
    print("sup_norm          :", sup_norm([1.0, 2.0, 3.0], [1.0, 2.0, 5.0]))
    print("geometric_bound   :", geometric_bound(10.0, 0.9, 2))
    print("num_iters_for_tol :", num_iters_for_tol(1.0, 0.9, 0.01))


if __name__ == "__main__":
    main()
