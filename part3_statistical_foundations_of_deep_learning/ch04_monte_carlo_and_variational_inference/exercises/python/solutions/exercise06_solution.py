"""Chapter 4 -- reference solution (Research)."""
# level: research
import math


def gaussian_kl(mu, sigma2):
    return 0.5 * (sigma2 + mu ** 2 - 1 - math.log(sigma2))


def mc_expectation(samples):
    return sum(samples) / len(samples)


def elbo(recon_loglik, mu, sigma2):
    return recon_loglik - gaussian_kl(mu, sigma2)


def main():
    print("gaussian_kl(0,1)  :", gaussian_kl(0.0, 1.0))
    print("gaussian_kl(1,1)  :", gaussian_kl(1.0, 1.0))
    r = mc_expectation([-2.0, -1.0, -3.0])
    print("mc_expectation    :", r)
    print("elbo              :", elbo(r, 1.0, 1.0))


if __name__ == "__main__":
    main()
