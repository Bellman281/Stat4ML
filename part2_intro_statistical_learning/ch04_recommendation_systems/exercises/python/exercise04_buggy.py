"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (squared_error, rmse). Fix one function at a time until all
tests pass. Do not edit run_tests().
"""
# level: core
import math


def predict(p, q):
    return sum(pi * qi for pi, qi in zip(p, q))


def squared_error(r, p, q):
    # BUG: this returns the raw residual, not its SQUARE. The objective in
    # ch04_text.tex Section 2 sums (r - p.q)^2, so the error must be squared.
    return r - predict(p, q)


def rmse(preds, actuals):
    n = len(preds)
    mse = sum((pr - ac) ** 2 for pr, ac in zip(preds, actuals)) / n
    # BUG: RMSE is the *root* mean squared error -- take the square root.
    return mse


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("predict", predict([1.0, 2.0], [2.0, 0.5]), 3.0)
    # residual is 2, so the SQUARE is 4 -- a case where error != error^2
    check("squared_error", squared_error(5.0, [1.0, 2.0], [2.0, 0.5]), 4.0)
    check("rmse", rmse([3.0, 2.0, 5.0], [4.0, 2.0, 4.0]), math.sqrt(2.0 / 3.0))
    # a perfect prediction set has zero error either way
    check("rmse_zero", rmse([2.0, 2.0], [2.0, 2.0]), 0.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
