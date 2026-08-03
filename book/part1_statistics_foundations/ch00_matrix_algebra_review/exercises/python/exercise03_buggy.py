"""
Chapter 0 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 3
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (in trace, and in the discriminant
inside eigenvalues_2x2). Run this file, read the first failing assertion,
fix ONLY that bug, and re-run -- repeat until you see "All tests
passed!". Do not edit run_tests().
"""
import math


def trace(A):
    # BUG: sums all four entries of A instead of just the two diagonal
    # entries (see ch00_text.tex Section 5, trace(A) = a11 + a22).
    return A[0][0] + A[0][1] + A[1][0] + A[1][1]


def det2x2(A):
    # Correct.
    a, b = A[0]
    c, d = A[1]
    return a * d - b * c


def eigenvalues_2x2(A):
    tr = trace(A)
    d_ = det2x2(A)
    # BUG: discriminant should be trace(A)^2 - 4*det(A), not
    # trace(A)^2 - det(A) -- see ch00_text.tex Section 5, Theorem 5.1.
    disc = math.sqrt(tr * tr - d_)
    lam1 = (tr + disc) / 2.0
    lam2 = (tr - disc) / 2.0
    return lam1, lam2


def eigenvector_for_eigenvalue_2x2(A, lam):
    # Correct (not part of this exercise).
    a, b = A[0]
    c, d = A[1]
    if abs(b) > 1e-12:
        v = [b, lam - a]
    else:
        v = [lam - d, c]
    norm = math.sqrt(v[0] ** 2 + v[1] ** 2)
    return [v[0] / norm, v[1] / norm]


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    A = [[0.8, 0.3], [0.2, 0.7]]
    check("trace(A)", trace(A), 1.5)

    lam1, lam2 = eigenvalues_2x2(A)
    check("eigenvalues sum to trace(A)", lam1 + lam2, trace(A))
    check("eigenvalues product equals det(A)", lam1 * lam2, det2x2(A))
    check("lambda1", round(lam1, 6), 1.0)
    check("lambda2", round(lam2, 6), 0.5)

    v1 = eigenvector_for_eigenvalue_2x2(A, lam1)
    Av1_0 = A[0][0] * v1[0] + A[0][1] * v1[1]
    Av1_1 = A[1][0] * v1[0] + A[1][1] * v1[1]
    check("A@v1 component 0 == lambda1*v1 component 0", Av1_0, lam1 * v1[0])
    check("A@v1 component 1 == lambda1*v1 component 1", Av1_1, lam1 * v1[1])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
