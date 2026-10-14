"""
Chapter 9 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (rbf_kernel, linear_kernel). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def rbf_kernel(x1, x2, length):
    # BUG: the RBF kernel divides by 2*length^2, not length^2.
    return math.exp(-(x1 - x2) ** 2 / (length ** 2))


def kernel_vector(x, xs, length):
    return [rbf_kernel(x, xi, length) for xi in xs]


def linear_kernel(x1, x2):
    # BUG: the linear kernel is the PRODUCT x1*x2, not the sum.
    return x1 + x2


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(expected, list):
            ok = len(got) == len(expected) and all(abs(a - b) < tol for a, b in zip(got, expected))
        else:
            ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("rbf_same", rbf_kernel(0.0, 0.0, 1.0), 1.0)
    check("rbf_diff", rbf_kernel(0.0, 1.0, 1.0), math.exp(-0.5))
    check("kernel_vector", kernel_vector(0.0, [0.0, 1.0, 2.0], 1.0),
          [1.0, math.exp(-0.5), math.exp(-2.0)])
    check("linear_kernel", linear_kernel(2.0, 3.0), 6.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
