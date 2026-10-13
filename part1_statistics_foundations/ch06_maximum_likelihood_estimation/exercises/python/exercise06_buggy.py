"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (in bernoulli_loglik and normal_mle).
Run this file, read the first failing check, fix ONLY that function, and
re-run until you see "All tests passed!". Do not edit run_tests().
"""
# level: core
import math


def bernoulli_loglik(p, data):
    # BUG: drops the (1-x)*log(1-p) term -- only counts the successes.
    # See the Bernoulli example in ch06_text.tex Section 1.
    return sum(x * math.log(p) for x in data)


def bernoulli_mle(data):
    return sum(data) / len(data)


def poisson_mle(data):
    return sum(data) / len(data)


def normal_mle(data):
    # BUG: the MLE of sigma^2 divides by n, not n-1 (editorial note,
    # ch06_text.tex Section 1). This returns the unbiased estimator instead.
    n = len(data)
    mu = sum(data) / n
    sigma2 = sum((x - mu) ** 2 for x in data) / (n - 1)
    return (mu, sigma2)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    b = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    check("bernoulli_mle", bernoulli_mle(b), 0.6)
    check("bernoulli_loglik(0.6)", bernoulli_loglik(0.6, b),
          6 * math.log(0.6) + 4 * math.log(0.4))
    check("poisson_mle", poisson_mle([2, 1, 3, 0, 2, 1, 4, 2]), 1.875)
    mu, s2 = normal_mle([2, 4, 4, 4, 5, 5, 7, 9])
    check("normal_mle mu", mu, 5.0)
    check("normal_mle sigma2 (/n)", s2, 4.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
