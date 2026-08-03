"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 3
Part I: Statistics Foundation for ML

Three deliberate bugs are hiding below (in independence_check,
exponential_cdf, and probability_integral_transform_mean). Run this
file, read the first failing assertion, fix ONLY that function, and
re-run -- repeat until you see "All tests passed!". Do not edit
run_tests().
"""
import math
import random


def independence_check(p_a, p_b, p_a_and_b, tol=1e-9):
    # BUG: checks the disjoint-events additivity condition
    # (P(AnB) == P(A)+P(B)) instead of the independence condition
    # (P(AnB) == P(A)*P(B)) -- see ch01_text.tex Section 4.
    return abs(p_a_and_b - (p_a + p_b)) < tol


def intersection_with_complement(p_a, p_b_and_a):
    # Correct.
    return p_a - p_b_and_a


def exponential_cdf(y):
    # BUG: returns the density e^{-y} (from Section 8's change-of-
    # variables example) instead of integrating it to get the CDF
    # 1 - e^{-y}.
    return math.exp(-y) if y >= 0 else 0.0


def probability_integral_transform_mean(n, seed=0):
    # BUG: forgets to apply exponential_cdf -- averages the raw
    # Exponential(1) samples x_i instead of y_i = F_X(x_i), so this
    # converges to the Exponential(1) mean (1.0) instead of the
    # Uniform(0,1) mean (0.5) that the probability integral transform
    # theorem predicts.
    rng = random.Random(seed)
    total = 0.0
    for _ in range(n):
        u = max(rng.random(), 1e-12)
        x = -math.log(u)
        total += x
    return total / n


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = (got == expected) if isinstance(expected, bool) else abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("independence_check(0.5,0.4,0.2) True", independence_check(0.5, 0.4, 0.2), True)
    check("independence_check(0.5,0.4,0.3) False", independence_check(0.5, 0.4, 0.3), False)

    check("intersection_with_complement(0.5,0.3)", intersection_with_complement(0.5, 0.3), 0.2)

    check("exponential_cdf(0)", exponential_cdf(0), 0.0)
    check("exponential_cdf(1)", round(exponential_cdf(1), 4), round(1 - math.exp(-1), 4))

    mean = probability_integral_transform_mean(200_000, seed=7)
    check("probability_integral_transform_mean ~ 0.5 (Uniform(0,1))", round(mean, 1), 0.5, tol=0.15)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
