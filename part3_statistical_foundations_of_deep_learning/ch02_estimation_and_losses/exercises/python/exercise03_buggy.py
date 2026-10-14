"""
Chapter 2 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (ridge_lambda, ridge_estimate_1d). Fix one function at a
time until all tests pass. Do not edit run_tests(). The final test checks that
the MAP estimate minimises the penalised objective.
"""
# level: proof


def gaussian_log_prior(w, tau):
    return -w ** 2 / (2 * tau ** 2)


def ridge_lambda(sigma2, tau2):
    # BUG: a N(0,tau^2) prior under N(.,sigma^2) noise gives lam = sigma^2/tau^2,
    # not tau^2/sigma^2 (ch02_text.tex Theorem 2.1).
    return tau2 / sigma2


def ridge_estimate_1d(xs, ys, lam):
    sxy = sum(x * y for x, y in zip(xs, ys))
    sxx = sum(x * x for x in xs)
    # BUG: ridge ADDS lam to the denominator sum(x^2); subtracting it is wrong
    # (and blows up as lam -> sum(x^2)).
    return sxy / (sxx - lam)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    xs = [1, 2, 3]; ys = [2, 4, 6]
    check("gaussian_log_prior", gaussian_log_prior(2.0, 1.0), -2.0)
    check("ridge_lambda", ridge_lambda(1.0, 0.5), 2.0)
    check("ridge_ols", ridge_estimate_1d(xs, ys, 0.0), 2.0)

    # MAP must minimise J(w) = sum(y - x w)^2 + lam w^2; its minimiser is
    # sum(xy)/(sum(x^2)+lam). Check against a tiny grid search.
    lam = 5.0
    J = lambda w: sum((y - x * w) ** 2 for x, y in zip(xs, ys)) + lam * w * w
    grid = [i * 0.001 for i in range(0, 4000)]
    wgrid = min(grid, key=J)
    check("MAP minimises objective", ridge_estimate_1d(xs, ys, lam), wgrid, tol=2e-3)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
