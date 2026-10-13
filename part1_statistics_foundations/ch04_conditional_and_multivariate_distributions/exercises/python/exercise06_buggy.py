"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part I: Statistics Foundation for ML

Two deliberate bugs (bvn_conditional_mean, bvn_conditional_var). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: research
def bvn_conditional_mean(mu_y, rho, sy, sx, x, mu_x):
    # BUG: the slope is rho * sy/sx, not rho * sx/sy (ch04 Section 3).
    return mu_y + rho * (sx / sy) * (x - mu_x)


def bvn_conditional_var(sy, rho):
    # BUG: the conditional variance scales sy SQUARED, not sy.
    return sy * (1 - rho ** 2)


def mvn_conditional_mean_1d(mu1, s12, s22, x2, mu2):
    return mu1 + (s12 / s22) * (x2 - mu2)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("bvn_conditional_mean", bvn_conditional_mean(0.0, 0.7, 2.0, 1.0, 2.0, 0.0), 2.8)
    check("bvn_conditional_var", bvn_conditional_var(2.0, 0.7), 4.0 * (1 - 0.49))
    check("mvn_conditional_mean_1d", mvn_conditional_mean_1d(0.0, 0.7, 1.0, 2.0, 0.0), 1.4)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
