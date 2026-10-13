"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (clt_mgf_limit, delta_method_variance).
Fix one function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
import math


def mgf_standard_normal(t):
    return math.exp(t * t / 2)


def clt_mgf_limit(t, n):
    # BUG: the term is t SQUARED over 2n, i.e. (1 + t*t/(2n))^n -- this drops
    # the square, so the limit is wrong (ch05_text.tex Section 2).
    return (1 + t / (2 * n)) ** n


def delta_method_variance(gprime, sigma2):
    # BUG: the delta-method variance has g'(theta) SQUARED (ch05 Section 3).
    return gprime * sigma2


def delta_method_sd(gprime, sigma2):
    return abs(gprime) * math.sqrt(sigma2)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("mgf_standard_normal", mgf_standard_normal(0.5), math.exp(0.125))
    check("clt_mgf_limit -> exp(2)", clt_mgf_limit(2.0, 1_000_000), math.exp(2.0), tol=1e-2)
    check("delta_method_variance", delta_method_variance(2.0, 3.0), 12.0)
    check("delta_method_sd", delta_method_sd(2.0, 3.0), math.sqrt(12.0))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
