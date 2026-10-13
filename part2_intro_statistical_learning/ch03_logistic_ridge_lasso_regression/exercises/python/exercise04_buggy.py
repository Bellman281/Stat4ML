"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (ridge_estimator_1d, soft_threshold). Fix one function
at a time until all tests pass. Do not edit run_tests().
"""
# level: proof
import math


def ridge_estimator_1d(x, y, lam):
    # BUG: ridge adds lam to the denominator (Sxx + lam); this forgets it,
    # giving plain OLS (ch03_text.tex Section 2).
    xbar = sum(x) / len(x); ybar = sum(y) / len(y)
    sxy = sum((xi - xbar) * (yi - ybar) for xi, yi in zip(x, y))
    sxx = sum((xi - xbar) ** 2 for xi in x)
    return sxy / sxx


def soft_threshold(z, lam):
    # BUG: this drops the sign, so negative z comes out positive.
    return max(abs(z) - lam, 0.0)


def sigmoid_prime(z):
    s = 1.0 / (1.0 + math.exp(-z))
    return s * (1 - s)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    x = [1, 2, 3]; y = [2, 4, 6]            # Sxy = 4, Sxx = 2
    check("ridge (lam=2)", ridge_estimator_1d(x, y, 2.0), 1.0)
    check("soft_threshold(-2,1)", soft_threshold(-2.0, 1.0), -1.0)
    check("soft_threshold(0.5,1)", soft_threshold(0.5, 1.0), 0.0)
    check("sigmoid_prime(0)", sigmoid_prime(0.0), 0.25)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
