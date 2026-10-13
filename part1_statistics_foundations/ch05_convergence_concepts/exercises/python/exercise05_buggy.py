"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (var_of_sample_mean, chebyshev_bound).
Fix one function at a time until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def var_of_sample_mean(sigma2, n):
    # BUG: the sample mean's variance is sigma^2 / n, not sigma^2 * n -- it
    # SHRINKS as n grows (ch05_text.tex Section 1).
    return sigma2 * n


def chebyshev_bound(sigma2, n, eps):
    # BUG: Chebyshev divides by eps SQUARED, not eps (ch05_text.tex Sec. 2).
    return sigma2 / (n * eps)


def running_mean(data):
    out, total = [], 0.0
    for i, x in enumerate(data, start=1):
        total += x
        out.append(total / i)
    return out


def clt_standardized(xbar, mu, sigma, n):
    return (xbar - mu) / (sigma / math.sqrt(n))


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("var_of_sample_mean", var_of_sample_mean(4.0, 100), 0.04)
    check("chebyshev_bound", chebyshev_bound(4.0, 100, 0.5), 4.0 / (100 * 0.25))
    rm = running_mean([2, 4, 6])
    check("running_mean first", rm[0], 2.0)
    check("running_mean last", rm[-1], 4.0)
    check("clt_standardized", clt_standardized(1.6, 1.0, 2.0, 100), 3.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
