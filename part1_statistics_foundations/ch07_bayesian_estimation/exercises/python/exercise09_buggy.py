"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part I: Statistics Foundation for ML

Two deliberate bugs (gamma_poisson_posterior, bvm_posterior_sd). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
import math


def gamma_poisson_posterior(a, b, total, n):
    # BUG: the rate updates by the number of observations n, not the total
    # count (ch07_text.tex Section 1).
    return (a + total, b + total)


def posterior_predictive_next_success(alpha, beta):
    return alpha / (alpha + beta)


def bvm_posterior_sd(fisher_info_n):
    # BUG: the posterior *sd* is 1/sqrt(I_n); the variance is 1/I_n. This
    # returns the variance.
    return 1 / fisher_info_n


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    sh, rt = gamma_poisson_posterior(2, 1, 30, 10)
    check("gamma-poisson shape", sh, 32)
    check("gamma-poisson rate", rt, 11)
    check("predictive success", posterior_predictive_next_success(9, 3), 0.75)
    check("BvM posterior sd", bvm_posterior_sd(100), 0.1)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
