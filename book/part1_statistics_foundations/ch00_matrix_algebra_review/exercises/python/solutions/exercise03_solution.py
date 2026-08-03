"""Reference solution for exercise03.py (Chapter 0, Exercise 3)."""
import math


def trace(A):
    return A[0][0] + A[1][1]


def det2x2(A):
    a, b = A[0]
    c, d = A[1]
    return a * d - b * c


def eigenvalues_2x2(A):
    tr = trace(A)
    d_ = det2x2(A)
    disc = math.sqrt(tr * tr - 4 * d_)
    lam1 = (tr + disc) / 2.0
    lam2 = (tr - disc) / 2.0
    return lam1, lam2


def eigenvector_for_eigenvalue_2x2(A, lam):
    a, b = A[0]
    c, d = A[1]
    if abs(b) > 1e-12:
        v = [b, lam - a]
    else:
        v = [lam - d, c]
    norm = math.sqrt(v[0] ** 2 + v[1] ** 2)
    return [v[0] / norm, v[1] / norm]


def main():
    A = [[0.8, 0.3], [0.2, 0.7]]
    lam1, lam2 = eigenvalues_2x2(A)
    print(f"eigenvalues = {lam1}, {lam2}  (expect 1.0 and 0.5)")
    print(f"trace(A) = {trace(A)}, sum of eigenvalues = {lam1 + lam2}")
    print(f"det(A) = {det2x2(A)}, product of eigenvalues = {lam1 * lam2}")

    v1 = eigenvector_for_eigenvalue_2x2(A, lam1)
    Av1 = [A[0][0] * v1[0] + A[0][1] * v1[1], A[1][0] * v1[0] + A[1][1] * v1[1]]
    print(f"A @ v1 = {Av1}, lambda1 * v1 = {[lam1 * x for x in v1]}  -- should match")


if __name__ == "__main__":
    main()
