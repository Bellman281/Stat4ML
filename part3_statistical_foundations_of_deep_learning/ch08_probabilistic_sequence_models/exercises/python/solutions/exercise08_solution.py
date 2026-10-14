"""Chapter 8 -- reference solution (Core)."""
# level: core
import math


def seq_logprob(conditionals):
    return sum(math.log(p) for p in conditionals)


def perplexity_from_logprob(total_logprob, n):
    return math.exp(-total_logprob / n)


def ngram_prob(count, ctx_count, V, alpha):
    return (count + alpha) / (ctx_count + alpha * V)


def main():
    c = [0.5, 0.5, 0.25]
    lp = seq_logprob(c)
    print("seq_logprob            :", lp)
    print("perplexity_from_logprob:", perplexity_from_logprob(lp, len(c)))
    print("ngram_prob             :", ngram_prob(2, 10, 5, 1.0))


if __name__ == "__main__":
    main()
