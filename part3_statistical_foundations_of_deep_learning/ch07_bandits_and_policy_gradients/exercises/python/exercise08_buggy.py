"""
Chapter 7 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (logit_score, pg_grad). Fix one function at a time until all
tests pass. Do not edit run_tests(). The last test checks the mean-zero-score
identity, which only holds for the correct score.
"""
# level: proof
import math


def softmax(logits):
    m = max(logits)
    e = [math.exp(z - m) for z in logits]
    s = sum(e)
    return [ei / s for ei in e]


def logit_score(a, probs):
    # BUG: the score is e_a - p, i.e. (indicator - p_i); this drops the indicator
    # and returns -p_i for every component.
    return [-probs[i] for i in range(len(probs))]


def pg_grad(R, a, probs):
    # BUG: the REINFORCE estimate scales the score by the reward R.
    return [s for s in logit_score(a, probs)]


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = all(abs(a - b) < tol for a, b in zip(got, expected)) and len(got) == len(expected)
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("logit_score", logit_score(1, [0.2, 0.5, 0.3]), [-0.2, 0.5, -0.3])
    check("pg_grad", pg_grad(2.0, 1, [0.2, 0.5, 0.3]), [-0.4, 1.0, -0.6])
    p = softmax([0.0, 0.5, -0.5])
    mean = [sum(p[a] * logit_score(a, p)[i] for a in range(3)) for i in range(3)]
    check("mean score is zero", mean, [0.0, 0.0, 0.0])

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
