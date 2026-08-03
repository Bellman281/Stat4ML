"""Reference solution for exercise02.py (Chapter 0, Exercise 2)."""


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def lu_decompose_2x2(A):
    a11, a12 = A[0]
    a21, a22 = A[1]
    u11, u12 = a11, a12
    l21 = a21 / a11
    u22 = a22 - l21 * u12
    L = [[1.0, 0.0], [l21, 1.0]]
    U = [[u11, u12], [0.0, u22]]
    return L, U


def reconstruct(L, U):
    return matmul(L, U)


def main():
    A = [[4.0, 3.0], [6.0, 3.0]]
    L, U = lu_decompose_2x2(A)
    print(f"L = {L}")
    print(f"U = {U}")
    A_check = reconstruct(L, U)
    print(f"L @ U = {A_check}  -- should equal A = {A}")


if __name__ == "__main__":
    main()
