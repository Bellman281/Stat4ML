"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part I: Statistics Foundation for ML

Two deliberate bugs (between_var, total_variance). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: proof
def group_mean(means, weights):
    return sum(wi * mi for wi, mi in zip(weights, means))


def within_var(vars_, weights):
    return sum(wi * vi for wi, vi in zip(weights, vars_))


def between_var(means, weights):
    # BUG: Var(E[X|Y]) = E[m^2] - (E[m])^2; this forgets to subtract the
    # squared mean (ch04_text.tex Section 2).
    return sum(wi * mi * mi for wi, mi in zip(weights, means))


def total_variance(vars_, means, weights):
    # BUG: total variance is within + between; this returns within only,
    # dropping the variance of the group means.
    return within_var(vars_, weights)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    w, m, v = [0.5, 0.5], [0.0, 10.0], [1.0, 1.0]
    check("group_mean", group_mean(m, w), 5.0)
    check("within_var", within_var(v, w), 1.0)
    check("between_var", between_var(m, w), 25.0)
    check("total_variance", total_variance(v, m, w), 26.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
