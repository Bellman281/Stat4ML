"""
Chapter 1 -- RUSTLINGS-STYLE EXERCISE (Python edition), Exercise 3
Part II: Introduction to Statistical Learning

Three deliberate bugs are hiding below (in online_variance_update,
variance_from_state, and pseudo_label_accuracy). Run this file, read
the first failing assertion, fix ONLY that function, and re-run --
repeat until you see "All tests passed!". Do not edit run_tests().
"""


def online_variance_update(state, new_x):
    # BUG: reuses `delta` (computed from the OLD mean) a second time
    # instead of computing `delta2` from the UPDATED mean -- this is
    # the classic Welford's-algorithm mistake.
    n, mean, m2 = state
    n = n + 1
    delta = new_x - mean
    mean = mean + delta / n
    m2 = m2 + delta * delta
    return (n, mean, m2)


def variance_from_state(state):
    # BUG: uses the (n-1) sample-variance correction instead of the
    # population variance M2/n that ch02_text.tex defines Var(X) as.
    n, _mean, m2 = state
    return m2 / (n - 1) if n > 1 else 0.0


def pseudo_label_accuracy(teacher_preds, true_labels):
    # BUG: forgets to divide by the total count -- returns the raw
    # number of matches instead of a fraction.
    return sum(1 for p, t in zip(teacher_preds, true_labels) if p == t)


def semi_supervised_combined_accuracy(labeled_acc, labeled_frac, pseudo_acc, unlabeled_frac):
    # Correct (not part of this exercise).
    return labeled_frac * labeled_acc + unlabeled_frac * pseudo_acc


# --------------------------------------------------------------------------
# Test harness -- do not edit below this line.
# --------------------------------------------------------------------------
def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    stream = [4.0, 6.0, 8.0, 2.0, 10.0]
    state = (0, 0.0, 0.0)
    for x in stream:
        state = online_variance_update(state, x)
    var = variance_from_state(state)
    check("online variance of stream", var, 8.0)

    acc = pseudo_label_accuracy([1, 0, 1, 1, 0], [1, 0, 0, 1, 0])
    check("pseudo_label_accuracy", acc, 0.8)

    combined = semi_supervised_combined_accuracy(0.95, 0.1, acc, 0.9)
    check("semi_supervised_combined_accuracy", round(combined, 4), round(0.1 * 0.95 + 0.9 * 0.8, 4))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
