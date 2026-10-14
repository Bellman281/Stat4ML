"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (ou_stationary_var, polyak_var). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: research


def ou_stationary_var(lr, sigma2, H):
    # BUG: the stationary variance is lr*sigma2 / (2H); the factor 2 is missing.
    return lr * sigma2 / H


def critical_lr(H):
    return 2.0 / H


def polyak_var(stationary_var, k):
    # BUG: averaging k iterates DIVIDES the variance by k, it does not multiply.
    return stationary_var * k


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-12):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    v = ou_stationary_var(0.1, 1.0, 2.0)
    check("ou_stationary_var", v, 0.025)
    check("critical_lr", critical_lr(2.0), 1.0)
    check("polyak_var", polyak_var(0.025, 10), 0.0025)
    # noise ball is linear in the step: doubling lr doubles the variance
    check("linear in lr", ou_stationary_var(0.2, 1.0, 2.0), 2 * ou_stationary_var(0.1, 1.0, 2.0))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
