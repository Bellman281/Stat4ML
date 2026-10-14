"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (bernoulli_score, mle_mean). Fix one function at a time
until all tests pass. Do not edit run_tests(). The last test checks that the
total Gaussian score vanishes at mle_mean.
"""
# level: research


def gaussian_score(y, mu, sigma2):
    return (y - mu) / sigma2


def bernoulli_score(y, p):
    # BUG: the score is (y - p) / (p(1-p)); this divides by p only.
    return (y - p) / p


def mle_mean(ys):
    # BUG: the score equation sum_i (y_i - mu) = 0 solves to the MEAN, not the
    # sum; divide by len(ys).
    return sum(ys)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    ys = [2.0, 4.0, 6.0]
    check("gaussian_score", gaussian_score(3.0, 1.0, 2.0), 1.0)
    check("bernoulli_score", bernoulli_score(1, 0.5), 2.0)
    check("mle_mean", mle_mean(ys), 4.0)
    check("score zero at mle", sum(gaussian_score(y, mle_mean(ys), 1.0) for y in ys), 0.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
