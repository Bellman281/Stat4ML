"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part I: Statistics Foundation for ML

Two deliberate bugs are hiding below (markov_bound, chebyshev_bound).
Fix one function at a time until all tests pass. Do not edit run_tests().
"""
# level: proof
def markov_bound(mean_nonneg, a):
    # BUG: Markov is E[Y]/a, not a/E[Y] (ch05_text.tex Section 2).
    return a / mean_nonneg


def chebyshev_bound(var, eps):
    # BUG: Chebyshev divides by eps SQUARED, not eps.
    return var / eps


def empirical_tail(samples, mu, eps):
    return sum(1 for x in samples if abs(x - mu) >= eps) / len(samples)


def wlln_bound(sigma2, n, eps):
    return sigma2 / (n * eps ** 2)


def run_tests():
    failures = []
    def check(name, got, expected, tol=1e-6):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok: failures.append(name)

    data = [1, 2, 2, 2, 3, 2, 2, 2, 2, 10]
    check("markov_bound", markov_bound(2.0, 8), 0.25)
    check("chebyshev_bound", chebyshev_bound(1.0, 2.0), 0.25)
    check("empirical_tail", empirical_tail(data, 2, 5), 0.1)
    check("wlln_bound n=100", wlln_bound(4.0, 100, 0.5), 0.16)
    check("wlln_bound n=400", wlln_bound(4.0, 400, 0.5), 0.04)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
