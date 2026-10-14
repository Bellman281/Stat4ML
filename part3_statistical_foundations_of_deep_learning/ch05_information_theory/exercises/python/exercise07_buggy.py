"""
Chapter 5 -- RUSTLINGS-STYLE EXERCISE (Python, Research tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (perplexity, mutual_information). Fix one function at a time
until all tests pass. Do not edit run_tests().
"""
# level: research
import math


def perplexity(cross_entropy_nats):
    # BUG: perplexity is exp(cross-entropy), not the log of it.
    return math.log(cross_entropy_nats)


def joint_entropy(joint):
    h = 0.0
    for row in joint:
        for pxy in row:
            if pxy > 0:
                h -= pxy * math.log(pxy)
    return h


def mutual_information(joint):
    nx, ny = len(joint), len(joint[0])
    px = [sum(joint[i]) for i in range(nx)]
    py = [sum(joint[i][j] for i in range(nx)) for j in range(ny)]
    mi = 0.0
    for i in range(nx):
        for j in range(ny):
            pxy = joint[i][j]
            if pxy > 0:
                # BUG: MI uses log( p(x,y) / (p(x) p(y)) ); this inverts the ratio.
                mi += pxy * math.log(px[i] * py[j] / pxy)
    return mi


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    corr = [[0.5, 0.0], [0.0, 0.5]]
    indep = [[0.25, 0.25], [0.25, 0.25]]
    check("perplexity", perplexity(math.log(5)), 5.0)
    check("joint_entropy", joint_entropy(corr), math.log(2))
    check("MI_correlated", mutual_information(corr), math.log(2))
    check("MI_independent", mutual_information(indep), 0.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
