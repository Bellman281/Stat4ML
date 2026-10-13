"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part II: Introduction to Statistical Learning

Two deliberate bugs (hard_assignment, responsibility_based_weight). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
def hard_assignment(resp):
    # BUG: the hard assignment is the ARGMAX, not the argmin.
    best = 0
    for i in range(len(resp)):
        if resp[i] < resp[best]:
            best = i
    return best


def responsibility_based_weight(resp_column):
    # BUG: the mixing weight is the MEAN of the responsibilities, not the sum.
    return sum(resp_column)


def em_lower_bound_gap(ll_before, ll_after):
    return ll_after - ll_before


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("hard_assignment", hard_assignment([0.2, 0.7, 0.1]), 1)
    check("weight (mean)", responsibility_based_weight([0.5, 0.5, 1.0, 0.0]), 0.5)
    check("em_lower_bound_gap", em_lower_bound_gap(1.0, 1.5), 0.5)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
