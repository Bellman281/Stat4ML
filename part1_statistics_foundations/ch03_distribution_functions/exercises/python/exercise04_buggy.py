"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (numerical_pdf, change_of_variables).
Fix one function at a time until all tests pass. Do not edit run_tests().
"""
# level: proof
import math


def numerical_pdf(cdf, x, h=1e-5):
    # BUG: a centered difference divides by 2h, not h.
    return (cdf(x + h) - cdf(x - h)) / h


def change_of_variables(fx, hprime):
    # BUG: the change-of-variables factor is the ABSOLUTE value of h'(y)
    # (a density can't be negative). This drops the absolute value.
    return fx * hprime


def square_uniform_pdf(y):
    return 1.0 / (2.0 * math.sqrt(y))


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-4):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    cdf = lambda x: 1 - math.exp(-x)
    check("numerical_pdf ~ e^-1", numerical_pdf(cdf, 1.0), math.exp(-1.0))
    check("change_of_variables", change_of_variables(2.0, -3.0), 6.0)
    check("square_uniform_pdf", square_uniform_pdf(0.25), 1.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
