"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (squared_bias, estimator_variance). Fix one function at
a time until all tests pass. Do not edit run_tests().
"""
# level: proof
def squared_bias(preds, truth):
    # BUG: bias is SQUARED -- (mean - truth)^2, not (mean - truth).
    m = sum(preds) / len(preds)
    return m - truth


def estimator_variance(preds):
    # BUG: the variance here divides by n (population variance), not n-1.
    m = sum(preds) / len(preds)
    return sum((p - m) ** 2 for p in preds) / (len(preds) - 1)


def expected_mse(preds, truth):
    return sum((p - truth) ** 2 for p in preds) / len(preds)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    preds, truth = [2.0, 4.0, 6.0], 5.0
    check("squared_bias", squared_bias(preds, truth), 1.0)
    check("estimator_variance", estimator_variance(preds), 8.0 / 3.0)
    check("expected_mse", expected_mse(preds, truth), 11.0 / 3.0)
    check("identity bias^2+var=mse",
          squared_bias(preds, truth) + estimator_variance(preds), 11.0 / 3.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
