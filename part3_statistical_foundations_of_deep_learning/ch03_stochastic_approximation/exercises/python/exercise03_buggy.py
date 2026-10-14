"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (sgd_step, quad_grad). Fix one function at a time until all
tests pass. Do not edit run_tests().
"""
# level: core


def sgd_step(theta, grad, lr):
    # BUG: SGD moves AGAINST the gradient; this moves with it (gradient ascent).
    return theta + lr * grad


def inverse_time_lr(t, a0):
    return a0 / t


def quad_grad(theta, target):
    # BUG: d/dtheta (theta-target)^2 = 2(theta-target); the factor 2 is missing.
    return theta - target


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("sgd_step", sgd_step(5.0, 2.0, 0.1), 4.8)
    check("inverse_time_lr", inverse_time_lr(4, 0.5), 0.125)
    check("quad_grad", quad_grad(5.0, 3.0), 4.0)
    check("one_step", sgd_step(5.0, quad_grad(5.0, 3.0), 0.25), 4.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
