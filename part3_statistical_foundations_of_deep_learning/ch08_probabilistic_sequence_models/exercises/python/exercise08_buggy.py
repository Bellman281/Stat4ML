"""
Chapter 8 -- RUSTLINGS-STYLE EXERCISE (Python, Core tier)
Part III: Statistical Foundations of Deep Learning & RL

Two deliberate bugs (perplexity_from_logprob, ngram_prob). Fix one function at a
time until all tests pass. Do not edit run_tests().
"""
# level: core
import math


def seq_logprob(conditionals):
    return sum(math.log(p) for p in conditionals)


def perplexity_from_logprob(total_logprob, n):
    # BUG: perplexity is exp(-logprob/n); the minus sign is missing, so this
    # returns the reciprocal.
    return math.exp(total_logprob / n)


def ngram_prob(count, ctx_count, V, alpha):
    # BUG: add-alpha smoothing adds alpha*V to the denominator, not just alpha.
    return (count + alpha) / (ctx_count + alpha)


def run_tests():
    failures = []

    def check(name, got, expected, tol=1e-9):
        ok = abs(got - expected) < tol
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: got={got!r} expected={expected!r}")
        if not ok:
            failures.append(name)

    c = [0.5, 0.5, 0.25]
    lp = seq_logprob(c)
    check("seq_logprob", lp, math.log(0.5) + math.log(0.5) + math.log(0.25))
    check("perplexity_from_logprob", perplexity_from_logprob(lp, 3),
          math.exp(-lp / 3))
    check("ngram_prob", ngram_prob(2, 10, 5, 1.0), 3.0 / 15.0)

    print()
    if failures:
        print(f"{len(failures)} test(s) FAILED: {failures}")
        raise SystemExit(1)
    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
