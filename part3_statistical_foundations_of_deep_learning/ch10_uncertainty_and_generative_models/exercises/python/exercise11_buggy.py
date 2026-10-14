"""
Chapter 10 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (conformal_q, empirical_coverage). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: proof
import math


def conformal_q(cal_scores, alpha):
    n = len(cal_scores)
    # BUG: the rank rounds UP (ceil); floor can pick too small a threshold and
    # break the coverage guarantee.
    k = math.floor((n + 1) * (1 - alpha))
    if k > n:
        return math.inf
    return sorted(cal_scores)[k - 1]


def empirical_coverage(test_scores, q):
    # BUG: a score is covered when it is <= q, not >= q.
    return sum(1 for s in test_scores if s >= q) / len(test_scores)


def guarantee_holds(cov, alpha):
    return cov >= 1 - alpha - 1e-9


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, bool) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    cal = [0.2, 0.4, 0.6, 0.8, 1.0]           # n=5, alpha=0.2 -> k=ceil(4.8)=5 -> q=1.0
    check("conformal_q", conformal_q(cal, 0.2), 1.0)
    test = [0.5, 0.9, 1.5, 0.1, 0.7]          # four of five are <= 1.0
    check("empirical_coverage", empirical_coverage(test, 1.0), 0.8)
    check("guarantee_holds", guarantee_holds(empirical_coverage(test, 1.0), 0.2), True)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
