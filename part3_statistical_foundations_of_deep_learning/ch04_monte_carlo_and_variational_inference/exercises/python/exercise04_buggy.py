"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (mc_variance, mc_standard_error). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def mc_estimate(fvals):
    return sum(fvals) / len(fvals)


def mc_variance(fvals):
    m = mc_estimate(fvals)
    n = len(fvals)
    # BUG: the population variance divides by n, not n-1.
    return sum((x - m) ** 2 for x in fvals) / (n - 1)


def mc_standard_error(fvals):
    # BUG: the standard error is the SQUARE ROOT of variance/n; the sqrt is missing.
    return mc_variance(fvals) / len(fvals)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    f = [2, 4, 4, 4, 5, 5, 7, 9]
    check("mc_estimate", mc_estimate(f), 5.0)
    check("mc_variance", mc_variance(f), 4.0)
    check("mc_standard_error", mc_standard_error(f), math.sqrt(4.0 / 8))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
