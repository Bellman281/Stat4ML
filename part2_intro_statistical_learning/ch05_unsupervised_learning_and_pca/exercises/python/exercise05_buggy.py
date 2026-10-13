"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (covariance, variance_explained_ratio). Fix one function
at a time until all tests pass. Do not edit run_tests().
"""
# level: core
def center(v):
    m = sum(v) / len(v)
    return [vi - m for vi in v]


def variance(v):
    m = sum(v) / len(v)
    return sum((vi - m) ** 2 for vi in v) / len(v)


def covariance(x, y):
    # BUG: covariance works on CENTERED values; this averages the raw
    # products (ch05_text.tex Section 1).
    return sum(xi * yi for xi, yi in zip(x, y)) / len(x)


def variance_explained_ratio(eigvals):
    # BUG: each eigenvalue is divided by the SUM of eigenvalues, not the max.
    top = max(eigvals)
    return [e / top for e in eigvals]


def _approx(a, b, tol=1e-6):
    if isinstance(a, (list, tuple)):
        return len(a) == len(b) and all(abs(x - y) < tol for x, y in zip(a, b))
    return abs(a - b) < tol


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = _approx(got, expected, tol)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("center", center([1, 2, 3]), [-1.0, 0.0, 1.0])
    check("variance", variance([1, 2, 3]), 2 / 3)
    check("covariance", covariance([1, 2, 3], [1, 2, 3]), 2 / 3)
    check("var ratio", variance_explained_ratio([3, 1]), [0.75, 0.25])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
