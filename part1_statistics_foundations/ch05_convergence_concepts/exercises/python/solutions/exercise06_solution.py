"""Chapter 5 -- reference solution (Proof)."""
# level: proof
def markov_bound(mean_nonneg, a):
    return mean_nonneg / a


def chebyshev_bound(var, eps):
    return var / eps ** 2


def empirical_tail(samples, mu, eps):
    return sum(1 for x in samples if abs(x - mu) >= eps) / len(samples)


def wlln_bound(sigma2, n, eps):
    return sigma2 / (n * eps ** 2)


def main():
    data = [1, 2, 2, 2, 3, 2, 2, 2, 2, 10]
    print("Markov(E=2, a=8)      :", markov_bound(2.0, 8))
    print("Chebyshev(var=1, e=2) :", chebyshev_bound(1.0, 2.0))
    print("empirical tail        :", empirical_tail(data, 2, 5))
    print("WLLN bound n=100      :", wlln_bound(4.0, 100, 0.5))


if __name__ == "__main__":
    main()
