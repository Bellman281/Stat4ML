"""
Chapter 4 exercise -- the ALS ridge update (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: ch04_text.tex Section 2 / Theorem 2.1. With the item factors fixed,
each user's factor is the ridge estimator  p = (Q^T Q + lam I)^{-1} Q^T r.
Here k = 2, so solve2() (provided) handles the 2x2 inverse for you. Implement:
  - ridge_solution_2d : build Q^T Q + lam I and Q^T r, then solve
  - objective         : sum_i (r_i - q_i.p)^2 + lam |p|^2
  - grad_at           : -2 Q^T (r - Q p) + 2 lam p

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: proof


def solve2(M, v):
    """Solve the 2x2 system M x = v by Cramer's rule (given helper)."""
    (a, b), (c, d) = M
    det = a * d - b * c
    return [(d * v[0] - b * v[1]) / det, (-c * v[0] + a * v[1]) / det]


def predict(q, p):
    return q[0] * p[0] + q[1] * p[1]


def ridge_solution_2d(Q, r, lam):
    # TODO: accumulate Q^T Q (a 2x2) and Q^T r (length 2), add lam to the
    # diagonal, then return solve2(Q^T Q + lam I, Q^T r).
    raise NotImplementedError("TODO: ridge_solution_2d")


def objective(Q, r, p, lam):
    # TODO: sum of squared residuals over the rated items, plus lam * |p|^2
    raise NotImplementedError("TODO: objective")


def grad_at(Q, r, p, lam):
    # TODO: gradient -2 Q^T (r - Q p) + 2 lam p, returned as a length-2 list
    raise NotImplementedError("TODO: grad_at")


def main():
    Q = [[2.0, 0.0], [0.0, 1.0]]
    r = [4.0, 3.0]
    lam = 1.0
    p = ridge_solution_2d(Q, r, lam)
    print("ALS solution p :", p)
    print("objective      :", objective(Q, r, p, lam))
    print("grad at p      :", grad_at(Q, r, p, lam))


if __name__ == "__main__":
    main()
