"""
Chapter 0 exercise 3 -- Matrix Algebra Review: eigenvalues and eigenvectors
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using the 2x2 characteristic-polynomial
approach from ch00_text.tex Section 5 (Eigenvalues and Eigenvectors),
lambda^2 - trace(A) lambda + det(A) = 0.

Run with:  python3 exercise03.py
Reference solution: solutions/exercise03_solution.py
"""
import math


def trace(A):
    """Sum of the diagonal entries of A (NOT all four entries)."""
    # TODO
    raise NotImplementedError("TODO: trace")


def det2x2(A):
    a, b = A[0]
    c, d = A[1]
    return a * d - b * c


def eigenvalues_2x2(A):
    """The two roots of lambda^2 - trace(A) lambda + det(A) = 0, via the
    quadratic formula:
      lambda = (trace(A) +/- sqrt(trace(A)^2 - 4*det(A))) / 2
    Returns (lambda1, lambda2) with lambda1 >= lambda2."""
    # TODO
    raise NotImplementedError("TODO: eigenvalues_2x2")


def eigenvector_for_eigenvalue_2x2(A, lam):
    """A unit-norm eigenvector v with A v = lam v, found by solving
    (A - lam I) v = 0. If the (1,2) entry of A is nonzero, v is
    proportional to [b, lam - a] where A = [[a,b],[c,d]]; otherwise use
    [lam - d, c]. Provided for you -- not part of this exercise."""
    a, b = A[0]
    c, d = A[1]
    if abs(b) > 1e-12:
        v = [b, lam - a]
    else:
        v = [lam - d, c]
    norm = math.sqrt(v[0] ** 2 + v[1] ** 2)
    return [v[0] / norm, v[1] / norm]


def main():
    A = [[0.8, 0.3], [0.2, 0.7]]  # same example worked in ch00_text.tex
    lam1, lam2 = eigenvalues_2x2(A)
    print(f"eigenvalues = {lam1}, {lam2}  (expect 1.0 and 0.5)")
    print(f"trace(A) = {trace(A)}, sum of eigenvalues = {lam1 + lam2}")
    print(f"det(A) = {det2x2(A)}, product of eigenvalues = {lam1 * lam2}")

    v1 = eigenvector_for_eigenvalue_2x2(A, lam1)
    Av1 = [A[0][0] * v1[0] + A[0][1] * v1[1], A[1][0] * v1[0] + A[1][1] * v1[1]]
    print(f"A @ v1 = {Av1}, lambda1 * v1 = {[lam1 * x for x in v1]}  -- should match")


if __name__ == "__main__":
    main()
