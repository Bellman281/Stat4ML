"""
Chapter 3 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (harmonic_partial, rm_valid). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: proof


def harmonic_partial(T):
    # BUG: the sum runs t = 1..T inclusive; range(1, T) drops the last term t=T.
    return sum(1.0 / t for t in range(1, T))


def basel_partial(T):
    return sum(1.0 / t ** 2 for t in range(1, T + 1))


def rm_valid(p):
    # BUG: the squared sum converges only for p > 1/2 (strict); p = 1/2 diverges,
    # so the lower bound must be strict, not >=.
    return (p >= 0.5) and (p <= 1.0)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, bool) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("harmonic_partial", harmonic_partial(4), 1 + 1/2 + 1/3 + 1/4)
    check("basel_partial", basel_partial(2), 1 + 1/4)
    check("rm_valid_1.0", rm_valid(1.0), True)
    check("rm_valid_0.75", rm_valid(0.75), True)
    check("rm_valid_0.5", rm_valid(0.5), False)
    check("rm_valid_0.4", rm_valid(0.4), False)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
