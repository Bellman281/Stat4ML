"""
Chapter 3 exercise -- Non-monotone transforms and the Jacobian (Research tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch03_text.tex Section 3 (summing over
branches for a non-monotone transform, and the Jacobian determinant).

Run with:  python3 exercise05.py
Reference solution: solutions/exercise05_solution.py
"""
# level: research
import math


def chi1_from_normal_pdf(y):
    """Density of Y = Z^2 for Z ~ N(0,1): (1/sqrt(2*pi*y)) * exp(-y/2)."""
    raise NotImplementedError("TODO: chi1_from_normal_pdf")


def two_branch_pdf(fx_root1, fx_root2, gprime_abs):
    """Density of Y when g(x)=y has two roots: (f_X(x1)+f_X(x2))/|g'|."""
    raise NotImplementedError("TODO: two_branch_pdf")


def jacobian_det_2d(a, b, c, d):
    """|det| of the 2x2 Jacobian [[a,b],[c,d]] = |a*d - b*c|."""
    raise NotImplementedError("TODO: jacobian_det_2d")


def main():
    print("chi2_1 pdf at 1 :", chi1_from_normal_pdf(1.0))
    print("two_branch      :", two_branch_pdf(0.2, 0.2, 4.0))
    print("jacobian det    :", jacobian_det_2d(1, 2, 3, 4))


if __name__ == "__main__":
    main()
