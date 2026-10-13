"""
Chapter 5 exercise -- Markov, Chebyshev, and the WLLN (Proof tier)
Part I: Statistics Foundation for ML

HOMEWORK: implement each TODO using ch05_text.tex Section 2 (Markov's and
Chebyshev's inequalities and the weak law of large numbers).

Run with:  python3 exercise06.py
Reference solution: solutions/exercise06_solution.py
"""
# level: proof
def markov_bound(mean_nonneg, a):
    """Markov: for Y >= 0, P(Y >= a) <= E[Y] / a."""
    raise NotImplementedError("TODO: markov_bound")


def chebyshev_bound(var, eps):
    """Chebyshev: P(|X - mu| >= eps) <= var / eps^2."""
    raise NotImplementedError("TODO: chebyshev_bound")


def empirical_tail(samples, mu, eps):
    """Fraction of samples with |x - mu| >= eps -- the quantity the bounds
    above are supposed to dominate."""
    raise NotImplementedError("TODO: empirical_tail")


def wlln_bound(sigma2, n, eps):
    """The WLLN bound on P(|Xbar_n - mu| >= eps): sigma^2 / (n * eps^2),
    which goes to 0 as n grows."""
    raise NotImplementedError("TODO: wlln_bound")


def main():
    data = [1, 2, 2, 2, 3, 2, 2, 2, 2, 10]
    print("Markov(E=2, a=8)      :", markov_bound(2.0, 8))
    print("Chebyshev(var=1, e=2) :", chebyshev_bound(1.0, 2.0))
    print("empirical tail        :", empirical_tail(data, 2, 5))
    print("WLLN bound n=100      :", wlln_bound(4.0, 100, 0.5))


if __name__ == "__main__":
    main()
