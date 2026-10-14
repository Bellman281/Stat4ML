"""
Chapter 8 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (attention, pmi). Fix one function at a time until all tests
pass. Do not edit run_tests().
"""
# level: research
import math


def softmax_weights(scores):
    m = max(scores)
    e = [math.exp(s - m) for s in scores]
    tot = sum(e)
    return [ei / tot for ei in e]


def attention(scores, values):
    w = softmax_weights(scores)
    # BUG: the output is the weighted SUM sum_i w_i v_i; this forgets the values
    # and just returns the weight total (always 1).
    return sum(w)


def pmi(p_xy, p_x, p_y):
    # BUG: PMI is log( p(x,y) / (p(x) p(y)) ); this inverts the ratio.
    return math.log(p_x * p_y / p_xy)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        if isinstance(expected, list):
            ok = len(got) == len(expected) and all(abs(a - b) < tol for a, b in zip(got, expected))
        else:
            ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    check("softmax_weights", softmax_weights([0.0, 0.0]), [0.5, 0.5])
    check("attention", attention([0.0, 0.0], [2.0, 4.0]), 3.0)
    # a peaked score picks out its value
    check("attention_peaked", attention([100.0, 0.0], [7.0, 1.0]), 7.0, tol=1e-6)
    check("pmi", pmi(0.1, 0.2, 0.25), math.log(2.0))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
