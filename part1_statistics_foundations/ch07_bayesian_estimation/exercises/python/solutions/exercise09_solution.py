"""Chapter 7 -- reference solution (Research)."""
# level: research
import math


def gamma_poisson_posterior(a, b, total, n):
    return (a + total, b + n)


def posterior_predictive_next_success(alpha, beta):
    return alpha / (alpha + beta)


def bvm_posterior_sd(fisher_info_n):
    return 1 / math.sqrt(fisher_info_n)


def main():
    print("gamma-poisson post :", gamma_poisson_posterior(2, 1, 30, 10))
    print("predictive success :", posterior_predictive_next_success(9, 3))
    print("BvM posterior sd   :", bvm_posterior_sd(100))


if __name__ == "__main__":
    main()
