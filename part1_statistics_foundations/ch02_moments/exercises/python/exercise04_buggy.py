"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 4
Part I: Statistics Foundation for ML

Three deliberate bugs are hiding below (in first_derivative_at_zero,
second_derivative_at_zero, and variance_from_derivatives). Run this
file, read the first failing assertion, fix ONLY that function, and
re-run -- repeat until you see "All tests passed!". Do not edit
run_tests().
"""
import math


def mgf_normal(t, mu, sigma2):
    # Correct.
    return math.exp(mu * t + sigma2 * t * t / 2.0)


def first_derivative_at_zero(mu, sigma2, h):
    # BUG: forgets the factor of 2 in the central-difference denominator
    # -- divides by h instead of 2h, so the result is exactly double the
    # true derivative.
    return (mgf_normal(h, mu, sigma2) - mgf_normal(-h, mu, sigma2)) / h


def second_derivative_at_zero(mu, sigma2, h):
    # BUG: forgets the "-2*M(0)" term in the central second-difference
    # formula.
    return (mgf_normal(h, mu, sigma2) + mgf_normal(-h, mu, sigma2)) / (h * h)


def variance_from_derivatives(mu, sigma2, h):
    # BUG: forgets to subtract (E[X])^2 -- returns E[X^2] directly
    # instead of Var(X) = E[X^2] - (E[X])^2.
    d2 = second_derivative_at_zero(mu, sigma2, h)
    return d2


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol):
        ok = abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    mu, sigma2, h = 2.0, 4.0, 1e-4

    d1 = first_derivative_at_zero(mu, sigma2, h)
    check("first_derivative_at_zero ~= mu", d1, mu, tol=1e-3)

    d2 = second_derivative_at_zero(mu, sigma2, h)
    check("second_derivative_at_zero ~= sigma2+mu^2", d2, sigma2 + mu * mu, tol=1e-2)

    var = variance_from_derivatives(mu, sigma2, h)
    check("variance_from_derivatives ~= sigma2", var, sigma2, tol=1e-2)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
