"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part I: Statistics Foundation for ML

Two deliberate bugs (conditional_y_prob, joint_covariance). Fix one
function at a time until all tests pass. Do not edit run_tests().
"""
# level: core
JOINT = {(0, 0): 0.3, (0, 1): 0.2, (1, 0): 0.1, (1, 1): 0.4}


def marginal_x_prob(joint, x0):
    return sum(p for (x, y), p in joint.items() if x == x0)


def marginal_y_prob(joint, y0):
    return sum(p for (x, y), p in joint.items() if y == y0)


def conditional_y_prob(joint, y0, x0):
    # BUG: a conditional on X=x0 divides by P(X=x0), not P(Y=y0)
    # (ch04_text.tex Section 1).
    return joint.get((x0, y0), 0.0) / marginal_y_prob(joint, y0)


def joint_covariance(joint):
    # BUG: covariance subtracts E[X]E[Y]; this returns E[XY] alone.
    exy = sum(x * y * p for (x, y), p in joint.items())
    return exy


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    check("marginal_x_prob(0)", marginal_x_prob(JOINT, 0), 0.5)
    check("conditional P(Y=1|X=0)", conditional_y_prob(JOINT, 1, 0), 0.4)
    check("conditional P(Y=1|X=1)", conditional_y_prob(JOINT, 1, 1), 0.8)
    check("joint_covariance", joint_covariance(JOINT), 0.1)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
