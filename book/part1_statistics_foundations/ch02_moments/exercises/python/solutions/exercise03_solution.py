"""Reference solution for exercise03.py (Chapter 2, Exercise 3)."""


def var_sum_two(a, b, var_x, var_y, cov_xy):
    return a * a * var_x + b * b * var_y + 2 * a * b * cov_xy


def cov_matrix_2x2(var_x, var_y, cov_xy):
    return [[var_x, cov_xy], [cov_xy, var_y]]


def matvec(M, v):
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]


def var_linear_combo(a_vec, cov_matrix):
    sv = matvec(cov_matrix, a_vec)
    return a_vec[0] * sv[0] + a_vec[1] * sv[1]


def transpose2x2(M):
    return [[M[0][0], M[1][0]], [M[0][1], M[1][1]]]


def matmul2x2(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transform_covariance(R, sigma):
    return matmul2x2(matmul2x2(R, sigma), transpose2x2(R))


def main():
    var_x, var_y, cov_xy = 2.0, 3.0, 0.5
    a, b = 1.5, -2.0

    direct = var_sum_two(a, b, var_x, var_y, cov_xy)
    print(f"Var({a}X + ({b})Y) directly = {direct}")

    sigma = cov_matrix_2x2(var_x, var_y, cov_xy)
    print(f"Cov(X) = {sigma}")
    via_matrix = var_linear_combo([a, b], sigma)
    print(f"a^T Sigma a = {via_matrix}  -- should match the direct formula above")

    R = [[1.0, 0.0], [1.0, 1.0]]
    result = transform_covariance(R, sigma)
    print(f"R Sigma R^T = {result}  -- Cov(Y1,Y2) should be Var(X1)+Cov(X1,X2)")


if __name__ == "__main__":
    main()
