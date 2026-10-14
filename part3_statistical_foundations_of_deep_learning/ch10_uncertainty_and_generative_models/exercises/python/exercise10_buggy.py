"""
Chapter 10 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (nonconformity, coverage). Fix one function at a time until
all tests pass. Do not edit run_tests().
"""
# level: core
import math


def nonconformity(y, pred):
    # BUG: the nonconformity score is the ABSOLUTE residual |y - pred|.
    return y - pred


def quantile_rank(n, alpha):
    return math.ceil((n + 1) * (1 - alpha))


def coverage(ys, preds, q):
    # BUG: a point is covered when its nonconformity is <= q, not > q.
    return sum(1 for y, p in zip(ys, preds) if abs(y - p) > q) / len(ys)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, int) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("nonconformity", nonconformity(3.0, 2.5), 0.5)
    check("nonconformity_neg", nonconformity(2.0, 3.0), 1.0)
    check("quantile_rank", quantile_rank(99, 0.1), 90)
    check("coverage", coverage([1.0, 2.0, 3.0], [1.0, 2.0, 5.0], 1.0), 2.0 / 3.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
