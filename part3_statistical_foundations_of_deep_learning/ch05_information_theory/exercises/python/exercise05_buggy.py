"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (entropy, kl). Fix one function at a time until all tests
pass. Do not edit run_tests().
"""
# level: core
import math


def entropy(p):
    # BUG: entropy is the NEGATIVE sum of p log p; the minus sign is missing.
    return sum(pi * math.log(pi) for pi in p)


def cross_entropy(p, q):
    return -sum(pi * math.log(qi) for pi, qi in zip(p, q))


def kl(p, q):
    # BUG: KL(p||q) uses log(p_i / q_i), not log(q_i / p_i).
    return sum(pi * math.log(qi / pi) for pi, qi in zip(p, q))


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    p = [0.5, 0.5]; q = [0.25, 0.75]
    check("entropy", entropy(p), math.log(2))
    check("cross_entropy", cross_entropy(p, q),
          -(0.5 * math.log(0.25) + 0.5 * math.log(0.75)))
    check("kl", kl(p, q), 0.5 * math.log(0.5 / 0.25) + 0.5 * math.log(0.5 / 0.75))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
