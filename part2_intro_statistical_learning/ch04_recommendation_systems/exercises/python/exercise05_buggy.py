"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

The ALS update is the ridge estimator p = (Q^T Q + lam I)^{-1} Q^T r
(Theorem 2.1). Two deliberate bugs (ridge_solution_2d, grad_at). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: proof


def solve2(M, v):
    (a, b), (c, d) = M
    det = a * d - b * c
    return [(d * v[0] - b * v[1]) / det, (-c * v[0] + a * v[1]) / det]


def predict(q, p):
    return q[0] * p[0] + q[1] * p[1]


def ridge_solution_2d(Q, r, lam):
    a = b = d = 0.0
    g0 = g1 = 0.0
    for q, ri in zip(Q, r):
        a += q[0] * q[0]
        b += q[0] * q[1]
        d += q[1] * q[1]
        g0 += q[0] * ri
        g1 += q[1] * ri
    # BUG: the ridge term lam*I is missing from the diagonal. This solves the
    # UNREGULARIZED normal equations, so the result is not a stationary point
    # of the penalised objective (Theorem 2.1) and the Gram matrix can be
    # singular when a user rated fewer than k items.
    M = [[a, b], [b, d]]
    return solve2(M, [g0, g1])


def objective(Q, r, p, lam):
    s = sum((ri - predict(q, p)) ** 2 for q, ri in zip(Q, r))
    return s + lam * (p[0] * p[0] + p[1] * p[1])


def grad_at(Q, r, p, lam):
    g0 = g1 = 0.0
    for q, ri in zip(Q, r):
        e = ri - predict(q, p)
        # BUG: the data-term gradient of (r - q.p)^2 is -2 (r - q.p) q;
        # this has the sign flipped, so the gradient points the wrong way.
        g0 += 2.0 * q[0] * e
        g1 += 2.0 * q[1] * e
    g0 += 2.0 * lam * p[0]
    g1 += 2.0 * lam * p[1]
    return [g0, g1]


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    Q = [[2.0, 0.0], [0.0, 1.0]]   # orthogonal items -> clean closed form
    r = [4.0, 3.0]
    lam = 1.0

    # (Q^T Q + I) = diag(5, 2), Q^T r = (8, 3)  ->  p = (1.6, 1.5)
    p = ridge_solution_2d(Q, r, lam)
    check("ridge_p0", p[0], 1.6)
    check("ridge_p1", p[1], 1.5)

    # objective at the true minimiser
    check("objective", objective(Q, r, [1.6, 1.5], lam), 7.7)

    # gradient at a fixed off-optimum point p = (1, 1): value is (-6, -2)
    g = grad_at(Q, r, [1.0, 1.0], lam)
    check("grad0", g[0], -6.0)
    check("grad1", g[1], -2.0)

    # Theorem 2.1: the ALS update is a stationary point -- grad at it is ~0
    gstar = grad_at(Q, r, p, lam)
    check("optimality_0", gstar[0], 0.0, tol=1e-6)
    check("optimality_1", gstar[1], 0.0, tol=1e-6)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
