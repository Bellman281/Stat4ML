"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (two_branch_pdf, jacobian_det_2d).
Fix one function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
import math


def chi1_from_normal_pdf(y):
    return (1.0 / math.sqrt(2 * math.pi * y)) * math.exp(-y / 2)


def two_branch_pdf(fx_root1, fx_root2, gprime_abs):
    # BUG: a non-monotone transform collects BOTH roots; this keeps only one
    # (ch03_text.tex Section 3).
    return fx_root1 / gprime_abs


def jacobian_det_2d(a, b, c, d):
    # BUG: the determinant is a*d - b*c, not a*d + b*c.
    return abs(a * d + b * c)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("chi1_from_normal_pdf(1)", chi1_from_normal_pdf(1.0),
          (1.0 / math.sqrt(2 * math.pi)) * math.exp(-0.5))
    check("two_branch_pdf", two_branch_pdf(0.2, 0.2, 4.0), 0.1)
    check("jacobian_det_2d", jacobian_det_2d(1, 2, 3, 4), 2.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
