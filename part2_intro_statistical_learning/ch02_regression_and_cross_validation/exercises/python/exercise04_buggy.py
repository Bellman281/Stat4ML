"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (kfold_split_sizes, loocv_from_leverage). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
def kfold_split_sizes(n, k):
    # BUG: this drops the remainder, so the sizes don't sum to n. The first
    # (n mod k) folds must get one extra point (ch02_text.tex Section 3).
    base = n // k
    return [base] * k


def mean_cv_error(fold_errors):
    return sum(fold_errors) / len(fold_errors)


def loocv_from_leverage(residuals, leverages):
    # BUG: each leave-one-out residual e_i/(1-h_i) is SQUARED before
    # averaging.
    terms = [e / (1 - h) for e, h in zip(residuals, leverages)]
    return sum(terms) / len(terms)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = (got == expected) if isinstance(expected, list) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("kfold_split_sizes", kfold_split_sizes(10, 3), [4, 3, 3])
    check("kfold sizes sum", sum(kfold_split_sizes(10, 3)), 10)
    check("mean_cv_error", mean_cv_error([0.1, 0.2, 0.3]), 0.2)
    check("loocv_from_leverage", loocv_from_leverage([1.0, 1.0], [0.5, 0.5]), 4.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
