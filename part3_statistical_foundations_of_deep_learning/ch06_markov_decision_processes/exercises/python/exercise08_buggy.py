"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (mc_update, td_error). Fix one function at a time until all
tests pass. Do not edit run_tests(). The last test checks that one TD update
with v_next = v and r = 0 leaves v unchanged.
"""
# level: research


def mc_update(v, G, alpha):
    # BUG: the update moves TOWARD G: v + alpha*(G - v); this uses (G + v).
    return v + alpha * (G + v)


def td_error(r, gamma, v_next, v):
    # BUG: the TD error discounts the NEXT value: r + gamma*v_next - v; the
    # gamma factor is missing here.
    return r + v_next - v


def td_update(v, r, gamma, v_next, alpha):
    return v + alpha * td_error(r, gamma, v_next, v)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("mc_update", mc_update(0.5, 1.0, 0.1), 0.55)
    check("td_error", td_error(0.0, 0.9, 1.0, 0.5), 0.4)
    check("td_update", td_update(0.5, 0.0, 0.9, 1.0, 0.1), 0.54)
    # a self-consistent value is a fixed point: r=0, v_next=v leaves v unchanged
    check("fixed point", td_update(2.0, 0.0, 1.0, 2.0, 0.3), 2.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
