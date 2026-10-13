"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (sigmoid, cross_entropy). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def sigmoid(z):
    # BUG: the sigmoid is 1/(1+exp(-z)); this has the sign of z flipped.
    return 1.0 / (1.0 + math.exp(z))


def logistic_proba(w, x):
    return sigmoid(sum(wi * xi for wi, xi in zip(w, x)))


def cross_entropy(y, p):
    # BUG: cross-entropy keeps BOTH terms -- it drops the (1-y)*log(1-p) half.
    return -(y * math.log(p))


def classify(p, threshold=0.5):
    return 1 if p >= threshold else 0


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("sigmoid(0)", sigmoid(0.0), 0.5)
    check("sigmoid(2)", sigmoid(2.0), 1 / (1 + math.exp(-2)))
    check("logistic_proba", logistic_proba([0, 1, 1], [1, 2, -2]), 0.5)
    check("cross_entropy(1,0.5)", cross_entropy(1, 0.5), math.log(2))
    check("cross_entropy(0,0.5)", cross_entropy(0, 0.5), math.log(2))
    check("classify(0.7)", classify(0.7), 1)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
