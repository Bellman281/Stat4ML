"""
Chapter 5 exercise -- Variance and covariance (Core)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch05_text.tex Section 1 (centering,
variance, covariance, and the variance-explained ratio).

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: core
def center(v):
    """Subtract the mean from every entry."""
    raise NotImplementedError("TODO: center")


def variance(v):
    """Population variance: mean((vi - mean)^2)."""
    raise NotImplementedError("TODO: variance")


def covariance(x, y):
    """mean((xi - xbar)(yi - ybar))."""
    raise NotImplementedError("TODO: covariance")


def variance_explained_ratio(eigvals):
    """Each eigenvalue over the sum of all eigenvalues."""
    raise NotImplementedError("TODO: variance_explained_ratio")


def main():
    print("center      :", center([1, 2, 3]))
    print("variance    :", variance([1, 2, 3]))
    print("covariance  :", covariance([1, 2, 3], [1, 2, 3]))
    print("var ratio   :", variance_explained_ratio([3, 1]))


if __name__ == "__main__":
    main()
