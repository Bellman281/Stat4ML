"""
MLE cookbook -- maximum-likelihood estimators for the common distributions.
Chapter 6, Part I.  A reference gallery, not a graded exercise: read it, run
it, copy what you need. Standard library only.

    python3 mle_cookbook.py

Each estimator is the closed-form solution of the likelihood equation
l'(theta) = 0 for that family (see ch06_text.tex, Section 1). The last two
show the numeric recipe for families with no closed form.
"""
import math
from statistics import median


# ---- closed-form MLEs ------------------------------------------------------
def mle_bernoulli(x):           return sum(x) / len(x)                  # p
def mle_binomial(x, k):         return sum(x) / (k * len(x))            # p, k known
def mle_geometric(x):           return len(x) / sum(x)                  # p, support 1,2,...
def mle_poisson(x):             return sum(x) / len(x)                  # lambda
def mle_exponential(x):         return len(x) / sum(x)                  # rate lambda

def mle_normal(x):                                                      # (mu, sigma^2)
    mu = sum(x) / len(x)
    var = sum((xi - mu) ** 2 for xi in x) / len(x)                      # /n: the MLE
    return mu, var

def mle_uniform(x):             return max(x)                           # theta of U(0, theta)

def mle_laplace(x):                                                     # (mu, b)
    mu = median(x)
    b = sum(abs(xi - mu) for xi in x) / len(x)
    return mu, b

def mle_pareto(x, xm):          return len(x) / sum(math.log(xi / xm) for xi in x)  # alpha
def mle_gamma_scale(x, k):      return (sum(x) / len(x)) / k            # theta, shape k known


# ---- no closed form: solve the score numerically ---------------------------
def mle_newton(score, hess, init, iters=50):
    """Generic Newton solver for l'(theta)=0, given the score l'(theta) and
    the second derivative l''(theta) as functions of theta."""
    theta = init
    for _ in range(iters):
        theta = theta - score(theta) / hess(theta)
    return theta

def mle_exponential_numeric(x, init=1.0):
    """Exponential rate the numeric way, to show the recipe. (Its closed form
    is 1/mean; here we instead solve l'(lambda) = n/lambda - sum(x) = 0.)"""
    n, s = len(x), sum(x)
    return mle_newton(lambda L: n / L - s, lambda L: -n / L**2, init)


def _demo():
    print("Bernoulli  p    :", mle_bernoulli([1, 1, 0, 1, 0]))
    print("Binomial   p    :", mle_binomial([3, 5, 4, 6, 2], k=10))
    print("Geometric  p    :", mle_geometric([1, 2, 1, 4, 3, 1]))
    print("Poisson    lam  :", mle_poisson([2, 1, 3, 0, 2, 1, 4, 2]))
    print("Exponential lam :", mle_exponential([0.4, 1.2, 0.9, 2.1]))
    print("Normal   mu,s2  :", mle_normal([2, 4, 4, 4, 5, 5, 7, 9]))
    print("Uniform   theta :", mle_uniform([0.2, 0.9, 0.5, 0.8]))
    print("Laplace  mu,b   :", mle_laplace([1, 2, 2, 3, 10]))
    print("Pareto   alpha  :", mle_pareto([2.0, 3.0, 5.0, 8.0], xm=1.0))
    print("Gamma    theta  :", mle_gamma_scale([2, 4, 6, 8], k=2))
    print("Exp (Newton)    :", mle_exponential_numeric([0.4, 1.2, 0.9, 2.1]))


if __name__ == "__main__":
    _demo()
