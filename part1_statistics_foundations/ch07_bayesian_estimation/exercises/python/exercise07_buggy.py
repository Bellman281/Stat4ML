"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part I: Statistics Foundation for ML

Two deliberate bugs (beta_binomial_posterior, beta_map). Fix one function
at a time until all tests pass. Do not edit run_tests().
"""
# level: core
def beta_binomial_posterior(alpha, beta, k, n):
    # BUG: the second parameter is beta + (n - k) -- the failures -- not
    # beta + n (ch07_text.tex Section 1).
    return (alpha + k, beta + n)


def posterior_mean(alpha, beta):
    return alpha / (alpha + beta)


def beta_map(alpha, beta):
    # BUG: the mode numerator is (alpha - 1), not alpha.
    return alpha / (alpha + beta - 2)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    a, b = beta_binomial_posterior(1, 1, 8, 10)
    check("posterior alpha", a, 9)
    check("posterior beta", b, 3)
    check("posterior_mean", posterior_mean(9, 3), 0.75)
    check("beta_map", beta_map(9, 3), 0.8)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
