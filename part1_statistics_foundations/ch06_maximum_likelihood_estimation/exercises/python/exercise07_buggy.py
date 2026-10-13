"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (in score_bernoulli and
fisher_information_bernoulli). Fix one function at a time until all tests
pass. Do not edit run_tests().
"""
# level: proof
import math
import random


def score_bernoulli(p, data):
    # BUG: the second term should be SUBTRACTED, not added -- the score is
    # sum_i [ x_i/p - (1-x_i)/(1-p) ] (ch06_text.tex Section 2).
    return sum(x / p + (1 - x) / (1 - p) for x in data)


def fisher_information_bernoulli(p, n):
    # BUG: Fisher information is n / (p(1-p)), not n*p*(1-p).
    return n * p * (1 - p)


def cramer_rao_lower_bound(p, n):
    return p * (1 - p) / n


def mle_variance_sim(p, n, reps, seed=0):
    rng = random.Random(seed)
    est = []
    for _ in range(reps):
        ones = sum(1 for _ in range(n) if rng.random() < p)
        est.append(ones / n)
    m = sum(est) / reps
    return sum((e - m) ** 2 for e in est) / reps


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    data = [1] * 15 + [0] * 35  # MLE = 0.3
    check("score at MLE (=0)", score_bernoulli(0.3, data), 0.0)
    check("score at p=0.5", score_bernoulli(0.5, data), (15 - 50 * 0.5) / (0.5 * 0.5))
    check("Fisher info(0.3,50)", fisher_information_bernoulli(0.3, 50), 50 / (0.3 * 0.7))
    check("CRLB(0.3,50)", cramer_rao_lower_bound(0.3, 50), 0.3 * 0.7 / 50)
    check("sim var ~ CRLB", mle_variance_sim(0.3, 50, 20000, seed=0),
          0.3 * 0.7 / 50, tol=4e-4)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
