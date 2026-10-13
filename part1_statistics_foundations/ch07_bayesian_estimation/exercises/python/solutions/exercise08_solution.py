"""Chapter 7 -- reference solution (Proof)."""
# level: proof
def normal_posterior_precision(tau2, sigma2, n):
    return 1 / tau2 + n / sigma2


def normal_posterior_mean(mu0, tau2, xbar, sigma2, n):
    prec = normal_posterior_precision(tau2, sigma2, n)
    return (mu0 / tau2 + n * xbar / sigma2) / prec


def normal_posterior_var(tau2, sigma2, n):
    return 1 / normal_posterior_precision(tau2, sigma2, n)


def main():
    print("precision :", normal_posterior_precision(1.0, 1.0, 10))
    print("mean      :", normal_posterior_mean(0.0, 1.0, 2.0, 1.0, 10))
    print("variance  :", normal_posterior_var(1.0, 1.0, 10))


if __name__ == "__main__":
    main()
