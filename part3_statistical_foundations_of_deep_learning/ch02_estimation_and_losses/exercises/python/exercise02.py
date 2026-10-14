"""
Chapter 2 exercise -- losses are negative log-likelihoods (Core tier)
Part III: Statistical Foundations of Deep Learning & RL

HOMEWORK: implement each TODO using ch02_text.tex Section 1.
  - mse          : mean squared error.
  - bernoulli_nll: the NLL of a Bernoulli label y in {0,1} with prob p:
                   -(y log p + (1-y) log(1-p)).
  - gaussian_nll : the NLL of Gaussian noise, (n/2) log(2*pi*sigma^2)
                   + sum (y-mu)^2 / (2 sigma^2).

Run with:  python3 exercise02.py
Reference solution: solutions/exercise02_solution.py
"""
# level: core
import math


def mse(preds, targets):
    """Mean squared error between two equal-length lists."""
    raise NotImplementedError("TODO: mse")


def bernoulli_nll(p, y):
    """Negative log-likelihood of a single Bernoulli label y in {0,1}."""
    raise NotImplementedError("TODO: bernoulli_nll")


def gaussian_nll(mu, ys, sigma):
    """Negative log-likelihood of ys under N(mu, sigma^2)."""
    raise NotImplementedError("TODO: gaussian_nll")


def main():
    print("mse           :", mse([1, 2, 3], [1, 2, 5]))
    print("bernoulli_nll :", bernoulli_nll(0.8, 1))
    print("gaussian_nll  :", gaussian_nll(0.0, [1.0, -1.0], 2.0))


if __name__ == "__main__":
    main()
