"""
Chapter 0 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 1
Part I: Statistics Foundation for ML

Three deliberate bugs are hiding below (in transpose, det2x2, and
inverse2x2). Run this file, read the first failing assertion, fix ONLY
that function, and re-run -- repeat until you see "All tests passed!".
Do not edit run_tests().
"""


def matmul(A, B):
    # Correct.
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def transpose(A):
    # BUG: returns A unchanged -- forgets to actually swap row/column
    # indices (see ch00_text.tex Definition 4.1).
    return [row[:] for row in A]


def det2x2(A):
    # BUG: computes a*d + b*c instead of a*d - b*c (sign error on the
    # bc term -- see ch00_text.tex Section 2).
    a, b = A[0]
    c, d = A[1]
    return a * d + b * c


def inverse2x2(A):
    # BUG: forgets to divide by det(A) -- returns just the adjugate
    # matrix [[d, -b], [-c, a]] (see ch00_text.tex Section 3).
    a, b = A[0]
    c, d = A[1]
    return [[d, -b], [-c, a]]


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

    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]
    AB = matmul(A, B)
    check("matmul(A,B)", AB, [[19.0, 22.0], [43.0, 50.0]])

    lhs = transpose(AB)
    rhs = matmul(transpose(B), transpose(A))
    check("(AB)^T == B^T A^T", lhs, rhs)

    dA, dB, dAB = det2x2(A), det2x2(B), det2x2(AB)
    check("det(A)*det(B) == det(AB)", dA * dB, dAB)

    invA = inverse2x2(A)
    check_mat = matmul(A, invA)
    check("A @ inverse(A) == I", check_mat, [[1.0, 0.0], [0.0, 1.0]])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
