"""
Chapter 6 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (discounted_return, greedy_action). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: core


def discounted_return(rewards, gamma):
    # BUG: the discount on step t is gamma^t (t starts at 0); this uses gamma^(t+1).
    return sum(gamma ** (t + 1) * r for t, r in enumerate(rewards))


def q_backup(r, gamma, next_values, probs):
    return r + gamma * sum(p * v for p, v in zip(probs, next_values))


def greedy_action(q_values):
    # BUG: the greedy action MAXIMISES the Q-value, so this should be argmax.
    return min(range(len(q_values)), key=lambda i: q_values[i])


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, int) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("discounted_return", discounted_return([1, 1, 1], 0.5), 1 + 0.5 + 0.25)
    check("q_backup", q_backup(0.0, 0.9, [10.0, 0.0], [0.8, 0.2]), 7.2)
    check("greedy_action", greedy_action([1.0, 5.0, 3.0]), 1)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
