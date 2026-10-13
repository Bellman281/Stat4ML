"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (reconstruction_error_ratio, singular_value_from_eigenvalue).
Fix one function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
import math


def cumulative_variance_explained(eigvals):
    total = sum(eigvals)
    out, run = [], 0.0
    for e in eigvals:
        run += e
        out.append(run / total)
    return out


def reconstruction_error_ratio(eigvals, k):
    # BUG: the error is the variance DROPPED, eigvals[k:], not the variance
    # KEPT, eigvals[:k] (ch05_text.tex Section 3).
    return sum(eigvals[:k]) / sum(eigvals)


def singular_value_from_eigenvalue(eigval):
    # BUG: a singular value is the SQUARE ROOT of the X^T X eigenvalue.
    return eigval


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

    check("cumulative", cumulative_variance_explained([4, 1]), [0.8, 1.0])
    check("recon error", reconstruction_error_ratio([4, 1], 1), 0.2)
    check("singular value", singular_value_from_eigenvalue(9), 3.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
