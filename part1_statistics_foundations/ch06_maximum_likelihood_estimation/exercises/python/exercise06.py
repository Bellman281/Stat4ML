"""
Chapter 6 exercise -- Maximum Likelihood Estimation (Core)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using only ch06_text.tex Section 1 (the
likelihood, and the Bernoulli / Normal / Poisson MLEs) and Python's
standard library.

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: core
import math


def bernoulli_loglik(p, data):
    """Log-likelihood of iid Bernoulli(p) data (a list of 0/1) at p:
    sum_i [ x_i*log(p) + (1-x_i)*log(1-p) ]."""
    raise NotImplementedError("TODO: bernoulli_loglik")


def bernoulli_mle(data):
    """MLE of p for Bernoulli data: the sample mean."""
    raise NotImplementedError("TODO: bernoulli_mle")


def poisson_mle(data):
    """MLE of lambda for Poisson data: the sample mean."""
    raise NotImplementedError("TODO: poisson_mle")


def normal_mle(data):
    """MLE (mu, sigma2) for Normal data. sigma2 divides by n (the MLE is
    biased), NOT n-1 -- see ch06_text.tex Section 1, editorial note."""
    raise NotImplementedError("TODO: normal_mle")


def main():
    b = [1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    print(f"Bernoulli MLE p_hat = {bernoulli_mle(b)}  (expect 0.6)")
    print(f"log-lik at 0.6     = {bernoulli_loglik(0.6, b):.4f}")
    print(f"Poisson MLE        = {poisson_mle([2,1,3,0,2,1,4,2])}  (expect 1.875)")
    print(f"Normal MLE (mu,s2) = {normal_mle([2,4,4,4,5,5,7,9])}  (expect (5.0, 4.0))")


if __name__ == "__main__":
    main()
