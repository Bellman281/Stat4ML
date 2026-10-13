"""
Chapter 7 exercise -- Beta-Binomial updating (Core)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch07_text.tex Section 1 (the
Beta-Binomial posterior, its mean, and the MAP estimate).

Run with:  python3 exercise07.py
Reference solution: solutions/exercise07_solution.py
"""
# level: core
def beta_binomial_posterior(alpha, beta, k, n):
    """Posterior parameters after k successes in n trials with a
    Beta(alpha, beta) prior: (alpha + k, beta + n - k)."""
    raise NotImplementedError("TODO: beta_binomial_posterior")


def posterior_mean(alpha, beta):
    """Mean of Beta(alpha, beta): alpha / (alpha + beta)."""
    raise NotImplementedError("TODO: posterior_mean")


def beta_map(alpha, beta):
    """Mode (MAP) of Beta(alpha, beta) for alpha, beta > 1:
    (alpha - 1) / (alpha + beta - 2)."""
    raise NotImplementedError("TODO: beta_map")


def main():
    post = beta_binomial_posterior(1, 1, 8, 10)
    print("posterior params :", post)
    print("posterior mean   :", posterior_mean(*post))
    print("MAP estimate     :", beta_map(*post))


if __name__ == "__main__":
    main()
