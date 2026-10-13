"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part I: Statistics Foundation for ML

Two deliberate bugs (normal_posterior_mean, normal_posterior_var). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: proof
def normal_posterior_precision(tau2, sigma2, n):
    return 1 / tau2 + n / sigma2


def normal_posterior_mean(mu0, tau2, xbar, sigma2, n):
    # BUG: the weighted sum must be divided by the posterior precision
    # (ch07_text.tex Section 2); this returns the unnormalised numerator.
    return mu0 / tau2 + n * xbar / sigma2


def normal_posterior_var(tau2, sigma2, n):
    # BUG: the variance is 1 / precision, not the precision itself.
    return normal_posterior_precision(tau2, sigma2, n)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("precision", normal_posterior_precision(1.0, 1.0, 10), 11.0)
    check("mean", normal_posterior_mean(0.0, 1.0, 2.0, 1.0, 10), 20.0 / 11.0)
    check("variance", normal_posterior_var(1.0, 1.0, 10), 1.0 / 11.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
