"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (ols_slope, r_squared). Fix one function at a time until
all tests pass. Do not edit run_tests().
"""
# level: core
def ols_slope(x, y):
    # BUG: the slope uses CENTERED sums, Sxy/Sxx, not the raw
    # sum(xi*yi)/sum(xi^2) (ch02_text.tex Section 1).
    return sum(xi * yi for xi, yi in zip(x, y)) / sum(xi * xi for xi in x)


def ols_intercept(x, y):
    xbar = sum(x) / len(x); ybar = sum(y) / len(y)
    return ybar - ols_slope(x, y) * xbar


def predict(b0, b1, x):
    return b0 + b1 * x


def r_squared(x, y, b0, b1):
    # BUG: R^2 is 1 - SS_res/SS_tot, not SS_res/SS_tot.
    ybar = sum(y) / len(y)
    ss_res = sum((yi - (b0 + b1 * xi)) ** 2 for xi, yi in zip(x, y))
    ss_tot = sum((yi - ybar) ** 2 for yi in y)
    return ss_res / ss_tot


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    x = [0, 1, 2, 3]; y = [1, 3, 5, 7]
    b1 = ols_slope(x, y); b0 = ols_intercept(x, y)
    check("ols_slope", b1, 2.0)
    check("ols_intercept", b0, 1.0)
    check("predict(10)", predict(1.0, 2.0, 10), 21.0)
    check("r_squared", r_squared(x, y, 1.0, 2.0), 1.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
