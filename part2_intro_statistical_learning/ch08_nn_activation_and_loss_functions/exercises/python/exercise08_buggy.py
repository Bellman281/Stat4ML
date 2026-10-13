"""
Chapter 8 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (relu, softmax). Fix one function at a time until all
tests pass. Do not edit run_tests().
"""
# level: core
import math


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


def relu(z):
    # BUG: ReLU is max(0, z), which zeros NEGATIVE inputs; this zeros positives.
    return min(0.0, z)


def softmax(zs):
    # BUG: the stable softmax subtracts max(zs) before exp; without it this
    # overflows on large logits (ch08_text.tex Section 1).
    exps = [math.exp(z) for z in zs]
    tot = sum(exps)
    return [e / tot for e in exps]


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(expected, list):
            ok = len(got) == len(expected) and all(abs(g - e) < tol for g, e in zip(got, expected))
        else:
            ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("sigmoid", sigmoid(0.0), 0.5)
    check("relu_neg", relu(-2.0), 0.0)
    check("relu_pos", relu(3.0), 3.0)
    check("softmax_uniform", softmax([1.0, 1.0, 1.0]), [1 / 3, 1 / 3, 1 / 3])
    # stability: large equal logits must still give a uniform distribution
    check("softmax_stable", softmax([1000.0, 1000.0]), [0.5, 0.5])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
