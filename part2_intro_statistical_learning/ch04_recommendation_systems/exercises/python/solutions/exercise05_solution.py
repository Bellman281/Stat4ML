"""Chapter 4 -- reference solution (Proof): the ALS ridge update, k = 2."""
# level: proof


def solve2(M, v):
    """Solve the 2x2 system M x = v by Cramer's rule (given helper)."""
    (a, b), (c, d) = M
    det = a * d - b * c
    return [(d * v[0] - b * v[1]) / det, (-c * v[0] + a * v[1]) / det]


def predict(q, p):
    return q[0] * p[0] + q[1] * p[1]


def ridge_solution_2d(Q, r, lam):
    """ALS update: p = (Q^T Q + lam I)^{-1} Q^T r  for k = 2.
    Q is a list of rated-item factor rows (each length 2); r the ratings."""
    a = b = d = 0.0
    g0 = g1 = 0.0
    for q, ri in zip(Q, r):
        a += q[0] * q[0]
        b += q[0] * q[1]
        d += q[1] * q[1]
        g0 += q[0] * ri
        g1 += q[1] * ri
    M = [[a + lam, b], [b, d + lam]]   # Q^T Q + lam I
    return solve2(M, [g0, g1])


def objective(Q, r, p, lam):
    """sum_i (r_i - q_i.p)^2 + lam |p|^2."""
    s = sum((ri - predict(q, p)) ** 2 for q, ri in zip(Q, r))
    return s + lam * (p[0] * p[0] + p[1] * p[1])


def grad_at(Q, r, p, lam):
    """Gradient of the objective at p: -2 Q^T (r - Q p) + 2 lam p."""
    g0 = g1 = 0.0
    for q, ri in zip(Q, r):
        e = ri - predict(q, p)
        g0 += -2.0 * q[0] * e
        g1 += -2.0 * q[1] * e
    g0 += 2.0 * lam * p[0]
    g1 += 2.0 * lam * p[1]
    return [g0, g1]


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
