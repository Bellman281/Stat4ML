"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (bernoulli_nll, gaussian_nll). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def mse(preds, targets):
    return sum((p - t) ** 2 for p, t in zip(preds, targets)) / len(targets)


def bernoulli_nll(p, y):
    # BUG: it is the NEGATIVE log-likelihood; the leading minus sign is missing.
    return y * math.log(p) + (1 - y) * math.log(1 - p)


def gaussian_nll(mu, ys, sigma):
    n = len(ys)
    const = n / 2 * math.log(2 * math.pi * sigma ** 2)
    # BUG: the quadratic term is divided by 2*sigma^2, not 2*sigma.
    return const + sum((y - mu) ** 2 for y in ys) / (2 * sigma)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("mse", mse([1, 2, 3], [1, 2, 5]), 4 / 3)
    check("bernoulli_nll", bernoulli_nll(0.8, 1), -math.log(0.8))
    expected_g = 2 / 2 * math.log(2 * math.pi * 4) + (1 + 1) / (2 * 4)
    check("gaussian_nll", gaussian_nll(0.0, [1.0, -1.0], 2.0), expected_g)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
