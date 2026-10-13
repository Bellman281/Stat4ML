"""
Chapter 5 exercise -- Singular values and variance explained (Research tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch05_text.tex Section 3 (cumulative
variance explained, reconstruction error, and the eigenvalue-to-singular-value
relation).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: research
import math


def cumulative_variance_explained(eigvals):
    """Running cumulative fraction of total variance:
    [l1, l1+l2, ...] / sum(eigvals)."""
    raise NotImplementedError("TODO: cumulative_variance_explained")


def reconstruction_error_ratio(eigvals, k):
    """Fraction of variance lost by keeping the top k components:
    sum(eigvals[k:]) / sum(eigvals)."""
    raise NotImplementedError("TODO: reconstruction_error_ratio")


def singular_value_from_eigenvalue(eigval):
    """Singular value of X from an eigenvalue of X^T X: sqrt(eigval)."""
    raise NotImplementedError("TODO: singular_value_from_eigenvalue")


def main():
    print("cumulative    :", cumulative_variance_explained([4, 1]))
    print("recon error   :", reconstruction_error_ratio([4, 1], 1))
    print("singular value:", singular_value_from_eigenvalue(9))


if __name__ == "__main__":
    main()
