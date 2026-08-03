"""
Chapter 0 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 2
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding in lu_decompose_2x2 (wrong pivot for l21,
and a u22 that forgets to subtract the update term). Run this file, read
the first failing assertion, fix ONLY that bug, and re-run -- repeat
until you see "All tests passed!". Do not edit run_tests().
"""


def matmul(A, B):
    # Correct.
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def lu_decompose_2x2(A):
    a11, a12 = A[0]
    a21, a22 = A[1]
    u11, u12 = a11, a12
    # BUG: divides by a22 (the wrong pivot) instead of a11 -- see
    # ch00_text.tex Section 6.1, l21 = a21 / a11.
    l21 = a21 / a22
    # BUG: forgets to subtract l21 * u12 -- returns a22 unchanged instead
    # of the Schur-complement update u22 = a22 - l21 * u12.
    u22 = a22
    L = [[1.0, 0.0], [l21, 1.0]]
    U = [[u11, u12], [0.0, u22]]
    return L, U


def reconstruct(L, U):
    # Correct.
    return matmul(L, U)


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(expected, list):
            ok = all(abs(g - e) < tol for grow, erow in zip(got, expected) for g, e in zip(grow, erow))
        else:
            ok = abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    A = [[4.0, 3.0], [6.0, 3.0]]
    L, U = lu_decompose_2x2(A)
    check("L", L, [[1.0, 0.0], [1.5, 1.0]])
    check("U", U, [[4.0, 3.0], [0.0, -1.5]])
    check("reconstruct(L, U) == A", reconstruct(L, U), A)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
