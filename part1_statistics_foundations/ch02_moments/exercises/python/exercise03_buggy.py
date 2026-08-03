"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 3
Part I: Statistics Foundation for ML

Three deliberate bugs are hiding below (in var_sum_two, cov_matrix_2x2,
and transform_covariance). Run this file, read the first failing
assertion, fix ONLY that function, and re-run -- repeat until you see
"All tests passed!". Do not edit run_tests().
"""


def var_sum_two(a, b, var_x, var_y, cov_xy):
    # BUG: forgets the cross term "2ab*Cov(X,Y)" -- treats X and Y as if
    # independent (see ch02_text.tex Section 2, Theorem 3).
    return a * a * var_x + b * b * var_y


def cov_matrix_2x2(var_x, var_y, cov_xy):
    # BUG: swaps the diagonal entries -- puts Var(Y) where Var(X) should
    # be and vice versa (see ch02_text.tex Section 4).
    return [[var_y, cov_xy], [cov_xy, var_x]]


def matvec(M, v):
    # Correct.
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]


def var_linear_combo(a_vec, cov_matrix):
    # Correct.
    sv = matvec(cov_matrix, a_vec)
    return a_vec[0] * sv[0] + a_vec[1] * sv[1]


def transpose2x2(M):
    return [[M[0][0], M[1][0]], [M[0][1], M[1][1]]]


def matmul2x2(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transform_covariance(R, sigma):
    # BUG: forgets the trailing "@ R^T" -- returns R @ Sigma instead of
    # R @ Sigma @ R^T (see ch02_text.tex Section 4).
    return matmul2x2(R, sigma)


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

    var_x, var_y, cov_xy = 2.0, 3.0, 0.5
    a, b = 1.5, -2.0

    direct = var_sum_two(a, b, var_x, var_y, cov_xy)
    check("var_sum_two", direct, 13.5)

    sigma = cov_matrix_2x2(var_x, var_y, cov_xy)
    check("cov_matrix_2x2", sigma, [[2.0, 0.5], [0.5, 3.0]])

    via_matrix = var_linear_combo([a, b], sigma)
    check("var_linear_combo matches var_sum_two", via_matrix, 13.5)

    R = [[1.0, 0.0], [1.0, 1.0]]
    result = transform_covariance(R, sigma)
    check("transform_covariance", result, [[2.0, 2.5], [2.5, 6.0]])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
