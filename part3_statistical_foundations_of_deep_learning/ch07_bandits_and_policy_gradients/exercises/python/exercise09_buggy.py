"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (advantage, expected_grad). Fix one function at a time until
all tests pass. Do not edit run_tests(). The last test checks baseline
invariance of the expected gradient.
"""
# level: research


def logit_score(a, probs):
    return [(1.0 if i == a else 0.0) - probs[i] for i in range(len(probs))]


def advantage(R, baseline):
    # BUG: the advantage is R - baseline, not baseline - R.
    return baseline - R


def grad_estimate(R, b, a, probs):
    return [(R - b) * s for s in logit_score(a, probs)]


def expected_grad(rewards, b, probs):
    n = len(probs)
    acc = [0.0] * n
    for a in range(n):
        g = grad_estimate(rewards[a], b, a, probs)
        for i in range(n):
            # BUG: each action's gradient is weighted by its probability probs[a];
            # this omits the weighting.
            acc[i] += g[i]
    return acc


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(got, list):
            ok = len(got) == len(expected) and all(abs(a - b) < tol for a, b in zip(got, expected))
        else:
            ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    probs = [0.2, 0.5, 0.3]; rewards = [1.0, 2.0, 3.0]
    check("advantage", advantage(3.0, 2.0), 1.0)
    check("grad_estimate", grad_estimate(3.0, 2.0, 1, probs), [-0.2, 0.5, -0.3])

    g0 = expected_grad(rewards, 0.0, probs)
    g5 = expected_grad(rewards, 5.0, probs)
    # baseline invariance: the expected gradient must not depend on b
    check("baseline invariance", g0, g5)
    # and it equals sum_a p_a R_a score_a (the true policy gradient)
    true_g = [sum(probs[a] * rewards[a] * logit_score(a, probs)[i] for a in range(3)) for i in range(3)]
    check("equals true gradient", g0, true_g)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
