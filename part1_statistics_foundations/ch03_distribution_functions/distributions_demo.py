"""Chapter 3 -- Distribution Functions: visual demo script.

Converted from the original `distributions.ipynb` notebook (a Jupyter
notebook is no longer carried in this repo -- this plain script reproduces
every plot/calculation from it, organized as one function per
distribution). Run directly:

    python3 distributions_demo.py

Each function pops up its own matplotlib window (or, if no display is
available, saves a PNG into ./figures/ instead) and prints any numeric
results to stdout. Requires numpy, matplotlib, seaborn, and scipy
(`pip install numpy matplotlib seaborn scipy --break-system-packages`).
"""

import os

import matplotlib

# Fall back to a non-interactive backend and save PNGs when no display is
# available (e.g. running this in a headless terminal or CI).
if not os.environ.get("DISPLAY") and matplotlib.get_backend().lower() != "agg":
    try:
        import matplotlib.pyplot as _plt_probe  # noqa: F401
    except Exception:
        pass

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy.stats import uniform, laplace, beta, lognorm

FIGURES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")


def _show_or_save(name):
    """Show the current figure interactively, or save it if there's no display."""
    os.makedirs(FIGURES_DIR, exist_ok=True)
    if os.environ.get("DISPLAY") or matplotlib.get_backend().lower() not in ("agg",):
        try:
            plt.show()
            return
        except Exception:
            pass
    out = os.path.join(FIGURES_DIR, name)
    plt.savefig(out, dpi=120, bbox_inches="tight")
    print(f"  (no display detected -- saved plot to {out})")
    plt.close()


def normal_distribution():
    r"""Normal distribution.

    f(x|mu, sigma^2) = 1/(sigma*sqrt(2*pi)) * exp(-(x-mu)^2 / (2*sigma^2))

    mu = 0, sigma = 0.1
    """
    mu, sigma = 0, 0.1
    s = np.random.normal(mu, sigma, 10000)
    count, bins, ignored = plt.hist(s, 1000, density=True)
    plt.plot(
        bins,
        1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((bins - mu) ** 2) / (2 * sigma**2)),
        linewidth=2,
        color="r",
    )
    plt.title("Normal distribution (mu=0, sigma=0.1)")
    _show_or_save("01_normal.png")


def binomial_distribution():
    r"""Binomial distribution.

    P(Y=y|n,p) = C(n,y) * p^y * (1-p)^(n-y), y = 0, 1, ..., n

    n = 100, p = 0.6
    """
    n, p = 100, 0.6
    s = np.random.binomial(n, p, size=100)
    count, bins, ignored = plt.hist(s, 100, density=True)
    plt.title("Binomial distribution (n=100, p=0.6)")
    _show_or_save("02_binomial.png")


def poisson_distribution():
    r"""Poisson distribution.

    P(X=x|lambda) = exp(-lambda) * lambda^x / x!, x = 0, 1, ...

    lambda = 3
    """
    lambda_ = 3
    sns.histplot(random.poisson(lam=lambda_, size=1000), kde=True, stat="density")
    plt.title("Poisson distribution (lambda=3)")
    _show_or_save("03_poisson.png")


def continuous_uniform_distribution():
    r"""Continuous uniform distribution.

    f(x|a,b) = 1/(b-a) for x in [a,b], 0 otherwise

    a = 5, b = 20, N = 4000
    """
    a = 5
    b = 20
    size = 4000

    x = np.linspace(a, b, size)
    dist = uniform(loc=a, scale=b)
    pdf = dist.pdf(x)

    plt.plot(x, pdf)
    plt.xlabel("X")
    plt.ylabel("Probability")
    plt.title("Continuous uniform distribution (a=5, b=20)")
    _show_or_save("04_continuous_uniform.png")


def exponential_distribution():
    r"""Exponential distribution.

    f(x|beta) = (1/beta) * exp(-x/beta), 0 < x < infinity

    beta (scale parameter) = 5
    """
    sns.histplot(random.exponential(scale=5, size=1000000), stat="density")
    plt.title("Exponential distribution (beta=5)")
    _show_or_save("05_exponential.png")


def laplace_distribution():
    r"""Laplace distribution.

    f(x|mu,b) = 1/(2b) * exp(-|x-mu|/b)

    b = 5, mu = 2
    """
    b = 5
    mu = 2
    fig, ax = plt.subplots(1, 1)

    x = np.linspace(laplace.ppf(0.01, mu, b), laplace.ppf(0.99, mu, b), 100)
    ax.plot(x, laplace.pdf(x, mu, b), "k-", lw=2, alpha=0.6, label="laplace pdf")
    ax.legend()
    plt.title("Laplace distribution (mu=2, b=5)")
    _show_or_save("06_laplace.png")


def beta_distribution():
    r"""Beta distribution.

    f(x;alpha,beta) = 1/B(alpha,beta) * x^(alpha-1) * (1-x)^(beta-1)

    alpha = 2, beta = 5
    """
    a, b = 2, 5
    fig, ax = plt.subplots(1, 1)

    x = np.linspace(beta.ppf(0.01, a, b), beta.ppf(0.99, a, b), 100)
    ax.plot(x, beta.pdf(x, a, b), "k-", lw=2, alpha=0.6, label="beta pdf")
    ax.legend()
    plt.title("Beta distribution (alpha=2, beta=5)")
    _show_or_save("07_beta.png")


def lognormal_distribution():
    r"""Lognormal distribution.

    f(x|mu,sigma^2) = 1/sqrt(2*pi*sigma^2) * (1/x) * exp(-(log(x)-mu)^2 / (2*sigma^2))

    sigma = 0.8, mu = 0.5
    """
    s = 0.8
    mu = 0.5
    fig, ax = plt.subplots(1, 1)

    x = np.linspace(lognorm.ppf(0.01, s), lognorm.ppf(0.99, s), 100)
    ax.plot(x, lognorm.pdf(x, s, mu), "k-", lw=2, alpha=0.6, label="lognorm pdf")
    ax.legend()
    plt.title("Lognormal distribution (mu=0.5, sigma=0.8)")
    _show_or_save("08_lognormal.png")


def poisson_calculator_example():
    """Worked Poisson example.

    P(X=x|lambda) = exp(-lambda) * lambda^x / x!, x = 0, 1, ...

    A call center receives mu=12 calls per hour on average. Using the
    Poisson distribution, find the probability that it receives exactly
    2, 4, 6, or 8 calls in a given hour.

    (`mu` here plays the role of `lambda` in the slides/formula above;
    `k` plays the role of `x`.)

    Expected results (as worked in the original slides):
        P(X=2 calls)  = 0.00044
        P(X=4 calls)  = 0.00531
        P(X=6 calls)  = 0.02548
        P(X=8 calls)  = 0.06552
    """
    mu = 12
    x2 = scipy.stats.distributions.poisson.pmf(k=2, mu=mu)
    x4 = scipy.stats.distributions.poisson.pmf(k=4, mu=mu)
    x6 = scipy.stats.distributions.poisson.pmf(k=6, mu=mu)
    x8 = scipy.stats.distributions.poisson.pmf(k=8, mu=mu)
    print("P(X = 2 calls) =", x2)
    print("P(X = 4 calls) =", x4)
    print("P(X = 6 calls) =", x6)
    print("P(X = 8 calls) =", x8)


def main():
    print("Chapter 3 -- Distribution Functions demo")
    print("=" * 60)

    print("\n[1/9] Normal distribution")
    normal_distribution()

    print("\n[2/9] Binomial distribution")
    binomial_distribution()

    print("\n[3/9] Poisson distribution")
    poisson_distribution()

    print("\n[4/9] Continuous uniform distribution")
    continuous_uniform_distribution()

    print("\n[5/9] Exponential distribution")
    exponential_distribution()

    print("\n[6/9] Laplace distribution")
    laplace_distribution()

    print("\n[7/9] Beta distribution")
    beta_distribution()

    print("\n[8/9] Lognormal distribution")
    lognormal_distribution()

    print("\n[9/9] Poisson calculator example (call-center calls/hour)")
    poisson_calculator_example()


if __name__ == "__main__":
    main()
