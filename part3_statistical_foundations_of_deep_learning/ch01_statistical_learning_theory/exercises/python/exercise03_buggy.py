"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (sauer_bound, shatters). Fix one function at a time until
all tests pass. Do not edit run_tests().
"""
# level: research
import math


def sauer_bound(n, d):
    # BUG: Sauer-Shelah sums i from 0 to d (inclusive), not 1 to d; the i=0
    # term (the single empty dichotomy, C(n,0)=1) is missing here.
    return sum(math.comb(n, i) for i in range(1, d + 1))


def vc_bound_term(d, n, delta):
    return math.sqrt((d * (math.log(2 * n / d) + 1) + math.log(4 / delta)) / n)


def shatters(patterns, n):
    # BUG: shattering needs ALL 2^n labelings present; counting the patterns is
    # not enough unless they are distinct -- compare the DISTINCT set to 2^n.
    return len(list(patterns)) == 2 ** n


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, (bool, int)) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("sauer_bound", sauer_bound(5, 2), 16)                 # 1 + 5 + 10
    check("vc_bound_term", vc_bound_term(10, 1000, 0.05),
          math.sqrt((10 * (math.log(200) + 1) + math.log(80)) / 1000))
    check("shatters_full", shatters([(0, 0), (0, 1), (1, 0), (1, 1)], 2), True)
    # a duplicate-laden list of the right length must NOT count as shattering
    check("shatters_dupes", shatters([(0, 0), (0, 0), (1, 1), (1, 1)], 2), False)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
