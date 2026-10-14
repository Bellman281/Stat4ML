"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (ucb_index, cumulative_regret). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def ucb_index(mean, n, t, c):
    # BUG: the exploration bonus is sqrt(c log t / n); the sqrt is missing.
    return mean + c * math.log(t) / n


def argmax_index(values):
    return max(range(len(values)), key=lambda i: values[i])


def cumulative_regret(mu_star, chosen_means):
    # BUG: regret per round is (mu_star - chosen), not (chosen - mu_star).
    return sum(m - mu_star for m in chosen_means)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = (got == expected) if isinstance(expected, int) else abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("ucb_index", ucb_index(0.5, 4, 100, 2.0), 0.5 + math.sqrt(2.0 * math.log(100) / 4))
    check("argmax_index", argmax_index([1.0, 5.0, 3.0]), 1)
    check("cumulative_regret", cumulative_regret(1.0, [0.8, 0.9, 1.0]),
          (1.0 - 0.8) + (1.0 - 0.9) + (1.0 - 1.0))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
