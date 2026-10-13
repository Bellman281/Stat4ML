"""Chapter 3 -- reference solution (Research)."""
# level: research
import math


def chi1_from_normal_pdf(y):
    return (1.0 / math.sqrt(2 * math.pi * y)) * math.exp(-y / 2)


def two_branch_pdf(fx_root1, fx_root2, gprime_abs):
    return (fx_root1 + fx_root2) / gprime_abs


def jacobian_det_2d(a, b, c, d):
    return abs(a * d - b * c)


def main():
    print("chi2_1 pdf at 1 :", chi1_from_normal_pdf(1.0))
    print("two_branch      :", two_branch_pdf(0.2, 0.2, 4.0))
    print("jacobian det    :", jacobian_det_2d(1, 2, 3, 4))


if __name__ == "__main__":
    main()
