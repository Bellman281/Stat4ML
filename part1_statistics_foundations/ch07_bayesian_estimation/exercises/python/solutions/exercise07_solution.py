"""Chapter 7 -- reference solution (Core)."""
# level: core
def beta_binomial_posterior(alpha, beta, k, n):
    return (alpha + k, beta + n - k)


def posterior_mean(alpha, beta):
    return alpha / (alpha + beta)


def beta_map(alpha, beta):
    return (alpha - 1) / (alpha + beta - 2)


def main():
    post = beta_binomial_posterior(1, 1, 8, 10)
    print("posterior params :", post)
    print("posterior mean   :", posterior_mean(*post))
    print("MAP estimate     :", beta_map(*post))


if __name__ == "__main__":
    main()
