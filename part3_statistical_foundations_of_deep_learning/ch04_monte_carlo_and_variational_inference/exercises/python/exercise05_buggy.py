"""
Chapter 4 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (importance_weight, eff_sample_size). Fix one function at a
time until all tests pass. Do not edit run_tests(). The last test checks that
q = p reduces importance sampling to plain Monte Carlo.
"""
# level: proof


def importance_weight(px, qx):
    # BUG: the weight is p/q (target over proposal), not q/p.
    return qx / px


def is_estimate(fvals, pxs, qxs):
    n = len(fvals)
    return sum(f * (p / q) for f, p, q in zip(fvals, pxs, qxs)) / n


def eff_sample_size(weights):
    s1 = sum(weights)
    s2 = sum(w ** 2 for w in weights)
    # BUG: ESS is (sum w)^2 / sum(w^2); the numerator is squared.
    return s1 / s2


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("importance_weight", importance_weight(0.1, 0.2), 0.5)
    check("is_estimate", is_estimate([1.0, 1.0], [0.2, 0.2], [0.4, 0.4]), 0.5)
    check("ess_uniform", eff_sample_size([1, 1, 1, 1]), 4.0)
    check("ess_degenerate", eff_sample_size([2, 0, 0, 0]), 1.0)
    # q = p must reduce IS to the plain sample mean
    f = [1.0, 3.0, 5.0]; p = [0.3, 0.3, 0.3]
    check("q=p reduces to MC", is_estimate(f, p, p), sum(f) / len(f))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
