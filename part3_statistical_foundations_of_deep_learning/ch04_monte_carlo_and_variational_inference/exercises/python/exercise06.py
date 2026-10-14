"""
Chapter 4 exercise -- the ELBO and the VAE's KL term (Research tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch04_text.tex Section 2.
  - gaussian_kl  : KL( N(mu, sigma2) || N(0,1) ) = 0.5*(sigma2 + mu^2 - 1 - log sigma2).
  - mc_expectation: Monte Carlo estimate of the reconstruction term (a mean).
  - elbo         : reconstruction log-likelihood MINUS the KL to the prior.

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: research
import math


def gaussian_kl(mu, sigma2):
    """KL( N(mu, sigma2) || N(0,1) ) = 0.5*(sigma2 + mu^2 - 1 - log(sigma2))."""
    raise NotImplementedError("TODO: gaussian_kl")


def mc_expectation(samples):
    """Monte Carlo estimate of E[log p(x|z)] from decoder log-likelihood samples."""
    raise NotImplementedError("TODO: mc_expectation")


def elbo(recon_loglik, mu, sigma2):
    """VAE ELBO: reconstruction log-likelihood minus KL to the N(0,1) prior."""
    raise NotImplementedError("TODO: elbo")


def main():
    print("gaussian_kl(0,1)  :", gaussian_kl(0.0, 1.0))
    print("gaussian_kl(1,1)  :", gaussian_kl(1.0, 1.0))
    r = mc_expectation([-2.0, -1.0, -3.0])
    print("mc_expectation    :", r)
    print("elbo              :", elbo(r, 1.0, 1.0))


if __name__ == "__main__":
    main()
