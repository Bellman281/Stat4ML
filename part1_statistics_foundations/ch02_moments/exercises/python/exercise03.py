"""
Chapter 2 exercise 3 -- Variance of linear combinations, matrix covariance
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch02_text.tex Section 2 (Var(aX+bY))
and Section 4 (matrix notation for moments: Cov(X), Var(a^T X) = a^T Sigma a,
Var(RX) = R Sigma R^T).

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""


def var_sum_two(a, b, var_x, var_y, cov_xy):
    """Var(aX + bY) = a^2 Var(X) + b^2 Var(Y) + 2ab Cov(X,Y).
    See ch02_text.tex Section 2, Theorem 3."""
    # TODO
    raise NotImplementedError("TODO: var_sum_two")


def cov_matrix_2x2(var_x, var_y, cov_xy):
    """Build Cov(X) = [[Var(X1), Cov(X1,X2)], [Cov(X1,X2), Var(X2)]].
    See ch02_text.tex Section 4."""
    # TODO
    raise NotImplementedError("TODO: cov_matrix_2x2")


def matvec(M, v):
    """M @ v for a 2x2 matrix M and length-2 vector v. Provided for you."""
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]


def var_linear_combo(a_vec, cov_matrix):
    """Var(a^T X) = a^T Sigma a, for a length-2 vector a_vec and 2x2
    covariance matrix cov_matrix. See ch02_text.tex Section 4."""
    # TODO
    raise NotImplementedError("TODO: var_linear_combo")


def transform_covariance(R, sigma):
    """Var(RX) = R Sigma R^T, for 2x2 matrices R and sigma. See
    ch02_text.tex Section 4 (the "linear layer transforms covariance"
    identity)."""
    # TODO
    raise NotImplementedError("TODO: transform_covariance")


def main():
    var_x, var_y, cov_xy = 2.0, 3.0, 0.5
    a, b = 1.5, -2.0

    direct = var_sum_two(a, b, var_x, var_y, cov_xy)
    print(f"Var({a}X + ({b})Y) directly = {direct}")

    sigma = cov_matrix_2x2(var_x, var_y, cov_xy)
    print(f"Cov(X) = {sigma}")
    via_matrix = var_linear_combo([a, b], sigma)
    print(f"a^T Sigma a = {via_matrix}  -- should match the direct formula above")

    R = [[1.0, 0.0], [1.0, 1.0]]  # Y1 = X1, Y2 = X1 + X2
    result = transform_covariance(R, sigma)
    print(f"R Sigma R^T = {result}  -- Cov(Y1,Y2) should be Var(X1)+Cov(X1,X2)")


if __name__ == "__main__":
    main()
