"""Reference solution for exercise01.py (Chapter 0, Exercise 1)."""


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def transpose(A):
    rows, cols = len(A), len(A[0])
    return [[A[i][j] for i in range(rows)] for j in range(cols)]


def det2x2(A):
    a, b = A[0]
    c, d = A[1]
    return a * d - b * c


def inverse2x2(A):
    d_ = det2x2(A)
    a, b = A[0]
    c, d = A[1]
    return [[d / d_, -b / d_], [-c / d_, a / d_]]


def identity2x2():
    return [[1.0, 0.0], [0.0, 1.0]]


def main():
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]

    AB = matmul(A, B)
    print(f"AB = {AB}")

    lhs = transpose(AB)
    rhs = matmul(transpose(B), transpose(A))
    print(f"(AB)^T = {lhs}, B^T A^T = {rhs}  -- should match (Theorem 4.1)")

    dA, dB, dAB = det2x2(A), det2x2(B), det2x2(AB)
    print(f"det(A)*det(B) = {dA * dB}, det(AB) = {dAB}  -- should match (Theorem 2.1.8)")

    invA = inverse2x2(A)
    check = matmul(A, invA)
    print(f"A @ A^-1 = {check}  -- should be the 2x2 identity")


if __name__ == "__main__":
    main()
