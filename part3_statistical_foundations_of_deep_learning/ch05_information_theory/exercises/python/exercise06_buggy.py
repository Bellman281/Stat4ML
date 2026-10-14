"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (identity_residual, log_bound_gap). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: proof
import math


def _entropy(p):
    return -sum(pi * math.log(pi) for pi in p)


def _cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q))


def _kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q))


def identity_residual(p, q):
    # BUG: the decomposition is H(p,q) = H(p) + KL, so the residual is
    # cross_entropy - entropy - kl; this adds entropy instead of subtracting it.
    return _cross_entropy(p, q) + _entropy(p) - _kl(p, q)


def kl_is_nonneg(p, q):
    return _kl(p, q) >= -1e-12


def log_bound_gap(t):
    # BUG: the bound is log t <= t - 1, so the gap is (t-1) - log t, not
    # log t - (t-1) (which would be <= 0).
    return math.log(t) - (t - 1)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, bool) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    p = [0.2, 0.3, 0.5]; q = [0.3, 0.4, 0.3]
    check("identity_residual", identity_residual(p, q), 0.0)
    check("kl_is_nonneg", kl_is_nonneg(p, q), True)
    check("log_bound_gap_1", log_bound_gap(1.0), 0.0)
    check("log_bound_gap_2", log_bound_gap(2.0), (2 - 1) - math.log(2))
    check("log_bound_gap_half", log_bound_gap(0.5), (0.5 - 1) - math.log(0.5))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
