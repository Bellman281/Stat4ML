"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (confidence_width, finite_class_bound). Fix one function at
a time until all tests pass. Do not edit run_tests(). The final test checks
that confidence_width really inverts the Hoeffding tail.
"""
# level: proof
import math


def hoeffding_tail(n, eps):
    return 2 * math.exp(-2 * n * eps ** 2)


def confidence_width(n, delta):
    # BUG: inverting 2 exp(-2 n eps^2) = delta gives eps = sqrt(log(2/delta)/(2n)),
    # not log(1/delta); the factor 2 inside the log is missing.
    return math.sqrt(math.log(1 / delta) / (2 * n))


def finite_class_bound(emp_risk, m, n, delta):
    # BUG: the capacity term grows with log|H| = log(m), not m itself.
    return emp_risk + math.sqrt((m + math.log(2 / delta)) / (2 * n))


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("hoeffding_tail", hoeffding_tail(100, 0.1), 2 * math.exp(-2))
    check("confidence_width", confidence_width(200, 0.05),
          math.sqrt(math.log(2 / 0.05) / 400))
    check("finite_class_bound", finite_class_bound(0.1, 1000, 500, 0.05),
          0.1 + math.sqrt((math.log(1000) + math.log(2 / 0.05)) / 1000))

    # confidence_width must invert the tail: tail(n, width) == delta
    w = confidence_width(300, 0.1)
    check("width inverts tail", hoeffding_tail(300, w), 0.1)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
