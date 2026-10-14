"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (zero_one_loss, generalisation_gap). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: core


def zero_one_loss(pred, y):
    # BUG: the 0-1 loss is 1 when WRONG and 0 when correct; this is reversed.
    return 0.0 if pred != y else 1.0


def empirical_risk(preds, ys):
    return sum(zero_one_loss(p, y) for p, y in zip(preds, ys)) / len(ys)


def generalisation_gap(emp_risk, true_risk):
    # BUG: the gap is R - Rhat = true_risk - emp_risk, not the other way round.
    return emp_risk - true_risk


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("zero_one_correct", zero_one_loss(1, 1), 0.0)
    check("zero_one_wrong", zero_one_loss(1, 0), 1.0)
    check("empirical_risk", empirical_risk([1, 0, 1, 1], [1, 1, 1, 0]), 0.5)
    check("gap", generalisation_gap(0.3, 0.5), 0.2)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
