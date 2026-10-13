"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (in avg_negloglik and
sandwich_variance). Fix one function at a time until all tests pass.
Do not edit run_tests().
"""
# level: research
import math


def avg_negloglik(theta, data):
    # BUG: this SUMS the per-observation NLL instead of AVERAGING it -- the
    # MLE maximises the *average* log-likelihood (ch06_text.tex Section 3).
    return sum(0.5 * (x - theta) ** 2 + 0.5 * math.log(2 * math.pi) for x in data)


def fisher_scoring_mean(data, init, iters):
    n = len(data)
    theta = init
    for _ in range(iters):
        theta = theta + sum(x - theta for x in data) / n
    return theta


def naive_variance(data):
    return 1.0 / len(data)


def sandwich_variance(data, theta):
    # BUG: the sandwich is A^{-1} B A^{-1}, so divide by A twice (n^2).
    # This forgets one factor of A^{-1} and divides by n only.
    n = len(data)
    B = sum((x - theta) ** 2 for x in data)
    return B / n


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    data = [1.0, 3.0, 2.0, 6.0, 4.0, 2.0, 5.0, 1.0]  # mean 3.0, SS about mean 24
    check("fisher_scoring -> mean", fisher_scoring_mean(data, 0.0, 1), 3.0)
    check("avg NLL at 3.0", avg_negloglik(3.0, data),
          0.5 * 3.0 + 0.5 * math.log(2 * math.pi))
    check("naive var", naive_variance(data), 1.0 / 8)
    check("sandwich var", sandwich_variance(data, 3.0), 24.0 / (8 ** 2))
    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
