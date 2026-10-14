"""
Chapter 8 -- RUSTLINGS-STYLE EXERCISE (Python, Proof tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (avg_cross_entropy, perplexity). Fix one function at a time
until all tests pass. Do not edit run_tests(). The last test checks the identity
perplexity = joint^(-1/n).
"""
# level: proof
import math


def chain_rule_prob(conditionals):
    prod = 1.0
    for p in conditionals:
        prod *= p
    return prod


def avg_cross_entropy(conditionals):
    # BUG: cross-entropy is the NEGATIVE mean log-prob; the minus sign is missing.
    return sum(math.log(p) for p in conditionals) / len(conditionals)


def perplexity(avg_ce):
    # BUG: perplexity EXPONENTIATES the cross-entropy; this forgets the exp.
    return avg_ce


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    c = [0.5, 0.5, 0.25]
    check("chain_rule_prob", chain_rule_prob(c), 0.5 * 0.5 * 0.25)
    ace = avg_cross_entropy(c)
    check("avg_cross_entropy", ace, -(math.log(0.5) + math.log(0.5) + math.log(0.25)) / 3)
    check("perplexity", perplexity(ace), math.exp(ace))
    # identity: perplexity equals the joint probability to the power -1/n
    check("perplexity == joint^(-1/n)", perplexity(avg_cross_entropy(c)),
          chain_rule_prob(c) ** (-1 / 3))

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
