"""
Chapter 9 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (gp_post_mean, gp_post_var). Fix one function at a time
until all tests pass. Do not edit run_tests(). The last test checks that the
noise-free posterior variance at the training point is exactly 0.
"""
# level: proof


def gp_post_mean(k_star, k_11, sigma2, y):
    # BUG: the denominator includes the observation noise (k_11 + sigma2); this
    # omits it.
    return k_star / k_11 * y


def gp_post_var(k_ss, k_star, k_11, sigma2):
    # BUG: the predictive variance SUBTRACTS the reduction term; this adds it,
    # so the posterior would be more uncertain than the prior.
    return k_ss + k_star ** 2 / (k_11 + sigma2)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("gp_post_mean", gp_post_mean(0.6, 1.0, 0.1, 2.0), 0.6 / 1.1 * 2.0)
    check("gp_post_var", gp_post_var(1.0, 0.6, 1.0, 0.1), 1.0 - 0.36 / 1.1)
    check("var_at_data_is_zero", gp_post_var(1.0, 1.0, 1.0, 0.0), 0.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
