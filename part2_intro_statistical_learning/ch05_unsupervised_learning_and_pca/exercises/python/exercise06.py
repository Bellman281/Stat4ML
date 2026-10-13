"""
Chapter 5 exercise -- Variance maximisation and eigenvectors (Proof tier)
Part II: Introduction to Statistical Learning

HOMEWORK: implement each TODO using ch05_text.tex Section 2 (the variance of
a projection, and the top eigenvalue of a symmetric 2x2 covariance). S is a
2x2 covariance given as [[s11, s12], [s21, s22]].

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: proof
def matvec2(S, w):
    """The product S @ w for a 2x2 S and length-2 w."""
    raise NotImplementedError("TODO: matvec2")


def projected_variance(S, w):
    """Variance of the projection onto unit w: w . (S @ w)."""
    raise NotImplementedError("TODO: projected_variance")


def top_eigenvalue_2x2(S):
    """Largest eigenvalue of a symmetric 2x2 matrix:
    (tr + sqrt(tr^2 - 4*det)) / 2."""
    raise NotImplementedError("TODO: top_eigenvalue_2x2")


def main():
    S = [[2.0, 0.8], [0.8, 0.6]]
    print("matvec2       :", matvec2([[2, 0], [0, 1]], [1, 0]))
    print("proj variance :", projected_variance([[2, 0], [0, 1]], [0.6, 0.8]))
    print("top eigenvalue:", top_eigenvalue_2x2(S))


if __name__ == "__main__":
    main()
