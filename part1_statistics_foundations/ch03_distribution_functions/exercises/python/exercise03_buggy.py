"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (exponential_pdf, inverse_transform_
exponential). Fix one function at a time until all tests pass. Do not edit
run_tests().
"""
# level: core
import math


def exponential_cdf(x, rate):
    return 1 - math.exp(-rate * x)


def exponential_pdf(x, rate):
    # BUG: the density carries a factor of `rate` out front
    # (f = rate * e^{-rate x}); this drops it.
    return math.exp(-rate * x)


def inverse_transform_exponential(u, rate):
    # BUG: the inverse cdf is -log(1 - u)/rate; this is missing the minus,
    # so it returns negatives (ch03_text.tex Section 1).
    return math.log(1 - u) / rate


def empirical_cdf(data, x):
    return sum(1 for d in data if d <= x) / len(data)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("exponential_cdf(ln2)", exponential_cdf(math.log(2), 1.0), 0.5)
    check("exponential_pdf(0)", exponential_pdf(0.0, 1.0), 1.0)
    check("exponential_pdf(1,rate2)", exponential_pdf(1.0, 2.0), 2 * math.exp(-2))
    check("inverse_transform(0.5)", inverse_transform_exponential(0.5, 1.0), math.log(2))
    check("empirical_cdf(2.5)", empirical_cdf([1, 2, 3, 4], 2.5), 0.5)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
