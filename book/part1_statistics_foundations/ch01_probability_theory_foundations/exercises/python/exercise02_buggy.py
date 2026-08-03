"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 2
Part I: Statistics Foundation for ML

Three deliberate bugs are hiding below (in pmf_three_coins,
cdf_three_coins, and inverse_transform_sample). Run this file, read the
first failing assertion, fix ONLY that function, and re-run -- repeat
until you see "All tests passed!". Do not edit run_tests().
"""
import math
import random


def pmf_three_coins(x):
    # BUG: forgets the binomial coefficient C(3,x) -- returns (1/2)^3 for
    # every x, as if there were only one arrangement of each outcome
    # (see ch01_text.tex Section 5, three-fair-coins example).
    return 0.5 ** 3


def cdf_three_coins(x):
    # BUG: uses a strict "<" instead of "<=" when deciding which pmf
    # values to include -- an off-by-one that under-counts at integer
    # boundaries (see ch01_text.tex Section 6.1's F_X table).
    k = math.floor(x)
    return sum(pmf_three_coins(i) for i in range(4) if i < k)


def inverse_transform_sample(u):
    # BUG: missing the leading minus sign -- ch01_text.tex Section 8
    # derives Y = -log(X), not log(X); as written this returns negative
    # values instead of Exponential(1) samples.
    return math.log(u)


def exponential_pdf(y):
    # Correct (not part of this exercise).
    return math.exp(-y) if y >= 0 else 0.0


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line. Uses a correct, private
# reference implementation of pmf_three_coins for the cdf/pmf checks so
# that fixing cdf_three_coins alone can be verified independently.
# --------------------------------------------------------------------------
def _correct_pmf(x):
    return {0: 1, 1: 3, 2: 3, 3: 1}.get(x, 0) * (0.5 ** 3)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("pmf_three_coins(0)", pmf_three_coins(0), 1 / 8)
    check("pmf_three_coins(1)", pmf_three_coins(1), 3 / 8)
    check("pmf sums to 1", sum(pmf_three_coins(x) for x in range(4)), 1.0)

    check("cdf_three_coins(2.5)", cdf_three_coins(2.5), 7 / 8)
    check("cdf_three_coins(-1)", cdf_three_coins(-1), 0.0)
    check("cdf_three_coins(3.5)", cdf_three_coins(3.5), 1.0)

    rng = random.Random(7)
    n = 200_000
    samples = [inverse_transform_sample(max(rng.random(), 1e-12)) for _ in range(n)]
    mean = sum(samples) / n
    check("mean of inverse-transform samples ~ 1.0 (Exponential(1))", round(mean, 1), 1.0, tol=0.15)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
