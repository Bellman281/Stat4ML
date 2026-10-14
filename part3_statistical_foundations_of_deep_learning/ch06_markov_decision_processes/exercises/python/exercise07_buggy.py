"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (geometric_bound, num_iters_for_tol). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: proof
import math


def sup_norm(v, u):
    return max(abs(a - b) for a, b in zip(v, u))


def geometric_bound(init_err, gamma, k):
    # BUG: the contraction compounds MULTIPLICATIVELY: gamma^k, not gamma*k.
    return init_err * gamma * k


def num_iters_for_tol(init_err, gamma, tol):
    if init_err <= tol:
        return 0
    # BUG: we need gamma^k * init_err <= tol, so k must be rounded UP (ceil);
    # floor can leave the error above tolerance.
    return max(0, math.floor(math.log(tol / init_err) / math.log(gamma)))


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, int) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("sup_norm", sup_norm([1.0, 2.0, 3.0], [1.0, 2.0, 5.0]), 2.0)
    check("geometric_bound", geometric_bound(10.0, 0.9, 2), 8.1)
    k = num_iters_for_tol(1.0, 0.9, 0.01)
    check("num_iters_for_tol", k, 44)
    # the returned k must actually reach tolerance
    check("bound met at k", 0.9 ** k <= 0.01 + 1e-12, True)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
